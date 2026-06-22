<!--
  file: ch01_fundamentals
  tier: C (set algebra), B (inclusion-exclusion)
  outcomes: 1a, 1d, 1e
  tia: A.1.1-A.1.5
  locale: Route 1 (the Spearow swarm)
  type: flying
  maps_to: Route 1 -- you can't track every bird, so you reason about events. Tutorial route, no badge: the Trainer's License.
-->

# Fundamentals of Probability {.type-flying}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Pallet Town and Route 1 highlighted at the southern edge; the road north toward Viridian City stretches ahead, still unwalked." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>The journey to a 10 starts here — Pallet Town and Route 1, where every probability you will ever compute first needs a <em>place to live</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Sky Turns Black"**

You are ten years old, and the Poké Ball will not close.

Professor Oak warned you the last starter was unusual. You toss the ball anyway, and a small yellow Pokémon — **Pikachu, #025** — bats it aside and folds its arms. You sling it onto your shoulder and step out of Pallet Town onto **Route 1**.

Tall grass. Somewhere in it: a Pidgey, maybe a Rattata, maybe nothing at all — you can't see which. You throw a rock at a tree to scare something up, and you hit a **Spearow**.

That was a mistake.

The Spearow shrieks, and the sky answers. Not one bird but a *flock* — a dozen, two dozen, more — lifts off the treeline and wheels toward Pikachu, who is hurt, slow, and still refusing the ball that would protect it. Each diving Spearow may or may not strike. You **cannot track every bird**. You cannot list every dive. But you must decide *now* whether to run or make a stand, and that decision hinges on one number:

*What is the probability that **at least one** Spearow reaches Pikachu?*

The Pokédex chirps to **Actuary Mode**. Oak's voice crackles through: "You'll never get there by counting birds, Ash. First, count the **space** — the list of everything that *could* happen. Then count what you *don't* want, and subtract."

Far to the north, through the storm clouds gathering over the river, a band of color flickers for half a second — a rainbow that should not be there in the rain. You'll learn what it means much later. For now: *you have no idea what Oak meant.* You will by the end of this chapter.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP001 "Pokémon! I Choose You!" + EP002 "Pokémon Emergency!"**

Ash gets an unruly Pikachu, and on Route 1 a whole flock of Spearow descends — he can't track every bird, only reason about "will *any* of them reach Pikachu?" That "at least one of a swarm" question is exactly this chapter. EP002 brings the first Pokémon Center and Team Rocket's debut. Watch these before reading. *(The catalogue-the-route framing is our in-world extension.)*
:::

## Where You Are — 60-Second Retrieval

**Rank: Rookie Trainer · Badges: 0.** This is the first real chapter of the journey — you have just left Pallet Town, and there is no prior *probability* chapter to retrieve. But everything here stands on the **Toolkit** you already built in orientation: a **set** is just a collection of things, and you can read a fraction. That is all you need. Take sixty seconds and prove you still own it before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you own the toolkit**

Answer from memory; if any feels shaky, flip back to the orientation Toolkit before continuing.

1. A bag holds 4 red and 6 blue lures. You draw one at random. What is $P(\text{red})$? *(Answer: $4/10 = 0.4$ — favorable over total.)*
2. What does the word **set** mean? *(Answer: an unordered collection of distinct things, written in braces $\{\dots\}$.)*
3. What is $1 - 0.3$? *(Answer: $0.7$. Yes — this whole chapter leans on subtraction this easy.)*

All three instant? You're ready. Any hesitation? Reclaim it, then come back. The retrieval *is* the lesson.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Oak's hologram flickers up from the Pokédex as you run.

"Before you can ever ask *what's the chance*, Ash, you must answer *the chance — out of **what**?* Every probability in this book lives inside a **space of possible outcomes**. Today you build that space, learn its three unbreakable rules, and learn the bookkeeping — *not*, *or*, *and* — that turns a hopeless count of diving Spearow into one clean subtraction. Master this and you'll save Pikachu. Get sloppy with it, and you'll spend the rest of the syllabus double-counting."

By the end of this chapter you will be able to:

- **Describe** a **sample space** $S$, list its outcomes, and write events as subsets of $S$; **manipulate** set operations (union, intersection, complement), picture them in **Venn diagrams**, and use **De Morgan's laws** to rewrite "none / neither." *(Outcome 1a.)*
- **State** the three (Kolmogorov) probability **axioms** and **derive** their consequences: $P(\varnothing)=0$, the **complement rule**, and monotonicity. *(Outcome 1a.)*
- **Distinguish** *mutually exclusive* events from the addition rule's overlap term, and recognize disjointness. *(Outcome 1d.)*
- **Compute** probabilities with the **addition rule / inclusion–exclusion** for two and three events, and deploy the **complement trick** $P(\text{at least one}) = 1 - P(\text{none})$. *(Outcome 1e.)*
- **Avoid** the year's single most-confused pair: *mutually exclusive* versus *independent*. *(Outcomes 1d, 1e.)*

> *Exam-weight signpost.* This is **General Probability — Outcome 1a/1d/1e**, the foundation under every later chapter (General Probability is 23–30% of Exam P). The set-algebra is **Tier C** — the ideas are not hard, so we move briskly — but **inclusion–exclusion is Tier B** and the *mutually-exclusive-vs-independent* trap is tested *constantly*, so those two get the full treatment. Nothing here is compressed: each idea runs the complete arc with a real derivation.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Route 1?**

Already fluent? Prove it. Work these four, about 2 minutes each, *with correct method*:

1. A wild slot is Pidgey ($0.45$), Rattata ($0.30$), Spearow ($0.15$), or nothing. Find $P(\text{some Pokémon appears})$.
2. $P(A)=0.6$, $P(B)=0.5$, $P(A\cap B)=0.2$. Find $P(A\cup B)$.
3. Pikachu refuses each of $3$ independent throws w.p. $0.5$. Find $P(\text{the ball closes at least once})$.
4. $A,B$ each have positive probability and are *mutually exclusive*. Can they be *independent*? One word, with the reason.

*(Answers: $0.90$; $0.90$; $0.875$; **no** — disjoint positive-probability events are maximally dependent.)* Four for four with the right reasoning? **Skip to the Gym Challenge** and stamp your Trainer's License. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Five ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then a lesson sized to its difficulty, then a Pokédex Entry you can carry into the exam:

1. **The sample space** — naming the world of outcomes *(the foundation everything uses)*
2. **The three axioms** — the unbreakable rules, and what they force to be true
3. **Set operations & De Morgan** — *and*, *or*, *not*, and rewriting "none"
4. **Inclusion–exclusion** — "or," and the overlap you must not double-count
5. **Mutually exclusive vs. independent** — the trap that sinks people all year

## Concept 1 — The Sample Space: Naming the World

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sample Space**

A single Route 1 encounter yields a Pidgey, a Rattata, a Spearow, or nothing. Write the sample space $S$, and write the event "a bird appears" as a subset of it.

If you instantly wrote $S=\{\text{Pidgey},\text{Rattata},\text{Spearow},\text{nothing}\}$ and the event as $\{\text{Pidgey},\text{Spearow}\}$, you own this — **skip to Concept 2**. If "sample space" or "event as a subset" felt unfamiliar, read on.
:::

**Beat 1 — The one-sentence idea.** *Before you can measure a chance, you list every outcome that could happen; that complete list is the world the probability lives in.*

**Beat 2 — Anchor + concrete instance.** A **set** (from the Toolkit) is just a collection. Here the collection is *everything that could happen* on one wild encounter. Step into the Route 1 grass. Exactly one of four things greets you: a Pidgey, a Rattata, a Spearow, or nothing rustles.

**Beat 3 — Reason through it in plain words.** Write that complete list inside braces. Nothing outside the list can happen; the list misses nothing. *That* list — the universe of outcomes — is the thing every later probability is measured against. A *single outcome* is one item in the list (say, "Spearow"). An **event** is any yes/no question you can ask about the outcome — "did a bird appear?" — which corresponds to the *subset* of outcomes for which the answer is yes: $\{\text{Pidgey},\text{Spearow}\}$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The beginner's slip is to forget an outcome — to write $S=\{\text{Pidgey},\text{Rattata},\text{Spearow}\}$ and quietly drop "nothing." But if "nothing" can happen, it *must* be in the space, or your probabilities won't sum to $1$ and every later answer inherits the error. **The space must be exhaustive: list everything, even the boring outcome.**

**Beat 5 — Translate into notation, one glyph at a time.** We name the space with a capital $S$ (for *sample Space*). Braces $\{\ \}$ hold a set. The symbol $\subseteq$, read aloud **"is a subset of,"** says one set sits entirely inside another. And $\in$, read **"is an element of,"** says a single thing is a member.

$$S = \{s_1, s_2, \dots\}, \qquad A \subseteq S \ \ (\text{``}A \text{ is a subset of } S\text{''}), \qquad s \in A \ \ (\text{``}s \text{ is in } A\text{''}).$$

We say "**event $A$ occurs**" exactly when the realized outcome $s$ lands inside $A$ — that is, when $s \in A$.

**Beat 6 — Generalize.** There is nothing to derive here: the sample space is a *definition*, the starting board on which the whole game is played. Every other concept in this chapter is a move on this board. (When we *do* assign probabilities to those outcomes in Concept 2, the derivations begin.)

**Beat 7 — Ramp the difficulty.** *Simplest:* a four-outcome encounter, above. *Twist:* the space can be huge or even infinite — "how many Spearow dive before one hits Pikachu?" has space $\{1,2,3,\dots\}$. *Edge:* the **empty set** $\varnothing$ (read "the empty set") is the event with no outcomes — the *impossible* event, e.g. "the encounter is both a Pidgey and a Rattata at once."

**Beat 8 — Picture it.** Think of $S$ as a box and each outcome as a labeled chip dropped inside. The space is exhaustive exactly when no chip is missing — including the dull "nothing" chip it is so easy to forget.

<figure>
<img src="../../assets/diagrams/ch01_sample_space_box.png" alt="A rounded rectangle labeled 'S — the sample space (every outcome, nothing missing)' containing four labeled outcome chips in a row: Pidgey, Rattata, Spearow, and nothing. Each Pokemon chip shows its sprite; the 'nothing' chip reads '(no encounter)'. A red arrow points up at the 'nothing' chip with the warning 'don't drop the boring outcome', stressing that the easy-to-forget no-encounter outcome still belongs inside the space.">
<figcaption>The world $S$ as a box of outcome chips. Every chip that <em>can</em> happen must be in the box — drop the boring "nothing" chip and your probabilities no longer sum to $1$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any random situation, name its sample space $S$, and write any event as a subset of $S$. That single move — *name the world first* — is the discipline the entire book is built on.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Sample Space, Outcome, Event**

$$S = \{\,s_1, s_2, \dots\,\}, \qquad A \subseteq S, \qquad A \text{ occurs} \iff s \in A.$$

*In plain terms:* $S$ is the complete, exhaustive list of everything that could happen; an **outcome** is one item; an **event** is a yes/no question, i.e. the subset of outcomes that answer "yes."

*Recognition cue:* whenever a problem describes a random situation and asks "what is the chance of…," your **first move** is to name $S$ — the universe the probability lives in. If "nothing" can happen, put it in.
:::

## Concept 2 — The Three Axioms (and What They Force)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Axioms**

State the three probability axioms from memory, then use them to prove $P(A^c) = 1 - P(A)$.

If you can rattle off "non-negative · whole space has mass $1$ · disjoint events add" and derive the complement rule in two lines, **skip to Concept 3**. Otherwise, read on — this is the bedrock and the proof is short.
:::

**Beat 1 — The one-sentence idea.** *Three simple rules pin down what the word "probability" is allowed to mean — and everything else in the chapter is squeezed out of those three lines.*

**Beat 2 — Anchor + concrete instance.** You already used these rules without naming them: on Route 1 the four encounter masses $0.45, 0.30, 0.15, 0.10$ are each $\ge 0$ and add to $1$. The axioms (due to Kolmogorov) just *state out loud* what made that a legitimate assignment.

**Beat 3 — Reason through it in plain words.** What must any sensible "chance" obey? (i) A chance is never negative — there's no such thing as $-20\%$. (ii) *Something* in the space is certain to happen, so the whole space has chance $1$. (iii) If two events can't both occur, the chance that *one or the other* happens is just their two chances added — no overlap to worry about.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to think rule (iii) lets you *always* add: "$P(\text{Water-type}) + P(\text{lives in grass})$." No — rule (iii) only grants addition when the events are **disjoint** (cannot co-occur). Adding overlapping events double-counts the middle, and the axiom gives you *no* license to do it. (Fixing that overlap is Concept 4.) Whenever you add probabilities, silently check: *are these pieces really disjoint?*

**Beat 5 — Translate into notation, one glyph at a time.** The symbol $\varnothing$ is the empty set; $A \cap B = \varnothing$ (read "$A$ and $B$ are **disjoint**") says they share no outcome. The cup $\cup$ reads "or / union."

$$\textbf{(A1)}\ P(A) \ge 0, \qquad \textbf{(A2)}\ P(S) = 1, \qquad \textbf{(A3)}\ A\cap B=\varnothing \Rightarrow P(A\cup B)=P(A)+P(B).$$

(A3 extends to any countable pile of pairwise-disjoint events.)

**Beat 6 — Derive the consequences (this is the payoff).** We don't *assume* the complement rule — we *prove* it. An event $A$ and its opposite $A^c$ ("not $A$") are disjoint and together fill the whole space, so $A \cup A^c = S$. Apply A3 to the disjoint pair, then A2:

$$P(A) + P(A^c) = P(A \cup A^c) = P(S) = 1 \quad\Longrightarrow\quad \boxed{P(A^c) = 1 - P(A)}.$$

Set $A = S$ (so $A^c = \varnothing$) and you also get $P(\varnothing) = 1 - P(S) = 0$ — the impossible event has chance zero. And if $A$ sits inside $B$ ($A \subseteq B$), then $B$ is "$A$ plus the disjoint leftover $B\cap A^c$," so $P(B) = P(A) + P(B\cap A^c) \ge P(A)$ — **monotonicity**: a bigger event is at least as likely. Three free theorems, all from three lines.

**Beat 7 — Ramp the difficulty.** *Simplest:* read $P(A^c)=1-P(A)$ off a single given. *Twist:* the complement rule is the chapter's workhorse — "at least one" is almost always faster as $1 - P(\text{none})$ (Concept 4). *Edge:* monotonicity instantly bounds anything: since $A\cap B \subseteq A$, you always have $P(A\cap B) \le P(A)$, a free sanity check on every answer; and combined with A1/A2 it pins every probability into $0\le P(A)\le 1$.

**Beat 8 — Picture it.** No new figure is needed: picture the box $S$ from Concept 1 with total mass $1$ poured in. The complement rule is just "the part outside $A$ holds whatever mass $A$ didn't" — $1$ minus $A$'s share. The Venn rectangle of Concept 3 will make this literal.

**Beat 9 — Consolidate.** You can now state the three axioms and derive the complement rule, $P(\varnothing)=0$, and monotonicity on demand — and you know that adding probabilities is *only* licensed for disjoint events.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Axioms & Their Consequences**

$$\textbf{(A1)}\ P(A)\ge 0, \quad \textbf{(A2)}\ P(S)=1, \quad \textbf{(A3)}\ A\cap B=\varnothing \Rightarrow P(A\cup B)=P(A)+P(B).$$

Forced consequences: $\;P(A^c)=1-P(A)$ (complement rule), $\;P(\varnothing)=0$, $\;A\subseteq B\Rightarrow P(A)\le P(B)$ (monotonicity), $\;0\le P(A)\le 1$.

*In plain terms:* chances are never negative, the whole space is certain, and *disjoint* chances add. Everything else is squeezed out of those three.

*Recognition cue:* the words **"not," "at least," "complement"** call for $1-P(A)$. And before you *ever* add two probabilities, confirm the pieces are disjoint — A3 is the only rule that lets you add.
:::

## Concept 3 — Set Operations & De Morgan: *and*, *or*, *not*

::: concept-gate
**DO YOU ALREADY OWN THIS? — Set Operations & De Morgan**

Rewrite "**neither** $A$ **nor** $B$ happens" as an intersection of complements, and evaluate it given $P(A\cup B)=0.72$.

If you wrote $(A\cup B)^c = A^c\cap B^c$ and got $1-0.72 = 0.28$, **skip to Concept 4**. If "De Morgan" or "neither" felt slippery, read on.
:::

**Beat 1 — The one-sentence idea.** *Events combine with three operations — and, or, not — and one law (De Morgan) that turns any "none/neither" into an "and not… and not…".*

**Beat 2 — Anchor + concrete instance.** On Route 1, let $G$ = "the encounter is a Pidgey" and $W$ = "the encounter is a Spearow." From these you can build new events: "a bird (Pidgey *or* Spearow)," "*not* a Pidgey," and so on.

**Beat 3 — Reason through it in plain words.** "$A$ **or** $B$" (at least one happens) collects the outcomes in either event. "$A$ **and** $B$" (both happen) collects the outcomes in both. "**not** $A$" collects everything in $S$ outside $A$. The subtle one is **"neither / none."** "Neither $A$ nor $B$" means "$A$ didn't happen *and* $B$ didn't happen." So a statement about a *union* ("not even one of them") secretly becomes a statement about an *intersection* of "didn'ts." That swap — *negation flips* or *into* and — is **De Morgan's law**, and it is the single most useful rewrite in the chapter.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Tempting but wrong: "$(A\cup B)^c = A^c \cup B^c$." Test it in words: $(A\cup B)^c$ is "neither happened." $A^c \cup B^c$ is "at least one *didn't* happen" — which is true even if the *other* one did! Those are different events. The correct flip turns the *union's* complement into an *intersection*: $(A\cup B)^c = A^c \cap B^c$.

**Beat 5 — Translate into notation, one glyph at a time.** The union symbol $\cup$ reads **"or / union"**; the intersection $\cap$ reads **"and / intersect"**; the superscript $c$ in $A^c$ reads **"$A$-complement"** ("not $A$"). Backslash: $A\setminus B = A\cap B^c$ reads "$A$ but not $B$."

$$A\cup B\ (\text{or}), \quad A\cap B\ (\text{and}), \quad A^c = S\setminus A\ (\text{not}).$$

**Beat 6 — Derive De Morgan's first law by an element chase (not asserted).** Take any outcome $s$ and ask what it means to live in each side. To say $s \in (A\cup B)^c$ is to say $s$ is *not* in the union — $s$ is in **neither** circle. But "neither" unpacks directly: $s \notin A$ **and** $s \notin B$, i.e. $s \in A^c$ **and** $s \in B^c$, which is exactly $s \in A^c\cap B^c$. Every step was an "if and only if," so the two sides contain the *same* outcomes — they are the same set. Run the identical chase starting from $s \in (A\cap B)^c$ ("not in both" $=$ "missing from at least one") and you get the second law. Read aloud as "the complement of an *or* is the *and* of the complements," and vice versa:

$$\boxed{(A\cup B)^c = A^c\cap B^c, \qquad (A\cap B)^c = A^c\cup B^c.}$$

**Beat 7 — Ramp the difficulty.** *Simplest:* rewrite "neither $A$ nor $B$" $=(A\cup B)^c$ and finish with $1-P(A\cup B)$. *Twist:* De Morgan stretches across *many* events — "none of $n$ Spearow reaches Pikachu" is $\left(\bigcup_i A_i\right)^c = \bigcap_i A_i^c$, the workhorse of the Cold Open. *Edge:* the two laws are dual — flipping every $\cup\!\leftrightarrow\!\cap$ and complementing turns one identity into the other.

**Beat 8 — Picture it.** A Venn diagram makes "or," "and," and "neither" literal regions inside the rectangle $S$.

<figure>
<img src="../../assets/diagrams/ch01_venn_two.png" alt="A two-circle Venn diagram inside a rectangle labeled S. The left circle is event A, the right circle is event B, their lens-shaped overlap is A-intersect-B ('and'), the combined shaded area is A-union-B ('or'), and the region outside both circles is the complement of the union, labeled (A union B)-complement = A-complement intersect B-complement, the 'neither' region.">
<figcaption>Two events in $S$. "Or" is both circles together; "and" is the overlap; "neither" is the region <em>outside</em> both — which De Morgan names $A^c\cap B^c$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now translate any English event into set notation, and the instant you read "none" or "neither," reach for De Morgan and the complement rule together: $P(\text{neither}) = P((A\cup B)^c) = 1 - P(A\cup B)$.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Set Operations & De Morgan's Laws**

$$A\cup B\ (\text{or}), \quad A\cap B\ (\text{and}), \quad A^c\ (\text{not}), \quad A\setminus B = A\cap B^c.$$
$$(A\cup B)^c = A^c\cap B^c, \qquad (A\cap B)^c = A^c\cup B^c.$$

*In plain terms:* "none of them happened" $=$ "this one didn't *and* that one didn't." Negation flips unions to intersections and back.

*Recognition cue:* the words **"none," "neither," "not any"** are De Morgan announcing itself — rewrite as an intersection of complements, then usually finish with $1-P(\cup)$.
:::

## Concept 4 — Inclusion–Exclusion: "Or," and the Overlap

::: concept-gate
**DO YOU ALREADY OWN THIS? — Inclusion–Exclusion**

You log $100$ Route 24 Pokémon: $40$ are Water-type, $30$ live in tall grass, $12$ are *both*. Pick one log at random. What is $P(\text{Water } \textbf{or}\text{ grass})$?

If you answered **$0.58$** (not $0.70$) and can say *why you subtract the $12$*, **skip to Concept 5**. If you got $0.70$, you double-counted the overlap — read on.
:::

**Beat 1 — The one-sentence idea.** *The chance of $A$ **or** $B$ is the two pieces added together, minus the overlap you'd otherwise count twice.*

**Beat 2 — Anchor + concrete instance.** This is axiom A3 with the *disjoint* restriction lifted. Two circles, $A$ (Water-type) and $B$ (tall grass), inside the rectangle of $100$ logs, **overlapping** in the $12$ that are both.

On **Route 24** — the river path just north of your road — you log **$100$ Pokémon**: **$40$ Water-type**, **$30$ live in tall grass**, **$12$ are both**. *What fraction is Water-type or grass-dwelling (at least one)?*

**Beat 3 — Reason through it in plain words.** Just add the piles and you get $40 + 30 = 70$ — but you've counted the **$12$ "both" Pokémon twice**, once in each pile. Each is one Pokémon, not two. Subtract the $12$ back out, once:

$$40 + 30 - 12 = 58 \quad\Longrightarrow\quad P(\text{Water or grass}) = \frac{58}{100} = 0.58.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting answer is the bare sum:

$$P(A) + P(B) = 0.40 + 0.30 = 0.70. \qquad\textbf{(wrong — double-counts the 12)}$$

That over-counts by exactly the overlap $\tfrac{12}{100} = 0.12$, leaving the correct $0.58$. The bare sum is right *only* when the circles don't overlap. The reverse error is just as common — *assuming* events can't overlap when they can. Don't assume the overlap is zero; **check it**.

**Beat 5 — Translate into notation, one glyph at a time.** "$A$ or $B$" is the union $A\cup B$; "$A$ and $B$" is the intersection $A\cap B$. "Subtract the overlap once" becomes the **two-event** rule (the **addition rule**):

$$P(A\cup B) = P(A) + P(B) - P(A\cap B).$$

When $A,B$ are **mutually exclusive** ($A\cap B=\varnothing$, so $P(A\cap B)=0$) the subtraction disappears and you are back to axiom A3: $P(A\cup B)=P(A)+P(B)$.

**Beat 6 — Derive it from the Venn partition (don't just assert it).** Split the union into three *disjoint* regions: "$A$ only" $(A\cap B^c)$, "$B$ only" $(A^c\cap B)$, and "both" $(A\cap B)$. Because they're disjoint, A3 lets their probabilities add: $P(A\cup B) = P(A\cap B^c) + P(A^c\cap B) + P(A\cap B)$. Now $P(A) = P(A\cap B^c) + P(A\cap B)$ and $P(B) = P(A^c\cap B) + P(A\cap B)$ — each single event is "its own-only part plus the shared middle." Add those two and the middle gets counted **twice**; subtract one copy to recover the union. The "$-P(A\cap B)$" isn't a rule to memorize — it's exactly the over-count you created.

<figure>
<img src="../../assets/diagrams/ch01_incl_excl.png" alt="Two overlapping circles for 100 Route 24 logs: a Water-type circle holding 40 (28 alone plus 12 shared) and a grass circle holding 30 (18 alone plus 12 shared), the 12 in the lens labelled 'both'. To the right the arithmetic 40 + 30 - 12 = 58 gives P(Water union grass) = 58/100 = 0.58, with a green box stating the addition rule P(A or B) = P(A) + P(B) - P(A and B): add both piles, then remove the 12 counted in both.">
<figcaption>Add the two piles ($40+30$), then subtract the $12$ counted in both. The overlap term in the addition rule is exactly that over-count.</figcaption>
</figure>

**Beat 7 — Ramp the difficulty.** *Three events* repeat the bookkeeping: add the singles, subtract every pair, add back the triple (the center got subtracted one time too many):

$$P(A\cup B\cup C) = P(A)+P(B)+P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C).$$

*Twist (the complement is often faster):* $P(\text{neither}) = 1 - P(A\cup B) = 1 - 0.58 = 0.42$. For "at least one," $1-P(\text{none})$ is frequently the cleanest road (the Cold Open and the Gym Battle both lean on it). *Edge:* if you're *told* the events are disjoint, the overlap is $0$ and the subtraction vanishes (back to A3) — but never *assume* disjointness; that's the trap of Concept 5.

**Beat 8 — Picture it.** A three-circle diagram has **seven** cells: three "only," three pair-overlaps, and one triple-overlap. Inclusion–exclusion's $+$singles $-$pairs $+$triple is precisely the bookkeeping that counts each of those seven cells exactly once.

<figure>
<img src="../../assets/diagrams/ch01_venn_three.png" alt="A three-circle Venn diagram inside rectangle S, with circles A, B, C. Seven labeled cells: three 'only' regions (A only, B only, C only), three pairwise-overlap lens regions (A intersect B, A intersect C, B intersect C), and the central triple-overlap region A intersect B intersect C. A caption notes that +singles -pairs +triple counts every cell exactly once.">
<figcaption>The seven cells of a three-event diagram. Inclusion–exclusion's $+$singles $-$pairs $+$triple guarantees every cell is counted exactly once.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute "or" for two or three events by adding and removing overlaps, isolate a single Venn cell, and switch to the complement when it's faster.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Addition Rule / Inclusion–Exclusion**

$$P(A\cup B) = P(A) + P(B) - P(A\cap B).$$
$$P(A\cup B\cup C) = \sum P(\text{singles}) - \sum P(\text{pairs}) + P(A\cap B\cap C).$$

If $A,B$ are **mutually exclusive**: $\;P(A\cup B) = P(A)+P(B).$

*In plain terms:* "or" adds the pieces but subtracts the overlaps you counted twice; for three events, add the triple back. The pattern is $+$singles, $-$pairs, $+$triple.

*Recognition cue:* **"at least one of," "either…or," "$A$ or $B$"** with overlapping events → inclusion–exclusion. Drop the overlap term *only* if you're told the events can't co-occur. For "at least one," check whether $1 - P(\text{none})$ is the faster road.
:::

## Concept 5 — Mutually Exclusive vs. Independent (The Trap)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mutually Exclusive vs. Independent**

Two events $A,B$ each have positive probability and are *mutually exclusive*. Can they ever be *independent*?

If you answered **"no — disjoint positive-probability events are maximally *dependent*,"** and can say why in one sentence, **skip to the Worked Examples**. If you hesitated, or thought "mutually exclusive sounds like independent," this section is the most important one in the chapter.
:::

**Beat 1 — The one-sentence idea.** *"Mutually exclusive" means two events can't both happen; "independent" means one happening tells you nothing about the other — and for positive-probability events these are opposites, never the same.*

**Beat 2 — Anchor + concrete instance.** You met disjointness in A3 (the overlap is $\varnothing$). Independence is new: it's the condition under which a joint chance *factors* into a product. Picture two of Ash's traps. **Trap A** springs w.p. $0.5$, **Trap B** w.p. $0.5$. Two scenarios: (i) only one trap can fire because they share a single spring — *mutually exclusive*; (ii) the traps are on opposite ends of the route and don't talk — *independent*.

**Beat 3 — Reason through it in plain words.** *Mutually exclusive* (scenario i): if A fires, B *cannot* — so learning "A fired" tells you *everything* about B (it didn't). That's the opposite of "tells you nothing." *Independent* (scenario ii): learning "A fired" leaves B's chance untouched at $0.5$, so the chance both fire is $0.5$ of $0.5 = 0.25$. The two scenarios give wildly different math from the *same two numbers* — which is exactly why confusing them is so costly.

**Beat 4 — Surface and dismantle the tempting wrong idea (the canonical misconception).** Here is the error that haunts the entire syllabus: **treating "mutually exclusive" and "independent" as synonyms.** They are nearly opposites. Suppose $A$ and $B$ each have positive probability and are mutually exclusive. Then if $A$ happens, $B$ is now *impossible* — knowing $A$ told you *everything* about $B$. Check the algebra: independence would require $P(A\cap B) = P(A)P(B) > 0$, but disjointness forces $P(A\cap B) = 0$. Contradiction. **Disjoint positive-probability events are maximally *dependent*, never independent.** And the practical fallout: for disjoint events you may *add* but never *multiply*; for independent events you may *multiply* but must *not* assume they're disjoint.

**Beat 5 — Translate into notation, one glyph at a time.** Two definitions, side by side:

$$\textbf{Mutually exclusive:}\ A\cap B = \varnothing \ \Rightarrow\ P(A\cap B) = 0.$$
$$\textbf{Independent:}\ P(A\cap B) = P(A)\,P(B).$$

Read the second aloud: "the chance both happen equals the chance of one *times* the chance of the other." Equivalently, "knowing $B$ doesn't change $A$": $P(A\mid B) = P(A)$ (the bar $\mid$ reads "given that" — you'll build it fully in the next chapter, at Cerulean).

**Beat 6 — These are definitions, not theorems.** Neither is derived: mutual exclusivity is a *fact about the outcomes* (the overlap is empty); independence is a *defining product condition*. The only content is keeping them straight — which the algebra in Beat 4 does permanently.

**Beat 7 — Ramp the difficulty.** *Simplest:* classify a stated pair. *Twist (the test cuts both ways):* given $P(A)=0.5$, $P(B)=0.4$, $P(A\cup B)=0.7$, back out $P(A\cap B) = 0.5+0.4-0.7 = 0.2$ and compare to $P(A)P(B) = 0.2$; equal, so **independent** (Worked Example 5). *Edge:* if two *disjoint* events have positive marginals, asking "are they independent?" is a trick — the answer is always **no**.

**Beat 8 — Picture it.** The Venn picture nails the contrast: mutually exclusive circles *don't touch*; independent circles *overlap by exactly $P(A)P(B)$* — the overlap is forced to a specific size, not zero.

<figure>
<img src="../../assets/diagrams/ch01_me_vs_indep.png" alt="Two side-by-side Venn panels inside rectangle S. Left panel, 'Mutually exclusive': two non-touching circles A and B with no overlap, labeled P(A and B)=0, captioned 'no overlap, you may ADD' and 'if A happens, B is impossible, so maximally DEPENDENT'. Right panel, 'Independent': two overlapping circles whose lens area equals exactly P(A) times P(B), labeled P(A and B)=P(A)P(B), captioned 'overlap FORCED nonzero, you may MULTIPLY', emphasizing the overlap is a forced specific size, not empty.">
<figcaption>Mutually exclusive (no overlap, so you may add) versus independent (overlap forced to $P(A)P(B)$, so you may multiply). They are opposite situations, never the same.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now classify any stated pair, test independence with the product rule, and — crucially — you will never again multiply disjoint events or assume that "can't both happen" means "tells you nothing."

::: pokedex-entry
**POKÉDEX ENTRY №05 — Mutually Exclusive vs. Independent**

$$\textbf{Mutually exclusive:}\ P(A\cap B)=0 \quad(\text{may } \textit{add}). \qquad \textbf{Independent:}\ P(A\cap B)=P(A)P(B) \quad(\text{may } \textit{multiply}).$$

*In plain terms:* mutually exclusive = "can't both happen"; independent = "one tells you nothing about the other." Two positive-probability events **cannot be both** — disjoint ones are maximally dependent.

*Recognition cue:* **"cannot both occur," "disjoint," "either…or but not both"** → mutually exclusive (multiplying is *forbidden*). **"does not affect," "separate mechanisms," "with replacement"** → independent (multiplying is *required*). Never assume either; you must be told it or derive it.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/25.png" alt="Pikachu" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#025 Pikachu</strong> — refusing the ball, counting on your math</figcaption>
</figure>

Five examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the "at least one" complement is the move you'll reuse most all year.

### Worked Example 1 — Saving Pikachu from the Flock (full narration; understanding-first)

**ARCHETYPE:** *"At least one" via the complement of independent events.*

**Setup.** This is the Cold Open, now a clean exam item. The Pokédex estimates each of the $n=12$ Spearow independently reaches Pikachu w.p. $p=0.20$. Find $P(\text{at least one reaches Pikachu})$.

<figure style="margin:1.25em auto; max-width:140px; text-align:center;">
<img src="../../assets/sprites/front/21.png" alt="Spearow, a Flying-type Pokemon" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#021 Spearow — one bird of the diving flock</figcaption>
</figure>

**Step 1 — Identify (which move?).** Let $A_i$ = "Spearow $i$ reaches Pikachu," $P(A_i)=0.2$, independent. We want $P(A_1\cup\cdots\cup A_{12})$. Inclusion–exclusion over $12$ events is hopeless. The phrase **"at least one"** is the tell: complement it.

**Step 2 — Professor's Path (the why).** "At least one reaches" is the opposite of "**none** reaches." First, three glyphs you'll meet stretched over many events — each is just a Concept-3 operator repeated. The big union $\bigcup_i A_i$ reads **"the union over all $i$"** — the *or* of Concept 3 run across every bird ("$A_1$ or $A_2$ or … or $A_{12}$"). The big intersection $\bigcap_i A_i^c$ reads **"the intersection over all $i$"** — the *and* across every bird ("$A_1^c$ and $A_2^c$ and …"). And the capital pi $\prod_{i=1}^{12}$ reads **"the product of"** — just multiply the twelve terms together, the multiplicative cousin of a sum.

Now the move. By De Morgan (Entry №03), stretched from two events to twelve, $\left(\bigcup_i A_i\right)^c = \bigcap_i A_i^c$ — "none reaches" is the *and* of all the "didn't reach"s. Because the dives are independent (Entry №05), that intersection's probability **factors** into a product:

$$P(\text{none}) = P\!\left(\bigcap_{i=1}^{12} A_i^c\right) = \prod_{i=1}^{12} P(A_i^c) = \underbrace{(0.8)(0.8)\cdots(0.8)}_{12 \text{ terms}} = (1-0.2)^{12} = (0.8)^{12}.$$

Then the complement rule (Entry №02) gives the answer in one subtraction.

**Step 3 — Trainer's Path (the fast how).**
$$P(\text{at least one}) = 1 - P(\text{none}) = 1 - (0.8)^{12} = 1 - 0.0687 = 0.9313.$$

On the TI-30XS MultiView this is one keystroke chain — no parentheses gymnastics: [ 1 [−]{.kbd} 0.8 [^]{.kbd} 12 [enter]{.kbd} ]{.keystroke}.

**Step 4 — Check & pitfall.** With $12$ chances at $20\%$ each, "at least one" should be high — $0.93$ feels right ✓. **Pitfall:** *adding* the $A_i$ ($12\times 0.2 = 2.4 > 1$, impossible) — overlapping events can't be summed. The complement sidesteps every overlap. *(Back-ref: Entries №02, №03, №05.)*

### Worked Example 2 — Oak's Two-Species Census (partial guidance)

<figure style="margin:1.25em auto; max-width:220px; text-align:center;">
<img src="../../assets/sprites/front/16.png" alt="Pidgey" style="width:96px; display:inline-block; image-rendering: pixelated; vertical-align:middle;">
<img src="../../assets/sprites/front/19.png" alt="Rattata" style="width:96px; display:inline-block; image-rendering: pixelated; vertical-align:middle;">
<figcaption style="font-size:0.8em;"><strong>#016 Pidgey</strong> and <strong>#019 Rattata</strong> — the two species Oak is counting</figcaption>
</figure>

**ARCHETYPE:** *Two-event inclusion–exclusion; "exactly one."*

**Setup.** Over the morning, $P(\text{Pidgey seen})=0.6$, $P(\text{Rattata seen})=0.5$, $P(\text{both})=0.3$. Find $P(\text{at least one})$ and $P(\text{exactly one})$.

**Identify.** Let $G$ = Pidgey, $R$ = Rattata; want $P(G\cup R)$ and $P(\text{exactly one})$. *Your move: apply Entry №04, then peel off the "both."*

$$P(G\cup R) = P(G)+P(R)-P(G\cap R) = 0.6+0.5-0.3 = 0.8.$$
"Exactly one" is the union with the "both" cell removed:
$$P(\text{exactly one}) = P(G\cup R) - P(G\cap R) = 0.8 - 0.3 = 0.5.$$

**Check & pitfall.** $P(\text{exactly one}) + P(\text{both}) = 0.5 + 0.3 = 0.8 = P(G\cup R)$ ✓. **Pitfall:** reading "at least one" when the problem says "exactly one" — they differ by $P(\text{both})$, here a full $0.3$. *(Back-ref: Entry №04.)*

### Worked Example 3 — The Three-Species Survey (light guidance)

**ARCHETYPE:** *Three-event inclusion–exclusion + complement.*

**Setup.** $P(P)=0.5,\ P(R)=0.4,\ P(W)=0.3$; pairs $P(P\cap R)=0.2,\ P(P\cap W)=0.15,\ P(R\cap W)=0.1$; triple $P(P\cap R\cap W)=0.05$. Find $P(\text{at least one species seen})$ and $P(\text{none})$.

$$P(P\cup R\cup W) = (0.5+0.4+0.3) - (0.2+0.15+0.1) + 0.05 = 1.2 - 0.45 + 0.05 = 0.80.$$
$$P(\text{none}) = 1 - 0.80 = 0.20.$$

**Check & pitfall.** Sanity-check a single cell: "$P$ only" $= 0.5 - 0.2 - 0.15 + 0.05 = 0.20 \ge 0$ ✓. **Pitfall:** forgetting to *add back* the triple — drop it and you'd get $0.75$, because the center was subtracted three times but added only twice. *(Back-ref: Entry №04.)*

### Worked Example 4 — Disjoint, So You May Add (exam speed)

**ARCHETYPE:** *Mutually-exclusive union (no overlap term).*

**Setup.** One wild slot holds exactly one Pokémon, so it cannot be a Pidgey *and* a Spearow at once. $P(\text{Pidgey})=0.45$, $P(\text{Spearow})=0.15$. Find $P(\text{Pidgey or Spearow})$, and state the relationship.

$$\text{Since } G\cap S=\varnothing:\quad P(G\cup S) = P(G)+P(S) = 0.45+0.15 = 0.60.$$
They are **mutually exclusive** (one slot, one Pokémon), so by A3 you simply add — no overlap to subtract.

**Check & pitfall.** They are **not** independent: $P(G\cap S)=0\neq P(G)P(S)=0.0675$. **Pitfall:** "multiplying" $0.45\times0.15$ because the events "feel separate" — disjoint events are the *opposite* of independent; multiplying is forbidden. *(Back-ref: Entries №04, №05.)*

### Worked Example 5 — Independent, or Just Disjoint? (exam speed)

**ARCHETYPE:** *Independence test via inclusion–exclusion.*

**Setup.** $P(A)=0.5$, $P(B)=0.4$, $P(A\cup B)=0.7$. Are $A$ and $B$ independent?

$$P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.5+0.4-0.7 = 0.2, \qquad P(A)P(B) = (0.5)(0.4) = 0.2.$$
Since $P(A\cap B) = P(A)P(B)$, the events **are independent**.

**Check & pitfall.** They are *not* disjoint ($P(A\cap B)=0.2\neq 0$), which is consistent — disjoint would have *forbidden* independence. **Pitfall:** eyeballing "they overlap, so dependent" — independence is a *numeric* test ($P(A\cap B)$ vs. $P(A)P(B)$), not a yes/no-overlap question. *(Back-ref: Entries №04, №05.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — "At least one" → complement, every time**

The instant you read **"at least one,"** write $1 - P(\text{none})$ before anything else. A direct union of three or more events costs minutes; the complement is one line. On the TI-30XS MultiView, $1-(0.8)^{12}$ is the single chain [ 1 [−]{.kbd} 0.8 [^]{.kbd} 12 [enter]{.kbd} ]{.keystroke} — no parentheses to balance.
:::

::: trainers-tip
**TRAINER'S TIP — Build a Venn ledger for three events**

For any three-event problem, write the seven region values (three "only," three "pair-only," one triple) and confirm they sum to $\le 1$ and each is $\ge 0$. A negative cell means you misread a given — catch it *before* you compute, not in the answer choices.
:::

::: trainers-tip
**TRAINER'S TIP — Before you add or multiply, name the relationship**

Adding requires **disjoint**; multiplying requires **independent**. They are different licenses. The fastest way to lose a point is to multiply two events that merely "can't both happen," or add two that merely "don't affect each other." Say which one you've been *told* out loud before you reach for an operation.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie has rigged a net to catch Pikachu in the chaos. "Two snares!" she crows. "Snare A catches it with probability $0.5$, snare B with probability $0.5$ — and they're *mutually exclusive*, James, so that means they're *independent*, so the chance we catch it is $0.5 \times 0.5 = 0.25$… no wait, that's *worse*. Ugh — just add them: $0.5 + 0.5 = 1$, guaranteed!"

Meowth nods sagely. Pikachu strolls between both snares untouched, and the net snaps shut on James.

**Where it fails:** Jessie committed the canonical error twice. **Mutually exclusive is the *opposite* of independent** — disjoint positive-probability events are maximally *dependent*, so you may **never** multiply their chances. And $P(A)+P(B)$ equals $P(A\cup B)$ *only because* the snares are disjoint, never because they're "independent"; here it lands at $1.0$, which should have screamed *impossible* (two single-spring snares can't guarantee a catch). Name the relationship first, *then* pick the operation — exactly the habit the last Trainer's Tip drilled. *(You'll audit this exact blunder yourself in Problem C1.17.)*
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal first move of **insurance pricing.**

Every policy an actuary prices begins exactly the way you began Route 1: by defining the **sample space** of loss events. A homeowner's policy might cover fire, theft, and water damage — *overlapping* events, because a burst pipe during a fire is both. **Inclusion–exclusion** is precisely how an actuary computes "the probability of **at least one** covered loss this year" without double-counting the households that suffer two at once, and the **complement trick** — $1 - P(\text{no claims})$ — is the single fastest route to a loss frequency.

The mutually-exclusive-vs-independent distinction is not academic here: modeling two perils as "independent" when a single storm causes both (so they're *positively dependent*) **under-prices the catastrophe** and can sink an insurer. The very same arithmetic you used to save Pikachu — $1-(1-q)^n$ — is how a reinsurer estimates the chance a portfolio suffers at least one large catastrophe across many regions in a year.

*Series bridge:* this set-and-axiom foundation is the bedrock under every later exam. Next chapter at Cerulean, conditioning will *shrink* these very spaces; and as the journey continues, "events" grow up into "loss **random variables**" — but the addition rule and the complement trick never leave your toolkit.

*Transfer check:* could you solve this with **no Pokémon in it**? "$P(\text{fire})=0.04$, $P(\text{theft})=0.03$, $P(\text{both})=0.01$ — find the probability of at least one claim." Same inclusion–exclusion: $0.04+0.03-0.01 = 0.06$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Trainer's License Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/flying.png" alt="Flying type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">Route 1 has no gym — clear the capstone to stamp your Trainer's License.</figcaption>
</figure>

**The Challenge.** Route 1 is a tutorial road — there is no gym leader and no badge here. Instead, with Pikachu cornered, Oak poses the integrative problem that decides whether you stand or flee; clear it and the Pokédex stamps your **Trainer's License**, your proof you may walk the road north. You've classified each Spearow's dive by the threats it carries:

- $T$ = "targets Pikachu," $P(T)=0.40$;
- $L$ = "comes in low (hard to dodge)," $P(L)=0.35$;
- $F$ = "is a fast diver," $P(F)=0.30$.

The Pokédex's threat model gives the overlaps:
$$P(T\cap L)=0.18,\quad P(T\cap F)=0.12,\quad P(L\cap F)=0.10,\quad P(T\cap L\cap F)=0.05.$$

A Spearow is **"dangerous"** if it satisfies *at least one* of $T,L,F$. Answer three questions to choose your move:

1. $P(\text{a random Spearow is dangerous}) = P(T\cup L\cup F)$.
2. $P(\text{it targets Pikachu but is neither low nor fast})$ — the "pure $T$" cell.
3. With $n=12$ independent Spearow, $P(\text{at least one dangerous})$.

**ARCHETYPE:** *Three-event inclusion–exclusion + a single Venn cell + the "at least one" complement, integrated.*

**Step 1 — Identify.** Part 1 is Entry №04. Part 2 is one Venn cell built from the same givens. Part 3 chains the per-bird danger probability into the complement trick of Entry №02.

**Step 2 — Trainer's Path.**

*Part 1 — inclusion–exclusion.*
$$P(T\cup L\cup F) = (0.40+0.35+0.30) - (0.18+0.12+0.10) + 0.05 = 1.05 - 0.40 + 0.05 = 0.70.$$

*Part 2 — the pure-$T$ cell.* "Targets, but not low and not fast" is $P(T\cap L^c\cap F^c)$. Apply inclusion–exclusion *inside* $T$:
$$P(T\cap L^c\cap F^c) = P(T) - P(T\cap L) - P(T\cap F) + P(T\cap L\cap F) = 0.40 - 0.18 - 0.12 + 0.05 = 0.15.$$

*Part 3 — at least one dangerous.* Each bird is dangerous w.p. $q = 0.70$, independently, so
$$P(\text{at least one dangerous}) = 1 - (1-q)^{12} = 1 - (0.30)^{12} \approx 1 - 5.3\times 10^{-7} \approx 1.$$

**Step 3 — Professor's Path (Part 2, the long way, to prove the one-liner).** Decompose $T$ into four sub-regions by membership in $L$ and $F$: pure-$T$, "$T\cap L$ only," "$T\cap F$ only," and the triple. Their probabilities are $P(T\cap L\text{ only}) = 0.18 - 0.05 = 0.13$, $P(T\cap F\text{ only}) = 0.12 - 0.05 = 0.07$, triple $= 0.05$, and the four must sum to $P(T) = 0.40$. So pure-$T$ $= 0.40 - 0.13 - 0.07 - 0.05 = 0.15$ ✓ — matching the one-line formula.

**Step 4 — Check, verdict & pitfall.** $P(T\cup L\cup F) = 0.70 \le 1$ ✓; pure-$T$ $= 0.15 \le P(T) = 0.40$ ✓ (monotonicity). The flock's danger is essentially **certain**: twelve independent $0.70$ chances leave a vanishing "none" probability — so you make your stand, and Pikachu's Thunderbolt does the rest. **Pitfall:** in Part 3, using $P(T)=0.40$ instead of the *danger* probability $q=0.70$ — always read which event "at least one" refers to.

> Oak's hologram dims with a satisfied flicker. "You counted the space, then counted what you didn't want. That's the whole game, Ash. Your **Trainer's License** is stamped — the road north is yours."

## The Gym Challenge — Problem Set

::: problem-set
**THE ROUTE 1 QUESTLINE.** Oak has commissioned you to survey the road before you walk it. This problem set is one escalating mission: the **Route Trainer** legs are field-work on Route 1 (cataloguing the grass, scouting threats); the **Gym Battle** tier is the boss fight (the Spearow flock at exam difficulty); the **Elite Challenge** tier is optional post-game once the License is stamped. Work it timed (~5 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline and stamp your Trainer's License. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (the early legs — scouting & cataloguing)

**C1.1.** 🔴 *(Oak's first task: catalog one wild slot.)* The next Route 1 encounter is Pidgey ($0.45$), Rattata ($0.30$), Spearow ($0.15$), or "nothing rustles" otherwise. Write the sample space and find $P(\text{some Pokémon appears})$.

**C1.2.** 🔴 *(Tagging the bird-types in the catalog.)* Ash is tagging the catalog: a Route 1 sighting is a bird-type (event $A$) with $P(A)=0.55$. Oak needs the non-bird share for the same row, so every sighting is filed exactly once. Using only the axioms, find $P(A^c)$ — the chance the sighting is **not** a bird-type — and name the rule you used.

**C1.3.** 🔴 *(Two species share one slot, so both can't appear.)* $G$ = "it's a Pidgey" ($0.45$), $S$ = "it's a Spearow" ($0.15$). One wild slot holds one Pokémon. Find $P(G\cup S)$ and state whether $G,S$ are mutually exclusive, independent, or both.

**C1.4.** 🟡 *(Will rain and a berry both appear on the route today?)* $P(\text{rain})=0.40$, $P(\text{berry on a bush})=0.50$, and the two are **independent**. Find $P(\text{rain and berry})$, then $P(\text{at least one})$.

**C1.5.** 🟡 *(Filling the four-cell ledger for the survey.)* Oak wants the four-cell Venn ledger for two survey traits: $A$ = "bird-type" with $P(A)=0.6$, $B$ = "lives in tall grass" with $P(B)=0.5$, and both at once $P(A\cap B)=0.2$. A ledger that doesn't total $1$ means a sighting was lost, so fill the four cells $P(A\cap B^c),\,P(A^c\cap B),\,P(A\cap B),\,P(A^c\cap B^c)$ and confirm they sum to $1$.

**C1.6.** 🟡 *(Will the stubborn Poké Ball ever close?)* Pikachu refuses each of $3$ independent throws w.p. $0.5$. Using the complement, find $P(\text{the ball closes at least once})$.

**C1.7.** 🔴 *(Rewriting "neither" for the threat report.)* Officer Jenny's Route 1 danger report needs the "all-clear" line: the chance that **neither** threat $A$ nor threat $B$ turns up. A wrong all-clear sends a trainer up the road unwarned, so be exact. The scouts already logged $P(A\cup B)=0.72$ (at least one threat). Rewrite $P(\text{neither } A \text{ nor } B)$ using De Morgan's law, then evaluate it.

**C1.8.** 🟡 *(AUDIT — Team Rocket's recon notes claim two traits are independent.)* Your tallies of wild Pokémon give $P(A)=0.4$ for "bird-type," $P(B)=0.5$ for "found in tall grass," and $P(A\cup B)=0.65$. Meowth's note declares "$A$ and $B$ are independent — assume it." Are they? Compute $P(A\cap B)$ and the independence check, and name Meowth's error if he is wrong.

> *Questline beat: the legwork is done. The flock descends. The Gym Battle is the boss.*

### Gym Battles (the boss fight — true SOA difficulty)

**C1.9.** 🟡 *(Triaging arrivals at the trailside Center.)* Among Pokémon brought in, $70\%$ need a Potion, $40\%$ a status cure, $25\%$ both. For a random arrival find (a) $P(\text{at least one treatment})$, (b) $P(\text{exactly one})$, (c) $P(\text{neither})$.

**C1.10.** 🟡 *(Cross-tabulating habitats in the survey.)* Catches are logged by habitat: $P(F)=0.5,\,P(W)=0.4,\,P(C)=0.3$; pairs $0.2,\,0.15,\,0.1$; triple $0.05$. Find $P(\text{at least one habitat})$ and $P(\text{none})$.

**C1.11.** 🟡 *(Every challenger carries at least one type — solve for the overlap.)* Trainers on the route use a Water-type w.p. $0.6$, an Electric-type w.p. $0.5$, and *both* w.p. $p$; every trainer uses at least one (so the union is $1$). Find $p$ and $P(\text{exactly one type})$.

**C1.12.** 🟡 *(Two pulls at a roadside slot machine.)* A slot pull wins the jackpot ($0.02$) or a small prize ($0.15$), mutually exclusive. Find $P(\text{win something on one pull})$ and $P(\text{win something at least once over two independent pulls})$.

**C1.13.** 🔵 *(The overlap went unrecorded — bound it.)* Oak's threat survey logged each Spearow trait separately — $T$ = "targets Pikachu" with $P(T)=0.40$ and $L$ = "comes in low" with $P(L)=0.35$ — but the field scout never recorded how often a bird did both, so $P(T\cap L)$ is blank. Before the survey can ship, Oak needs the worst- and best-case bounds. Find the smallest and largest possible values of $P(T\cup L)$, and of $P(T\cap L)$.

**C1.14.** 🟡 *(Two bug species in the next forest census.)* Oak is previewing the next forest census, where one log can list two bug species at once: $P(\text{Caterpie})=0.55$, $P(\text{Weedle})=0.45$, and $P(\text{both on the same log})=0.30$. To size the net order he needs the Caterpie-only count and the "crowded log" rate. Find $P(\text{Caterpie but not Weedle})$ and $P(\text{at most one of the two species})$.

**C1.15.** 🟡 *(RIVAL TRAP — Gary eyeballs an overlap and calls it dependent.)* Scouting the same Route 1 grass, Gary tracks two sighting traits: $A$ with $P(A)=0.5$, $B$ with $P(B)=0.4$, and at least one showing with $P(A\cup B)=0.7$. If he ships a wrong dependence call, his whole threat sheet is off. Gary scoffs, "They obviously overlap, so they're dependent — done." Decide whether $A,B$ are independent by computing $P(A\cap B)$ and comparing it to $P(A)P(B)$, and say whether Gary is right.

**C1.16.** 🔵 *(Officer Jenny's gate audit across three items.)* Officer Jenny is auditing how well Route 1 trainers are provisioned: each carries a Potion ($0.8$), an Antidote ($0.5$), a map ($0.6$); pairs $P(\text{Pot}\cap\text{Anti})=0.4,\,P(\text{Pot}\cap\text{map})=0.5,\,P(\text{Anti}\cap\text{map})=0.35$; all three $0.3$. The "carries nothing" rate is who she has to turn back at the gate, so find $P(\text{at least one item})$ and $P(\text{none})$.

> *Questline beat: the flock is beaten back. The post-game below is optional — but it's where the real surveyors play.*

### Elite Challenge (post-game — integrative / stretch)

**C1.17.** 🔵 *(AUDIT — recycle Team Rocket's snare blunder.)* Jessie's two snares: $P(A)=0.5$, $P(B)=0.5$. She claims they are "mutually exclusive, so independent, so $P(\text{catch})=0.5\times0.5=0.25$ — or maybe $0.5+0.5=1$." Suppose the snares are genuinely **mutually exclusive**. (a) What is the *correct* $P(\text{at least one fires})$? (b) Can mutually exclusive positive-probability events be independent? (c) Name both of Jessie's errors.

**C1.18.** 🔵 *(The full flock, integrated.)* $n=12$ independent Spearow. Per bird: $P(T)=0.40,\,P(L)=0.35,\,P(F)=0.30$; pairs $0.18,\,0.12,\,0.10$; triple $0.05$. "Dangerous" = at least one of $T,L,F$. Find (a) the per-bird danger probability $q$; (b) $P(\text{none of the 12 dangerous})$; (c) $P(\text{purely fast: } F \text{ but neither } T \text{ nor } L)$ for one bird.

**C1.19.** 🔵 *(Solve, test, and check feasibility.)* Two traps: $P(A)=0.6$, $P(B)=0.5$, $P(\text{at least one})=0.8$. (a) Find $P(\text{both})$. (b) Are the traps independent? (c) If instead the traps were *mutually exclusive*, could $P(\text{at least one})=0.8$ hold? Explain via the axioms.

**C1.20.** 🔵 *(DECISION — make a stand, or flee to Viridian?)* Each of the $n=12$ Spearow reaches Pikachu independently w.p. $0.20$. **Option A (flee):** you escape cleanly only if **none** reaches Pikachu before you clear the route. **Option B (stand):** Pikachu's Thunderbolt scatters the whole flock, succeeding w.p. $0.85$ regardless of the dives. Compute $P(\text{clean escape})$ for Option A and compare it to Option B's $0.85$; state which gives the better chance of keeping Pikachu safe.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C1.1** — *(standard) Sample space + complement (Entries №01, №02).* $S=\{\text{Pidgey},\text{Rattata},\text{Spearow},\text{nothing}\}$ with masses $0.45,0.30,0.15,0.10$ (the last fills to $1$). "Some Pokémon appears" is the complement of "nothing":
$$P(\text{some}) = 1 - P(\text{nothing}) = 1 - 0.10 = 0.90.$$

**C1.2** — *(standard) Complement rule from the axioms (Entry №02).* $P(A^c) = 1 - P(A) = 1 - 0.55 = 0.45$, by the **complement rule**, itself a consequence of A2 ($P(S)=1$) and A3 applied to the disjoint pair $A, A^c$.

**C1.3** — *(standard) Disjoint union; ME vs. independent (Entries №04, №05).* One slot holds one Pokémon, so $G\cap S = \varnothing$ — **mutually exclusive**. By A3, $P(G\cup S) = 0.45 + 0.15 = 0.60$. They are **not** independent: $P(G\cap S) = 0 \neq P(G)P(S) = 0.0675$. Disjoint positive-probability events are never independent.

**C1.4** — *(standard) Independent intersection, then union (Entries №04, №05).* Independence factors the joint: $P(\text{rain}\cap\text{berry}) = (0.40)(0.50) = 0.20$. Union: $P(\text{rain}\cup\text{berry}) = 0.40 + 0.50 - 0.20 = 0.70$.

**C1.5** — *(standard) Four-cell Venn ledger (Entry №04).*
$$P(A\cap B^c) = 0.6 - 0.2 = 0.4, \quad P(A^c\cap B) = 0.5 - 0.2 = 0.3,$$
$$P(A\cap B) = 0.2, \quad P(A^c\cap B^c) = 1 - (0.4+0.3+0.2) = 0.1.$$
Sum: $0.4+0.3+0.2+0.1 = 1.0$ ✓.

**C1.6** — *(standard) "At least one" complement, independent trials (Entry №02).*
$$P(\text{closes at least once}) = 1 - P(\text{refuses all three}) = 1 - (0.5)^3 = 1 - 0.125 = 0.875.$$

**C1.7** — *(standard) De Morgan + complement (Entries №02, №03).*
$$P(\text{neither}) = P(A^c\cap B^c) = P\!\left((A\cup B)^c\right) = 1 - P(A\cup B) = 1 - 0.72 = 0.28.$$

**C1.8** — *(audit) Independence test via inclusion–exclusion (Entries №04, №05).* By inclusion–exclusion, $P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.4+0.5-0.65 = 0.25$. Compare to $P(A)P(B) = (0.4)(0.5) = 0.20$. Since $0.25 \neq 0.20$, $A$ and $B$ are **not independent** — they are positively associated. **Meowth's error:** he *assumed* independence (you may never assume it; it must be told or derived). The true overlap $0.25$ exceeds the $0.20$ that independence would require.

**C1.9** — *(standard) Two-event inclusion–exclusion: all three quantities (Entries №02, №04).* Let $P$ = Potion ($0.70$), $S$ = status cure ($0.40$), $P\cap S = 0.25$.
(a) At least one: $0.70 + 0.40 - 0.25 = 0.85$.
(b) Exactly one: $0.85 - 0.25 = 0.60$.
(c) Neither: $1 - 0.85 = 0.15$.

**C1.10** — *(standard) Three-event inclusion–exclusion + complement (Entries №02, №04).*
$$P(F\cup W\cup C) = (0.5+0.4+0.3) - (0.2+0.15+0.1) + 0.05 = 1.2 - 0.45 + 0.05 = 0.80,$$
$$P(\text{none}) = 1 - 0.80 = 0.20.$$

**C1.11** — *(standard) Solve for an unknown overlap given the union (Entry №04).* "At least one type" means $P(W\cup E) = 1$, so $1 = 0.6 + 0.5 - p \Rightarrow p = 0.10$. Exactly one: $P(W\cup E) - P(W\cap E) = 1 - 0.10 = 0.90$.

**C1.12** — *(standard) Disjoint union + "at least once" over two independent trials (Entries №02, №04, №05).* Single pull (disjoint prizes): $P(\text{win}) = 0.02 + 0.15 = 0.17$. Two independent pulls, at least once: $1 - (1-0.17)^2 = 1 - (0.83)^2 = 1 - 0.6889 = 0.3111$.

**C1.13** — *(standard) Bounding union and intersection with unknown overlap (Entries №02, №04).* The overlap satisfies $P(T\cap L)\in[\max(0,\,0.40+0.35-1),\ \min(0.40,0.35)] = [0,\,0.35]$. Since $P(T\cup L) = 0.75 - P(T\cap L)$,
$$P(T\cup L)\in[0.75-0.35,\ 0.75-0] = [0.40,\ 0.75].$$
So $0.40\le P(T\cup L)\le 0.75$ and $0\le P(T\cap L)\le 0.35$.

**C1.14** — *(standard) Single Venn cell + "at most one" (Entries №02, №04).* Caterpie but not Weedle: $P(C) - P(C\cap W) = 0.55 - 0.30 = 0.25$. "At most one" is the complement of "both": $1 - P(\text{both}) = 1 - 0.30 = 0.70$.

**C1.15** — *(rival_trap) Independence test via inclusion–exclusion (Entries №04, №05).* From inclusion–exclusion, $P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.5+0.4-0.7 = 0.2$. Compare $P(A)P(B) = (0.5)(0.4) = 0.2$. Since they're **equal**, $A$ and $B$ **are independent**. **Gary is wrong:** he conflated "overlapping" with "dependent." Overlap alone says nothing — independence is the *numeric* test $P(A\cap B)\overset{?}{=}P(A)P(B)$, and here it passes despite the overlap.

**C1.16** — *(standard) Three-event inclusion–exclusion (Entry №04).*
$$P(\cup) = (0.8+0.5+0.6) - (0.4+0.5+0.35) + 0.3 = 1.9 - 1.25 + 0.3 = 0.95,$$
$$P(\text{none}) = 1 - 0.95 = 0.05.$$

**C1.17** — *(audit) Mutually exclusive ≠ independent; the snare blunder (Entries №04, №05).*
(a) Mutually exclusive snares add: $P(\text{at least one fires}) = P(A) + P(B) = 0.5 + 0.5 = 1.0$. (With these numbers the disjoint snares exactly tile the space — *some* snare always fires. Note this is the *union*, not a "catch guarantee.")
(b) **No.** Independence would need $P(A\cap B)=P(A)P(B)=0.25>0$, but disjointness forces $P(A\cap B)=0$. Contradiction — they are maximally *dependent*.
(c) Jessie's errors: (i) calling mutually exclusive "independent" and then **multiplying** ($0.5\times0.5$), which is forbidden for disjoint events; (ii) treating the union $P(A)+P(B)=1$ as a *catch guarantee*, when it is only the probability that *some snare fires* — and Pikachu can still walk between two snares that "fire" at empty air.

**C1.18** — *(standard) Inclusion–exclusion + complement over $n$ trials, integrated (Entries №02, №04).*
(a) $q = (0.40+0.35+0.30) - (0.18+0.12+0.10) + 0.05 = 1.05 - 0.40 + 0.05 = 0.70$.
(b) $P(\text{none of 12 dangerous}) = (1-q)^{12} = (0.30)^{12} \approx 5.31\times 10^{-7} \approx 0$.
(c) Purely fast $= P(F\cap T^c\cap L^c) = P(F) - P(F\cap T) - P(F\cap L) + P(T\cap L\cap F) = 0.30 - 0.12 - 0.10 + 0.05 = 0.13$.

**C1.19** — *(standard) Solve overlap, independence test, axiom feasibility (Entries №02, №04, №05).*
(a) $P(\text{both}) = P(A) + P(B) - P(\text{at least one}) = 0.6 + 0.5 - 0.8 = 0.3$.
(b) Independent? $P(A)P(B) = (0.6)(0.5) = 0.30 = P(A\cap B)$, so **yes, independent**.
(c) If mutually exclusive, $P(A\cap B) = 0$, forcing $P(\text{at least one}) = P(A) + P(B) = 1.1 > 1$ — impossible by A1/A2. So disjoint traps could **not** give $0.8$ with these marginals.

**C1.20** — *(decision) "At least one" complement feeding a decision (Entries №02, №05).* Option A (clean escape) needs **none** of the $12$ independent dives to land:
$$P(\text{clean escape}) = P(\text{none reaches}) = (1-0.20)^{12} = (0.8)^{12} \approx 0.0687.$$
Option B (stand) succeeds w.p. $0.85$. Since $0.85 \gg 0.0687$, **standing is far safer** — fleeing leaves only a $\approx 6.9\%$ chance of getting through untouched. (This is the Cold Open's verdict: make the stand.)

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C1.1 | $0.90$ | standard | | C1.11 | $p=0.10$; exactly one $0.90$ | standard |
| C1.2 | $0.45$ (complement rule) | standard | | C1.12 | $0.17$; $0.3111$ | standard |
| C1.3 | $0.60$; ME, not independent | standard | | C1.13 | $P(\cup)\in[0.40,0.75]$; $P(\cap)\in[0,0.35]$ | standard |
| C1.4 | $0.20$; $0.70$ | standard | | C1.14 | $0.25$; $0.70$ | standard |
| C1.5 | $0.4,\,0.3,\,0.2,\,0.1$ | standard | | C1.15 | independent; Gary wrong | rival_trap |
| C1.6 | $0.875$ | standard | | C1.16 | $0.95$; none $0.05$ | standard |
| C1.7 | $0.28$ | standard | | C1.17 | (a) $1.0$; (b) no; (c) two errors | audit |
| C1.8 | not independent | audit | | C1.18 | $q=0.70$; none $\approx 5.3\times10^{-7}$; pure-$F$ $0.13$ | standard |
| C1.9 | $0.85$; $0.60$; $0.15$ | standard | | C1.19 | $0.3$; independent; (c) impossible | standard |
| C1.10 | $0.80$; none $0.20$ | standard | | C1.20 | A $\approx 0.0687$; B $0.85$ → stand | decision |
:::

## Badge Earned — the Trainer's License

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/sprites/types/flying.png" alt="Flying type emblem standing in for the Trainer's License stamp" style="width:120px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Trainer's License stamped!</strong> Route 1 cleared — Rank: Rookie Trainer (0 badges). The road north to Viridian and Cerulean is open.</figcaption>
</figure>

You counted the space, complemented "at least one," and made your stand — Pikachu's Thunderbolt scattered the flock, and the Pokédex stamped your **Trainer's License**. There is no gym badge on Route 1; this stamp is your proof you may walk on. The bike you'll wreck fishing Pikachu out of the river is a problem for Cerulean.

**Mastery checklist — tick each before you move on (mapped to the SOA outcomes):**

- ☐ **(1a)** I can **name a sample space** $S$ from a word problem, write events as subsets, apply set operations and **Venn diagrams**, and use **De Morgan's laws** to rewrite "none / neither / not both." *(Rematch: Concepts 1, 3; WE 3.)*
- ☐ **(1a)** I can **state the three (Kolmogorov) axioms** and **derive** $P(\varnothing)=0$, the complement rule, and monotonicity on demand. *(Rematch: Concept 2 + its derivation; C1.2.)*
- ☐ **(1e)** I can **execute the addition rule / inclusion–exclusion** for two and three events — isolating a single Venn cell and bounding a union when the overlap is unknown — and reach for the **complement** the instant I read "at least one" ($1-P(\text{none})$). *(Rematch: Concept 4, WE 1–3, the Gym Battle; C1.6, C1.10, C1.13, C1.16, C1.20.)*
- ☐ **(1d)** I can recognize **mutually exclusive** events, add them with no overlap term, and never confuse them with **independent** events. *(Rematch: Concepts 4–5, Team Rocket's Trap, WE 4–5; C1.3, C1.8, C1.15, C1.17, C1.19.)*

**Gym Rematch pointers.** Reached for a plain sum on overlapping events? Concept 4, Beat 4, then redo C1.9 / C1.16. Multiplied disjoint events (or called them "independent")? Concept 5, Beat 4 + Team Rocket's Trap, then redo C1.3 and C1.17. Forgot the complement on "at least one"? WE 1 + the Gym Battle, then C1.6 and C1.20.

> Next stop: **Viridian City, then Cerulean** — where a phantom thief strikes the Pokémon Center and the question stops being "what could happen?" and becomes "given a clue, *who probably did it*?" — the art of **conditioning**. Pack the complement trick; you'll reuse it there too.

---

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
