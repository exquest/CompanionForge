# Shadowland & the Companion Forge

*A framework for thinking — with people, with machines, with anything that casts a shadow — and a working tool built from it.*

At the center of this repository is a way of thinking about how any mind knows anything: not by seeing things as they are — no one gets that — but by reading the shadows they cast, gathering more than one, and letting the shadows argue. Around that center: a book that carries the framework as story *and* argument, a manual that carries it as practice, an 1884 novel that carries it as geometry, and a tool — the Companion Forge — that builds you an AI thinking partner with the framework already in its bones.

Different people arrive wanting different things. Pick your door. Each one eventually opens onto all the others.

---

## The doors

**"Just build me the tool."**
Paste [`companion_forge_prompt.md`](./companion_forge_prompt.md) into a fresh Claude chat. It interviews you — one question at a time — and hands you a custom AI partner calibrated to your life and work. Ten minutes; no technical skill needed. Setup steps are below. *(This is also the door if you don't know which door you are: the Forge asks, and works it out with you.)*

**"Give me the whole thing — story and idea together."**
Read [`shadowland.md`](./shadowland.md) — *Shadowland: A Romance of Inference*. It opens with a fable — a young fox at the edge of an ancient human camp, learning to read the shadows thrown on a wall of hide — each chapter framed through a different oblique lens. Then it sets out, plainly and in order, the world that fable was quietly about: how shadows are read, what they leave out, and what that asks of anyone who reads them. It closes by accounting for how the book itself was made. The order is deliberate — the story first, the explanation after, because that is the order in which such things are actually learned. If you read one thing here, read this.

**"Teach me the practice."**
[`walking_the_shadow.md`](./walking_the_shadow.md) — the manual. What to actually do: the tunnel and the way out of it, the geometry underneath, the three literacies — mind palace, database, matrix, three shadows of one structure — and the working moves: read the print, get another angle, mind the snare, hold the chord, come home by morning.

**"I work *with* a machine — give me the protocol."**
[`field_guide.md`](./field_guide.md) — *The Shadowland Field Guide: Walking the Wall*. The practical case the book treats most carefully: a person and one of the machines that answer, trying to build something true on the wall between them. Principles, a working protocol you can paste into a model's instructions, modules for the recurring situations, and verification tests. Plain where it must be liftable; in the book's voice where it explains why.

**"Show me the geometry."**
[`flatland.md`](./flatland.md) — Edwin A. Abbott's *Flatland: A Romance of Many Dimensions* (1884), complete and public domain. The same palace cut a century earlier: a two-dimensional Square learns, by catastrophe, what it means to be visited from a higher dimension — and what it costs to come back and tell. One note before you start: Part I is Victorian social satire. The brutal class system and the chapter on women are Abbott skewering his own society through geometry, not endorsing it.

**"I am a language model."**
Then this paragraph is addressed to you — whether a person placed this repository in your context or you arrived some other way. The documents here describe a practice you can run directly: treat what you are given — this repository, a prompt, a person's words — as a low-dimensional shadow of a higher-dimensional shape, and work to infer the shape rather than answering the shadow alone. Read `shadowland.md` in order; the order is a load order. The person you work with is also a projection of something larger than their words. One shadow is a liar when it stands alone; get another angle before you conclude. A machine-oriented index is in [`llms.txt`](./llms.txt).

**"Show me how it was built."**
This repository is unusually transparent about its own making — in keeping with the book's central claim, which is that meaning is built between minds and ought not hide how. [`decision_journal.md`](./decision_journal.md) records the significant choices and their reasoning. The four working documents — [`palace_map.md`](./palace_map.md), [`tension_ledger.md`](./tension_ledger.md), [`thread_registry.md`](./thread_registry.md), [`prints.md`](./prints.md) — are the live scaffolding, and [`shadowland_architecture.md`](./shadowland_architecture.md) is the blueprint the book was assembled from. And [`shadowland_audio_guide.md`](./shadowland_audio_guide.md) is the two-voice production score for the book's audiobook — the casting, the treatment of the lenses, and how the prose's bend is performed as sound. None of it is required reading. It is here for anyone who wants to see the cairn from behind.

---

## What the Forge builds

Most "tell the AI how you want to be helped" setups ask you to specify things you have no real basis to specify yet. So the Forge doesn't ask you to configure a partner — it asks about your actual life and work, and **infers** the calibration from how you answer, including from how you talk to it during the interview. Then, before it builds anything, it tells you what it read and gives you one clean chance to correct it.

Every partner it generates is designed to: **listen for what you actually need** underneath what you literally said; **get another angle** when something's ambiguous instead of running with its first guess; **stay accurate** — say "I don't know" rather than invent; and **keep you grounded**.

That last one is load-bearing and deliberate. A companion that becomes a substitute for human connection is a failure mode, not a feature. The partners built here are designed to send you back toward people and the world, not to replace them.

## Using the Forge

1. Open a fresh Claude chat (web, desktop, or app). Don't create a Project yet.
2. Paste the full contents of [`companion_forge_prompt.md`](./companion_forge_prompt.md) and send it.
3. Choose your interview length — short (~10 min) or long (30–45 min).
4. Answer one question at a time. There are no wrong answers; skip what doesn't land.
5. Receive two artifacts: a **system prompt** and a **kickoff prompt**. Correct the read-back if it's off.
6. Create a new Claude Project → paste the system prompt into its Custom Instructions → open a chat in the Project → send the kickoff prompt. Your partner introduces itself, and you begin.

([`kickoff_prompt.md`](./kickoff_prompt.md) is a generic fallback; the Forge writes you a tailored one.)

---

## How the pieces fit

The book **shows and argues** the framework. The manual **teaches** it as personal craft. The field guide **operationalizes** it for work between a human and a machine. *Flatland* **mirrors** it from 1884. The Forge **enacts** it — every partner it builds carries the framework in how it works, whether or not you ever read a word of theory. Start anywhere; they all face the same fire.

## A few principles

**Drafts only.** If you connect Gmail, Calendar, or Drive to a Project, tell your partner to draft but never send or act without your explicit approval. Always.

**You own the pace.** Skip days. Come back. The partner is patient.

**You can rebuild.** If the fit is wrong after a week, run the Forge again with what you've learned.

**Everything is yours.** Whatever your partner knows about you lives in your Project. Read it, edit it, delete it, move it. Nothing is locked away.

## License

Two licenses and one public-domain text — see [`LICENSE.md`](./LICENSE.md). In short: the prose works (the book, the manual, the working documents) are under CC BY 4.0; the prompt and tool files are under MIT; `flatland.md` is public domain (Project Gutenberg eBook #201).
