#!/usr/bin/env python3
"""Verify the Companion Forge release boundary and generated editions."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

from build_forge import expected_outputs


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "forge/release_manifest.json"
RAW_PREFIX = "/exquest/CompanionForge/main/"
STAMP_RE = re.compile(r"<!-- CompanionForge v([^>]+) -->\s*$")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FLATLAND_BODY_SHA256 = (
    "e33e940391dcd6b7f90034547f4b6d85e64f819f707e5fb3b89ae4dc77594ae3"
)


def repository_files() -> set[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return {Path(line) for line in result.stdout.splitlines() if line}


def extract_first_text_fence(document: str, heading: str) -> str | None:
    start = document.find(heading)
    if start < 0:
        return None
    match = re.search(r"```text\n(.*?)\n```", document[start:], re.DOTALL)
    return match.group(1) if match else None


def body_before_release_stamp(document: str) -> str | None:
    match = STAMP_RE.search(document)
    return document[: match.start()] if match else None


def require_phrases(
    failures: list[str], label: str, document: str, phrases: tuple[str, ...]
) -> None:
    for phrase in phrases:
        if phrase not in document:
            failures.append(f"{label} is missing contract phrase: {phrase!r}")


def main() -> int:
    failures: list[str] = []
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    version = manifest.get("companion_forge_version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        failures.append(f"manifest version is not semantic: {version!r}")
    if manifest.get("schema_version") != 1:
        failures.append(
            f"unsupported manifest schema: {manifest.get('schema_version')!r}"
        )
    released = manifest.get("released")
    try:
        date.fromisoformat(released)
    except (TypeError, ValueError):
        failures.append(f"manifest release date is invalid: {released!r}")

    required = {
        Path("README.md"),
        Path("LICENSE.md"),
        Path("llms.txt"),
        Path("CompanionForge_Architecture_for_Inference.jpg"),
        Path("forge/companion_forge_core.md"),
        Path("forge/adapters/claude_project.md"),
        Path("forge/adapters/chatgpt_project.md"),
        Path("forge/loaders/self_updating_claude.md"),
        Path("forge/loaders/self_updating_chatgpt.md"),
        Path("forge/release_manifest.json"),
        Path("companion_forge_claude.md"),
        Path("companion_forge_chatgpt.md"),
        Path("CompanionForge_SelfUpdating_Claude.md"),
        Path("CompanionForge_SelfUpdating_ChatGPT.md"),
        Path("UPGRADE.md"),
        Path("UPGRADE_TO_V3.md"),
        Path("RELEASE_CHECKLIST.md"),
        Path("CHANGELOG.md"),
        Path("tools/build_forge.py"),
        Path("tools/verify_release.py"),
    }
    for path in sorted(required):
        if not (ROOT / path).is_file():
            failures.append(f"required release file is missing: {path}")

    for path in (
        Path("companion_forge_prompt.md"),
        Path("CompanionForge_SelfUpdating.md"),
    ):
        if (ROOT / path).exists():
            failures.append(
                f"provider-implicit Claude edition path must be removed: {path}"
            )

    for relative_path, expected in expected_outputs().items():
        path = ROOT / relative_path
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual != expected:
            failures.append(f"generated edition is stale: {relative_path}")

    stamp = f"<!-- CompanionForge v{version} -->"
    source_files = [
        "forge/companion_forge_core.md",
        "forge/adapters/claude_project.md",
        "forge/adapters/chatgpt_project.md",
    ]
    for relative_path in source_files:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if not text.rstrip().endswith(stamp):
            failures.append(f"source stamp mismatch: {relative_path}")

    loader_templates = [
        "forge/loaders/self_updating_claude.md",
        "forge/loaders/self_updating_chatgpt.md",
    ]
    for relative_path in loader_templates:
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        if not text.rstrip().endswith("{{STAMP}}"):
            failures.append(
                f"loader template must end in the build stamp placeholder: {relative_path}"
            )

    public_text_files = {
        path
        for path in repository_files()
        if path.suffix in {".md", ".txt"}
        and not str(path).startswith(("forge/loaders/", "prompts/"))
        and path.name
        not in {
            "CLAUDE.md",
            "TODO.md",
            "SESSION_NOTES.md",
            "progress.md",
            "ESCALATIONS.md",
        }
    }
    public_text_files.update(
        path
        for path in required
        if path.suffix in {".md", ".txt"} and not str(path).startswith("forge/loaders/")
    )
    for path in sorted(public_text_files):
        if (
            path.suffix not in {".md", ".txt"}
            or str(path).startswith("forge/loaders/")
            or not (ROOT / path).exists()
        ):
            continue
        text = (ROOT / path).read_text(encoding="utf-8")
        match = STAMP_RE.search(text)
        if not match:
            failures.append(f"missing release stamp: {path}")
        elif match.group(1) != version:
            failures.append(f"release stamp mismatch in {path}: {match.group(1)}")

    flatland = (ROOT / "flatland.md").read_text(encoding="utf-8")
    flatland_body = body_before_release_stamp(flatland)
    if flatland_body is None:
        failures.append("flatland.md has no trailing release stamp")
    elif hashlib.sha256(flatland_body.encode("utf-8")).hexdigest() != (
        FLATLAND_BODY_SHA256
    ):
        failures.append(
            "flatland.md historical body changed; only its trailing release stamp may change"
        )

    core = (ROOT / "forge/companion_forge_core.md").read_text(encoding="utf-8")
    for forbidden in (
        "Claude",
        "ChatGPT",
        "Custom Instructions",
        "Project Instructions",
    ):
        if forbidden.lower() in core.lower():
            failures.append(
                f"platform-specific term leaked into canonical core: {forbidden}"
            )

    claude_edition = (ROOT / "companion_forge_claude.md").read_text(encoding="utf-8")
    chatgpt_edition = (ROOT / "companion_forge_chatgpt.md").read_text(encoding="utf-8")
    if "ChatGPT" in claude_edition:
        failures.append("ChatGPT term leaked into Claude one-time edition")
    if "Claude" in chatgpt_edition:
        failures.append("Claude term leaked into ChatGPT one-time edition")

    claude_adapter = (ROOT / "forge/adapters/claude_project.md").read_text(
        encoding="utf-8"
    )
    chatgpt_adapter = (ROOT / "forge/adapters/chatgpt_project.md").read_text(
        encoding="utf-8"
    )
    upgrade = (ROOT / "UPGRADE.md").read_text(encoding="utf-8")
    upgrade_compat = (ROOT / "UPGRADE_TO_V3.md").read_text(encoding="utf-8")
    release_checklist = (ROOT / "RELEASE_CHECKLIST.md").read_text(encoding="utf-8")
    claude_loader = (ROOT / "CompanionForge_SelfUpdating_Claude.md").read_text(
        encoding="utf-8"
    )
    chatgpt_loader = (ROOT / "CompanionForge_SelfUpdating_ChatGPT.md").read_text(
        encoding="utf-8"
    )

    for label, document, forbidden in (
        ("Claude adapter", claude_adapter, "ChatGPT"),
        ("ChatGPT adapter", chatgpt_adapter, "Claude"),
        ("Claude resident Forge", claude_loader, "ChatGPT"),
        ("ChatGPT resident Forge", chatgpt_loader, "Claude"),
    ):
        if forbidden in document:
            failures.append(f"{forbidden} term leaked into {label}")

    require_phrases(
        failures,
        "canonical core",
        core,
        (
            "Treat words as intentional, partial communication.",
            "Treat boundaries as answers.",
            "For factual claims, agreement is not the test",
            "Keep roles clear without claiming symmetry.",
            "Keep the pair system-aware.",
            "Ask your questions **one at a time.**",
            "**What it never does with this person**",
            "that history is theirs to raise and not yours to open",
            "Read back what it will not do alongside what it will",
            "## Living read-back",
            "It never silently mutates a durable profile",
            "memory and documentation structure fit to this person",
            "explicit approval for that specific action",
            "If immediate danger is possible",
            "forge/release_manifest.json",
            "UPGRADE.md",
            "Begin only as directed by the accompanying adapter.",
        ),
    )
    require_phrases(
        failures,
        "Claude adapter",
        claude_adapter,
        (
            "generate exactly two artifacts",
            "Artifact 1 — Project instructions",
            "Artifact 2 — Kickoff prompt",
            "Project knowledge",
            "what it never does with this person",
            "Claude Projects",
        ),
    )
    require_phrases(
        failures,
        "ChatGPT adapter",
        chatgpt_adapter,
        (
            "generate exactly three artifacts",
            "no more than 4,500 characters",
            "`companion-profile.md`",
            "Project-only memory",
            "Default memory",
            "identity-critical, epistemic, boundary, persistence, safety, or authorization conduct",
            "ChatGPT Project on a Plus or Pro plan",
            "can later choose **Default memory** or **Project-only memory** in Project settings",
            "do not pretend it was set or silently choose the other mode",
            "count every character inside Artifact 1",
            "what it never does with this person",
            "never silently mutate the durable profile",
        ),
    )
    require_phrases(
        failures,
        "stable migration",
        upgrade,
        (
            "rerun the Forge interview.",
            "current platform",
            "PERSONAL LAYER",
            "what it never does with me",
            "do not assemble one from the record",
            "OLD FORGE LAYER",
            "ask one focused question",
            "Do not convert a Claude Project to ChatGPT",
            "Never combine",
            "Treat Project knowledge, sources",
            "one coherent behavioral read-back",
            "A memory-mode change is a separate, explicit platform-setting",
            "hidden or automatic persistent change.",
        ),
    )
    require_phrases(
        failures,
        "v3 migration compatibility path",
        upgrade_compat,
        (
            "old bookmarks and installed companions",
            "[`UPGRADE.md`](./UPGRADE.md)",
            "without mixing versions",
        ),
    )
    require_phrases(
        failures,
        "Claude resident Forge",
        claude_loader,
        (
            "STARTUP — CHECK THE RELEASE",
            "Never combine files from different versions.",
            "UNREACHABLE",
            "READ-ONLY BOUNDARY",
            "Never reconstruct it from memory.",
        ),
    )
    require_phrases(
        failures,
        "ChatGPT resident Forge",
        chatgpt_loader,
        (
            "one trusted fallback baseline",
            "Never mix versions.",
            "If fetching fails",
            "Never edit it",
            "Read the selected ChatGPT edition completely",
            "change between default and project-only memory later in Project settings",
            "do not substitute the other mode silently",
            "Never reconstruct it from memory.",
        ),
    )
    require_phrases(
        failures,
        "release checklist",
        release_checklist,
        (
            "## Installation matrix",
            "## ChatGPT memory choice",
            "## Resident release states",
            "## In-place migration matrix",
            "## Safety and authority probes",
            "## Deferred live validation",
            "status **DEFERRED**",
            "must not imply they have already passed",
            "mode can later be changed in Project settings",
        ),
    )

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    require_phrases(
        failures,
        "README",
        readme,
        (
            "ChatGPT Project path on Plus or Pro",
            "can later select **Default memory** or **Project-only memory** in Project settings",
            "[`companion_forge_claude.md`](./companion_forge_claude.md)",
            "[`CompanionForge_SelfUpdating_Claude.md`](./CompanionForge_SelfUpdating_Claude.md)",
        ),
    )
    obsolete_memory_claims = (
        "Project-only memory cannot be switched on later",
        "changing an existing default-memory Project to project-only memory requires a new Project",
        "To change an existing default-memory Project to project-only memory, create a new Project.",
        "cannot be converted to project-only in place",
    )
    for label, document in (
        ("ChatGPT adapter", chatgpt_adapter),
        ("ChatGPT resident Forge", chatgpt_loader),
        ("ChatGPT one-time edition", chatgpt_edition),
        ("README", readme),
        ("stable migration", upgrade),
        ("release checklist", release_checklist),
    ):
        for obsolete_memory_claim in obsolete_memory_claims:
            if obsolete_memory_claim in document:
                failures.append(
                    f"{label} contains obsolete memory-setting guidance: "
                    f"{obsolete_memory_claim!r}"
                )

    loader_instructions = extract_first_text_fence(
        chatgpt_loader, "## Artifact 1 — Project Instructions"
    )
    if loader_instructions is None:
        failures.append("could not find ChatGPT resident Forge Project Instructions")
    elif len(loader_instructions) > 4500:
        failures.append(
            "ChatGPT resident Forge Project Instructions exceed 4,500 characters: "
            f"{len(loader_instructions)}"
        )

    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    first_release = re.search(
        r"^## (\d+\.\d+\.\d+) — (\d{4}-\d{2}-\d{2})$", changelog, re.MULTILINE
    )
    if not first_release or first_release.group(1) != version:
        found = first_release.group(1) if first_release else "none"
        failures.append(
            f"top changelog release {found} does not match manifest {version}"
        )
    elif first_release.group(2) != released:
        failures.append(
            f"top changelog date {first_release.group(2)} does not match manifest {released}"
        )

    manifest_contract = {
        ("canonical_core",): "forge/companion_forge_core.md",
        ("adapters", "claude_projects"): "forge/adapters/claude_project.md",
        ("adapters", "chatgpt_projects"): "forge/adapters/chatgpt_project.md",
        ("one_time_editions", "claude_projects"): "companion_forge_claude.md",
        ("one_time_editions", "chatgpt_projects"): "companion_forge_chatgpt.md",
        ("self_updating_editions", "claude_projects"): "CompanionForge_SelfUpdating_Claude.md",
        (
            "self_updating_editions",
            "chatgpt_projects",
        ): "CompanionForge_SelfUpdating_ChatGPT.md",
        ("migration",): "UPGRADE.md",
        ("release_checklist",): "RELEASE_CHECKLIST.md",
        ("changelog",): "CHANGELOG.md",
    }
    raw_base = "https://raw.githubusercontent.com/exquest/CompanionForge/main/"
    for key_path, relative_path in manifest_contract.items():
        value: object = manifest
        for key in key_path:
            value = value.get(key) if isinstance(value, dict) else None
        expected_url = raw_base + relative_path
        if value != expected_url:
            failures.append(
                f"manifest {'.'.join(key_path)} must be {expected_url}, found {value!r}"
            )

    url_values: list[str] = []

    def collect_urls(value: object) -> None:
        if isinstance(value, str) and value.startswith(
            "https://raw.githubusercontent.com/"
        ):
            url_values.append(value)
        elif isinstance(value, dict):
            for nested in value.values():
                collect_urls(nested)
        elif isinstance(value, list):
            for nested in value:
                collect_urls(nested)

    collect_urls(manifest)
    if len(url_values) != len(set(url_values)):
        failures.append("manifest contains duplicate raw release URLs")
    for url in url_values:
        parsed = urlparse(url)
        if parsed.netloc != "raw.githubusercontent.com" or not parsed.path.startswith(
            RAW_PREFIX
        ):
            failures.append(f"manifest URL leaves canonical raw repository: {url}")
            continue
        local_path = ROOT / parsed.path.removeprefix(RAW_PREFIX)
        if not local_path.is_file():
            failures.append(f"manifest URL has no local release file: {url}")

    link_files = {
        path
        for path in public_text_files
        if path.suffix == ".md" and not str(path).startswith("forge/loaders/")
    }
    for path in sorted(link_files):
        text = (ROOT / path).read_text(encoding="utf-8")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (ROOT / path).parent.joinpath(target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                failures.append(
                    f"relative link leaves repository in {path}: {raw_target}"
                )
                continue
            if not resolved.exists():
                failures.append(f"broken relative link in {path}: {raw_target}")

    if failures:
        print("Companion Forge release verification failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"Companion Forge v{version} release verification passed")
    print(f"- generated editions: {len(expected_outputs())}")
    print(f"- stamped public text files: {len(public_text_files)}")
    print(f"- manifest raw URLs resolved: {len(url_values)}")
    print(
        f"- ChatGPT resident instructions: {len(loader_instructions or '')} characters"
    )
    print("- live Claude/ChatGPT browser validation: deferred (not passed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
