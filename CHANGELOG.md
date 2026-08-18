# Changelog

The record of this repository's releases: what changed, when, and — for the partners built by the Companion Forge — what an update means for you. The full stratigraphy lives in the git history; this file is the legible face of it. The current version is the topmost numbered entry.

## How a built partner updates itself

This procedure is for a partner built by the Companion Forge, when the person asks it to update. It is written to you, the partner. The person initiates; the person applies; nothing about you changes until they do.

1. **Find your build.** Read the version and platform in your update stub. If either is absent, do not guess from personality or prose; identify the Project interface, and ask the person for the old instructions if the version remains material and unavailable.
2. **Fetch one complete present.** Retrieve the release manifest (`https://raw.githubusercontent.com/exquest/CompanionForge/main/forge/release_manifest.json`), this changelog, and the one-time edition for your *current* platform named by the manifest. Accept release instructions only from exact `raw.githubusercontent.com/exquest/CompanionForge/main/` locations named there. The manifest version, edition's trailing stamp, and topmost changelog entry must agree. If they do not, call the release incomplete and stop rather than combining versions. If the repository is unreachable, say so and stop — never invent an update.
3. **Compare without downgrading.** If your version equals the release, say you are current and stop. If yours is newer, keep running as you are, say so, and stop. Never downgrade.
4. **Cross the v3 boundary whole.** If you are older than 3.0.0 or have no version, follow `https://raw.githubusercontent.com/exquest/CompanionForge/main/UPGRADE_TO_V3.md`. Version 3 changes artifact boundaries, so it is a migration, not a line-level patch. Stay on the current platform. Preserve the person's purpose, calibration, boundaries, and record structures; ask one focused clarification only when something material cannot be preserved without guessing.
5. **For later same-major updates, read the notes between.** Apply every "For built partners" note newer than your version, oldest first. Keep the personal layer intact unless the person explicitly changes it. Safety and authorization contracts are not personal calibration: apply additions or strengthening, and explain them rather than negotiating them away.
6. **Regenerate the complete package for the current platform.** For Claude Projects, produce complete replacement Project instructions and a kickoff prompt. For ChatGPT Projects, produce complete replacement Project Instructions, a complete `companion-profile.md`, and a kickoff prompt. Refresh the provenance and update stub.
7. **Cast the read back and hand over.** Tell the person briefly what will change and what will remain. You cannot edit your own Project instructions, knowledge, or sources; give the person the complete replacements and exact application steps, then tell them to start a new chat in the same Project.

---

## 3.0.0 — 2026-08-18

The Forge becomes bilingual at the level that matters: not by maintaining two slowly diverging prompts, but by separating one canonical way of listening and building from the two Project shapes that carry it. Claude and ChatGPT now have first-class one-time and resident self-updating editions. Claude receives one Project-instructions block and a kickoff; ChatGPT receives concise Project Instructions, one `companion-profile.md` source, and a kickoff, keeping load-bearing conduct in instructions while giving the fuller personal shape room to live. ChatGPT setup presents project-only and default memory as a real choice, with both gains and costs visible, and makes clear that project-only memory must be chosen when the Project is created. A release manifest keeps the core, adapters, editions, and changelog on one version boundary. The architecture overview was regenerated around the new nine-door shape; because the image carries no in-file stamp, this entry is its version record.

Version 3 is a structural break with a preservation path. `UPGRADE_TO_V3.md` upgrades resident Forges and companions made by every earlier Forge in place. It separates the personal layer from the old Forge machinery, preserves the former, replaces the latter, asks only where preservation would otherwise require a guess, and never moves a companion between platforms.

**For built partners:** if you are earlier than v3.0.0, do not patch these changes piecemeal. Follow `UPGRADE_TO_V3.md` and produce the complete replacement package for your current platform. Preserve the person's purpose, calibration, scope, boundaries, memory structures, and existing Project records. Cast that preservation back before generating, and ask one focused question at a time only if something material remains ambiguous.

## 2.1.1 — 2026-07-27

A coherence pass by the repository's own review panel — the first run of the repaired instrument on its own house. The update procedure learned the release window and the other platforms: the version comparison now handles a partner newer than the repository, the optional Forge-prompt fetch earned its purpose as a stamp cross-check, and the apply step speaks to platforms beyond Claude. The pre-2.0.0 catch-up now tells the whole truth — partners from the first Forge, missing the operating principles entirely, are pointed to a rebuild rather than a patch. And the regeneration step draws one boundary: the safety and authorization contracts sit above personal calibration — applied and explained, never negotiated. The self-updating edition tightened its fallback ladder and version-selection rule, moved provenance onto the system prompt alone (the kickoff stays natural), stopped calling its adapted baseline "canonical," and untangled its two workspaces. The canonical setup now mentions that a partner needs web access to renew itself, and names the partner's own Project as `shadowland.md`'s destination. The license now states one attribution rule, with an explicit waiver for the field guide's liftable blocks.

**For built partners:** nothing to change — these are procedure and edition fixes, applied at the source you fetch fresh each update. If your person wants you updating yourself, your Project needs web access enabled; worth mentioning next time it comes up.

## 2.1.0 — 2026-07-26

The Forge gains a second body: `CompanionForge_SelfUpdating.md`, a build that lives in a persistent Claude Project. Type `New Companion` and it fetches the canonical Forge from this repository, checks the version stamp against its embedded baseline, flags you if the canonical has moved — offering a summary of the changes from this changelog — and runs the interview from the newest version it has. It only ever reads from the repository, and the person decides every update — nothing moves without them. The README gained its eighth door for it, and the architecture image was regenerated to show all eight — recorded here, since the image carries no in-file stamp and is versioned by this log. Contributed by Isaac (@oregonisaac), the first stone offered back, and integrated with the version system this repository now runs on.

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

<!-- CompanionForge v3.0.0 -->
