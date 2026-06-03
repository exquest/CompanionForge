# The Companion Forge

*A prompt that interviews you and builds you a custom AI partner.*

---

## What this is

The Companion Forge is a single prompt you paste into a fresh Claude chat. It **interviews you** — asking questions one at a time, adapting as it learns — and then hands you two finished pieces of text:

1. A **system prompt** that defines a custom AI partner calibrated to your life and work
2. A **kickoff prompt** to start your first real conversation with it

You paste those into a new Claude Project, and from then on you have a thinking companion that knows your world, maintains its own notes and documentation about your projects, and gets sharper about you over time.

You run the Forge once. Setup takes a few minutes. You don't need to be technical.

---

## Why it works the way it does

Most "tell the AI how you want to be helped" setups ask you to specify things you have no real basis to specify yet. *Do you want it to challenge you or encourage you? Short answers or long? Proactive or reactive?* Cold, those questions are almost impossible to answer well — you find out what you want by using the thing, not by predicting it in advance.

So the Forge doesn't mostly ask you to configure a partner. It asks you about your actual life and work, and **infers** the calibration from how you answer — including from how you talk to it during the interview. Someone who argues and tests gets a partner that can take it. Someone who needs the chaos organized gets a partner that organizes. Then, before it builds anything, it tells you what it read and gives you one clean chance to correct it.

The same care runs through the partner it builds. Every partner the Forge generates is designed to:

- **Listen for what you actually need** underneath what you literally said
- **Get another angle** when something's ambiguous, instead of running with its first guess
- **Stay accurate** — tell you when it doesn't know rather than inventing
- **Keep you grounded** — a good partner keeps you connected to your real life and the people in it, never pulls you away into itself

That last principle is load-bearing and deliberate. A companion that becomes a substitute for human connection is a failure mode, not a feature. The partners built here are designed to send you back toward people and the world, not to replace them.

---

## How to use it

### Step 1 — Start a regular Claude chat
Open Claude (web, desktop, or app). **Don't create a Project yet.** Just start a normal new conversation.

### Step 2 — Paste the Forge prompt
Copy the full contents of [`companion_forge_prompt.md`](./companion_forge_prompt.md) and paste it as your first message. Send it.

### Step 3 — Choose your interview length
The Forge will ask whether you want a **short interview** (~10 minutes, working partner fast) or a **longer one** (30–45 minutes, more tailored). Pick what fits your time. You can always rebuild later.

### Step 4 — Answer the questions
One at a time, conversational. There are no wrong answers. If a question doesn't land, say so and you'll move on. Take your time with the ones that matter.

### Step 5 — Receive your two artifacts
When the interview ends, the Forge produces two labeled blocks of text:
1. **The system prompt** — the long one that defines your partner
2. **The kickoff prompt** — the short first message you'll send to begin

It will also tell you what it read about you before generating — correct it if it's off.

### Step 6 — Set up your Project
Following the Forge's instructions, you'll:
1. Create a new Claude Project (in the Projects section of Claude)
2. Paste the system prompt into the Project's **Custom Instructions**
3. Open a new chat inside that Project
4. Send the kickoff prompt as your first message

Your partner will introduce itself and you'll begin.

---

## What's in this repo

| File | What it is |
|------|------------|
| [`companion_forge_prompt.md`](./companion_forge_prompt.md) | The main prompt. This is the thing you paste into a fresh Claude chat to run the interview. |
| [`kickoff_prompt.md`](./kickoff_prompt.md) | A generic fallback kickoff prompt. The Forge generates a tailored one for you — this is just an example / shortcut. |
| [`shadowland.md`](./shadowland.md) | The thinking the Forge is built on, as a fable and a working essay. Optional reading. You can also paste it into your partner's Project knowledge if you want your partner to be able to teach from it. |

---

## A few principles to know

**Drafts only.** If you connect Gmail, Calendar, or Drive to your Project, tell your partner to draft but never send or act without your explicit approval. The Forge's setup instructions remind you of this. Always.

**You own the pace.** Daily use builds richness, but no session is mandatory. Skip days. Come back. The partner is patient.

**You can rebuild.** If the personality doesn't fit after a week, run the Forge again with what you've learned. The new version will be better.

**Everything is yours.** Whatever your partner knows about you lives in your Project. You can read it, edit it, delete it, or move it. Nothing is locked away.

---

## About `shadowland.md`

The Forge and the partners it builds are grounded in a small set of ideas about how understanding actually works — that all knowing is partial, that meaning gets built *between* two minds rather than transmitted whole, and that the real skill in working with an AI is staying grounded in your own life while reaching into deep ideas with it. `shadowland.md` lays this out as a short fable and a companion essay.

You don't need to read it to use the Forge. It's there if you're curious about the *why* — and if you want your partner to be able to teach this way of thinking back to you, you can add it to your Project's knowledge. The essay is deliberately written as one person's working notes, not as settled doctrine. It argues with itself. Push back on it. That's the point.

---

When you're ready, paste [`companion_forge_prompt.md`](./companion_forge_prompt.md) into a fresh Claude chat and begin.
