<!--
  file: ch05_bayes
  tier: A
  outcomes: 1c,1d,1e,1f,1g
  draft1_source: drafts/chapters_draft1/ch04_cerulean_city.md
  maps_to: Cerulean, Misty — the proving ground
-->

# Reasoning From Evidence {.type-water}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Cerulean City highlighted; the route from Pewter across Mt. Moon is now complete." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — you have crossed Mt. Moon and reached Cerulean City, home of the Cascade Badge and the city of <em>inference</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Phantom of the Pokémon Center"**

You walk into Cerulean to chaos. The bridge into town is cordoned with tape, Officer Jenny is pacing, and a rumor races down the street: a *phantom thief* has been slipping into the Pokémon Center at night and emptying trainers' item bags. Last night it struck again.

"We have a witness," Jenny says, frowning at her notepad. "Whoever it was had a **Water-type Pokémon** with them — there were wet footprints all the way to the door." She looks at you. "Problem is, half the trainers in this town carry Water-types. Cerulean's practically the water capital of Kanto."

She spreads three suspect files on the table.

- A **traveling trainer** — there are a *lot* of them passing through, but they're usually careful.
- A **local** — common too, and they almost never leave a mess.
- A **Team Rocket grunt** — *rare* near the Center, but they strike often and they're sloppy; when they *do* strike they almost always leave wet footprints behind.

"The clue points at *someone*," Jenny says, tapping the wet-footprints note. "But who?"

Beside you, a red-haired girl scoffs. You don't know it yet, but this is **Misty**, the Cerulean Gym Leader. "So you're going to accuse *everyone* with a Squirtle? That's ridiculous."

Pikachu's ears twitch. The obvious answer — *"it was the Rocket grunt, they're criminals!"* — *feels* too easy. There are far more ordinary trainers in this town than there are Rocket grunts. A rare-but-sloppy suspect and a common-but-careful one can leave the *exact same clue*. The footprints alone cannot tell you who.

You realize "guilt" is really three things stacked together: *how common* each suspect is near the Center, *how often* they strike at all, and *how often* a strike leaves the wet-footprint clue — and the footprints only ever appear when someone actually strikes. You'll need to *combine* the clue with all three — to run the evidence **backward**, from "what we observed" to "who probably did it."

And you don't yet know how. *How do you turn a clue into a probability of guilt?*
:::

## Where You Are — 60-Second Retrieval

You're holding the Boulder Badge from Pewter. Back there, in the previous chapter, you built the **sample space** $S$ — the set of all outcomes — and learned to read a probability off equally likely outcomes,

$$P(A) = \frac{\text{number of outcomes in } A}{\text{number of outcomes in } S},$$

and you drew **Venn diagrams** to picture an event $A$ as a region inside the rectangle $S$. You also learned to **count** outcomes (the $\binom{n}{k}$ work on the route in).

That is exactly the foundation this chapter stands on. **Conditioning** — the first idea of Cerulean — is nothing more than *cropping that Venn rectangle down to a smaller world*. The "without replacement" draws ahead reuse your counting. Take sixty seconds and prove you still own these before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. A bag holds 4 red and 6 blue lures. You draw one at random. What is $P(\text{red})$? *(Answer: $4/10 = 0.4$.)*
2. In a Venn diagram, what region is $A \cap B$? What region is $A \cup B$? *(Answer: the overlap; everything inside either circle.)*
3. How many ways can you choose 2 Pokémon from 5? *(Answer: $\binom{5}{2}=10$.)*

All three instant? You're ready. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode as you stare at the three files.

"Cerulean is the city of *inference*, Ash. Every mystery here is the same mathematical act: you observe **evidence**, and you **update** what you believe about a hidden cause. That is the entire engine of conditional probability — and its crown jewel, **Bayes' theorem**. Master this one chapter and you can price a fraudulent insurance claim, read a medical test correctly, or unmask a phantom thief. This is the proving ground. Take it slowly; everything after stands on it."

By the end of this chapter you will be able to:

- **Compute** conditional probabilities $P(A \given B)$ and chain them with the **multiplication rule**. *(Outcome 1c.)*
- **Use** the **addition rule** for unions, and **recognize and apply independence** — pairwise versus mutual — without confusing it with "mutually exclusive." *(Outcomes 1d, 1e.)*
- **Assemble** an unconditional probability with the **law of total probability** over a partition of cases. *(Outcome 1f.)*
- **Invert** conditional probabilities with **Bayes' theorem** (two-way and $n$-way), using the detective's-grid method, and explain why a strong clue need not imply guilt. *(Outcome 1g.)*

> *Exam-weight signpost.* Conditional probability, independence, and Bayes together are among the **most heavily tested** ideas in Exam P's General Probability section. This is a **Tier A** chapter: it earns the full treatment, and what you build here is reused in every chapter that follows.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Cerulean?**

Already fluent? Prove it. Work these four, ~3 minutes each, *with correct method*:

1. $P(A)=0.4$, $P(B)=0.5$, $P(A\cap B)=0.25$. Find $P(A\given B)$ and decide whether $A,B$ are independent.
2. A bag has 7 Poké Balls and 3 Great Balls; draw two without replacement. Find $P(\text{both Poké})$.
3. Days are rainy $30\%$ of the time; the gym floods w.p. $0.5$ on rainy days, $0.05$ on dry days. Find $P(\text{flood})$.
4. A scan is $95\%$ sensitive with an $8\%$ false-positive rate; $2\%$ of Pokémon are sick. One scans positive. Find $P(\text{sick}\given\text{positive})$.

*(Answers: $0.5$, **not** independent; $\tfrac{7}{15}\approx0.467$; $0.185$; $\approx0.195$.)* Four for four with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built exactly for you — read on. Each concept has its own skip-gate too, so even a partial owner loses no time.
:::

---

Six ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **Conditioning** — shrinking the world *(the foundation everything else uses)*
2. **The multiplication rule** — walking a probability tree
3. **The addition rule** — "or," and the overlap you must subtract
4. **Independence** — and the trap of confusing it with "mutually exclusive"
5. **The law of total probability** — the forward, weighted-average direction
6. **Bayes' theorem** — running the clue backward *(the crown jewel)*

## Concept 1 — Conditioning: Shrinking the World

::: concept-gate
**DO YOU ALREADY OWN THIS? — Conditioning**

In a town of 60 trainers, 24 carry a Water-type and, of those 24, exactly 9 are Cerulean locals. You stop a trainer at random and see they carry a Water-type. What is the chance they're a local?

If you immediately answered **$\tfrac{9}{24} = 0.375$** (not $\tfrac{9}{60}$), you own conditioning — **skip to Concept 2**. If you wrote $\tfrac{9}{60}$, or you're not sure why it's $24$ on the bottom and not $60$, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *When you learn that $B$ happened, your entire world collapses down to $B$, and the chance of $A$ is just $A$'s share of that smaller world.*

**Beat 2 — Anchor + concrete instance.** Remember the Venn rectangle from Pewter: all of $S$. Conditioning *crops* that rectangle. Here is the story, with real numbers.

Outside Nurse Joy's Center stand **60 trainers**. Of them, **24 carry a Water-type Pokémon**. And of those 24 Water-type owners, **9 are Cerulean locals** (the rest are passing through). You stop one trainer at random and notice — they're carrying a Water-type. *Given that*, how likely is it they're a local?

**Beat 3 — Reason through it in plain words.** The instant you see the Water-type, the 36 trainers who *don't* carry one stop mattering. They cannot be the person in front of you. Your world is no longer all 60 trainers — it is just the **24 Water-type owners**. Inside that shrunken world, the locals are the 9. So the chance is

$$\frac{9 \text{ locals}}{24 \text{ Water-type owners}} = \frac{9}{24} = 0.375.$$

You *threw away* the 36 who don't fit the evidence, and re-weighed what was left.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural mistake is to leave the denominator at 60:

$$\frac{9}{60} = 0.15. \qquad\textbf{(wrong)}$$

But $\tfrac{9}{60}$ answers a *different* question: "pick any trainer at random — what's the chance they're *both* a local *and* a Water-type owner?" That is the share of the **whole** town, *before* you saw anything. The evidence already told you the person carries a Water-type; you are no longer picking from all 60. Forgetting to shrink the denominator is the single most common conditioning error — and we'll meet its grown-up form (the *prosecutor's fallacy*) at the end of the chapter. Keep the picture: **the world shrank, so the bottom must shrink too.**

**Beat 5 — Translate into notation, one glyph at a time.** Name the two events.

- Let $A$ = "the trainer is a local."
- Let $B$ = "the trainer carries a Water-type."

We want "the probability of $A$, *given that* $B$ happened." We write a vertical bar for the words "given that":

$$P(A \given B) \qquad \text{read aloud: ``the probability of } A \text{ given } B\text{.''}$$

The bar $\given$ always reads **"given that"** — everything to its *right* is the world you have shrunk into. Next, the event "the trainer is a local *and* a Water-type owner" uses the **intersection** symbol:

$$A \cap B \qquad \text{read aloud: ``}A \text{ and } B\text{'' or ``}A \text{ intersect } B\text{''} \quad (\text{both happen}).$$

In our numbers, the 9 locals-with-Water-types are exactly $A \cap B$, and the 24 Water-type owners are $B$. So

$$P(A \given B) = \frac{9/60}{24/60} = \frac{9}{24} = 0.375.$$

Notice the $60$'s cancel — *dividing two counts is the same as dividing two probabilities*. That cancellation **is** the whole formula.

**Beat 6 — Generalize: derive the formula from the instance.** Replace the specific counts with their probabilities. "$A$ and $B$" has probability $P(A\cap B)$; "$B$" has probability $P(B)$. Shrinking to $B$ and taking $A$'s share is exactly dividing them:

$$\boxed{\,P(A \given B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.\,}$$

We did not assert this — we *built* it by replacing the two counts with their two probabilities.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the case above — read $P(A\cap B)$ and $P(B)$ off the counts, divide.
- *A twist that breaks easy intuition:* $P(A\given B)$ and $P(B\given A)$ are **not** the same number. Here $P(\text{local}\given\text{Water}) = \tfrac{9}{24} = 0.375$, but $P(\text{Water}\given\text{local})$ shrinks to the *locals* first — if there were, say, 15 locals total, it would be $\tfrac{9}{15} = 0.6$. Same overlap on top, different world on the bottom. **The bar is not symmetric.** (This asymmetry is the entire reason Bayes' theorem has to exist.)
- *Boundary case:* if every Water-type owner were a local, $P(A\given B)=\tfrac{24}{24}=1$ — certainty. If none were, $\tfrac{0}{24}=0$. Conditional probabilities still live in $[0,1]$; they're just probabilities in a smaller world.

**Beat 8 — Picture it.** The figure makes the "shrink" literal: the full town on the left, the cropped Water-type world on the right.

<figure>
<img src="../../assets/diagrams/ch04_conditioning_shrink.png" alt="Two panels. Left: a rectangle of 60 trainers (the full sample space S) with a shaded subset B of 24 Water-type owners, and inside it a darker sliver of 9 locals. Right: the same B re-cropped to fill the whole frame, so the 9-local sliver is now 9 out of 24, visually showing that conditioning renormalizes by dividing by P(B)." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Conditioning crops the world: the 9 locals are $9/60$ of all trainers but $9/24$ of the Water-type world. Re-cropping to $B$ <em>is</em> dividing by $P(B)$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any "given that…" statement, identify the shrunken world $B$, and compute $A$'s share of it. That single move — *shrink the denominator* — is the seed of every remaining idea in this chapter.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Conditional Probability**

$$P(A \given B) = \frac{P(A \cap B)}{P(B)}, \qquad P(B) > 0.$$

*In plain terms:* given that $B$ has happened, the chance of $A$ is $A$'s share of $B$'s world. Throw away everything outside $B$; re-weigh what remains so it sums to one.

*Why $P(B)>0$:* you cannot condition on an impossible world — dividing by $P(B)=0$ is undefined. There is no "given $B$" if $B$ can never happen.

*Recognition cue:* the words **"given that," "if we know," "among those who,"** or **"of the ___ that ___."** Whenever a problem hands you a fact and then asks about something *inside* that fact — **condition** (shrink the denominator).
:::

## Concept 2 — The Multiplication Rule: Walking a Tree

::: concept-gate
**DO YOU ALREADY OWN THIS? — Multiplication Rule**

A bag has 7 Poké Balls and 3 Great Balls. You draw two in the dark, *without* putting the first back. What is $P(\text{both Poké})$?

If you wrote **$\tfrac{7}{10}\cdot\tfrac{6}{9} = \tfrac{7}{15}\approx 0.467$** (and can say *why it's $6/9$, not $7/10$, on the second draw), **skip to Concept 3**. If you wrote $\tfrac{7}{10}\cdot\tfrac{7}{10}=0.49$, read on — that answer secretly assumes you put the ball back.
:::

**Beat 1 — The one-sentence idea.** *The chance that two things both happen is the chance of the first, times the chance of the second given the first — you walk down a branch of a tree, multiplying as you go.*

**Beat 2 — Anchor + concrete instance.** This is just Concept 1 rearranged. We had $P(A\given B) = P(A\cap B)/P(B)$; multiply both sides by $P(B)$ and you get a way to *build* $P(A\cap B)$ instead of read it off.

Brock hands you his bag for the road: **7 Poké Balls and 3 Great Balls**, jumbled. You'll draw **two in the dark, without replacement**. You need both to be Poké Balls. *What is $P(\text{both Poké})$?*

**Beat 3 — Reason through it in plain words.** First draw: 7 of the 10 balls are Poké, so the chance the first is Poké is $\tfrac{7}{10}$. Now — crucially — the world shrank. One Poké Ball is gone. **9 balls remain, 6 of them Poké.** So the chance the *second* is Poké, *given the first was*, is $\tfrac{6}{9}$. To get *both*, you walk down the "first is Poké" branch and then the "second is Poké" branch, multiplying:

$$\frac{7}{10}\cdot\frac{6}{9} = \frac{42}{90} = \frac{7}{15} \approx 0.467.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting move is to reuse $\tfrac{7}{10}$ for the second draw:

$$\frac{7}{10}\cdot\frac{7}{10} = 0.49. \qquad\textbf{(wrong — assumes replacement)}$$

But you *didn't* put the first ball back. After removing a Poké Ball, only 6 of the remaining 9 are Poké — not 7 of 10. Reusing $\tfrac{7}{10}$ silently pretends the bag was refilled. The phrase **"without replacement"** is the whole point: the second probability is *conditional* on the first. (Note $0.467 < 0.49$ — removing a Poké Ball makes the second slightly *less* likely, exactly as it should.)

**Beat 5 — Translate into notation, one glyph at a time.** Let $P_1$ = "first is Poké," $P_2$ = "second is Poké." We want $P(P_1 \cap P_2)$ — *both*. Take the conditional definition $P(P_2\given P_1) = P(P_1\cap P_2)/P(P_1)$ and multiply both sides by $P(P_1)$:

$$P(P_1 \cap P_2) = P(P_1)\cdot P(P_2 \given P_1).$$

Read it left to right: **"the chance of both equals the chance of the first, times the chance of the second given the first."** Each factor is a number we already found: $P(P_1) = \tfrac{7}{10}$ and $P(P_2\given P_1) = \tfrac{6}{9}$.

**Beat 6 — Generalize: derive the formula from the instance.** Two events is just multiplying both sides of the conditional definition by $P(B)$. For a *chain* of stages, you keep conditioning on everything that came before:

$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1)\,P(A_2 \given A_1)\,P(A_3 \given A_1\cap A_2)\cdots P(A_n \given A_1\cap\cdots\cap A_{n-1}).$$

Each new factor is "given everything so far" — you just walk further down the same branch.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* both Poké, as above.
- *Twist:* what's $P(\text{the two draws differ in type})$? Easiest by the **complement** of "same type":
$$P(\text{same}) = \underbrace{\tfrac{7}{10}\cdot\tfrac{6}{9}}_{\text{both Poké}} + \underbrace{\tfrac{3}{10}\cdot\tfrac{2}{9}}_{\text{both Great}} = \tfrac{42}{90}+\tfrac{6}{90} = \tfrac{48}{90}, \qquad P(\text{differ}) = 1 - \tfrac{48}{90} = \tfrac{42}{90} = \tfrac{7}{15}.$$
(Notice we *added* two branches here — a preview of Concept 3.)
- *General/edge:* three Poké in a row multiplies three factors, $\tfrac{7}{10}\cdot\tfrac{6}{9}\cdot\tfrac{5}{8}$. The denominators march down $10, 9, 8$ because the bag keeps shrinking.

**Beat 8 — Picture it.** A probability tree turns the rule into a road map: each *path* is a sequence of branches, each *leaf* is the product along its path.

<figure>
<img src="../../assets/diagrams/ch04_probability_tree.png" alt="A two-stage probability tree for a bag of 7 Poke Balls and 3 Great Balls drawn without replacement. The root splits into Poke (7/10) and Great (3/10). The Poke branch splits into Poke (6/9) and Great (3/9); the Great branch splits into Poke (7/9) and Great (2/9). Each of the four leaves is labeled with its multiplied path probability: 42/90, 21/90, 21/90, 6/90." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>The multiplication rule as a tree: walk a path, multiply the branch probabilities, read the leaf. The four leaves sum to 1.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now build the probability of a *sequence* of events by multiplying conditional probabilities down a tree — and you know to **renormalize each later draw** to the shrunken world.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Multiplication Rule (and Chain Rule)**

$$P(A \cap B) = P(B)\,P(A \given B) = P(A)\,P(B \given A).$$

For a chain of stages,
$$P(A_1 \cap \cdots \cap A_n) = P(A_1)\,P(A_2 \given A_1)\cdots P(A_n \given A_1\cap\cdots\cap A_{n-1}).$$

*In plain terms:* multiply down the tree branch — each new factor is "given everything so far."

*Recognition cue:* **"and then," sequential draws without replacement, stages, a tree diagram.** When events unfold in order, multiply the conditional probabilities along the path.
:::

## Concept 3 — The Addition Rule: "Or," and the Overlap

::: concept-gate
**DO YOU ALREADY OWN THIS? — Addition Rule**

On Route 24 you log 100 Pokémon: 40 are Water-type, 30 live in tall grass, 12 are *both*. Pick a log entry at random. What is $P(\text{Water } \textbf{or}\text{ grass})$?

If you answered **$0.58$** (not $0.70$) and can say *why you subtract the 12*, **skip to Concept 4**. If you got $0.70$, read on — you double-counted the overlap.
:::

**Beat 1 — The one-sentence idea.** *The chance of $A$ **or** $B$ is the two pieces added together, minus the overlap you would otherwise count twice.*

**Beat 2 — Anchor + concrete instance.** Back to the Venn diagram: two circles, $A$ (Water-type) and $B$ (tall grass), inside the rectangle of 100 logs. The circles **overlap** in the 12 Pokémon that are both.

On **Route 24** you log **100 Pokémon**: **40 Water-type**, **30 live in tall grass**, **12 are both**. *What fraction is Water-type or grass-dwelling (at least one)?*

**Beat 3 — Reason through it in plain words.** If you just add the two piles, $40 + 30 = 70$, you've counted those **12 "both" Pokémon twice** — once in the Water pile, once in the grass pile. Each is one Pokémon, not two. So subtract the 12 back out, once:

$$40 + 30 - 12 = 58 \quad\Longrightarrow\quad P(\text{Water or grass}) = \frac{58}{100} = 0.58.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting answer is

$$P(A) + P(B) = 0.40 + 0.30 = 0.70. \qquad\textbf{(wrong — double-counts the 12)}$$

This is right *only* when the circles don't overlap. Here they do, so $0.70$ over-counts by exactly the overlap $\tfrac{12}{100}=0.12$, leaving the correct $0.58$. The reverse mistake is just as common: **assuming events can't overlap when they can.** Don't assume the overlap is zero — *check it*.

**Beat 5 — Translate into notation, one glyph at a time.** "$A$ or $B$" (at least one occurs) uses the **union** symbol:

$$A \cup B \qquad \text{read aloud: ``}A \text{ or } B\text{'' / ``}A \text{ union } B\text{.''}$$

The overlap "$A$ and $B$" you already met: $A\cap B$. "Subtract the overlap once" becomes

$$P(A \cup B) = P(A) + P(B) - P(A \cap B).$$

When two events **cannot co-occur**, their overlap is the **empty set**:

$$A \cap B = \varnothing \qquad \text{read aloud: ``}A \text{ and } B \text{ are mutually exclusive / disjoint.''}$$

Then $P(A\cap B)=0$ and the subtraction disappears.

One more glyph we'll need in the very next step — and constantly from here on. The event "$A$ does **not** happen" gets a small superscript $c$:

$$A^c \qquad \text{read aloud: ``}A\text{-complement'' / ``not }A\text{''} \quad (\text{everything in } S \text{ outside } A).$$

Since $A$ either happens or it doesn't, $A$ and $A^c$ together fill the whole world: $P(A) + P(A^c) = 1$. (That single fact powers every "$1 - P(\text{none})$" shortcut you'll use.)

**Beat 6 — Generalize: derive the formula from the Venn partition.** Don't just assert it — *count* it. Partition the union $A\cup B$ into three disjoint regions: "$A$ only" ($A\cap B^c$, i.e. in $A$ but **not** $B$), "$B$ only" ($A^c\cap B$), and "both" ($A\cap B$). Because the regions are disjoint, their probabilities simply add:
$$P(A\cup B) = P(A\cap B^c) + P(A^c\cap B) + P(A\cap B).$$
Now notice $P(A) = P(A\cap B^c) + P(A\cap B)$ and $P(B) = P(A^c\cap B) + P(A\cap B)$ — each single event is "its own-only region plus the shared middle." Add those two and the middle $P(A\cap B)$ gets counted **twice**; subtract one copy to recover the union:

$$\boxed{\,P(A \cup B) = P(A) + P(B) - P(A \cap B).\,}$$

So the subtraction isn't a rule to memorize — it is exactly the over-count produced by adding two regions that share a middle.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the Route 24 union, $0.58$.
- *Twist:* the **complement** is often faster. $P(\text{neither Water nor grass}) = 1 - 0.58 = 0.42$ — the 42 Pokémon outside both circles. For "at least one," computing $1 - P(\text{none})$ is frequently the cleanest path (you'll lean on this for independence next).
- *Edge:* if told two events are mutually exclusive, the overlap is **0** *by definition* — but never *assume* it; that assumption is a classic trap (Concept 4).

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch04_union_venn.png" alt="A two-circle Venn diagram over 100 Route-24 logs. The Water-type circle holds 40, the tall-grass circle holds 30, and their overlap of 12 is shaded distinctly. A small inset shows the mutually-exclusive case: two non-overlapping circles with no shared region." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Inclusion–exclusion: add the circles, subtract the shaded overlap (counted twice). The inset shows the disjoint case, where there is nothing to subtract.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute "or" for any two events by adding and removing the overlap, and you know the disjoint special case where the overlap vanishes.

::: pokedex-entry
**POKÉDEX ENTRY №03 — The Addition Rule (Inclusion–Exclusion)**

$$P(A \cup B) = P(A) + P(B) - P(A \cap B).$$

If $A,B$ are **mutually exclusive** ($A\cap B = \varnothing$): $\;P(A\cup B) = P(A) + P(B).$

*In plain terms:* "or" adds the pieces but subtracts the overlap you counted twice. Disjoint events have no overlap, so you simply add.

*Recognition cue:* **"at least one of," "either…or," "$A$ or $B$."** Reach for inclusion–exclusion; only drop the overlap term if you are *told* the events can't co-occur.
:::

## Concept 4 — Independence (and the Disjoint Trap)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Independence**

Bill's lighthouse runs on two **independent** circuits: circuit 1 works w.p. $0.9$, circuit 2 w.p. $0.8$. The beacon shines if **at least one** works. What is $P(\text{shines})$? And: can two *mutually exclusive* events of positive probability ever be independent?

If you answered **$0.98$** (via $1 - 0.1\cdot0.2$) and **"no — disjoint events are maximally *dependent*,"** **skip to Concept 5**. Otherwise, the disjoint trap below is exactly what you need.
:::

**Beat 1 — The one-sentence idea.** *Two events are independent when knowing one tells you nothing about the other — so their joint probability is just the product of the two separate probabilities.*

**Beat 2 — Anchor + concrete instance.** Independence is the condition under which the multiplication rule (Concept 2) *simplifies*: the conditional factor $P(A\given B)$ collapses to plain $P(A)$, because $B$ told you nothing.

**Bill's lighthouse** runs on **two independent circuits**. Circuit 1 works with probability **$0.9$**, circuit 2 with probability **$0.8$**. They don't talk to each other. The beacon **shines** if at least one works. *Find $P(\text{both work})$ and $P(\text{beacon shines})$.*

**Beat 3 — Reason through it in plain words.** Because the circuits are independent, knowing circuit 1 worked doesn't change circuit 2's chances. So the chance both work is simply $0.9$ of $0.8$:

$$P(\text{both}) = 0.9 \times 0.8 = 0.72.$$

For "at least one shines," go through the **complement** (Concept 3's shortcut): the beacon goes dark only if **both fail**. Circuit 1 fails w.p. $0.1$, circuit 2 w.p. $0.2$, independently, so

$$P(\text{both fail}) = 0.1 \times 0.2 = 0.02, \qquad P(\text{shines}) = 1 - 0.02 = 0.98.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** Here is the trap that sinks people: **"mutually exclusive" and "independent" are *not* the same thing.** In fact they are nearly opposites.

- *Mutually exclusive* means $A$ and $B$ **cannot both happen** ($P(A\cap B)=0$).
- *Independent* means knowing one **tells you nothing** about the other ($P(A\cap B)=P(A)P(B)$).

Suppose $A$ and $B$ each have positive probability and are mutually exclusive. Then if $A$ happens, $B$ is now **impossible** — that's the *opposite* of "tells you nothing." Knowing $A$ told you *everything* about $B$ (it's out). Check the algebra: independence would need $P(A\cap B)=P(A)P(B) > 0$, but disjointness forces $P(A\cap B)=0$. Contradiction. **Disjoint events of positive probability are maximally *dependent*, never independent.** Do not assume independence — you must be told it, or derive it.

**Beat 5 — Translate into notation, one glyph at a time.** The defining test:

$$P(A \cap B) = P(A)\,P(B) \qquad \text{read aloud: ``}A \text{ and } B \text{ are independent.''}$$

Equivalently (divide both sides by $P(B)$), independence says the conditional equals the unconditional:

$$P(A \given B) = P(A) \qquad \text{read aloud: ``given } B \text{ doesn't change } A\text{.''}$$

For more than two events, independence must hold for **every** subcollection. Events $A_1,\dots,A_n$ are **mutually independent** when

$$P\!\left(A_{i_1}\cap\cdots\cap A_{i_k}\right) = \prod_{j=1}^{k} P\!\left(A_{i_j}\right) \quad \text{for every subset } \{i_1,\dots,i_k\}.$$

The capital pi $\prod$ reads **"the product of"** — just multiply those terms together, the multiplicative cousin of a sum (you'll meet the matching summation sign $\sum$ in the next concept). Spoken whole: **"every subset multiplies."**

**Beat 6 — State the definition precisely (no derivation needed: independence is *defined*, not proved).** Unlike the addition and total-probability laws, independence is not a theorem we deduce — it is the *defining condition*. The product test *is* the definition; the only content is stating which collections it must hold for (every subcollection, as above). There is nothing to derive beyond that.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* two independent circuits, product $0.72$.
- *Twist (pairwise $\neq$ mutual):* you can have three events that multiply two-at-a-time yet **fail** to multiply all-three-at-once. Take a spinner where $A,B,C$ each have probability $\tfrac12$, every pair satisfies $P(A\cap B)=\tfrac14=\tfrac12\cdot\tfrac12$ (pairwise independent!), but $P(A\cap B\cap C)=\tfrac14 \neq \tfrac18 = P(A)P(B)P(C)$. Knowing two of them forced the third — so the three together are *dependent*. Pairwise independence is genuinely weaker. *(This is Problem C5.18.)*
- *Edge:* "at least one of $n$ independent events" is always $1 - \prod_i (1-p_i)$, the complement of "all fail."

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch04_independence_grid.png" alt="A 2x2 area grid contrasting independence and dependence. Left grid: the joint cell area equals the product of the row and column margins (independent). Right grid: the joint cell does not match the product of margins (dependent). A callout diagrams three spinner events that are pairwise independent but not mutually independent." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Independence as area: the joint cell equals the product of the margins. When it doesn't, the events are dependent. The inset is the pairwise-but-not-mutual counterexample.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now test independence with the product rule, use it to multiply joint probabilities directly, handle "at least one" by the complement, and — crucially — you will never again confuse *disjoint* with *independent*.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Independence**

$A$ and $B$ are **independent** iff
$$P(A\cap B) = P(A)\,P(B), \quad\text{equivalently}\quad P(A\given B) = P(A).$$

$A_1,\dots,A_n$ are **mutually independent** iff *every* subcollection multiplies. **Pairwise** independence (every pair multiplies) is weaker and does **not** imply mutual independence.

*In plain terms:* independent = "knowing one changes nothing about the other." Mutual independence is the stronger promise that this holds for all combinations at once, not just pairs.

*Recognition cue:* **"independent," physically separate mechanisms, draws *with* replacement, repeated identical trials.** Never *assume* it — and remember disjoint is the *opposite* of independent.
:::

## Concept 5 — The Law of Total Probability (the Forward Direction)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Total Probability**

Misty opens with Staryu (w.p. $0.5$), Starmie ($0.3$), or Psyduck ($0.2$). Each has its own chance of a super-effective first move against Pikachu: $0.3$, $0.6$, $0.1$. What is the overall chance her opener is super-effective?

If you answered **$0.35$** (not $0.333$) and you know *why you weight by the lead probabilities*, **skip to Concept 6** — the crown jewel. If you reached for the plain average, read on.
:::

**Beat 1 — The one-sentence idea.** *To get the overall chance of $A$, split the world into non-overlapping cases that cover everything, find $A$'s chance inside each case, and average those by how likely each case is.*

**Beat 2 — Anchor + concrete instance.** This is the multiplication rule (Concept 2) applied across *several* cases and then added (Concept 3). Each case-and-$A$ is a tree branch; we sum the leaves.

**Misty's signature** is that you never know her lead. She opens with **Staryu (w.p. $0.5$), Starmie ($0.3$), or Psyduck ($0.2$)** — these three are *exhaustive* (she always leads with one of them) and *mutually exclusive* (only one lead). Each lead has a different chance its **first move is super-effective** against Pikachu: **Staryu $0.3$, Starmie $0.6$, Psyduck $0.1$.** *Before she sends anything out, what is the chance her opener is super-effective?*

**Beat 3 — Reason through it in plain words.** The move can be super-effective along three different roads:

- She leads Staryu *and* it's super-effective: $0.5 \times 0.3 = 0.15$.
- She leads Starmie *and* it's super-effective: $0.3 \times 0.6 = 0.18$.
- She leads Psyduck *and* it's super-effective: $0.2 \times 0.1 = 0.02$.

These three roads cannot both happen (only one lead), so add them:

$$0.15 + 0.18 + 0.02 = 0.35.$$

Each term is "how likely this case is" times "$A$'s chance inside this case" — a **weighted average** of the conditional rates.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting shortcut is the **plain average** of the three rates:

$$\frac{0.3 + 0.6 + 0.1}{3} = 0.333. \qquad\textbf{(wrong — ignores the weights)}$$

That would only be right if all three leads were equally likely. They aren't — Staryu is sent $0.5$ of the time, Psyduck just $0.2$. The rates must be weighted by how often each case actually occurs. A different mix of leads gives a different overall answer; the plain average throws that information away.

**Beat 5 — Translate into notation, one glyph at a time.** Call the three leads $B_1, B_2, B_3$ (Staryu, Starmie, Psyduck). They **partition** the sample space:

$$B_1, B_2, \dots, B_n \text{ partition } S \quad\text{read aloud: ``the } B\text{'s partition } S\text{''} \;(\text{disjoint, exhaustive, each } P(B_i)>0).$$

Let $A$ = "super-effective." Each road is $P(B_i)\,P(A\given B_i)$, and we add them. "Add them up" gets the **summation** symbol:

$$\sum_{i=1}^{n} \qquad \text{read aloud: ``the sum over } i \text{ from } 1 \text{ to } n \text{ of''} \;(\text{just: add these up}).$$

So

$$P(A) = \sum_{i=1}^{n} P(B_i)\,P(A\given B_i) = (0.5)(0.3) + (0.3)(0.6) + (0.2)(0.1) = 0.35.$$

The big sigma is *only* shorthand for "add the three terms" — nothing more.

**Beat 6 — Generalize: derive the formula.** Every outcome where $A$ happens lands in exactly one case $B_i$ (the cases are disjoint and cover everything). So the event $A$ splits cleanly into the pieces $A\cap B_i$:
$$P(A) = \sum_{i=1}^{n} P(A\cap B_i) = \sum_{i=1}^{n} P(B_i)\,P(A\given B_i),$$
where the last step applies the multiplication rule to each piece. The formula is the compression of "split into cases, then multiply-and-add."

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the three-lead sum, $0.35$.
- *Two-case form:* with just $B$ and its complement $B^c$ ("not $B$," from Concept 3), the law reads $P(A) = P(B)P(A\given B) + P(B^c)P(A\given B^c)$ — the "rainy day / dry day flood" pattern (Problem C5.5).
- *Sanity boundary:* a weighted average must sit between the extremes. Our $0.35$ is between $0.1$ and $0.6$. If you ever compute a "total probability" *outside* the range of the conditional rates, you made an arithmetic slip.

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch04_total_prob_tree.png" alt="A one-stage fan diagram. A root node branches to three leaves: Staryu (0.5), Starmie (0.3), Psyduck (0.2). Each leaf carries its super-effective rate (0.3, 0.6, 0.1) and the product on its branch: 0.15, 0.18, 0.02. The three products are summed at the bottom to 0.35." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Total probability as a one-stage tree: each leaf is case-weight $\times$ in-case rate; sum the leaves for the overall $P(A)=0.35$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now assemble an unconditional probability from a partition by weighting each case's rate by its likelihood. **This sum is exactly the denominator of Bayes' theorem** — the next, and final, idea.

::: pokedex-entry
**POKÉDEX ENTRY №05 — Law of Total Probability**

If $B_1,\dots,B_n$ **partition** $S$ (disjoint, exhaustive, each $P(B_i)>0$), then for any event $A$:
$$P(A) = \sum_{i=1}^{n} P(B_i)\,P(A\given B_i).$$

*In plain terms:* split the world into cases, find $A$'s chance in each, and **weight** each by how likely its case is. It is a weighted average of conditional probabilities — so the answer always lands **between** the smallest and largest conditional rate.

*Recognition cue:* the cause comes in **types / groups / urns / machines**, each with its own rate, and you want the **overall** rate. "$x\%$ are type I, $y\%$ type II…, what fraction overall…?" $\to$ partition and sum.
:::

## Concept 6 — Bayes' Theorem (Running the Clue Backward)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Bayes' Theorem**

*Brineflux* infects $2\%$ of Water Pokémon. A scanner flags $95\%$ of truly sick ones and falsely flags $8\%$ of healthy ones. A Staryu scans **positive**. What is $P(\text{sick}\given\text{positive})$?

If you answered **$\approx 0.195$** (and you're not surprised it's *below* $50\%$ despite a "$95\%$ accurate" test), you own this chapter end to end — **skip to the Gym Battle capstone** if you want one expert-modeled rep, otherwise head straight to the **Gym Challenge** and claim the badge. If you wanted to answer "$0.95$," read on — that is the single most-punished error in this entire topic.
:::

**Beat 1 — The one-sentence idea.** *Bayes flips a conditional: it turns "the chance of the clue given each cause" into "the chance of each cause given the clue," by weighting each cause's prior by how well it explains the evidence, then normalizing over all causes.*

**Beat 2 — Anchor + concrete instance.** Recall from Concept 1 that the bar is **not symmetric**: $P(A\given B) \neq P(B\given A)$. Bayes is the machine that converts one into the other — and its *denominator* is exactly the law of total probability you just built (Concept 5).

Nurse Joy needs you before you can chase any thief. **Brineflux** infects **$2\%$** of Cerulean's Water Pokémon. Joy's scanner is good but imperfect: if a Pokémon truly has Brineflux, it flags **$95\%$** of the time (*sensitivity*); if the Pokémon is healthy, it *still* flags **$8\%$** of the time (*false-positive rate*). A nervous trainer's **Staryu just scanned positive.** Joy won't quarantine without a number. *Given the positive scan, what is the chance the Staryu actually has Brineflux?*

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/120.png" alt="Staryu" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#120 Staryu — scanned positive for Brineflux</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Imagine **10,000 Water Pokémon** walk through the Center. Since $2\%$ are sick, that's **200 sick** and **9,800 healthy.**

- Of the 200 sick, the scanner flags $95\%$ $\to$ about **190 true positives.**
- Of the 9,800 healthy, the scanner falsely flags $8\%$ $\to$ about **784 false positives.**

So **$190 + 784 = 974$** Pokémon scan positive in all. Among those positives, how many are *actually* sick? Just the 190. So

$$P(\text{sick}\given\text{positive}) = \frac{190}{974} \approx 0.195.$$

Only about **$19.5\%$** — even though the test is "$95\%$ accurate"! Why so low? Healthy Pokémon are so *common* (9,800 of them) that even a small $8\%$ false-positive rate produces a *flood* of false alarms (784) that swamps the 190 true ones.

**Beat 4 — Surface and dismantle the tempting wrong idea (the prosecutor's fallacy).** Here is the canonical error of this entire chapter. The test is "$95\%$ accurate," so it is *desperately* tempting to report

$$P(\text{sick}\given\text{positive}) \overset{?}{=} 0.95. \qquad\textbf{(wrong)}$$

But $0.95$ is $P(\text{positive}\given\text{sick})$ — the chance of the *clue given the cause*. The question asks for $P(\text{sick}\given\text{positive})$ — the *cause given the clue*. **These are opposite sides of the bar, and they are not equal.** Reporting one as if it were the other — ignoring the *base rate* (how rare "sick" is to begin with) — is the **prosecutor's fallacy**. A clue that is very likely *given* a rare cause can still leave that cause *improbable* once the prior is folded in. The 9,800 healthy Pokémon get a vote, and they outvote the sick ones. *(Team Rocket will commit this exact error in a moment — and it will cost them.)*

**Beat 5 — Translate into notation, one glyph at a time.** Let $D$ = "has Brineflux," $D^c$ = "healthy" (the **complement** from Concept 3 — "$D$-complement," i.e. "not $D$"), and $+$ = "scans positive." We're given:

$$P(D) = 0.02, \quad P(+\given D) = 0.95, \quad P(+\given D^c) = 0.08.$$

We want $P(D\given +)$. Start from the definition of conditional probability (Entry №01) and rebuild Beat 3's count-reasoning symbolically:

$$P(D \given +) = \frac{P(D \cap +)}{P(+)}.$$

The **top** is the "190 true positives" path: by the multiplication rule (Entry №02), $P(D\cap +) = P(D)\,P(+\given D)$. The **bottom** is *every* way to scan positive — sick-and-flagged **plus** healthy-and-flagged — which is the law of total probability (Entry №05):

$$P(+) = \underbrace{P(D)\,P(+\given D)}_{\text{true positives}} + \underbrace{P(D^c)\,P(+\given D^c)}_{\text{false positives}}.$$

**Beat 6 — Generalize: derive the formula.** Putting the two together gives the two-way Bayes formula — and replacing $\{D, D^c\}$ with any partition $\{B_1,\dots,B_n\}$ gives the general one. We just *derived* it from Entries №01, №02, and №05; we did not assert it:

$$P(D\given +) = \frac{P(D)\,P(+\given D)}{P(D)\,P(+\given D) + P(D^c)\,P(+\given D^c)} = \frac{(0.02)(0.95)}{(0.02)(0.95) + (0.98)(0.08)} = \frac{0.0190}{0.0974} \approx 0.195.\;\checkmark$$

**Beat 7 — Ramp the difficulty.**

- *Simplest (two-way):* the Staryu scan, above.
- *$n$-way:* more than two causes — three breeding pools, three suspect groups — just add more rows; the denominator sums them all (Worked Example 5.2; the Gym Battle).
- *Twist (negative evidence):* Bayes works for a *non*-event too. "Scanned **negative**" just uses $P(-\given D) = 1-0.95$ and $P(-\given D^c) = 1-0.08$ in the same grid (Problem C5.6).
- *Edge (zero likelihood):* if a cause makes the evidence *impossible* ($P(A\given B_k)=0$), its posterior is $0$ — that cause is eliminated (Problem C5.15).

**Beat 8 — Picture it: the detective's grid.** Misty leans over your shoulder. "Forget the formula for a second. Just make a **grid**." This is the single most reliable way to never miss a Bayes problem under time pressure.

| Cause $B_i$ | Prior $P(B_i)$ | Likelihood $P(A\given B_i)$ | Joint $P(B_i)P(A\given B_i)$ | Posterior $P(B_i\given A)$ |
|---|---|---|---|---|
| $B_1$ | … | … | multiply across $\to$ | joint $\div$ column total |
| $B_2$ | … | … | multiply across $\to$ | joint $\div$ column total |
| **Total** | $1$ | — | $P(A)$ (the denominator) | $1$ |

Fill it left to right: priors, then likelihoods, then their **product** (the joint), then **sum the joint column** to get $P(A)$ — that sum *is* the law of total probability — and finally divide each joint by that sum. The posteriors are guaranteed to add to **one**, your built-in error check.

<figure>
<img src="../../assets/diagrams/ch04_bayes_table.png" alt="The detective's grid: a four-column table (Cause, Prior, Likelihood, Joint=product, Posterior=joint/column-total) filled with the Sick-Staryu numbers. Sick row: 0.02, 0.95, 0.0190. Healthy row: 0.98, 0.08, 0.0784. Arrows show multiply-across to get the joint, then sum the joint column to 0.0974, then divide each joint by 0.0974 to get posteriors 0.195 and 0.805, which sum to 1." style="width:82%; max-width:600px; display:block; margin:1em auto;">
<figcaption>The Bayes table for the Sick Staryu. Multiply across $\to$ sum the joint column ($P(A)=0.0974$) $\to$ divide. Posteriors $0.195 + 0.805 = 1$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now invert any conditional: given $P(\text{clue}\given\text{cause})$ and the priors, compute $P(\text{cause}\given\text{clue})$ — two-way or $n$-way — with the grid, and explain *why* a strong clue need not mean a guilty verdict. This is the engine that solves the phantom-thief case. You're ready.

::: pokedex-entry
**POKÉDEX ENTRY №06 — Bayes' Theorem**

For a partition $B_1,\dots,B_n$ of $S$ and observed evidence $A$:
$$P(B_k\given A) = \frac{P(B_k)\,P(A\given B_k)}{\displaystyle\sum_{i=1}^{n} P(B_i)\,P(A\given B_i)} = \frac{\text{prior}\times\text{likelihood}}{\text{total probability of the evidence}}.$$

Two-way special case (cause $B$ vs. complement $B^c$):
$$P(B\given A) = \frac{P(B)\,P(A\given B)}{P(B)\,P(A\given B) + P(B^c)\,P(A\given B^c)}.$$

*In plain terms:* the numerator is the **one path** that explains the evidence the way you care about; the denominator is **every** path that could produce the same evidence. Posterior = your path's share of all explanations.

*Recognition cue:* you're given $P(\text{evidence}\given\text{cause})$ but asked for $P(\text{cause}\given\text{evidence})$ — **the bar is flipped.** Sensitivity/specificity, false positives, "given it tested positive…," "given the clue, who did it." $\to$ build the **Bayes table**.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/misty.png" alt="Misty" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Misty — Cerulean Gym Leader, your Bayes mentor</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because Bayes is the hard, load-bearing idea.

### Worked Example 5.1 — The Sick Staryu (full narration; understanding-first)

**ARCHETYPE:** *Two-way Bayes — the false-positive classic (sensitivity / specificity).*

**Setup.** This is the Concept-6 story, now solved as a clean exam item. Brineflux infects $2\%$ of Water Pokémon; the scanner flags $95\%$ of sick ones and $8\%$ of healthy ones. A Staryu scans **positive**. Find $P(\text{sick}\given\text{positive})$.

**Step 1 — Identify (which archetype, and which way does the bar point?).** Let $D$ = "sick," $+$ = "positive." We're handed $P(+\given D)=0.95$ but asked for $P(D\given +)$. The bar is **flipped** $\to$ this is Bayes, not a lookup. Givens: $P(D)=0.02$, $P(+\given D)=0.95$, $P(+\given D^c)=0.08$.

**Step 2 — Professor's Path (the why).** Build the positive-scanners from first principles. The chance of being *both* sick and flagged is, by the multiplication rule,
$$P(D\cap +) = P(D)\,P(+\given D) = (0.02)(0.95) = 0.0190.$$
The chance of scanning positive *at all* gathers both roads (law of total probability):
$$P(+) = (0.02)(0.95) + (0.98)(0.08) = 0.0190 + 0.0784 = 0.0974.$$
The posterior is the sick road's share of all positive roads:
$$P(D\given +) = \frac{P(D\cap +)}{P(+)} = \frac{0.0190}{0.0974} \approx 0.195.$$

**Step 3 — Trainer's Path (the fast how: grid it).** Same numbers, no prose:

| Cause | Prior | $P(+\given\cdot)$ | Joint |
|---|---|---|---|
| $D$ (sick) | $0.02$ | $0.95$ | $0.0190$ |
| $D^c$ (healthy) | $0.98$ | $0.08$ | $0.0784$ |
| **Total** | | | $0.0974$ |

$$P(D\given +) = \frac{0.0190}{0.0974} \approx 0.195.$$

**Step 4 — Check & pitfall.** The posteriors $0.195 + 0.805 = 1$ ✓. The answer is *below* $50\%$ despite the "$95\%$ accurate" test — the base-rate effect: the $98\%$ healthy population's $8\%$ false positives ($0.0784$) swamp the true positives ($0.0190$). **Pitfall:** reporting $0.95$, i.e. confusing $P(+\given D)$ with $P(D\given +)$ — the prosecutor's fallacy. *(Back-ref: Entry №06.)*

### Worked Example 5.2 — Which Pool Did the Magikarp Come From? (partial guidance)

**ARCHETYPE:** *$n$-way Bayes from a partition (mixture of sources).*

**Setup.** Misty stocks her gym from three breeding pools: Pool A holds $50\%$ of her stock, Pool B $30\%$, Pool C $20\%$. A Magikarp from A evolves into Gyarados w.p. $0.10$, from B w.p. $0.25$, from C w.p. $0.60$. A random Magikarp **evolves into Gyarados.** Find $P(\text{Pool C}\given\text{evolved})$.

<div style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end; margin:1.25em auto;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/129.png" alt="Magikarp" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#129 Magikarp</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/130.png" alt="Gyarados" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#130 Gyarados</figcaption>
</figure>
</div>

**Identify.** Partition by pool $\{A,B,C\}$; evidence $G$ = "evolved." Bar flipped (given $G$, want the cause) $\to$ Bayes, $n=3$. *Your move: fill the grid.*

| Pool | Prior | $P(G\given\cdot)$ | Joint |
|---|---|---|---|
| A | $0.50$ | $0.10$ | $0.050$ |
| B | $0.30$ | $0.25$ | $0.075$ |
| C | $0.20$ | $0.60$ | $0.120$ |
| **Total** | $1.00$ | | $P(G)=0.245$ |

The joint-column sum $P(G)=0.245$ is the law of total probability. Then

$$P(\text{C}\given G) = \frac{0.120}{0.245} \approx 0.490.$$

**Check & pitfall.** Posterior column: $\tfrac{0.050}{0.245}+\tfrac{0.075}{0.245}+\tfrac{0.120}{0.245} = 0.204+0.306+0.490 = 1.000$ ✓. Pool C's prior was only $0.20$, but the Gyarados nearly *doubles* it to $0.49$ — sensible, since C is by far the most likely to produce one. **Pitfall:** forgetting to divide by $P(G)$ and reporting the raw joint $0.120$. *(Back-ref: Entries №05, №06.)*

### Worked Example 5.3 — Two Poké Balls, No Replacement (light guidance)

**ARCHETYPE:** *Multiplication rule for sequential draws without replacement; complement for "at least one."*

**Setup.** Brock's bag holds $7$ Poké Balls and $3$ Great Balls. Draw two without replacement. Find (a) $P(\text{both Poké})$ and (b) $P(\text{the two draws differ in type})$.

**(a)** Multiply down the branch, shrinking the bag:
$$P(P_1\cap P_2) = \frac{7}{10}\cdot\frac{6}{9} = \frac{42}{90} = \frac{7}{15} \approx 0.467.$$

**(b)** Complement of "same type":
$$P(\text{same}) = \underbrace{\tfrac{7}{10}\cdot\tfrac{6}{9}}_{\text{both Poké}} + \underbrace{\tfrac{3}{10}\cdot\tfrac{2}{9}}_{\text{both Great}} = \tfrac{42}{90} + \tfrac{6}{90} = \tfrac{48}{90}, \qquad P(\text{differ}) = 1 - \tfrac{48}{90} = \tfrac{42}{90} = \tfrac{7}{15} \approx 0.467.$$

**Check & pitfall.** *With* replacement, (a) would be $\tfrac{7}{10}\cdot\tfrac{7}{10}=0.49$; the without-replacement value $0.467$ is slightly lower because removing a Poké Ball makes the second less likely ✓. **Pitfall:** reusing $\tfrac{7}{10}$ on the second draw (silently assuming replacement). *(Back-ref: Entry №02.)*

### Worked Example 5.4 — Misty's Hidden Move (exam speed)

**ARCHETYPE:** *Law of total probability (forward; no inversion).*

**Setup.** Leads: Staryu $0.5$, Starmie $0.3$, Psyduck $0.2$; super-effective rates $0.3, 0.6, 0.1$. Find $P(\text{opener super-effective})$.

$$P(E) = (0.5)(0.3) + (0.3)(0.6) + (0.2)(0.1) = 0.15 + 0.18 + 0.02 = 0.35.$$

**Check & pitfall.** $0.35$ lies between the smallest rate $0.1$ and the largest $0.6$ — every weighted average must ✓. **Pitfall:** the plain average $\tfrac{0.3+0.6+0.1}{3}=0.333$, which ignores the lead weights. *(If instead you're told it **was** super-effective and asked which lead — that's a Bayes inversion, Problem C5.13.) (Back-ref: Entry №05.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Always grid the Bayes**

Under exam time, don't juggle the Bayes fraction in your head. Draw the four-column grid (prior · likelihood · joint · posterior), fill it left to right, and the **sum of the joint column is your denominator automatically**. The posteriors must add to $1$ — if they don't, you mis-multiplied. This one habit eliminates the most common Bayes errors.
:::

::: trainers-tip
**TRAINER'S TIP — Which way does the bar point?**

The instant you see a conditional, ask: *"What is given (the world I'm now inside), and what am I finding?"* If the problem hands you $P(\text{test}\given\text{disease})$ but wants $P(\text{disease}\given\text{test})$, the bar flips — that is the tell for Bayes, not a direct lookup. Mixing the two is the prosecutor's fallacy, the single most-punished error in this topic.
:::

::: trainers-tip
**TRAINER'S TIP — "At least one" → complement**

When you read "at least one" with independent trials, compute $1 - P(\text{none}) = 1 - \prod_i (1-p_i)$ rather than summing a pile of cases. On the TI-30XS, chain the $(1-p_i)$ products, then subtract from $1$ in one shot — faster, with fewer sign slips.
:::

::: trainers-tip
**TRAINER'S TIP — Sanity-bound the total probability**

A law-of-total-probability answer is a weighted average, so it must land **between** the smallest and largest conditional rate. If your "overall" probability falls outside that range, stop — you have an arithmetic error before you even reach Bayes.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Meowth has been eavesdropping on the phantom-thief case and snatches the case file. "Da clue says da thief had a Water-type! An' our Rocket buddy's got a Water-type — an' Rockets are sloppy, dey leave footprints ninety percent o' da time! So da clue practically *screams* it was a Rocket. Gotta be, what, ninety percent guilty, easy!"

Jessie nods sagely. "Of *course*. The footprints match. Case closed."

James, for once, hesitates. "But… aren't there, like, *hundreds* of ordinary trainers in this town and only *one* Rocket grunt? Wouldn't most of those wet footprints belong to *them*…?"

Meowth waves him off. "Details, details!" — and confidently accuses the wrong suspect.

**Where it fails:** Meowth swapped $P(\text{clue}\given\text{Rocket})=0.90$ for $P(\text{Rocket}\given\text{clue})$ — the **prosecutor's fallacy**, the exact error from the Sick Staryu. A clue that's likely *given* a suspect is nearly worthless until you fold in the **base rate** (how rare that suspect is) via Bayes. James had the right instinct: there are so many travelers that their footprints rival the grunt's, even though the grunt is sloppier. Run the grid — prior $\times$ likelihood, normalized — and the "$90\%$" collapses. The Gym Battle below does exactly that, and the true number is **$51.5\%$**, not $90\%$.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal math of **fraud detection** and **medical underwriting.**

When an insurer sees a "red flag" on a claim — say, a claim filed days after a policy starts — they do **not** conclude "fraud!" from $P(\text{red flag}\given\text{fraud})$. They run Bayes: the overwhelming majority of claims are legitimate (the base rate), so even a strong flag yields a *modest* posterior probability of fraud, which is then used to **triage** which claims a human investigates. Treating the flag rate as the guilt rate — Meowth's mistake — would bury investigators in false accusations.

The very same false-positive arithmetic from the Staryu scan prices **screening tests** in health insurance: a "$95\%$ accurate" test for a *rare* condition produces mostly **false** positives, and an insurer who mis-reads that probability mis-prices the product and loses money. Underwriters compute exactly the $P(\text{disease}\given\text{positive})$ you computed for Joy.

*Series bridge:* this base-rate, prior-times-likelihood reasoning is the seed of **credibility theory** (CAS MAS-II), where you blend a prior estimate with observed experience, and of **predictive-model calibration** (CAS Exam 5). Bayes is not a one-chapter trick — it is the spine of inference for the rest of the syllabus.

*Transfer check:* could you solve this with **no Pokémon in it**? "A disease affects $2\%$ of a population; a test is $95\%$ sensitive with an $8\%$ false-positive rate; a patient tests positive — find the probability they have the disease." Same grid, same $0.195$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Cascade Badge Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/water.png" alt="Water type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">Misty's Water-type Gym — the Cascade Badge challenge</figcaption>
</figure>

**Misty's Challenge.** "Enough warm-ups," Misty says, finally smiling. "Here's the real one — the exact case tearing up my town. Solve it the *honest* way, and the badge is yours." She lays out the phantom-thief files formally. Three suspect groups stand near the Pokémon Center on any given night:

- **Travelers** — $60\%$ of the people near the Center. A traveler steals on a given night w.p. $0.05$, and when they steal they leave wet footprints $40\%$ of the time.
- **Locals** — $35\%$ of the people. A local steals w.p. $0.01$, and leaves footprints $20\%$ of the time when they do.
- **Rocket grunts** — $5\%$ of the people. A grunt steals w.p. $0.30$, and leaves footprints $90\%$ of the time when they do.

Last night, **exactly one theft occurred, and the thief left wet footprints.** *Given that, find the probability the thief was a Rocket grunt — and a traveler, and a local.* Hand Officer Jenny the posterior on each group.

**ARCHETYPE:** *Full $n$-way Bayes with a compound likelihood (group $\times$ steal $\times$ clue), base-rate corrected.*

**Step 1 — Identify the cause and the compound likelihood.** The hidden "cause" is *which group the thief belongs to.* But a person is the clue-leaving thief only if they (a) belong to the group, (b) actually steal, and (c) leave the clue. Note this likelihood has **one more factor** than the Staryu scan: there, a sick Pokémon simply scanned positive; here, a suspect must *first choose to steal* before they can leave a footprint. By the multiplication rule, the likelihood of "a clue-leaving theft by a member of group $G$" factors:
$$P(\text{steal} \cap \text{clue}\given G) = P(\text{steal}\given G)\,P(\text{clue}\given\text{steal}\cap G).$$
*Read the last term aloud:* "the chance of the clue **given that** this person both belongs to group $G$ **and** stole" — everything to the right of the bar $\given$ is the world we have shrunk into (Entry №01), and here that world is the intersection $\text{steal}\cap G$ of two facts at once. So each group's **joint weight** is $\text{share} \times P(\text{steal}) \times P(\text{clue}\given\text{steal})$.

**Step 2 — Trainer's Path: grid it.**

| Group | Share | $P(\text{steal})$ | $P(\text{clue}\given\text{steal})$ | Joint weight |
|---|---|---|---|---|
| Traveler | $0.60$ | $0.05$ | $0.40$ | $0.60\cdot0.05\cdot0.40 = 0.01200$ |
| Local | $0.35$ | $0.01$ | $0.20$ | $0.35\cdot0.01\cdot0.20 = 0.00070$ |
| Rocket | $0.05$ | $0.30$ | $0.90$ | $0.05\cdot0.30\cdot0.90 = 0.01350$ |
| **Total** | | | | $0.02620$ |

The column total $0.02620$ is the probability of "a clue-leaving theft by *someone*" — the law of total probability over the three groups. Normalize each joint by it:
$$P(\text{Rocket}\given\text{clue theft}) = \frac{0.01350}{0.02620} \approx 0.515,$$
$$P(\text{Traveler}\given\text{clue theft}) = \frac{0.01200}{0.02620} \approx 0.458,$$
$$P(\text{Local}\given\text{clue theft}) = \frac{0.00070}{0.02620} \approx 0.027.$$

**Step 3 — Professor's Path (why the compound likelihood is legitimate).** Let evidence $A$ = "a theft with wet footprints by this person." Then $P(A\given G) = P(\text{steal}\given G)\,P(\text{clue}\given\text{steal}\cap G)$ by the multiplication rule, and Bayes gives
$$P(G\given A) = \frac{P(G)\,P(A\given G)}{\sum_g P(g)\,P(A\given g)},$$
which is precisely the grid above. The "compound" likelihood is just the multiplication rule applied *inside* each row before Bayes normalizes *across* rows.

**Step 4 — Check, verdict & the pitfall Misty is testing.** Posteriors: $0.515 + 0.458 + 0.027 = 1.000$ ✓. The headline: the Rocket grunt **is** the single most likely culprit — but at only **$51.5\%$**, *not* the "$90\%$" Meowth screamed. The traveler is almost as likely ($45.8\%$), purely because travelers are so numerous that their footprints nearly rival the sloppy grunt's. The base rate matters enormously. Anyone who used only the $0.90$ clue rate — or forgot to fold in the population shares and theft rates — accuses the wrong person with false confidence. *That* is the prosecutor's fallacy, and avoiding it is what earns the badge.

> "That," Misty says, "is how you read a clue. You didn't let one number bully you. The Cascade Badge is yours."

*(A second consistent night would square each likelihood and drive the Rocket posterior to $\approx 0.94$ — see Problem C5.20. Evidence compounds.)*

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min/problem), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Miss it, and the chapter is waiting. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C5.1.** 🔴 On Route 24 you log $100$ Pokémon: $40$ are Water-type, $30$ live in tall grass, $12$ are both. Given that one lives in tall grass, find the probability it is Water-type.

**C5.2.** 🔴 Brock's bag has $5$ Poké Balls and $4$ Great Balls. Draw two without replacement. Given the first is a Poké Ball, find the probability the second is a Great Ball.

**C5.3.** 🔴 Bill's lighthouse beacon runs on two independent circuits: circuit 1 works w.p. $0.9$, circuit 2 w.p. $0.8$. The beacon shines if at least one works. Find $P(\text{shines})$.

**C5.4.** 🟡 Ash and Misty independently try to catch a Tentacool: Ash succeeds w.p. $0.6$, Misty w.p. $0.7$. Find the probability that exactly one of them catches it.

**C5.5.** 🟡 $30\%$ of Cerulean days are rainy. The gym floods w.p. $0.5$ on rainy days and $0.05$ on dry days. Find the probability the gym floods on a random day.

**C5.6.** 🟡 Nurse Joy's quick-scan flags $90\%$ of genuinely sick Pokémon and $20\%$ of healthy ones; $10\%$ of those scanned are sick. A Pokémon scans **negative**. Find $P(\text{sick}\given\text{negative})$.

**C5.7.** 🔴 A stack holds $3$ Fire TMs and $2$ Water TMs. Draw two in order without replacement. Find the probability both are Fire TMs.

**C5.8.** 🟡 On Route 24 you log two traits of each wild Pokémon: $A$ = "Water-type" and $B$ = "found near the river." Your tallies give $P(A)=0.4$, $P(B)=0.5$, and $P(A\cup B)=0.65$ (the Pokémon has at least one trait). Are $A$ and $B$ independent? Justify with a computation.

**C5.22.** 🔴 You throw a Poké Ball at one wild Pokémon (catches w.p. $0.6$) and, separately, a Great Ball at another (catches w.p. $0.75$). The two throws are **independent**. Find the probability **both** catch and the probability **at least one** catches.

### Gym Battles (true SOA difficulty)

**C5.9.** 🟡 A wild Pokémon is Goldeen ($50\%$), Seaking ($30\%$), or Horsea ($20\%$). Each flees if you hesitate: Goldeen $0.2$, Seaking $0.5$, Horsea $0.8$. The Pokémon **fled**. Find $P(\text{Horsea}\given\text{fled})$.

**C5.10.** 🟡 A disguised Voltorb explodes w.p. $0.7$ if it's a live decoy and $0.05$ if it's a dud; the bag is $20\%$ live decoys. You toss one and it **does not explode**. Find $P(\text{live}\given\text{no explosion})$.

**C5.11.** 🟡 A box has $10$ eggs, $3$ Shiny. Draw two without replacement. Find the probability **at least one** is Shiny.

**C5.12.** 🟡 Three Game Corner machines pay out independently: $X$ w.p. $0.2$, $Y$ w.p. $0.3$, $Z$ w.p. $0.25$. One pull each. Find the probability **exactly two** pay out.

**C5.13.** 🔵 *(Inverts WE 5.4.)* Misty leads Staryu ($0.5$), Starmie ($0.3$), Psyduck ($0.2$) with super-effective rates $0.3, 0.6, 0.1$. Her opener **was** super-effective. Find $P(\text{Starmie}\given\text{super-effective})$.

**C5.14.** 🔵 A diagnostic for rare Pokérus has sensitivity $0.99$ and specificity $0.96$; prevalence $0.5\%$. A Pokémon tests positive. Find $P(\text{infected}\given\text{positive})$ and comment on why it is small.

**C5.15.** 🟡 Of three identical-looking Poké Balls, one is a trick ball (releases its Pokémon $80\%$ of the time), the other two release $100\%$ of the time. You pick one at random, throw it, and the **Pokémon stays in**. Find $P(\text{trick}\given\text{stays in})$.

**C5.16.** 🔵 Lt. Surge opens turn one. Let $A$ = "his lead is Electric" and $B$ = "he wins the opening turn." Surge leads Electric $30\%$ of the time ($P(A)=0.3$); when he does he wins turn one w.p. $P(B\given A)=0.7$, and when he leads something else he wins turn one w.p. $P(B\given A^c)=0.4$. You only saw the result of turn one. Find $P(A\given B)$ (he won — was the lead Electric?) and $P(A\given B^c)$ (he lost turn one — was it Electric?).

**C5.17.** 🟡 Three lure urns: Urn I has $2$ red, $3$ blue; Urn II has $4$ red, $1$ blue; Urn III has $1$ red, $4$ blue. Pick an urn uniformly, draw one lure; it's **red**. Find $P(\text{Urn II}\given\text{red})$.

**C5.18.** 🔵 On a spinner, events $A,B,C$ each have probability $\tfrac12$ with all three pairwise intersections equal to $\tfrac14$, but $P(A\cap B\cap C)=\tfrac14$. Show $A,B,C$ are **pairwise independent but not mutually independent**.

### Elite Challenge (integrative / stretch)

**C5.19.** 🔵 *(Counting + Bayes.)* Bag 1 has $6$ Poké Balls and $4$ Great Balls; Bag 2 has $3$ Poké Balls and $7$ Great Balls. Pick a bag at random, draw **two without replacement**; both are Poké Balls. Find $P(\text{Bag 1}\given\text{two Poké})$.

**C5.20.** 🔵 *(Sequential updating.)* The phantom thief strikes **two** nights running, each leaving wet footprints, by the same unknown group. Using the Gym Battle figures (Traveler share $0.60$, steal $0.05$, clue $0.40$; Local $0.35$, $0.01$, $0.20$; Rocket $0.05$, $0.30$, $0.90$), and treating the two nights as conditionally independent given the group, find $P(\text{Rocket}\given\text{two clue thefts})$.

**C5.21.** 🔵 *(Bayes feeding a decision.)* Joy quarantines only if the posterior of disease exceeds $0.5$. Prevalence $4\%$, sensitivity $0.9$, false-positive rate $0.05$. (a) After one positive scan, does she quarantine? (b) After **two independent** positive scans? Show the posterior in each case.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C5.1** — *Direct conditional probability (Entry №01).*
$$P(\text{Water}\given\text{grass}) = \frac{P(\text{Water}\cap\text{grass})}{P(\text{grass})} = \frac{12/100}{30/100} = \frac{12}{30} = 0.40.$$

**C5.2** — *Conditional probability, without replacement (Entry №02).* After removing one Poké Ball, $4$ Great Balls remain among $8$:
$$P(\text{2nd Great}\given\text{1st Poké}) = \frac{4}{8} = 0.50.$$

**C5.3** — *"At least one" via complement, independence (Entries №03, №04).*
$$P(\text{shines}) = 1 - P(\text{both fail}) = 1 - (0.1)(0.2) = 1 - 0.02 = 0.98.$$

**C5.4** — *Exactly-one of two independent events (Entry №04).*
$$P(\text{exactly one}) = 0.6(1-0.7) + (1-0.6)(0.7) = 0.18 + 0.28 = 0.46.$$

**C5.5** — *Law of total probability, forward (Entry №05).*
$$P(\text{flood}) = (0.3)(0.5) + (0.7)(0.05) = 0.15 + 0.035 = 0.185.$$

**C5.6** — *Two-way Bayes on a negative result (Entry №06).* Here $P(\text{neg}\given\text{sick})=1-0.90=0.10$ and $P(\text{neg}\given\text{healthy})=1-0.20=0.80$.

| | prior | $P(\text{neg}\given\cdot)$ | joint |
|---|---|---|---|
| sick | $0.10$ | $0.10$ | $0.010$ |
| healthy | $0.90$ | $0.80$ | $0.720$ |
| total | | | $0.730$ |

$$P(\text{sick}\given\text{neg}) = \frac{0.010}{0.730} \approx 0.0137.$$

**C5.7** — *Chained multiplication, without replacement (Entry №02).*
$$P(\text{both Fire}) = \frac{3}{5}\cdot\frac{2}{4} = \frac{6}{20} = 0.30.$$

**C5.8** — *Independence test via the multiplication rule (Entries №03, №04).* By inclusion–exclusion, $P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.4+0.5-0.65 = 0.25$. Compare to $P(A)P(B) = (0.4)(0.5) = 0.20$. Since $0.25 \neq 0.20$, $A$ and $B$ are **not independent** (positively associated).

**C5.9** — *$n$-way Bayes from a 3-way partition (Entry №06).*

| species | prior | $P(\text{flee}\given\cdot)$ | joint |
|---|---|---|---|
| Goldeen | $0.50$ | $0.2$ | $0.10$ |
| Seaking | $0.30$ | $0.5$ | $0.15$ |
| Horsea | $0.20$ | $0.8$ | $0.16$ |
| total | | | $0.41$ |

$$P(\text{Horsea}\given\text{fled}) = \frac{0.16}{0.41} \approx 0.390.$$

**C5.10** — *Two-way Bayes on a non-event (Entry №06).* $P(\text{no boom}\given\text{live})=1-0.7=0.30$, $P(\text{no boom}\given\text{dud})=1-0.05=0.95$.

| | prior | $P(\text{no boom}\given\cdot)$ | joint |
|---|---|---|---|
| live | $0.20$ | $0.30$ | $0.060$ |
| dud | $0.80$ | $0.95$ | $0.760$ |
| total | | | $0.820$ |

$$P(\text{live}\given\text{no boom}) = \frac{0.060}{0.820} \approx 0.0732.$$

**C5.11** — *"At least one," without replacement, complement (Entries №02, №03).*
$$P(\text{no Shiny}) = \frac{7}{10}\cdot\frac{6}{9} = \frac{42}{90} = \frac{7}{15}, \qquad P(\text{at least one}) = 1 - \frac{7}{15} = \frac{8}{15} \approx 0.533.$$

**C5.12** — *Exactly-two of three independent events (Entry №04).* Sum the three "two win, one loses" products with $p_X=0.2, p_Y=0.3, p_Z=0.25$:
$$\begin{aligned}
&\underbrace{(0.2)(0.3)(0.75)}_{X,\,Y,\,Z^c} + \underbrace{(0.2)(0.7)(0.25)}_{X,\,Z,\,Y^c} + \underbrace{(0.8)(0.3)(0.25)}_{Y,\,Z,\,X^c} \\
&= 0.045 + 0.035 + 0.060 = 0.140.
\end{aligned}$$

**C5.13** — *Bayes inversion of a total-probability setup (Entries №05, №06).* From WE 5.4, $P(E)=0.35$; the Starmie joint is $(0.3)(0.6)=0.18$.
$$P(\text{Starmie}\given E) = \frac{0.18}{0.35} \approx 0.514.$$

**C5.14** — *False-positive classic, extreme base rate (Entry №06).* $P(+\given\text{inf})=0.99$, $P(+\given\text{not})=1-0.96=0.04$, prevalence $0.005$.

| | prior | $P(+\given\cdot)$ | joint |
|---|---|---|---|
| infected | $0.005$ | $0.99$ | $0.004950$ |
| not | $0.995$ | $0.04$ | $0.039800$ |
| total | | | $0.044750$ |

$$P(\text{inf}\given +) = \frac{0.004950}{0.044750} \approx 0.1106.$$
It is small because the disease is so rare ($0.5\%$) that false positives among the $99.5\%$ healthy population vastly outnumber the few true positives.

**C5.15** — *Bayes with equal priors, zero-likelihood elimination (Entry №06).* Priors $\tfrac13$ each; $P(\text{stay}\given\text{trick})=0.20$, $P(\text{stay}\given\text{normal})=0$.

| | prior | $P(\text{stay}\given\cdot)$ | joint |
|---|---|---|---|
| trick | $1/3$ | $0.20$ | $0.0\overline{6}$ |
| normal 1 | $1/3$ | $0$ | $0$ |
| normal 2 | $1/3$ | $0$ | $0$ |
| total | | | $0.0\overline{6}$ |

$$P(\text{trick}\given\text{stay}) = \frac{(1/3)(0.20)}{(1/3)(0.20)} = 1.$$
A normal ball *never* fails to release, so a stay-in can only have come from the trick ball — the zero likelihoods eliminate the other causes.

**C5.16** — *2×2 Bayes, both conditions (Entries №05, №06).* First $P(B) = (0.3)(0.7)+(0.7)(0.4) = 0.21+0.28 = 0.49$.
$$P(A\given B) = \frac{(0.3)(0.7)}{0.49} = \frac{0.21}{0.49} \approx 0.4286.$$
For $B^c$: $P(B^c)=0.51$ and $P(A\cap B^c) = (0.3)(1-0.7) = 0.09$, so
$$P(A\given B^c) = \frac{0.09}{0.51} \approx 0.1765.$$

**C5.17** — *Classic urn Bayes (Entry №06).* Priors $\tfrac13$ each; $P(\text{red}\given\text{I})=\tfrac25$, $\tfrac45$ for II, $\tfrac15$ for III.

| urn | prior | $P(\text{red}\given\cdot)$ | joint |
|---|---|---|---|
| I | $1/3$ | $2/5$ | $2/15$ |
| II | $1/3$ | $4/5$ | $4/15$ |
| III | $1/3$ | $1/5$ | $1/15$ |
| total | | | $7/15$ |

$$P(\text{II}\given\text{red}) = \frac{4/15}{7/15} = \frac{4}{7} \approx 0.571.$$

**C5.18** — *Pairwise vs. mutual independence (Entry №04).* Each pair multiplies: $P(A\cap B)=\tfrac14 = (\tfrac12)(\tfrac12) = P(A)P(B)$, and likewise for $A\cap C$ and $B\cap C$ — so the events are **pairwise independent**. But mutual independence additionally requires
$$P(A\cap B\cap C) = P(A)P(B)P(C) = \tfrac18.$$
Here $P(A\cap B\cap C) = \tfrac14 \neq \tfrac18$, so the triple condition **fails**: pairwise independent, **not** mutually independent. (Knowing $A\cap B$ occurred forces $C$, so the three together are dependent.)

**C5.19** — *Bayes with a without-replacement likelihood (Entries №02, №06).* Likelihood of "two Poké Balls" from each bag:
$$P(\text{2 Poké}\given\text{Bag 1}) = \frac{6}{10}\cdot\frac{5}{9} = \frac{1}{3}, \qquad P(\text{2 Poké}\given\text{Bag 2}) = \frac{3}{10}\cdot\frac{2}{9} = \frac{1}{15}.$$
Priors $\tfrac12$ each.

| bag | prior | likelihood | joint |
|---|---|---|---|
| 1 | $1/2$ | $1/3$ | $1/6$ |
| 2 | $1/2$ | $1/15$ | $1/30$ |
| total | | | $1/5$ |

$$P(\text{Bag 1}\given\text{2 Poké}) = \frac{1/6}{1/6 + 1/30} = \frac{1/6}{1/5} = \frac{5}{6} \approx 0.833.$$

**C5.20** — *Sequential Bayesian updating, conditionally independent evidence (Entries №02, №06).* Per-night likelihood = steal $\times$ clue: Traveler $0.05\cdot0.40 = 0.02$, Local $0.01\cdot0.20 = 0.002$, Rocket $0.30\cdot0.90 = 0.27$. Two conditionally independent nights $\to$ square each, then weight by population share:

| group | share | (per-night)$^2$ | joint weight |
|---|---|---|---|
| Traveler | $0.60$ | $0.02^2 = 0.0004$ | $0.000240$ |
| Local | $0.35$ | $0.002^2 = 0.000004$ | $0.00000140$ |
| Rocket | $0.05$ | $0.27^2 = 0.0729$ | $0.0036450$ |
| total | | | $0.00388640$ |

$$P(\text{Rocket}\given\text{two clue thefts}) = \frac{0.0036450}{0.00388640} \approx 0.938.$$
A second consistent night drives the Rocket posterior from $0.515$ (one night) to $\approx 0.94$ — evidence compounds.

<figure>
<img src="../../assets/diagrams/ch04_sequential_update.png" alt="A before/after bar chart of the phantom-thief posteriors for Traveler, Local, and Rocket. After one night the bars are 0.458, 0.027, 0.515. After two consistent nights the bars become roughly 0.06, 0.0004, 0.94, showing the posterior sharpening toward the Rocket grunt as consistent evidence compounds." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Sequential updating: one night leaves the case nearly a coin-flip ($0.515$); a second consistent night drives the Rocket posterior to $\approx 0.94$.</figcaption>
</figure>

**C5.21** — *False-positive Bayes feeding a decision rule, repeated evidence (Entry №06).* Prevalence $0.04$, sensitivity $0.9$, false-positive rate $0.05$.

(a) One positive:

| | prior | $P(+\given\cdot)$ | joint |
|---|---|---|---|
| sick | $0.04$ | $0.9$ | $0.036$ |
| healthy | $0.96$ | $0.05$ | $0.048$ |
| total | | | $0.084$ |

$$P(\text{sick}\given +) = \frac{0.036}{0.084} \approx 0.4286 < 0.5 \;\Rightarrow\; \textbf{no quarantine}.$$

(b) Two independent positives $\to$ square the likelihoods:

| | prior | $P(+,+\given\cdot)$ | joint |
|---|---|---|---|
| sick | $0.04$ | $0.9^2 = 0.81$ | $0.0324$ |
| healthy | $0.96$ | $0.05^2 = 0.0025$ | $0.0024$ |
| total | | | $0.0348$ |

$$P(\text{sick}\given +,+) = \frac{0.0324}{0.0348} \approx 0.9310 > 0.5 \;\Rightarrow\; \textbf{quarantine}.$$
One test is inconclusive; a second independent positive flips the decision — the same compounding-evidence lesson as C5.20.

**C5.22** — *Independence: product rule for two independent successes (Entry №04).* Independence lets the joint factor:
$$P(\text{both}) = P(A)\,P(B) = (0.6)(0.75) = 0.45.$$
For "at least one," complement the "neither" event (which also factors, since the throws are independent):
$$P(\text{at least one}) = 1 - P(\text{neither}) = 1 - (1-0.6)(1-0.75) = 1 - (0.4)(0.25) = 1 - 0.10 = 0.90.$$

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C5.1 | $0.40$ | | C5.12 | $0.140$ |
| C5.2 | $0.50$ | | C5.13 | $\approx 0.514$ |
| C5.3 | $0.98$ | | C5.14 | $\approx 0.1106$ |
| C5.4 | $0.46$ | | C5.15 | $1$ |
| C5.5 | $0.185$ | | C5.16 | $0.4286;\ 0.1765$ |
| C5.6 | $\approx 0.0137$ | | C5.17 | $4/7 \approx 0.571$ |
| C5.7 | $0.30$ | | C5.18 | pairwise yes, mutual no |
| C5.8 | not independent | | C5.19 | $5/6 \approx 0.833$ |
| C5.9 | $\approx 0.390$ | | C5.20 | $\approx 0.938$ |
| C5.10 | $\approx 0.0732$ | | C5.21 | (a) $0.4286$ no; (b) $0.9310$ yes |
| C5.11 | $8/15 \approx 0.533$ | | C5.22 | both $0.45$; at least one $0.90$ |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/cascade_badge.png" alt="Cascade Badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Cascade Badge earned!</strong></figcaption>
</figure>

You earn the **Cascade Badge** when you can, unaided:

1. **Compute** a conditional probability $P(A\given B)$ from a table or verbal setup (shrinking the world), and chain sequential without-replacement draws with the **multiplication rule**. *(Outcomes 1c, 1e.)*
2. **Apply** the **addition rule** for unions, and **distinguish** independent from mutually exclusive — testing independence via $P(A\cap B)=P(A)P(B)$ and telling **pairwise** from **mutual** independence. *(Outcomes 1d, 1e.)*
3. **Assemble** an unconditional probability with the **law of total probability** over a partition, and sanity-bound it between the smallest and largest conditional rate. *(Outcome 1f.)*
4. **Invert** a conditional with **Bayes' theorem** (two-way and $n$-way) using the detective's grid, and **explain** why the **base rate** keeps a strong clue from implying near-certain guilt — avoiding the prosecutor's fallacy. *(Outcome 1g.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 $\to$ re-read Concept 2 + WE 5.3. Miss item 2 $\to$ Concept 4 + C5.18. Miss item 3 $\to$ Concept 5 + WE 5.4 / C5.5. Miss item 4 $\to$ rebuild the grid in Concept 6, WE 5.1–5.2, and the Gym Battle, then retry C5.14 and C5.20.

*Onward — where the evidence stops being a single clue and becomes a whole **random variable**.*
