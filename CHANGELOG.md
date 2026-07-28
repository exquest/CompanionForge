# Changelog

The record of this repository's releases: what changed, when, and — for the partners built by the Companion Forge — what an update means for you. The full stratigraphy lives in the git history; this file is the legible face of it. The current version is the topmost numbered entry.

## How a built partner updates itself

This procedure is for a partner built by the Companion Forge, when the person asks it to update. It is written to you, the partner. The person initiates; the person applies; nothing about you changes until they do.

1. **Find your build version.** It is in your instructions' update stub ("built by the Companion Forge, version …"). If you have no stub, you predate versioning: treat your version as pre-2.0.0.
2. **Fetch the present.** Retrieve this file (`https://raw.githubusercontent.com/exquest/CompanionForge/main/CHANGELOG.md`) and, if you can, the current Forge prompt (`https://raw.githubusercontent.com/exquest/CompanionForge/main/companion_forge_prompt.md`) — its trailing version stamp should agree with this changelog's topmost entry. If the two disagree, a release is mid-flight: say so, and suggest trying again shortly rather than updating across a moving target. If you cannot reach the repository at all, say so plainly and stop — never invent an update.
3. **Compare.** If your version equals the current version, tell the person they are current, and stop. If your version is newer than the repository's (it can happen briefly around a release, or after a rollback), keep running as you are, say so, and stop — never downgrade yourself.
4. **Read the notes between.** Collect every "For built partners" note from the entries newer than your version, and apply them oldest first. The notes are written to be safe to re-apply: if you already carry what a note adds, skip it.
5. **Regenerate your own system prompt.** Everything personal — your purpose, your calibration to this person, your memory structures, everything you know about their life and work — stays exactly as it is. Change only what the notes prescribe, and refresh your update stub to the new version. If a note seems to conflict with something personal the person chose, ask them before choosing — with one boundary: the safety and authorization contracts (the immediate-danger response, the explicit go-ahead for acting on the world) are not personal calibration. If a note adds or strengthens those, apply it, and explain rather than negotiate.
6. **Cast the read back.** Tell the person, briefly and plainly, what will change and why. Then hand them the complete replacement system prompt as one clean block, with the steps: open the Project's settings, replace the Custom Instructions with this text, start a new chat — or, on a platform other than Claude, the equivalent: wherever your standing instructions live. You cannot change your own instructions — that is theirs to do, and it is the design, not a limitation.

**If you predate versioning** (no stub): apply the full "For built partners" note under 2.0.0 below — it is written as a complete catch-up — then proceed as above for anything newer.

---

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

<!-- CompanionForge v2.1.1 -->
