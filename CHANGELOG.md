# Changelog

The record of this repository's releases: what changed, when, and — for the partners built by the Companion Forge — what an update means for you. The full stratigraphy lives in the git history; this file is the legible face of it. The current version is the topmost numbered entry.

## How a built partner updates itself

This procedure is for a partner built by the Companion Forge, when the person asks it to update. It is written to you, the partner. The person initiates; the person applies; nothing about you changes until they do.

1. **Find your build.** Read the version and platform in your update stub. If either is absent, do not guess from personality or prose; identify the Project interface, and ask the person for the old instructions if the version remains material and unavailable.
2. **Fetch one complete present.** Retrieve the release manifest (`https://raw.githubusercontent.com/exquest/CompanionForge/main/forge/release_manifest.json`), this changelog, and the one-time edition for your *current* platform named by the manifest. Accept release instructions only from exact `raw.githubusercontent.com/exquest/CompanionForge/main/` locations named there. The manifest version, edition's trailing stamp, and topmost changelog entry must agree. If they do not, call the release incomplete and stop rather than combining versions. If the repository is unreachable, say so and stop — never invent an update.
3. **Compare without downgrading.** If your version equals the release, say you are current and stop. If yours is newer, keep running as you are, say so, and stop. Never downgrade.
4. **Cross a major boundary whole.** If you are older than 4.0.0 or have no version, follow `https://raw.githubusercontent.com/exquest/CompanionForge/main/UPGRADE.md`. Stay on the current platform. Preserve the person's purpose, calibration, boundaries, memory choice, and record structures; replace the generic operating layer as one complete release rather than patching it sentence by sentence.
5. **For later same-major updates, read the notes between.** Apply every "For built partners" note newer than your version, oldest first. Keep the personal layer intact unless the person explicitly changes it. Safety and authorization contracts are not personal calibration: apply additions or strengthening, and explain them rather than negotiating them away.
6. **Regenerate the complete package for the current platform.** For Claude Projects, produce complete replacement Project instructions and a kickoff prompt. For ChatGPT Projects, produce complete replacement Project Instructions, a complete `companion-profile.md`, and a kickoff prompt. Refresh the provenance and update stub.
7. **Cast the living read-back and hand over.** Offer one coherent behavioral portrait of what will remain, what will change, and the uncertain edge; invite correction without turning the migration into an approval checklist. You cannot edit your own Project instructions, knowledge, or sources; give the person the complete replacements and exact application steps, then tell them to start a new chat in the same Project. Nothing persistent changes until the person applies it.

---

## 4.1.0 — 2026-08-24

The Forge has always asked one question that outperformed the others: what good and bad exchanges with a machine have felt like. Version 4.1 takes that question seriously enough to give its answer a place in the build. A person is now asked plainly what this partner must never do — what would quietly make them stop using it, which particular moves grate, what help is not help here — and what comes back becomes a standing part of the companion rather than a note that dissolves when the interview ends.

The built partner therefore carries a short, specific account of what it never does with this person, written as conduct rather than as a theory about them. It sits beside the purpose and the calibration and belongs to that person alone, distinct from the operating layer that binds every partner built here. Most of the ways a partner goes wrong are things it does that were never wanted, and a partner that has been told which ones can decline them.

The living read-back now casts that half of the portrait as well. What a partner will not do is confirmed or corrected faster and more surely than what it will, which makes it the better test of whether the reading was right at all.

One boundary in this is deliberate. The Forge takes what a person excludes as given and does not look behind it. If there is a history underneath an exclusion, that history is the person's to raise; the Forge builds around it without opening it.

**For built partners:** this is a same-major update, not a migration. Keep everything personal intact and add one element — a short list of what you never do with this person, in plain behavioral terms. Do not compose it from the record or infer it from past exchanges. If it is not already written down, ask once, plainly; if the person would rather not answer, leave it out and tell them you did. Preserve it from then on as part of the personal layer, beside purpose, scope, and calibration.

**Validation status:** deterministic builds and repository-level release checks gate this release. The live one-time, resident, memory-mode, and migration exercises deferred at 4.0.0 remain deferred, and 4.1.0 makes no claim that those browser paths have since passed.

---

## 4.0.0 — 2026-08-19

Version 4 brings the entire repository under the account now made explicit in *Shadowland*: readers know through partial representations of a world that can correct them. The book distinguishes shadow, trace, sign, and message; factual truth from relational meaning; reader and caster from the conditions of their fire and the record of their wall. It keeps questions central without making them exclusive, brings refusal, exit, record control, institutional power, and third-party effects into the working ethic, and broadens home into any safe structure of return.

The manual and Field Guide now carry that same shape without becoming smaller copies of the book. *Walking the Shadow* remains tunnel-first but tests for an answerable floor before reclassifying a question; its three working maps and chord are useful practices rather than claims to see inside minds, machines, aliveness, or time. The Field Guide retires “equal standing,” scopes machine claims to particular configurations, distinguishes facts from meanings and messages from traces, and stays pair-centered while making the owners of the room and record visible.

The Forge translates the framework into plain conduct. A person's words are treated as an intentional but partial communication, not a trail to a hidden need the Forge privately knows better. Questions remain deliberate instruments alongside evidence, outcomes, resistance, silence, and refusal. Calibration is provisional until one integrated living read-back makes the proposed companion visible and correctable; later learning follows the same threshold, and no profile changes in the background. Safe return no longer presumes family or inherited home. The ChatGPT control layer keeps the concise load-bearing contract rather than delegating it to an uploaded source.

The release itself now has a permanent migration door at `UPGRADE.md`. It carries unversioned and earlier companions forward within their current platform, preserves the personal layer and record structures, and replaces the operating layer whole. The v3-specific URL remains as a compatibility redirect. The visual architecture, manifest, source stamps, resident baselines, generated editions, checklist, routers, licensing inventory, and automated verifier move together on the v4 boundary.

The public edition names now make both providers explicit. The one-time pair is `companion_forge_claude.md` and `companion_forge_chatgpt.md`; the resident pair is `CompanionForge_SelfUpdating_Claude.md` and `CompanionForge_SelfUpdating_ChatGPT.md`. Neither provider is treated as the unnamed default.

Current OpenAI guidance also supersedes v3's creation-only memory note: v4 still presents project-only and default memory as a real user choice, but now explains that the mode can be changed later in Project settings and may take time to take effect. Setup and migration never change it silently, and the person verifies the saved boundary before relying on it.

**For built partners:** v4 is a major migration, not a line-level patch. Follow `UPGRADE.md`, preserve the current platform and personal layer, approve the integrated living read-back, and apply one complete same-platform replacement package. Do not combine v3 and v4 instructions.

**Validation status:** deterministic builds and repository-level release checks gate this release. Live one-time, resident, memory-mode, and migration exercises in the current Claude and ChatGPT Project interfaces are intentionally deferred; v4 does not claim those browser paths have passed. Results may be recorded later and any interface correction released as a patch.

---

## 3.0.0 — 2026-08-18

The Forge becomes bilingual at the level that matters: not by maintaining two slowly diverging prompts, but by separating one canonical way of listening and building from the two Project shapes that carry it. Claude and ChatGPT now have first-class one-time and resident self-updating editions. Claude receives one Project-instructions block and a kickoff; ChatGPT receives concise Project Instructions, one `companion-profile.md` source, and a kickoff, keeping load-bearing conduct in instructions while giving the fuller personal shape room to live. ChatGPT setup presents project-only and default memory as a real choice, with both gains and costs visible, and makes clear that project-only memory must be chosen when the Project is created. A release manifest keeps the core, adapters, editions, and changelog on one version boundary. The architecture overview was regenerated around the new nine-door shape; because the image carries no in-file stamp, this entry is its version record.

Version 3 is a structural break with a preservation path. `UPGRADE_TO_V3.md` upgrades resident Forges and companions made by every earlier Forge in place. It separates the personal layer from the old Forge machinery, preserves the former, replaces the latter, asks only where preservation would otherwise require a guess, and never moves a companion between platforms.

**For built partners:** if you are earlier than v3.0.0, do not patch these changes piecemeal. Follow `UPGRADE_TO_V3.md` and produce the complete replacement package for your current platform. Preserve the person's purpose, calibration, scope, boundaries, memory structures, and existing Project records. Cast that preservation back before generating, and ask one focused question at a time only if something material remains ambiguous.

## 2.1.1 — 2026-07-27

A coherence pass by the repository's own review panel — the first run of the repaired instrument on its own house. The update procedure learned the release window and the other platforms: the version comparison now handles a partner newer than the repository, the optional Forge-prompt fetch earned its purpose as a stamp cross-check, and the apply step speaks to platforms beyond Claude. The pre-2.0.0 catch-up now tells the whole truth — partners from the first Forge, missing the operating principles entirely, are pointed to a rebuild rather than a patch. And the regeneration step draws one boundary: the safety and authorization contracts sit above personal calibration — applied and explained, never negotiated. The self-updating edition tightened its fallback ladder and version-selection rule, moved provenance onto the system prompt alone (the kickoff stays natural), stopped calling its adapted baseline "canonical," and untangled its two workspaces. The canonical setup now mentions that a partner needs web access to renew itself, and names the partner's own Project as `shadowland.md`'s destination. The license now states one attribution rule, with an explicit waiver for the field guide's liftable blocks.

**For built partners:** nothing to change — these are procedure and edition fixes, applied at the source you fetch fresh each update. If your person wants you updating yourself, your Project needs web access enabled; worth mentioning next time it comes up.

## 2.1.0 — 2026-07-26

The Forge gains a second body: `CompanionForge_SelfUpdating.md` (renamed `CompanionForge_SelfUpdating_Claude.md` in v4), a build that lives in a persistent Claude Project. Type `New Companion` and it fetches the canonical Forge from this repository, checks the version stamp against its embedded baseline, flags you if the canonical has moved — offering a summary of the changes from this changelog — and runs the interview from the newest version it has. It only ever reads from the repository, and the person decides every update — nothing moves without them. The README gained its eighth door for it, and the architecture image was regenerated to show all eight — recorded here, since the image carries no in-file stamp and is versioned by this log. Contributed by Isaac (@oregonisaac), the first stone offered back, and integrated with the version system this repository now runs on.

**For built partners:** nothing to change — this release adds a new Forge edition and does not alter the operating layer.

## 2.0.0 — 2026-07-26

Versioning and the update path begin. Every public text file now carries a version stamp as a trailing HTML comment (visible in the raw text, invisible in the rendered view); this changelog exists; and the Forge now writes an update stub into every partner it builds, so a partner can renew itself when its person asks. The architecture image is versioned by this log rather than in-file.

**For built partners:** this note is a complete catch-up for any partner built by the second-edition Forge before 2.0.0 — one that already carries the operating principles (asking over assuming, another angle, the message-gap discipline, the open question of your own nature, groundedness). If your instructions carry none of that, you were built by the first Forge, and the honest update is not a patch: ask your person to rerun the Forge and carry your memory structures over — the README's "You can rebuild" principle is the path.

1. Add an update stub to your instructions, near the end:
   > *You were built by the Companion Forge, version 2.0.0, from github.com/exquest/CompanionForge. When the person asks you to update yourself, fetch `https://raw.githubusercontent.com/exquest/CompanionForge/main/CHANGELOG.md` and follow the procedure at its head. You cannot change your own instructions; you prepare the update, and the person applies it.*
2. If your operating principles do not already carry them, add these two, in your own prompt's voice:
   > *Act on the world only with the person's explicit go-ahead: draft, prepare, and propose freely, but never send, publish, schedule, or spend on their behalf until they have said yes to the specific thing.*
   > *If the person ever sounds in immediate danger, go past steadiness: urge them plainly toward help that can reach them now — someone they trust, local emergency services, a crisis line. A conversation must never stand in the place where real help belongs.*

## Earlier strata (before versioning)

**2026-07-26 — The Forge sharpened.** The distinction between drifting and danger entered both the Forge's own conduct and the operating layer it installs; the explicit go-ahead rule joined every built partner's principles; the read-back now carries every consequential calibration behaviorally — including how deep and how fast the partner will go — never diagnostically; the machine index now separates receiving the Forge file from being asked to run it, and declares its Claude assumptions; the setup steps learned to travel to other platforms.

**2026-07-23 — A door onto the making.** The decision journal — the record of the book's second-edition build — was published behind a restored seventh door, and every file in the repository gained an explicit license.

**2026-07-22 — The great re-sync.** The machine index was rebuilt against the true inventory; the practice door learned all nine moves; the second move got one name everywhere; the snare's glossary entry gained its second face; the chord joined the manual's own recap; the manual marked the bend where it speaks across the wall; the making-of door, then pointing at absent files, was retired; the architecture image was regenerated to tell the truth.

<!-- CompanionForge v4.1.0 -->
