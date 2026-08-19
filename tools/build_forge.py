#!/usr/bin/env python3
"""Build the four public Companion Forge editions from canonical sources."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "forge/release_manifest.json"
STAMP_RE = re.compile(r"\n?<!-- CompanionForge v[^>]+ -->\s*$")


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def source_body(relative_path: str) -> str:
    return STAMP_RE.sub("", read_text(relative_path)).rstrip()


def render_one_time(
    *, platform_name: str, paste_target: str, adapter_path: str, core: str, version: str
) -> str:
    adapter = source_body(adapter_path)
    return f"""# The Companion Forge — {platform_name} Edition

> Paste everything below the line into a **fresh {paste_target} chat** as the first message. Do not create the companion Project yet; the Forge will interview you first and then give you the finished setup.

<!-- Assembled from the canonical core and the {platform_name} adapter. -->

---

{adapter}

---

{core}

<!-- CompanionForge v{version} -->
"""


def render_loader(
    template_path: str, *, version: str, stamp: str, **values: str
) -> str:
    rendered = read_text(template_path)
    replacements = {"VERSION": version, "STAMP": stamp, **values}
    for name, value in replacements.items():
        rendered = rendered.replace("{{" + name + "}}", value)
    unresolved = re.findall(r"{{[A-Z_]+}}", rendered)
    if unresolved:
        raise ValueError(f"Unresolved template tokens in {template_path}: {unresolved}")
    return rendered.rstrip() + "\n"


def expected_outputs() -> dict[str, str]:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    version = manifest["companion_forge_version"]
    stamp = f"<!-- CompanionForge v{version} -->"
    core = source_body("forge/companion_forge_core.md")

    claude = render_one_time(
        platform_name="Claude",
        paste_target="Claude",
        adapter_path="forge/adapters/claude_project.md",
        core=core,
        version=version,
    )
    chatgpt = render_one_time(
        platform_name="ChatGPT",
        paste_target="ChatGPT",
        adapter_path="forge/adapters/chatgpt_project.md",
        core=core,
        version=version,
    )

    return {
        "companion_forge_prompt.md": claude,
        "companion_forge_chatgpt.md": chatgpt,
        "CompanionForge_SelfUpdating.md": render_loader(
            "forge/loaders/self_updating_claude.md",
            version=version,
            stamp=stamp,
            CLAUDE_BUNDLE=claude.rstrip(),
        ),
        "CompanionForge_SelfUpdating_ChatGPT.md": render_loader(
            "forge/loaders/self_updating_chatgpt.md",
            version=version,
            stamp=stamp,
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if checked-in editions differ from generated output",
    )
    args = parser.parse_args()

    failures: list[str] = []
    for relative_path, expected in expected_outputs().items():
        output_path = ROOT / relative_path
        if args.check:
            actual = (
                output_path.read_text(encoding="utf-8")
                if output_path.exists()
                else None
            )
            if actual != expected:
                failures.append(relative_path)
        else:
            output_path.write_text(expected, encoding="utf-8")
            print(f"built {relative_path}")

    if failures:
        print("Generated editions are stale or missing:", file=sys.stderr)
        for path in failures:
            print(f"  {path}", file=sys.stderr)
        print("Run: python3 tools/build_forge.py", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
