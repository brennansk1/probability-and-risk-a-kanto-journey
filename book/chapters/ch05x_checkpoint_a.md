<!--
  file: ch05x_checkpoint_a
  tier: C
  outcomes: review
  draft1_source: drafts/chapters_draft1/.md
  maps_to: Spaced-retrieval review of Topic 1
-->

# Checkpoint A — The Rocket Hideout {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map: the General Probability leg from the Space of Outcomes through Counting to Cerulean is complete; a side-stairwell leads down into the Rocket Hideout." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Topic 1 complete — before you press on, a detour beneath the Game Corner to prove the General Probability toolkit is yours for keeps.</figcaption>
</figure>

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/25.png" alt="Pikachu" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#025 Pikachu — perched on the terminal for the Topic 1 audit</strong></figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — CHECKPOINT: "The Rocket Hideout"**

The elevator doors grind open on the lowest floor of the Rocket Hideout, and the lights flicker on. No grunts. No Giovanni. Just a long corridor lined with locked doors — and one terminal, screen glowing, waiting.

Pikachu hops onto the desk. The screen reads: **SECURITY AUDIT — TOPIC 1 CLEARANCE REQUIRED.** Below it, a slow montage of everything you have done since Pallet flickers past: the **sample space** you mapped in the Space of Outcomes, the **counting** you drilled on the route in, and the whole city of **inference** — conditioning, the rules, independence, total probability, and Bayes.

This is not a new badge. There is nothing new behind these doors. This is the Hideout's way of asking the only question that matters before you go deeper: **do you still own all of it?** Not "did you read it once." *Own it.* From memory, fast, cold.

The cursor blinks. Time to retrieve.
:::

## Checkpoint — Spaced Retrieval

This is a **review checkpoint**: no new ideas, just recall under light pressure. The single most powerful study move in this book is *retrieval* — pulling an idea out of your own head before you look it up. Reading the formula again feels productive and mostly isn't; *recalling* it is what welds it in place. So close the previous chapters. Answer each prompt **out loud or on paper from memory first**, then check yourself against the answer.

::: trainers-tip
**RETRIEVAL DRILL — say each answer before you read it**

Cover the answers. For each prompt, state the rule *and* why it is true.

1. **Conditioning.** Write the definition of $P(A \given B)$ as a formula, and say in one sentence *why* the denominator is $P(B)$ and not $P(S)$. *(Answer: $P(A\given B) = \dfrac{P(A\cap B)}{P(B)}$; learning $B$ happened crops the world down to $B$, so $B$ becomes the new "everything.")*

2. **Multiplication rule.** Finish it: $P(A \cap B) = \underline{\hphantom{XXXX}}$. *(Answer: $P(A)\,P(B\given A)$ — equivalently $P(B)\,P(A\given B)$. Walk one branch of the tree, then the next.)*

3. **Addition rule.** Finish it: $P(A \cup B) = \underline{\hphantom{XXXX}}$, and say why the last term is there. *(Answer: $P(A)+P(B)-P(A\cap B)$; subtract the overlap so it isn't double-counted.)*

4. **Independence vs. mutually exclusive.** Give the test for independence, and state the trap in one line. *(Answer: independent $\iff P(A\cap B)=P(A)P(B)$. Mutually exclusive means $P(A\cap B)=0$ — the **opposite** of independent for events of positive probability, not the same thing.)*

5. **"At least one."** What is the fastest route to $P(\text{at least one})$? *(Answer: the complement — $1 - P(\text{none})$.)*

6. **Counting.** When does order matter (permutation) and when not (combination)? Write $\binom{n}{k}$. *(Answer: ordered $\Rightarrow$ permutation $\tfrac{n!}{(n-k)!}$; unordered $\Rightarrow$ combination $\binom{n}{k}=\tfrac{n!}{k!\,(n-k)!}$.)*

7. **Law of total probability.** Over a partition $B_1,\dots,B_n$, write $P(A)$. *(Answer: $P(A)=\sum_i P(B_i)\,P(A\given B_i)$ — a weighted average of the conditional rates.)*

8. **Bayes' theorem.** Write $P(B_k \given A)$, and say in one sentence what each piece does. *(Answer: $P(B_k\given A)=\dfrac{P(B_k)\,P(A\given B_k)}{\sum_i P(B_i)\,P(A\given B_i)}$ — prior $\times$ likelihood on top, the total-probability denominator normalizes; it runs the clue **backward** from evidence to cause.)*

All eight instant and correct? The Hideout clears you — go straight on to Chapter 6. Any hesitation? That prompt *is* your study list: flip back, reclaim it, then take the mixed set below to be sure.
:::

The retrieval drill tested the rules one at a time. Real exam questions don't announce which rule they want — they *mix*. The set below pulls problems from across the whole General Probability leg (the Space of Outcomes, Counting, and Cerulean) and shuffles the archetypes, so you have to **recognize** the method before you apply it. That recognition is the skill the exam actually scores.

## Mixed Retrieval Problems

::: problem-set
**HOW TO USE THIS SET.** Ten mixed problems spanning Topic 1. Work them **timed (~3 min each)** and *do not* peek at the chapters — the point is to retrieve, not re-read. Then check the **Answer Key** below; every solution back-references the rule it exercises. Hit **80%+ with correct method** and the Hideout clears you for Chapter 6. Miss it, and the flagged chapter is waiting. Problems first; full worked solutions follow afterward, never interleaved. Markers: 🔴 routine · 🟡 routine-with-a-twist · 🔵 stretch.

**CA.1.** 🔴 In a crate of seized Rocket loot, $P(\text{useful})=0.55$, $P(\text{rare})=0.30$, and $P(\text{useful}\cap\text{rare})=0.20$. Find $P(\text{useful}\cup\text{rare})$.

**CA.2.** 🔴 Giovanni must pick a squad of $3$ grunts from the $8$ on duty (order does not matter). How many distinct squads are possible?

**CA.3.** 🔴 Three independent alarm sensors each trip with probability $0.10$. Find the probability that **at least one** trips.

**CA.4.** 🟡 Of $200$ logged intrusions, $80$ reached Floor B2, and of those $50$ were caught. Given an intrusion reached Floor B2, find the probability it was caught.

**CA.5.** 🟡 $40\%$ of entries use a **stolen** keycard and $60\%$ a **forged** one. The lift alarm sounds w.p. $0.30$ for stolen cards and $0.10$ for forged ones. Find the probability the alarm sounds on a random entry.

**CA.6.** 🟡 Among the grunts, $A=$ "carries a Zubat" and $B=$ "guards the vault," with $P(A)=0.5$, $P(B)=0.4$, and $P(A\cup B)=0.7$. Are $A$ and $B$ independent? Justify with a computation.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/41.png" alt="Zubat" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#041 Zubat — the grunt's signature in event $A$</strong></figcaption>
</figure>

**CA.7.** 🔵 A key ring holds $4$ master keys and $6$ decoys. You draw **three** in order without replacement. Find the probability all three are master keys.

**CA.8.** 🔵 *(Inverts CA.5.)* Using the CA.5 setup ($40\%$ stolen, $60\%$ forged; alarm w.p. $0.30$ stolen, $0.10$ forged), the alarm **sounded**. Find $P(\text{stolen}\given\text{alarm})$.

**CA.9.** 🔵 An infiltrator wore a Scientist coat ($0.50$), a Grunt uniform ($0.30$), or a Trainer outfit ($0.20$). The cameras spot each disguise w.p. $0.10$, $0.40$, $0.70$ respectively. The infiltrator **was spotted**. Find $P(\text{Trainer outfit}\given\text{spotted})$.

**CA.10.** 🔵 *(Counting + Bayes.)* Armory A holds $5$ live and $5$ dud grenades; Armory B holds $2$ live and $8$ duds. An armory is chosen at random and **two** grenades are drawn without replacement; both turn out **live**. Find $P(\text{Armory A}\given\text{both live})$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, labeled with the General Probability rule it retrieves. A quick-answer table closes the section.**

**CA.1** — *Addition rule / inclusion–exclusion.* Subtract the overlap so it isn't counted twice:
$$P(\text{useful}\cup\text{rare}) = P(\text{useful}) + P(\text{rare}) - P(\text{useful}\cap\text{rare}) = 0.55 + 0.30 - 0.20 = 0.65.$$

**CA.2** — *Counting (combination — order irrelevant).* A squad is a set, not a ranking, so use $\binom{n}{k}$:
$$\binom{8}{3} = \frac{8\cdot 7\cdot 6}{3\cdot 2\cdot 1} = \frac{336}{6} = 56.$$

**CA.3** — *Complement + independence.* The fast route to "at least one" is $1-P(\text{none})$; independence multiplies the three "no trip" probabilities:
$$P(\text{at least one}) = 1 - (0.9)^3 = 1 - 0.729 = 0.271.$$

**CA.4** — *Conditioning.* Learning the intrusion reached B2 crops the world to those $80$:
$$P(\text{caught}\given\text{B2}) = \frac{P(\text{caught}\cap\text{B2})}{P(\text{B2})} = \frac{50/200}{80/200} = \frac{50}{80} = 0.625.$$

**CA.5** — *Law of total probability (forward).* Weight each conditional alarm rate by how common that keycard is:
$$P(\text{alarm}) = (0.40)(0.30) + (0.60)(0.10) = 0.12 + 0.06 = 0.18.$$

**CA.6** — *Independence test via the multiplication rule.* First recover the intersection from inclusion–exclusion, then compare to the product:
$$P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.5+0.4-0.7 = 0.2, \qquad P(A)\,P(B) = (0.5)(0.4) = 0.2.$$
Since $0.2 = 0.2$, $A$ and $B$ **are independent**. *(Note: they are clearly not mutually exclusive — $P(A\cap B)=0.2\neq 0$ — a reminder those two ideas are different.)*

**CA.7** — *Multiplication rule, without replacement.* Each draw removes a key, shrinking both numerator and denominator:
$$P(\text{all 3 master}) = \frac{4}{10}\cdot\frac{3}{9}\cdot\frac{2}{8} = \frac{24}{720} = \frac{1}{30} \approx 0.0333.$$

**CA.8** — *Bayes' theorem (inverts CA.5).* The CA.5 weighted average is the denominator; the "stolen" branch is the numerator.

| keycard | prior | $P(\text{alarm}\given\cdot)$ | joint |
|---|---|---|---|
| stolen | $0.40$ | $0.30$ | $0.12$ |
| forged | $0.60$ | $0.10$ | $0.06$ |
| total | | | $0.18$ |

$$P(\text{stolen}\given\text{alarm}) = \frac{0.12}{0.18} = \frac{2}{3} \approx 0.6667.$$

**CA.9** — *$n$-way Bayes from a 3-way partition.* Build the grid; the total-probability denominator normalizes the spotted disguises.

| disguise | prior | $P(\text{spotted}\given\cdot)$ | joint |
|---|---|---|---|
| Scientist | $0.50$ | $0.10$ | $0.05$ |
| Grunt | $0.30$ | $0.40$ | $0.12$ |
| Trainer | $0.20$ | $0.70$ | $0.14$ |
| total | | | $0.31$ |

$$P(\text{Trainer}\given\text{spotted}) = \frac{0.14}{0.31} \approx 0.4516.$$

**CA.10** — *Counting likelihood feeding Bayes.* First get each armory's chance of "two live" by the without-replacement multiplication rule, then invert with Bayes (equal priors $\tfrac12$).
$$P(\text{2 live}\given A) = \frac{5}{10}\cdot\frac{4}{9} = \frac{2}{9}, \qquad P(\text{2 live}\given B) = \frac{2}{10}\cdot\frac{1}{9} = \frac{1}{45}.$$

| armory | prior | $P(\text{2 live}\given\cdot)$ | joint |
|---|---|---|---|
| A | $0.50$ | $2/9$ | $1/9$ |
| B | $0.50$ | $1/45$ | $1/90$ |
| total | | | $11/90$ |

$$P(\text{Armory A}\given\text{both live}) = \frac{1/9}{11/90} = \frac{10/90}{11/90} = \frac{10}{11} \approx 0.9091.$$

---

**Quick-answer table.**

| # | Answer | Rule retrieved |
|---|---|---|
| CA.1 | $0.65$ | Addition rule |
| CA.2 | $56$ | Combination |
| CA.3 | $0.271$ | Complement + independence |
| CA.4 | $0.625$ | Conditioning |
| CA.5 | $0.18$ | Total probability |
| CA.6 | independent ($0.2=0.2$) | Independence test |
| CA.7 | $1/30 \approx 0.0333$ | Multiplication, no replacement |
| CA.8 | $2/3 \approx 0.6667$ | Bayes (2-way) |
| CA.9 | $\approx 0.4516$ | Bayes (3-way) |
| CA.10 | $10/11 \approx 0.9091$ | Counting + Bayes |

**Scored $8$ or more of $10$ with correct method?** The Rocket Hideout clears your Topic 1 audit — the elevator opens and Chapter 6 awaits. **Missed three or more?** Note which rule each miss belongs to in the table above and reclaim that section before you descend further; every chapter ahead stands on this floor.
:::
