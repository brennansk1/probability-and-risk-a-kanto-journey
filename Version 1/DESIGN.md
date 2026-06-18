# Probability & Risk: A Kanto Journey
### The Indigo League Edition — A Narrative Study Companion for SOA/CAS Exam P (Exam 1)
**Complete Textbook Design Document**

In a world where Pokémon roam, a ten-year-old from Pallet Town sets out not just to become a Pokémon Master — but to understand risk itself. Every route hides uncertainty. Every battle is a gamble. Every gym leader is a problem to be solved. This is the story of Ash Ketchum, Trainer and Actuary-in-Training, told across the Indigo League — and by the time he reaches the Pokémon League at the Indigo Plateau, you will be ready to walk into a Prometric center and pass Exam P with a perfect score.

---

## Part 0 — Design Charter

### The premise

This is a standalone study textbook, the first volume of a new CAS Actuarial series (Gen 1 / Kanto = Exam 1 / P), entirely separate from any other Pokémon-themed book project. It follows the Kanto/Indigo League anime arc loosely — hitting the iconic beats and characters (Pallet Town, Pikachu's refusal of the Poké Ball, Brock and Misty as companions, the St. Anne, Team Rocket's recurring schemes, the eight gyms, the Indigo Plateau) — but deviates freely whenever Ash needs to use his actuarial skills to resolve a situation. The narrative is the delivery vehicle; the probability curriculum is the cargo, and the cargo is complete.

### The protagonist's twist

In this alternate universe, Ash is captivated not only by Pokémon but by the mathematics of uncertainty. Professor Oak is both a Pokémon researcher and a risk theorist who sets Ash on a dual quest: collect the eight badges and master probability well enough to one day price the risks that Pokémon trainers face. Ash's Pokédex has an "Actuary Mode" that poses problems; solving them is how he earns money, saves towns, wins battles, and protects his friends. Every problem in the book is a task Ash must accomplish for a narrative reason — never a decontextualized drill.

### The pedagogical promise (a perfect score, not a bare pass)

A reader who works through every chapter, every worked example, and every problem set — and drills practice software in parallel — should sit Exam P expecting a 9 or 10, not a coin-flip 6. To that end the book covers the full 2026 syllabus plus the margin material that separates top scorers from passers (the gamma-integral shortcut, the Darth Vader/survival-function rule, MGF kernel-recognition, continuity correction, calculator technique). Target benchmarks stated to the reader throughout: 24/30 on practice exams, Coaching Actuaries Earned Level 7+, 6-minute-per-question pacing.

### Verified exam facts the book is built around

- 3 hours · 30 multiple-choice questions (A–E) · computer-based · scored 0–10 (6 passes) · no penalty for wrong answers — never leave a blank.
- A normal distribution table is provided on-screen; you cannot bring your own.
- Calculator: TI-30XS MultiView (recommended) or BA II Plus, memory cleared.
- Fee ~$275 (Tier 1); continuous registration via Prometric; ~300 study hours typical.
- Calculus (integration, differentiation, series) is assumed, not taught by the SOA — so this book teaches it anyway (Chapter 1).
- Topic weights: General Probability 23–30% · Univariate Random Variables 44–50% · Multivariate Random Variables 23–30%.
- In scope: discrete — binomial, geometric, hypergeometric, negative binomial, Poisson, discrete uniform (Bernoulli as n=1); continuous — beta, exponential, gamma, normal, uniform. Out of scope (enrichment only): lognormal, Pareto, Weibull, chi-square.

### The self-diagnostic "skip" mechanism (reader's instruction, printed in front matter)

Think you already know a chapter? Go straight to its Gym Challenge problem set. Work it timed, then check the full solutions. Score the chapter's stated mastery bar (typically 80%+ with correct method) and you may skip ahead. Miss it, and the chapter is waiting for you. The exam doesn't care what you recognize — only what you can DO under time. The skip test measures exactly that.

### The standard chapter architecture (every chapter, same skeleton)

1. **Cold Open (Episode):** a second-person anime scene that is the chapter's core problem in disguise, ending on a question Ash (you) can't yet answer.
2. **Oak's Briefing — Learning Outcomes:** the exact SOA outcomes this chapter discharges, tagged (e.g., Topic 2(e)), with a cross-reference to the manual/sample-question numbers.
3. **The Theory (Pokédex Entries):** definitions, theorems, formulas in boxed entries — each with the formula, its plain meaning, and the recognition cue ("when you see ___, reach for this").
4. **Worked Examples (3–5):** in-world tasks, each solved twice when methods differ — Trainer's Path (fast, exam-efficient) beside Professor's Path (rigorous) — and each labeled with its archetype.
5. **Trainer's Tips:** calculator keystrokes, pacing, archetype recognition, shortcut deployment.
6. **Team Rocket's Trap (the Wally-equivalent):** Jessie & James attempt the problem and commit the canonical mistake; it's diagnosed and the one-line guardrail given. (Team Rocket replaces "Wally" as the recurring blunder-foil — fitting, since their schemes always fail in instructive ways.)
7. **The Gym Battle (Capstone):** the chapter's hardest single problem, framed as the leader's challenge, solved completely — the model the reader imitates.
8. **The Gym Challenge (Problem Set):** tiered — Route Trainers (mechanics, 6–10) → Gym Battles (true SOA difficulty, 10–15) → Elite Challenge (integrative/stretch, 3–5). Problem counts scale to syllabus weight.
9. **Full Answer Key:** complete worked solutions with archetype labels and back-references.
10. **Badge Earned — Mastery Checklist:** "You earn the [Badge] when you can, unaided, (1)…(2)…(3)…", tied one-to-one to the learning outcomes.

### The recurring "Real-World Risk" box (the colored callout you requested)

Throughout every chapter, a distinctly colored text box titled **"⬛ FROM KANTO TO THE REAL WORLD"** connects the concept to actual actuarial/insurance practice — e.g., how Bayes' theorem underlies medical-test pricing, how the deductible math Ash uses is exactly what a P&C actuary computes, how the CLT justifies pooling thousands of policies. These boxes are where the reader sees why this matters for the career the exam unlocks, and they double as the bridge to the later CAS volumes.

### Recurring cast and their pedagogical function

- **Ash (you):** second-person narrator; the actuary-in-training.
- **Professor Oak:** the formalizer — delivers every rigorous definition and the axioms; runs the diagnostic.
- **Pikachu:** the intuition check — reacts when Ash's reasoning "feels" off, foreshadowing a trap before it's named.
- **Misty & Brock:** companions who pose sub-problems from their own expertise (Misty/water-and-luck framing for distributions; Brock/rock-solid logic for combinatorics and proofs).
- **Gary Oak (rival):** the benchmark — always shown solving the problem the correct, non-obvious way one step ahead.
- **Team Rocket (Jessie, James, Meowth):** the blunder-foil — their failed schemes embody each topic's canonical mistake.

---

## Part 1 — The Chapters

Thirteen chapters in dependency order. Chapter 1 is the prerequisite "Trainer School." Chapters 2–4 cover General Probability (23–30%). Chapters 5–8 cover Univariate Random Variables (44–50%) — the largest block, the most chapters, the biggest problem sets. Chapters 9–12 cover Multivariate Random Variables (23–30%). Chapter 13 is exam execution.

### CHAPTER 1 — Trainer School, Pallet Town: The Tools of the Trade

**Maps to:** The pre-journey — the night before Ash gets his first Pokémon. He can't sleep (famously oversleeps in canon); here, he's up late in Oak's lab learning the mathematical tools every risk-trainer needs.
**Discharges:** Prerequisite calculus/algebra (assumed by the SOA, taught here so nothing is missing).

**Narrative connection.** Before a trainer is handed a Pokémon, Oak insists Ash prove he can handle the instruments of an actuary — just as no trainer survives Viridian Forest without knowing how to throw a Poké Ball, no exam-taker survives Exam P without fluent calculus. Oak frames each tool as a piece of trainer gear: integration is "the net that sums up infinitely many tiny outcomes," series are "the way to add an endless swarm of Caterpie," and the gamma-function identity is "the Master Ball of integrals — it catches the hard ones instantly." The chapter is short on narrative and long on toolkit, by design: it's the one chapter a well-prepared reader may skip via the diagnostic.

**Content (bullet-complete):**

- Exponent and logarithm laws; completing the square (for the normal kernel later).
- Summation notation; geometric series Σarᵏ = a/(1−r); exponential series Σλᵏ/k! = eˡ.
- Derivatives (product/quotient/chain); optimization for modes; L'Hôpital's rule.
- Integration: u-substitution, integration by parts (the tabular method), improper integrals over [0,∞).
- The gamma-function identity: ∫₀^∞ x^(α−1)e^(−x/θ)dx = Γ(α)θ^α; ∫₀^∞ xⁿe^(−x)dx = n!; Γ(½)=√π.
- Partial derivatives; double/iterated integrals, including non-rectangular regions and reversing order of integration.

**In-world problem framings:**

- For Professor Oak: calibrate the Pokédex's energy model by evaluating the improper integral that gives a Pokémon's expected lifetime activity — the gamma identity makes it one line.
- For yourself: you have limited time before dawn; set up and reverse the order of a double integral describing the overlap of two Pokémon's territories so you can finish before Oak quizzes you.

**⬛ FROM KANTO TO THE REAL WORLD:** Actuaries integrate loss densities daily to price policies; the gamma identity is one of the most-used shortcuts in real actuarial exams and on the job when working with exponential and gamma loss models.

**Badge:** Toolkit Cleared (not a gym badge — a "Trainer's License" stamp).

### CHAPTER 2 — Pallet Town & Route 1: The Space of All Possible Outcomes

**Maps to:** Ash receives Pikachu (who refuses the Poké Ball) and steps onto Route 1; the famous Pidgey/Spearow encounter. Which Pokémon appears is uncertain — the founding idea of a sample space.
**Discharges:** Topic 1(a) — sets, sample spaces, events, axioms.

**Narrative connection.** Ash's very first decision — which ball, which path, whether the flock of Spearow attacks — is a draw from a sample space he can't control. When the Spearow swarm descends (canon's first crisis), Ash must reason about events ("at least one Spearow targets Pikachu") using complements and unions, because enumerating every bird is hopeless. Pikachu's refusal to enter the ball is the book's first lesson that outcomes aren't always what you'd assign them — the sample space is bigger than your assumptions. Oak narrates the axioms over the Pokédex as Ash runs.

**Content:**

- Sample space S, outcomes, events as subsets; simple vs. compound events.
- Set operations (∪, ∩, complement, difference); Venn diagrams; De Morgan's laws.
- Kolmogorov axioms; derived properties (P(∅)=0, complement rule, monotonicity).
- Inclusion–exclusion for two and three events; the "at least one" = 1 − P(none) complement trick.
- Mutually exclusive vs. independent, contrasted immediately (the year's most confused pair).

**In-world problem framings:**

- To save Pikachu: compute P(at least one Spearow in the flock reaches Pikachu) via the complement, given per-bird probabilities.
- For Route 1 cataloguing: fill a three-event Venn diagram (Pidgey / Rattata / both seen) and compute P(exactly one species seen) for Oak's survey.

**⬛ FROM KANTO TO THE REAL WORLD:** Insurers define the "sample space" of possible claim events; inclusion–exclusion is how they avoid double-counting overlapping coverages, and the complement trick is the fastest route to "probability of at least one claim."

**Team Rocket's Trap:** Jessie insists "mutually exclusive means independent," so their trap fails to catch Pikachu. Diagnosed: disjoint events are maximally dependent.

**Badge:** Boulder Badge — General Probability foundations. (Re-skinned: the first badge anchors the first real topic.)

### CHAPTER 3 — Viridian Forest & Pewter City: Counting the Uncountable — Gym Leader Brock (Rock)

**Maps to:** Viridian Forest (the maze of bug-catchers and countless Pokémon) leading to Brock's Pewter Gym, Ash's first official badge.
**Discharges:** Topic 1(b) — combinatorics.

**Narrative connection.** Viridian Forest is wall-to-wall with Pokémon and trainers — far too many to track individually, so Ash must count by rule, not by sight. How many ways to arrange a team, how many distinct routes through the forest, how many ways to draw three Caterpie from a cluster without replacement — these are permutations, combinations, and the seed of the hypergeometric model. Brock, master of solid foundations, tests whether Ash can count rigorously before he'll grant the Boulder Badge's successor here; Brock's rock-steady logic is the perfect foil for combinatorial precision.

**Content:**

- Fundamental counting principle; permutations P(n,k); combinations C(n,k).
- Permutations with repetition (n!/n₁!n₂!…); multinomial coefficients; partitions.
- Combinatorial probability (favorable/total) under equal likelihood.
- The ordered/unordered × with/without replacement 2×2 classifier.

**In-world problem framings:**

- To navigate the forest: count the distinct paths through a branching trail map so Ash picks the route with the best encounter odds.
- For Brock's challenge: how many distinct 6-Pokémon teams can be built from the species caught so far, and how many battle orders each allows?
- Without replacement: probability of drawing exactly two Pikachu-line Pokémon when grabbing three from a cluster (hypergeometric setup, paying off in Chapter 6).

**⬛ FROM KANTO TO THE REAL WORLD:** Combinatorics underlies risk classification — counting how many rating cells a pricing model splits policyholders into, and computing lottery/catastrophe-coincidence probabilities.

**Team Rocket's Trap:** James counts an unordered team selection as if order matters, vastly overcounting their "plan."

**Badge:** Cascade-prep / Counting Badge (narratively, Brock's badge) — combinatorics mastery.

### CHAPTER 4 — Cerulean City: Reasoning From Evidence — Gym Leader Misty (Water)

**Maps to:** Cerulean City and Misty's gym; also the Bill's-lighthouse / mystery beats. Misty joins as a companion. Ash must infer hidden truths from clues.
**Discharges:** Topic 1(c)–(g) — conditional probability, independence, multiplication/addition rules, total probability, Bayes.

**Narrative connection.** A string of mysteries around Cerulean (a "phantom" thief, a sick Pokémon at the Center, Misty's hidden gym-leader identity) forces Ash to update beliefs as evidence arrives — the essence of conditional probability and Bayes. Misty, whose Water Pokémon thrive on reading currents others can't see, challenges Ash to deduce a hidden type from the damage a move deals (conditioning on observed evidence). The Bayes-table method is introduced as "the detective's grid." Team Rocket's recurring disguises become a base-rate lesson: a clue that looks damning is weak once base rates are included.

**Content:**

- Conditional probability P(A|B); multiplication & addition rules; independence (incl. pairwise vs. mutual).
- Mutually exclusive computations; law of total probability; Bayes' theorem (2-way and n-way).
- Bayes-table method (prior × likelihood → joint → normalize); tree diagrams.

**In-world problem framings:**

- To catch the phantom thief: given base rates for three suspect groups and the likelihood each leaves the found clue, compute the posterior of who's responsible (full Bayes table).
- For Nurse Joy: a Poké-scan test has known sensitivity/specificity; find P(actually sick | tested positive) before quarantining a Pokémon (the false-positive classic).
- For Misty's gym: P(her Starmie's next move is super-effective | observed type) via total probability.

**⬛ FROM KANTO TO THE REAL WORLD:** Bayes' theorem is the backbone of insurance underwriting and fraud detection — updating the probability a claim is fraudulent given observed red flags, and the false-positive math behind medical-test and screening pricing.

**Team Rocket's Trap:** Meowth swaps P(clue|guilty) for P(guilty|clue) and accuses the wrong Pokémon — the prosecutor's fallacy.

**Badge:** Cascade Badge — conditional probability & Bayes mastery.

### CHAPTER 5 — S.S. Anne & Vermilion City: Variables of Fortune — Gym Leader Lt. Surge (Electric)

**Maps to:** The S.S. Anne voyage (where Ash's Charmander/Charmeleon arc and the ship's sinking occur) and Lt. Surge's Vermilion Gym. Quantities aboard the ship — passenger counts, voltages, times — vary randomly.
**Discharges:** Topic 2(a)–(d) — random variables, pmf/pdf/cdf/survival, expectation, moments, variance, MGFs.

**Narrative connection.** On the crowded S.S. Anne, Ash can't track every passenger or every battle outcome — only their distribution. The chapter introduces the random variable as "a number whose value is left to chance," and Lt. Surge's high-voltage gym makes the moments physical: expected voltage (mean), how wildly it surges (variance), the generator that produces every moment on demand (the MGF). When the ship begins to sink (canon), Ash uses the survival function S(x) = P(X > x) — literally "the probability the ship survives past time x" — introducing the Darth Vader rule in its most thematically perfect setting.

**Content:**

- Random variables (discrete/continuous); pmf, pdf, cdf, survival function; valid-distribution conditions; finding the normalizing constant.
- Conditional probabilities for a single RV; truncated/conditional densities.
- Expectation, linearity, E[g(X)]; moments; mode, median, percentiles.
- Variance = E[X²] − (E[X])²; SD; coefficient of variation; Var(aX+b)=a²Var(X).
- MGFs (kernel-recognition derivation; moments by differentiation; uniqueness; sums).
- The Darth Vader rule: E[X] = ∫₀^∞ S(x)dx for X ≥ 0; discrete analog Σ P(X>k).

**In-world problem framings:**

- To escape the sinking ship: given the survival function of "time until the hull floods," use the Darth Vader rule to compute expected escape time.
- For Lt. Surge: his Raichu's variable shock damage has a given density — compute E[X], Var(X), and the 90th percentile so Ash knows the worst-case jolt.
- MGF task: recover a Pokémon's mean and variance from a given MGF by differentiation.

**⬛ FROM KANTO TO THE REAL WORLD:** The survival function is the central object of life and health actuarial work; E[X] via the survival function is exactly how actuaries compute expected lifetimes and expected claim sizes when given only the survival curve.

**Team Rocket's Trap:** Jessie computes E[g(X)] as g(E[X]) (Jensen's trap) and mis-prices their scheme.

**Badge:** Thunder Badge — random variables, expectation, and moments.

### CHAPTER 6 — Lavender Town & Celadon City: The Named Patterns of Chance (Discrete) — Gym Leader Erika (Grass)

**Maps to:** Lavender Town (the Pokémon Tower, Ghost-type counts, the eerie randomness) and Celadon City with Erika's gym and the Game Corner (slots, gambling — discrete probability made literal).
**Discharges:** Topic 2 (discrete distributions) — binomial, geometric, negative binomial, hypergeometric, Poisson, discrete uniform, Bernoulli.

**Narrative connection.** Lavender Town's haunted tower throws counts at Ash — how many Gastly appear in a window (Poisson), how many encounters until the Marowak ghost manifests (geometric). Then Celadon's Game Corner makes discrete distributions a matter of money: the slot machine is a Bernoulli/binomial engine, and Ash must decide whether the prize is worth the expected loss. Erika's gym, with its many similar Grass Pokémon drawn from a fixed bed, is the hypergeometric model in bloom. Each distribution is introduced as "the named pattern" a situation falls into, with the recognition cue front and center.

**Content (each family: pmf, support, mean, variance, MGF, recognition cue):**

- Bernoulli / Binomial; Geometric (state convention) with memorylessness; Negative Binomial.
- Hypergeometric (without replacement, finite-population correction).
- Poisson (mean = variance = λ; sum of independent Poissons; Poisson process intro; binomial→Poisson approximation).
- Discrete Uniform.
- Choosing the family from the story (with/without replacement; fixed n vs. wait-time).

**In-world problem framings:**

- In the Pokémon Tower: model Gastly appearances per minute as Poisson; find P(at least two in five minutes) so Ash can time his passage.
- At the Game Corner: compute the slot machine's expected payout and variance to show Misty (about to gamble her savings) that E[net] is negative.
- For Erika: probability of drawing at least two Gloom-line Pokémon from her fixed garden bed (hypergeometric).

**⬛ FROM KANTO TO THE REAL WORLD:** The Poisson distribution models claim frequency — the number of accidents per year per policyholder — the single most important count model in P&C insurance ratemaking.

**Team Rocket's Trap:** James uses the binomial for a without-replacement draw, ignoring the finite-population correction.

**Badge:** Rainbow Badge — discrete distributions.

### CHAPTER 7 — Saffron City & the Normal World: The Continuous Patterns & the Bell Curve — Gym Leader Sabrina (Psychic)

**Maps to:** Saffron City and Sabrina's psychic gym (the most mind-bending arc — the doll/dimension episode). Continuous, smooth, infinite-valued quantities; the normal distribution as the "shape of the ordinary."
**Discharges:** Topic 2 (continuous distributions) + single-variable transformations — uniform, exponential, gamma, beta, normal.

**Narrative connection.** Sabrina's psychic powers warp the continuous fabric of reality — fitting for the chapter where outcomes stop being countable and become continuous. The normal distribution is the centerpiece: Sabrina's power follows a bell curve, and Ash must standardize (Z = (X−μ)/σ) to measure how far her ability deviates from the norm — "measuring the extraordinary against the ordinary." The exponential's memorylessness is dramatized by a recovery-time puzzle (a fainted Pokémon's remaining recovery doesn't depend on time already elapsed). Transformations appear when Sabrina rescales reality — a change of variable with a Jacobian.

**Content:**

- Uniform; Exponential (memorylessness; time-to-event); Gamma (sum of exponentials; gamma-integral shortcuts); Beta (proportions).
- Normal: standardization, the provided Z-table, symmetry, 68–95–99.7, inverse lookups.
- Transformations of a single RV: CDF method; change-of-variable / Jacobian; inflation as a scaling transform (bridges to Chapter 8).

**In-world problem framings:**

- Against Sabrina: standardize her psychic-power reading to find the probability it exceeds a threshold (normal table).
- For a fainted Pokémon: using exponential memorylessness, show that remaining recovery time is unaffected by time already waited; compute P(recovery within 5 more minutes).
- Transformation task: Sabrina rescales a quantity by a known function — find the new density via the Jacobian.

**⬛ FROM KANTO TO THE REAL WORLD:** The normal distribution and standardization underpin the Central Limit Theorem and nearly all statistical inference; the exponential is the workhorse model for time-to-failure and time-between-claims.

**Team Rocket's Trap:** Jessie forgets to standardize (sign error in Z) and misreads the table.

**Badge:** Marsh Badge — continuous distributions and transformations.

### CHAPTER 8 — Fuchsia City & the Safari Zone: Pricing the Risk — Gym Leader Koga (Poison)

**Maps to:** Fuchsia City, the Safari Zone (limited Safari Balls, capped attempts — a natural deductible/limit metaphor), and Koga's gym.
**Discharges:** Topic 2(e)–(f) — the insurance loss-and-payment model. The highest-weighted, most exam-critical applied chapter.

**Narrative connection.** The Safari Zone runs on limited resources: you get a fixed number of balls, capped attempts, partial reimbursements — the exact structure of deductibles, limits, and coinsurance. Ash, in Actuary Mode, is hired by the Safari Zone warden to price a policy protecting trainers against the cost of Pokémon that flee with their items. Suddenly the loss random variable is "what a fled Pokémon costs," the deductible is "the first few balls you cover yourself," and the per-loss-vs-per-payment distinction is "every escape" versus "only escapes the policy reimburses." Koga's poison damage-over-time even models inflation eroding a fixed deductible. This chapter gets the largest applied problem set in the book.

**Content:**

- Ordinary deductible d: payment (X−d)₊; point mass at 0.
- Policy limit / benefit maximum u: payment min(X,u); limited expected value E[X∧u] and the identity E[X] = E[X∧u] + E[(X−u)₊].
- Coinsurance α; inflation (1+r) applied before deductible/limit; the fixed-deductible-erosion trap.
- Loss vs. payment random variables; payment-per-loss vs. payment-per-payment (conditioning on a payment occurring).
- E, Var, SD of both loss and payment variables; exponential-deductible memoryless shortcut; loss elimination ratio.

**In-world problem framings:**

- For the Safari warden: given the loss distribution and a policy with deductible d, limit u, and coinsurance α, compute expected payment per loss, expected payment per payment, and the variance of what the Zone pays — the full 2(e)/2(f) workout, framed as the quote Ash must produce.
- Inflation task: show how a fixed deductible erodes under Koga's damage-over-time inflation, raising expected payments by less than losses rise.

**⬛ FROM KANTO TO THE REAL WORLD:** This is entry-level P&C actuarial work — computing expected claim payments under deductibles, limits, and coinsurance is the daily math of pricing auto, home, and health policies. (Explicit pointer: this chapter is the bridge to CAS Exam 5 and the predictive-analytics work.)

**Team Rocket's Trap:** Meowth conflates "per loss" with "per payment," forgetting to divide by P(loss > deductible).

**Badge:** Soul Badge — the insurance loss-and-payment model.

### CHAPTER 9 — Cinnabar Island: Two Fates Entwined (Joint Distributions) — Gym Leader Blaine (Fire)

**Maps to:** Cinnabar Island, the Pokémon Mansion and its research logs (the Mewtwo origin lore — paired experimental variables), and Blaine's fire gym with its riddles.
**Discharges:** Topic 3(a)–(b) — joint, marginal, conditional distributions; independence; double integrals.

**Narrative connection.** The Cinnabar Mansion's research logs describe pairs of linked quantities — two experimental Pokémon whose attributes rise and fall together — the natural home of two random variables considered jointly. Blaine's riddle-gym frames each question as "given what you know about one, what can you say about the other?" — conditional and marginal distributions. Ash must integrate a joint density over the mansion's irregular floor plan (a non-rectangular region), the chapter's central skill and the exam's most common multivariate stumbling block.

**Content:**

- Joint pmf/pdf and joint cdf (discrete-led, per syllabus, with continuous joint densities).
- Marginal (sum/integrate out) and conditional distributions.
- Independence of RVs (factorization over rectangular support).
- Double integrals over general regions; choosing/reversing order of integration.

**In-world problem framings:**

- Decoding the mansion logs: from the joint distribution of two linked attributes, find each marginal and the conditional of one given the other.
- For Blaine's riddle: integrate a joint density over the mansion's triangular chamber to find P(both attributes below a threshold).

**⬛ FROM KANTO TO THE REAL WORLD:** Joint distributions model correlated risks — fire and smoke damage, or flood and wind — and getting the dependence right is what keeps insurers from underpricing bundled coverage.

**Team Rocket's Trap:** James assumes independence and factors a joint density that isn't separable over its support.

**Badge:** Volcano Badge — joint and multivariate distributions.

### CHAPTER 10 — Viridian Gym & the Giovanni Confrontation: Expectation Within Expectation — Gym Leader Giovanni (Ground)

**Maps to:** The return to Viridian City, whose gym leader is revealed as Giovanni, head of Team Rocket — a layered reveal mirroring layered (conditional, then total) expectation.
**Discharges:** Topic 3(c)–(d) — conditional and double expectation, conditional variance.

**Narrative connection.** Giovanni's nature is hidden inside another role (gym leader concealing crime boss) — a perfect metaphor for conditional expectation, where the expected value of one thing depends on the realized value of another, and you must average over that hidden layer. Ash, facing Team Rocket's true leader, computes Giovanni's expected strength given the random tier of grunts he commands, then uses the law of total expectation to get the overall threat. The law of total variance quantifies how much of the uncertainty comes from the grunts versus from Giovanni himself.

**Content:**

- E[X|Y] and Var(X|Y) as functions of Y.
- Law of total expectation: E[X] = E[E[X|Y]].
- Law of total variance: Var(X) = E[Var(X|Y)] + Var(E[X|Y]).
- Compound/mixture distributions (number-of-claims-times-severity intuition).

**In-world problem framings:**

- Sizing up Giovanni: his battle strength depends on a randomly drawn grunt tier; use double expectation to find his overall expected strength and total variance.
- Compound task: total item-damage when the number of Rocket attacks is itself random (compound distribution via conditioning).

**⬛ FROM KANTO TO THE REAL WORLD:** The law of total variance decomposes risk into "process variance" and "parameter variance" — the foundation of credibility theory, which is the heart of how insurers blend individual and group experience (and a core CAS Exam MAS-II topic).

**Team Rocket's Trap:** Jessie treats E[X|Y] as a fixed number rather than a random variable, breaking the total-expectation calculation.

**Badge:** Earth Badge — conditional and double expectation. (All eight badges earned.)

### CHAPTER 11 — Victory Road: Combining Forces (Covariance, Correlation & Sums)

**Maps to:** Victory Road — the gauntlet between the badges and the League, where trainers and Pokémon combine their strengths for the final ascent.
**Discharges:** Topic 3(e), (g), (h) — covariance, correlation, linear combinations, moments of sums.

**Narrative connection.** Victory Road is where Ash's team must function as a combination — the whole team's performance is a sum of correlated individual performances. Covariance measures how teammates' outcomes move together; the variance of the team's total includes the cross-terms when Pokémon's performances are correlated. Ash computes the expected total strength of a six-Pokémon team and its variance, learning that ignoring covariance (assuming independence) dangerously misstates the team's reliability on the climb.

**Content:**

- Covariance Cov(X,Y)=E[XY]−E[X]E[Y]; bilinearity; correlation ρ (−1≤ρ≤1; independence ⇒ ρ=0, not conversely).
- Variance of a sum: Var(X+Y)=Var X+Var Y+2Cov(X,Y); general linear combinations Var(ΣaᵢXᵢ).
- Sums of independent families that stay in-family: Normal+Normal, Poisson+Poisson, Gamma+Gamma (same scale), Binomial+Binomial (same p).
- Combinations of independent and normal RVs; moments of linear combinations; MGF method for sums.

**In-world problem framings:**

- For the team's ascent: given each Pokémon's mean and variance and their pairwise covariances, compute the team's total expected strength and its variance — and show why ignoring covariance underestimates risk.
- Sum-in-family task: combine two independent Poisson encounter-counts into one and find the probability of a total threshold.

**⬛ FROM KANTO TO THE REAL WORLD:** Portfolio risk is all covariance — diversification works precisely because combining imperfectly correlated risks reduces total variance; this is the mathematical core of reinsurance and capital management.

**Team Rocket's Trap:** Meowth adds standard deviations instead of variances when combining two schemes.

**Badge:** Victory Road Cleared (a checkpoint medallion, not a gym badge).

### CHAPTER 12 — The Indigo Plateau: Order from Chaos (Order Statistics & the CLT) — The Elite Four

**Maps to:** The Indigo Plateau and the Elite Four / League tournament — thousands of trainers, the best and worst rising to the extremes, and the aggregate settling into predictable form.
**Discharges:** Topic 3(f), (i) — order statistics; the Central Limit Theorem.

**Narrative connection.** The League gathers a vast field of trainers; Ash cares about the extremes (the strongest and weakest competitors — order statistics) and about how the aggregate of thousands of independent matches becomes predictably bell-shaped (the CLT). Facing the Elite Four, Ash computes the distribution of the strongest opponent he's likely to face (the maximum) and uses the CLT to estimate the probability that the tournament's total prize payout exceeds the League's budget — the same aggregation logic Sootopolis-style risk pooling relies on.

**Content:**

- Order statistics of independent RVs: F_max(x)=[F(x)]ⁿ, F_min(x)=1−[S(x)]ⁿ; pdf of max/min; general k-th order statistic; min of independent exponentials.
- System reliability (series = min, parallel = max).
- Central Limit Theorem: sample sum/mean of i.i.d. → approximately normal; standardize and use the table; continuity correction for discrete sums.

**In-world problem framings:**

- Facing the Elite Four: given n independent challengers' strength distributions, find the distribution and expected value of the strongest (maximum order statistic).
- For the League treasurer: approximate P(total prize payout across 100 matches exceeds budget) via the CLT, with continuity correction.

**⬛ FROM KANTO TO THE REAL WORLD:** The CLT is why insurance works — pooling thousands of independent policies makes the average loss predictable even when any single loss is wild; order statistics price catastrophe layers and reinsurance "excess" coverage.

**Team Rocket's Trap:** Jessie skips the continuity correction and mis-approximates a discrete total.

**Badge:** League Finalist — order statistics and the CLT (the last content badge).

### CHAPTER 13 — Champion's Challenge: Becoming a Master — Exam Strategy & Full Mocks

**Maps to:** The final battle against the Champion (Gary/the rival) and Ash's reflection on the whole journey — synthesis, not new theory.
**Discharges:** Exam execution; integrative review across all three topics.

**Narrative connection.** The Champion battle isn't a new gym — it's everything Ash has learned, deployed under pressure against an opponent who knows it all too. The chapter teaches the meta-skills that separate a 6 from a 10: pacing at six minutes a question, recognizing each problem's archetype on sight, deploying the right shortcut instantly, and managing the clock and nerves. It closes the narrative arc — Ash, now both Trainer and actuary-in-training, is ready for the real exam beyond the story.

**Content:**

- The 6-minute-per-question budget; the two-pass strategy (answer recognized archetypes first, flag the rest); never leaving a blank.
- Calculator mastery: TI-30XS nCr/nPr, STO→ to avoid rounding, fraction/decimal toggle, stat lists for summing pmfs; bringing a cleared backup.
- The shortcut catalog consolidated: gamma integral, Darth Vader rule, kernel recognition, memorylessness, Poisson mean=variance, binomial→Poisson, continuity correction.
- Sanity checks: probabilities in [0,1], variances ≥ 0, expected payment ≤ expected loss, support consistency.
- The error-log method: categorize every missed practice problem by root cause and retest.
- Three full 30-question, 3-hour mock exams, weight-matched (~8 General / ~14 Univariate / ~8 Multivariate), with scored keys, topic diagnostics, and pacing post-mortems.
- Readiness gates restated: 24/30 on mocks, Earned Level 7+, six-minute pacing before sitting.

**In-world problem framings:**

- The Champion battle itself: a mixed gauntlet of problems drawn from all twelve prior chapters, presented as successive turns against Gary's team, each turn a different archetype under the clock.

**⬛ FROM KANTO TO THE REAL WORLD:** Real actuaries are judged on accuracy under deadline — exam technique is job technique; the discipline of the error log and the sanity check is exactly how working actuaries catch pricing mistakes before they reach a customer.

**Badge:** Indigo League Champion / Exam P Ready.

---

## Part 2 — Appendices (the perfect-score reference layer)

- **A — Master Formula Sheet** (one page) + the Shortcut Catalog on the reverse (gamma integral, Darth Vader, kernel recognition, memorylessness, continuity correction).
- **B — Distribution Reference Tables** — every in-scope family: support, pmf/pdf, cdf, mean, variance, MGF, recognition cue. (Out-of-scope families flagged as enrichment.)
- **C — The Provided Normal Table** + symmetry techniques to lean on it less.
- **D — Calculator Guide** — TI-30XS MultiView and BA II Plus keystrokes for every recurring computation.
- **E — Exam-Day Logistics & Psychology** — registration, the CBT interface, the cleared-calculator rule, nerves, sleep, the two-pass plan.
- **F — Cross-Reference to the ACTEX/Broverman & Finan Manuals + SOA Sample Questions** — chapter-by-chapter, so this narrative book and the official problem bank reinforce each other.
- **G — Glossary** (Kanto term ↔ formal term).
- **H — Consolidated Answer Keys** (full worked solutions).
- **I — "Risk and Insurance" Study-Note Primer** — the SOA-assumed background, summarized (essential for Chapter 8's outcomes).

---

## Part 3 — Build Notes & Series Position

- **Volume I of the CAS Actuarial series:** Gen 1 / Kanto = Exam 1 / P. Future volumes: Gen 2 / Johto = Exam 2 / FM (time-themed), Gen 3 / Hoenn = MAS-I, Gen 4 / Sinnoh = MAS-II, Gen 5 / Unova = Exam 5, Gen 6 / Kalos = Exam 6, Gen 7 / Alola = PCPA (trial-based, matching the hands-on project).
- **Write-as-you-study:** draft each chapter while learning that topic; the generation effect locks it in — but never let writing displace problem drilling. Read → write the chapter → drill randomized problems → advance.
- **Honor the weights:** Univariate is ~half the exam (Chapters 5–8 carry the largest problem sets); don't over-invest in counting or continuous multivariate beyond what the syllabus tests.
- **Reproducibility hook:** simulate every in-world "battle RNG" example in Python (seed = 151, the Kanto Pokédex count) so each probability claim is verifiable, making the book a portfolio artifact as well as a study guide.
- **Honest scope note:** the full book is a multi-month writing project; the chapter list above is itself a complete study syllabus — work it in ADAPT today and let the prose accrete behind your actual studying. Don't gate your exam date on finishing the book.

---

## Part 4 — The Production Bible (everything needed to start building)

This section converts the design into a buildable specification. It defines the exact anatomy of every recurring element, the budgets, the templates, the assets, the file structure, the build order, and the quality gates. A writer (you or a collaborator) should be able to open to any chapter and produce finished pages without further decisions.

### 4.1 — Global specifications

**Audience & reading level.** A motivated reader starting from beginning-of-college statistics. Prose is conversational and immersive in the narrative beats, precise and textbook-formal in the theory blocks. Never condescending; never padded.

**Voice & tense.** Second person, present tense for narrative ("You step onto Route 1…"); third person for theory and real-world boxes. Ash = "you." The book never breaks character except inside clearly-marked theory/strategy boxes.

**Length budget (target, full book ≈ 320–420 pages):**

- Chapter 1 (prerequisites): 18–24 pages.
- General Probability chapters (2–4): 22–30 pages each.
- Univariate chapters (5–8): 30–40 pages each (the heavy block).
- Multivariate chapters (9–12): 24–32 pages each.
- Chapter 13 (strategy + 3 mocks): 40–55 pages.
- Appendices A–I: 40–60 pages combined.
- Per-chapter word target: narrative + theory ≈ 3,500–6,000 words; the rest is worked examples, problems, and solutions.

**Problem-count budget (scales to syllabus weight):**

- General Probability chapters: ~18–22 problems each.
- Univariate chapters: ~28–34 problems each (largest sets).
- Multivariate chapters: ~20–26 problems each.
- Tier split per chapter: ~40% Route Trainers (mechanics), ~45% Gym Battles (true SOA difficulty), ~15% Elite Challenge (integrative).
- Total target: ~280–320 problems, every one with a full worked solution. At least 60% must be at genuine SOA difficulty and phrasing.
- Provenance rule: each problem is tagged in the source as `original`, `adapted-from-SOA-#`, or `inspired-by`. Never copy a copyrighted manual or SOA solution verbatim — re-skin and re-solve in original wording.

**Math typesetting.** LaTeX throughout (the repo compiles to PDF). Inline math `$...$`; display math `$$...$$`. A shared macro file (`macros.tex`) defines repeated symbols: `\E`, `\Var`, `\SD`, `\Cov`, `\Corr`, the distribution shorthands (`\Normal`, `\Expo`, `\Gamma`, `\Pois`, `\Binom`, etc.), `\given` for the conditional bar, and the payment operators `\dplus{x}{d}` for $(x-d)_+$ and `\limexp{X}{u}` for $E[X\wedge u]$.

### 4.2 — Anatomy of every recurring element (exact templates)

**The Cold Open (Episode)**

- 250–500 words, second person, present tense.
- Ends on an explicit unanswered question Ash needs to solve ("…and the only way off the ship is to know how long the hull will hold. How do you find that?").
- Introduces or advances at least one cast relationship; references the mapped anime beat without requiring the reader to know it.

**Oak's Briefing (Learning Outcomes box)**

- Bulleted list of the SOA outcomes discharged, each tagged (e.g., Topic 2(e)).
- One line: "By the end, you will be able to: [verbs — calculate, derive, recognize]."
- Cross-reference line to Appendix F (manual sections + SOA sample-question numbers).

**Pokédex Entry (theory/formula box) — the core teaching unit.** Fixed three-part structure every time:

1. **The Entry:** the definition/theorem/formula in LaTeX, boxed.
2. **In plain terms:** one or two sentences of intuition, no symbols.
3. **Recognition cue:** "When a problem says/shows ___, this is the tool." — the pattern-matching trigger that builds exam speed.

- Derivations appear below the entry only when they build durable intuition; otherwise a pointer to where the derivation lives.
- A margin "Calculus check" tag names the prerequisite skill each derivation step uses.

**Worked Example (the most important template — standardize it rigorously).** Every worked example uses this exact six-part skeleton:

1. **Setup (in-world):** the task framed as something Ash must accomplish, with the numbers embedded in the story.
2. **Archetype tag:** a labeled callout — "ARCHETYPE: deductible expected-payment per loss." This is what trains recognition.
3. **Identify:** one line naming what's being asked in formal terms and which tool applies.
4. **Trainer's Path:** the fast, exam-efficient solution with the shortcut deployed, every step shown, ~6-minute pace modeled.
5. **Professor's Path (only when it differs):** the rigorous/long method, so the reader trusts the shortcut.
6. **Check & pitfall:** a sanity check (range, units, support) and the one trap a careless solver would hit.

**Trainer's Tip box**

- 1–3 sentences. Pure exam craft: a calculator keystroke sequence, a pacing cue, an archetype tell, or a shortcut reminder. No new theory.

**Team Rocket's Trap box**

- Jessie/James/Meowth attempt the chapter's problem and commit the canonical error in-character (~80–150 words).
- Followed by "The fix:" one sentence naming the error and the guardrail.

**FROM KANTO TO THE REAL WORLD box (the colored callout)**

- 80–160 words. Distinct color (spec below). Connects the concept to actual actuarial/insurance practice.
- Must name a concrete application (claim frequency, fraud detection, reserving, capital, etc.), not a vague "actuaries use this."
- Where relevant, a one-line "Series bridge:" pointer to the CAS exam/volume this foreshadows.

**The Gym Battle (capstone)**

- One problem at or slightly above true exam difficulty, framed as the leader's challenge.
- Solved in complete detail using the Worked Example skeleton, but longer and integrative (pulls in earlier chapters).

**The Gym Challenge (problem set)**

- Three labeled tiers (Route Trainers / Gym Battles / Elite Challenge).
- Each problem numbered `C{chapter}.{n}` and tagged with its archetype and provenance.
- A short "Test-out instructions" header repeating the skip-diagnostic rule.

**Answer Key**

- Full worked solution per problem (not just final answers), each labeled with archetype and a back-reference to the Pokédex Entry used.
- A quick-answer table at the very end for fast self-grading.

**Badge Earned (mastery checklist)**

- "You earn the [Badge] when you can, unaided: (1)…(2)…(3)…" — 3–6 can-do statements mapped one-to-one to the learning outcomes.
- A "Gym rematch" pointer: which sections to revisit if a checklist item fails.

### 4.3 — Visual & asset specification

**Design system (carry the existing Kanto theme).** Reuse the established palette and matplotlib style from the prior Kanto asset work so figures are consistent:

- Kanto Red `#EE1515`, Blue `#3B4CCA`, Yellow `#FFD733`, Green `#4DAD5B`, Gray `#888888`, Background `#FAFAF5`.
- Box color assignments: Pokédex Entry = blue rule/tint; Trainer's Tip = yellow; Team Rocket's Trap = red; FROM KANTO TO THE REAL WORLD = green tint with a dark-green rule (the "colored text box" requested); Cold Open = light-gray italic block.

**Figures required (generated programmatically, matplotlib, no copyrighted sprites embedded):**

- Every chapter: at least one diagram (Venn diagrams Ch 2; tree/Bayes-table grids Ch 4; pmf bar charts and pdf curves Ch 6–7; the normal curve with shaded tails Ch 7; payment-vs-loss step graphs Ch 8; joint-density region sketches Ch 9; CLT convergence animation-stills Ch 12).
- A recurring "Kanto map" progress strip at each chapter head showing which town/badge the reader has reached (built from an original stylized map, not game assets).
- Distribution "trading cards": a one-per-distribution card graphic (pmf/pdf, mean, variance, MGF, recognition cue) reused in Ch 6–7 and Appendix B.

**Asset sourcing rule (decided).** All Pokémon imagery — Pokédex sprites, type icons, gym badges, character portraits, the Kanto map — is **pulled at build time from open community GitHub repositories**, never hand-drawn, AI-generated, or original-stylized. Sources (same as the sister project):

- **Sprites** (151 Kanto front sprites, incl. Pikachu #25, Meowth #52): `PokeAPI/sprites` → `sprites/pokemon/{id}.png` (`assets/download_sprites.py`).
- **Badges** (Boulder…Earth): `PokeAPI/sprites` → `sprites/badges/{1..8}.png`.
- **Type icons**: `PokeAPI/sprites` → `sprites/types/generation-viii/sword-shield/{id}.png`.
- **Characters** (Oak, Brock, Misty, gym leaders, rival Gary, Team Rocket grunt, Elite Four): `pret/pokered` Gen-1 disassembly → `gfx/trainers/*.png`.
- **Kanto map**: `pret/pokered` → `gfx/town_map/town_map.png`.

The **only** programmatically generated images are the *mathematical* figures (Venn diagrams, pmf/pdf curves, shaded normal tails, payment-vs-loss step graphs, Bayes grids, CLT convergence) — these contain no Pokémon art and exist because no repo holds a plot for our exact problems. `assets/` is `.gitignore`d and fetched on build. This is a personal, non-commercial, single-copy **printed & bound** study aid; the trademark disclaimer stays on the title page and colophon. For print fidelity, low-res sprites are upscaled with nearest-neighbor (`assets/upscale_assets.py`) so pixel art stays crisp at 300 DPI.

### 4.4 — Repository structure & toolchain

```
exam-p-kanto/
├── README.md                     # this design doc + build instructions
├── book/
│   ├── main.tex                  # master file, \include each chapter
│   ├── macros.tex                # shared LaTeX macros (see 4.1)
│   ├── theme.sty                 # box styles, colors, fonts (tcolorbox-based)
│   ├── frontmatter/              # title, colophon, how-to-use, diagnostic
│   ├── chapters/                 # ch01.tex … ch13.tex
│   ├── appendices/               # appA.tex … appI.tex
│   └── solutions/                # answer keys (compiled in or as separate PDF)
├── problems/
│   ├── bank.yaml                 # every problem: id, chapter, tier, archetype,
│   │                             #   provenance, statement, solution, answer
│   └── coverage.csv              # problem → SOA learning-outcome matrix
├── figures/
│   ├── src/                      # matplotlib generation scripts (+ kanto_theme.mplstyle)
│   └── out/                      # generated PNG/PDF figures
├── sims/                         # Python notebooks verifying each example (seed=151)
│   └── verify_examples.ipynb
├── assets/                       # optional, gitignored: fetched sprites for personal builds
└── build/                        # compiled PDF output
```

**Toolchain.** LaTeX (XeLaTeX/LuaLaTeX for fonts) + `tcolorbox` for the styled boxes + `pgfplots`/matplotlib for figures. A `Makefile` target `make book` regenerates figures, runs the sims to verify example numbers, then compiles `main.tex` → `build/exam-p-kanto.pdf`. Markdown is acceptable for drafting individual chapters, converted to LaTeX via Pandoc, but the canonical source is LaTeX so math and boxes render correctly for print.

> **Note on the actual toolchain we are adopting:** the sister project (*Causal Inference: A Pokémon Approach*) ships a **Markdown-source + Pandoc → HTML/CSS → PDF** pipeline that already works end-to-end and produces an 8 MB illustrated PDF. We are reusing that proven pipeline rather than the LaTeX-canonical one sketched above. See `FORMATTING.md` for the exact mechanism (how sprites, math, callout boxes, theme colors, and the build are wired). The LaTeX option remains available as a print-grade alternative if needed.

**Verification gate (the reproducibility hook made operational).** Every worked example and every problem with a numeric answer is reproduced in `sims/` with `seed=151`; the build fails if a printed answer disagrees with its simulation/closed-form check beyond tolerance. This is what lets the book claim "guaranteed correct."

### 4.5 — The problem-bank schema (so problems are data, not prose)

Each entry in `problems/bank.yaml`:

```yaml
- id: C8.14
  chapter: 8
  tier: gym_battle            # route_trainer | gym_battle | elite_challenge
  archetype: "expected payment per payment, exponential loss + deductible"
  outcomes: ["2e", "2f"]
  provenance: adapted-from-SOA-#152
  difficulty: 4               # 1–5, calibrated to ADAPT-style levels
  narrative_hook: "Pricing the Safari Zone warden's flee-cost policy"
  statement: |
    ...
  solution: |
    ... full worked steps ...
  answer: "E"                 # or numeric
  shortcut_used: ["memoryless exponential", "darth-vader"]
```

This makes it trivial to (a) auto-build the coverage matrix, (b) confirm every learning outcome is hit enough times, (c) assemble the Chapter-13 mock exams by sampling to the real weight split, and (d) reuse problems across formats.

### 4.6 — Coverage guarantee (how we prove completeness)

- `problems/coverage.csv` maps every problem to its SOA outcome(s). A build check asserts each outcome has ≥ 8 problems and each in-scope distribution appears in ≥ 6 problems.
- A second check asserts the mock exams in Chapter 13 match the live weight split (~8 General / ~14 Univariate / ~8 Multivariate per 30).
- The Part-2 coverage self-audit table (all outcomes 1a–3i) is regenerated from `coverage.csv` so it can never silently drift from the actual content.

### 4.7 — Build sequence (the order to actually write)

Don't write front-to-back. Write in this order to de-risk fastest:

1. `theme.sty` + `macros.tex` + one fully-built sample chapter — **Chapter 8 (Safari Zone / insurance)**. It's the highest exam weight and exercises every box, the worked-example skeleton, figures, and the real-world bridge. This is the gold-standard template; everything else is cloned from it.
2. **Appendix B (distribution tables) + Appendix A (formula/shortcut sheet).** Useful from day one of studying even before prose exists; they're the reference layer.
3. **Chapter 1 (prerequisites) and Chapter 5 (random variables/expectation)** — the load-bearing foundations.
4. The rest of the **Univariate block (6, 7)**, then **General Probability (2–4)**, then **Multivariate (9–12)**.
5. **Chapter 13 + the three mock exams**, assembled by sampling the problem bank to the weight split.
6. Remaining appendices (C–I), front matter, figures pass, full verification build.

A reader can study from the chapter list and Appendices A/B immediately; the prose accretes behind real studying.

### 4.8 — Definition of done (quality gates per chapter)

A chapter is "done" only when all are true:

- [ ] All mapped SOA outcomes covered with a Pokédex Entry and ≥ 1 worked example each.
- [ ] 3–5 worked examples, each using the full six-part skeleton with an archetype tag.
- [ ] Problem set meets its tier counts; every problem has a full solution and a provenance tag.
- [ ] One Team Rocket's Trap, ≥ 2 Trainer's Tips, ≥ 1 real-world box.
- [ ] Every numeric answer verified in `sims/` (build passes).
- [ ] Badge checklist maps one-to-one to the outcomes.
- [ ] At least one original figure; all figures use the theme palette.
- [ ] Skip-diagnostic instructions present; reading level and length within budget.
- [ ] No copyrighted text or sprites embedded; disclaimer intact.

### 4.9 — First-draft starting kit (what to hand a writer or tackle first)

To begin building this week, the minimum viable starting set is:

1. This design document (the spec).
2. `theme.sty` and `macros.tex` (a few hours of setup) — or, in the adopted Markdown pipeline, `theme.css` + `embed_visuals.py` (see `FORMATTING.md`).
3. A drafted Chapter 8 as the reference implementation.
4. Appendix B distribution cards.

Everything after that is repetition of an established pattern, which is exactly when the writing becomes fast — and exactly when it's safe to let it run behind your actual exam studying rather than ahead of it.

---

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc. This is an educational, non-commercial fan work. All exam details verified against the SOA Exam P syllabus (2026 administration) and official SOA sources; treat exam fees, formats, and resource availability as current-as-of-2026 and confirm against soa.org before any sitting.*
