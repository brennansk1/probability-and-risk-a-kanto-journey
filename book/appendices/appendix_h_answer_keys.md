<!--
  appendix: h_answer_keys
  status: done
-->

# Appendix H — Consolidated Answer Keys {.type-normal}

Every problem in this book already travels with its **full worked solution** — not just a final letter — at the end of its own chapter, inside that chapter's `::: answer-key` block. This appendix does **not** reprint those solutions; it is the consolidated index that points you to them, plus the master quick-answer table for fast self-grading. The full reasoning lives where it belongs, beside the problem; this page is the map.

::: trainers-tip
**WHY THE FULL SOLUTIONS STAY IN THE CHAPTERS**

A worked solution is a teaching object: it is most useful read *immediately after* you attempt the problem, with the chapter's Pokédex Entries and worked examples one scroll away. Ripping all the solutions into a single back-of-book dump would break every back-reference and tempt you to peek. So each chapter keeps its own complete key (archetype-labeled and cross-referenced to the Entry it tests), and this appendix tells you exactly where each key is and what each problem's final answer is.
:::

## H.1 — Where each chapter's full answer key lives

Each chapter's problem set is wrapped in `::: problem-set` and its full worked solutions in the `::: answer-key` block that immediately follows, at the end of the same chapter file. Problem IDs use the chapter-number prefix `C{n}.{k}` (for example, **C10.3** is the third problem of Chapter 10, *Pricing the Risk*).

| Problem IDs | Chapter | Title | Topic |
|---|---|---|---|
| **C0.×** | Ch 0 | Orientation — How to Use This Book | front matter |
| **C1.×** | Ch 1 | The Toolkit I — Numbers, Functions & Notation | prerequisite |
| **C2.×** | Ch 2 | The Toolkit II — Series & Calculus | prerequisite |
| **C3.×** | Ch 3 | The Space of Possible Outcomes | 1 — General |
| **C4.×** | Ch 4 | Counting the Uncountable | 1 — General |
| **C5.×** | Ch 5 | Reasoning From Evidence (Bayes) | 1 — General |
| — | Ch 5x | Checkpoint A — The Rocket Hideout | review |
| **C6.×** | Ch 6 | Variables of Fortune | 2 — Univariate |
| **C7.×** | Ch 7 | Center & Spread | 2 — Univariate |
| **C8.×** | Ch 8 | The Named Patterns I — Discrete Distributions | 2 — Univariate |
| **C9.×** | Ch 9 | The Named Patterns II — Continuous Distributions | 2 — Univariate |
| **C10.×** | Ch 10 | Pricing the Risk | 2 — Univariate |
| — | Ch 10x | Checkpoint B — The Univariate World | review |
| **C11.×** | Ch 11 | Two Fates Entwined (joint distributions) | 3 — Multivariate |
| **C12.×** | Ch 12 | Expectation Within Expectation | 3 — Multivariate |
| **C13.×** | Ch 13 | Combining Forces (covariance & sums) | 3 — Multivariate |
| **C14.×** | Ch 14 | Order From Chaos (order statistics & CLT) | 3 — Multivariate |
| **C15.×** | Ch 15 | Champion's Challenge — Mock Exams | all |

The two checkpoints (5x, 10x) carry their own self-contained keys inside their `::: answer-key` blocks; their items are spaced-retrieval review rather than numbered `C{n}.{k}` problems.

## H.2 — How to use the keys without spoiling the practice

::: pokedex-entry
**POKÉDEX ENTRY — The three-pass self-grading loop**

1. **Attempt cold.** Solve the problem fully on paper before opening any key — no peeking at the first line.
2. **Grade the answer, then the method.** Check your final value against the quick-answer table (H.3). Only after that, read the chapter's full worked solution to compare your *path*, not just your number.
3. **Tag and re-drill.** Every chapter solution carries an **archetype label** and a back-reference to the Pokédex Entry it tests. Log the archetype of anything you missed; when several misses share an archetype, that is your next drill target — reinforce with the matching SOA sample-question cluster in Appendix F.

*Recognition cue:* a right answer reached by a wrong method is a future wrong answer. Always reconcile the *method*, not only the final letter.
:::

## H.3 — Master quick-answer table

The single consolidated final-answer table for every problem in the book is **generated, not hand-maintained**, so it can never silently drift from the worked solutions it summarizes. Each chapter's `::: answer-key` block ends with that chapter's quick-answer table; the build assembles those per-chapter tables into one master grid here at compile time, keyed by problem ID.

::: trainers-tip
**INTEGRITY GUARANTEE (why you can trust these numbers)**

Per the production plan's integrity gates, **every** printed answer in this book is recomputed by the verification harness (`sims/verify_examples.py`, seed `151`) — in closed form where possible, otherwise by Monte Carlo — and asserted against the value printed in the chapter solution and in this table. The audit additionally cross-reads each problem against its worked steps and its quick-answer entry so the three never disagree. **A build with a single answer-key mismatch fails and does not ship.** That is why this consolidated table is auto-assembled from the verified per-chapter keys rather than retyped here: retyping would reintroduce exactly the silent drift the harness exists to prevent.
:::

To self-grade in bulk after a study block: work a chapter's problems cold, then scan its quick-answer table (chapter-end) or this consolidated grid for the final values, and reserve the full worked solutions for the items you missed.
