<!--
  file: ch08_calculus
  tier: C
  outcomes: prereq
  tia: B.0.1-B.0.3
  locale: Bill's lighthouse / a training montage (no gym, no badge — the "HM: Calculus")
  type: steel
  maps_to: the calculus prerequisites the SOA silently assumes — differentiation
           (rules, optimization/modes, L'Hopital) -> integration (u-sub, improper
           over [0,inf)) -> integration by parts (tabular) -> the gamma integral
           (the "Master Ball of integrals")
-->

# The Calculus Toolkit — the HM You Need for the Continuous Wilds {.type-steel}

<figure>
<img src="../../assets/maps/kanto_ch08.png" alt="Kanto town map with the coastline near Cerulean highlighted, a lone lighthouse tower marked on a spit of land north of the city, its beam sweeping out over dark water. No city is circled — this is a way-station between the discrete road behind you and the continuous wilds ahead." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>Not a gym — a <em>way-station</em>. Bill's lighthouse stands between the discrete road you have walked and the continuous wilds ahead. There is no badge here. There is an <strong>HM</strong>: the calculus you must own to cross.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Mystery at the Lighthouse"**

The lighthouse is dark when you arrive, and the man who lives in it answers only by intercom. **Bill** — the Pokémon researcher, the one who built the storage system that turns a caught Pokémon into *data* and back — will not open the door until you prove you can read his instruments.

"Everything past this point is *continuous*," his voice crackles. "On the road behind you, you counted. You summed. One Pokémon, then another, then another — discrete, tick by tick. But the sea out my window doesn't tick. The time until the next wave, the size of the next claim, the length of a life — these *flow*. And the only language that reads a flowing quantity is calculus."

A single line glows on his monitor:

$$\int_0^\infty x^{3}\, e^{-x/2}\, dx \;=\; ?$$

"This shape — a power of $x$ times a decaying exponential, swept from zero to infinity — is the most common integral on Exam P. Every expected lifetime, every gamma loss, every average claim collapses into it. A weak trainer grinds it out by parts, four times, and runs out of clock. A strong trainer *recognizes* it and writes the answer in one line."

Far out over the water, something enormous answers the beam — a shape too big to be a wave, rising on leathery wings. Bill's voice drops. "And *that*. The dragon the light calls in from the deep. You'll meet a quantity like it later — most of the time it's nothing, but its tail runs out past the edge of the chart, all the way to infinity. To know whether that tail's *area* is even finite, you'll integrate to a wall and slide the wall out forever."

The intercom clicks. "So. Before I open this door — prove you can wield the instruments. Find me that integral. Find me a curve's peak. Run an integral out to infinity without flinching. This is the HM you don't get to skip."
:::

## Where You Are — 60-Second Retrieval

**Rank: Ace Trainer · Badges: 5.** Five badges ride in your case — Boulder, Cascade, Thunder, Rainbow, and Soul. There is **no sixth to win here**: the lighthouse hands out no badge. What it hands out is an **HM** — a tool you carry forever, the calculus that every continuous chapter ahead silently assumes.

Look back at the road you walked. Across all of **Act I** you worked with *discrete* random variables: things you could **count**. A pmf assigned a lump of probability to each whole-number outcome, and every quantity you wanted — a mean, a variance, a moment generating function — was a **sum** over those lumps, $E[X] = \sum_x x\,p(x)$. That machine works perfectly as long as the outcomes are countable.

But the wilds ahead are **continuous**. Probability will no longer sit in lumps you can add; it will spread *smoothly* over a range, and "how much probability sits here" will be an **area under a curve**. The sum $\sum$ becomes an integral $\int$; the lump $p(x)$ becomes a density $f(x)$. To do *anything* in that world — normalize a density, find an expected value, read a tail — you need to differentiate, integrate, and handle integrals that run out to infinity. **That is exactly what this chapter installs.** Continuous needs calculus; here is the calculus.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you're ready to install the HM**

Answer from memory; if any feels shaky, flip back before continuing.

1. Simplify $e^{-x/\theta}\cdot e^{-x/\theta}$ to a single exponential. *(Answer: $e^{-2x/\theta}$ — add the exponents.)*
2. In Act I, how did you compute a discrete mean $E[X]$? *(Answer: $\sum_x x\,p(x)$ — a weighted sum over the pmf.)*
3. What is $e^{0}$, and what does $\ln(e^{k})$ equal? *(Answer: $1$; and $k$ — they undo each other.)*

All three instant? You're ready to install the tools. Any hesitation? Reclaim the exponent/log algebra (ch00 Toolkit) first — every line below leans on it.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP013 "Mystery at the Lighthouse"**

<figure><img src="../../assets/stills/ch08_now_playing.jpg" alt="A lighthouse beam sweeping over the dark sea at night (Indigo League EP013)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">Bill's lighthouse, EP013 — acquiring the tools for the continuous world.</figcaption></figure>

Ash and friends shelter at the lighthouse of **Bill**, the Pokémon researcher and inventor of the PC storage system. Through the night a vast, mysterious silhouette approaches across the sea, drawn by the lighthouse beam — a giant Pokémon answering a recorded cry. *Watch it before or after this chapter.* The episode's throughline is ours exactly: Bill is the man who turns living Pokémon into **continuous data** and back, and the thing in the dark — too large to fully see, its edges running off past the frame — is the picture of a quantity whose **tail extends to infinity**. (Bill's monitor-puzzle, the integral he sets you, and the dragon-as-heavy-tail are **in-world extensions** built to carry the calculus; the silhouette-at-the-lighthouse is the genuine on-screen scene.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — patched in to brief you; Bill runs the door</figcaption>
</figure>

Professor Oak patches into Bill's intercom. "Listen to Bill on this one, Ash — he's right. Exam P does not *teach* you calculus. The SOA **assumes** it is already in your bag and tests probability on top of it. This chapter is where we put it there — not as a list of formulas to memorize, but as a small set of instruments you understand well enough to reach for without thinking."

"This is a **Tier C** chapter," Oak adds, "which means two things. First: it is **fully skippable in pieces** — own a tool already? Prove it at its gate and move straight on; you lose no time. Second: skippable does *not* mean thin. Whatever you *do* stop to learn here, you learn **completely** — every step real, nothing waved past. We will be brief, never vague."

By the end of this chapter you will be able to:

- **Differentiate** with the product, quotient, and chain rules; **find a mode** by optimization (set $f'=0$); and resolve $\tfrac00$ or $\tfrac{\infty}{\infty}$ limits with **L'Hôpital's rule** and the "exponential beats polynomial" principle. *(Prereq — TIA B.0.1.)*
- **Integrate** by **$u$-substitution**, and evaluate **improper integrals** over $[0,\infty)$ — normalizing a density and reading a survival tail. *(Prereq — TIA B.0.2.)*
- **Integrate by parts**, fast, using the **tabular** layout that turns a power-times-exponential into a table instead of repeated by-hand rounds. *(Prereq — TIA B.0.3.)*
- **Deploy the gamma-integral identity** $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx = \Gamma(\alpha)\,\theta^{\alpha}$ as a one-line shortcut — the **Master Ball** of integrals, the single most leveraged tool in the book. *(Prereq — the capstone of this chapter.)*

> *Exam-weight signpost.* Nothing here is a numbered SOA *topic* — these are the **prerequisites** the exam silently demands, which is why they carry the tag `prereq`. But that makes them load-bearing in a different way: the gamma identity recurs in nearly every continuous chapter that follows (ch09–ch13, ch17), and a single dropped chain rule or lost limit will sink an otherwise-correct probability answer. This is a **Tier C** toolkit chapter — tight, complete, and **skippable in pieces**.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own This Whole Toolkit?**

Already fluent? Prove it. Work these four, ~2 minutes each, *with correct method*:

1. Find the mode of $f(x) = \tfrac14 x\,e^{-x/2}$ on $x>0$.
2. Find $c$ so that $f(x) = c\,e^{-x/7}$ ($x>0$) is a valid density, then write its survival $S(t)$.
3. Evaluate $\displaystyle\int_0^\infty x^{2} e^{-x/3}\,dx$ in one line.
4. Evaluate $\displaystyle\int_0^\infty x^{3} e^{-x/2}\,dx$ in one line.

*(Answers: mode $=2$; $c=\tfrac17$ and $S(t)=e^{-t/7}$; $\Gamma(3)\,3^3 = 2\cdot 27 = 54$; $\Gamma(4)\,2^4 = 6\cdot 16 = 96$.)* Four for four with the right reasoning? **Skip to the Gym Battle** (Bill's door) and stamp the HM. Any miss or hesitation? The teaching below was built exactly for you — and **each tool has its own skip-gate**, so even a partial owner loses no time.
:::

---

Four tools build here, in increasing difficulty, in TIA order. We teach them **in order**, each with its own "do you already own this?" skip-check, then a tight, complete lesson, then a Pokédex Entry you carry onto the exam:

1. **Differentiation, modes & limits** *(B.0.1)* — slopes, peaks, and who wins as $x\to\infty$
2. **Integration & improper integrals** *(B.0.2)* — summing slices, and running the upper limit to infinity
3. **Integration by parts, the tabular way** *(B.0.3)* — power $\times$ exponential without the grind
4. **The gamma identity** — the **Master Ball**: power $\times$ decaying exponential, in one line

## Concept 1 — Differentiation, Modes & Limits (B.0.1)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Derivatives, Modes & Limits**

For $f(x) = \tfrac14 x\,e^{-x/2}$ on $x>0$, find the value of $x$ where $f$ **peaks** (its mode). Then evaluate $\displaystyle\lim_{x\to\infty} x^2 e^{-x/3}$.

If you got **mode $=2$** (via the product + chain rule, setting $f'=0$) and **$\lim = 0$** ("exponential beats polynomial"), **skip to Concept 2**. If either made you hesitate — especially if you tried to differentiate $x\,e^{-x/2}$ without the product rule — read on.
:::

**The idea.** A derivative is the **slope** of a curve; where the slope is zero the curve is flat, which is exactly where a density **peaks** — and when a limit jams at $\tfrac00$ or $\tfrac{\infty}{\infty}$, differentiating top and bottom breaks the tie.

**Concrete instance.** You will meet densities that rise, crest, and fall — like $f(x)=\tfrac14 x\,e^{-x/2}$. The **mode** is the crest: the most likely value. At a crest the tangent line is horizontal, so the slope $f'(x) = 0$. Finding the peak means differentiating and solving $f'=0$.

**Reason it through.** The function $\tfrac14 x\,e^{-x/2}$ is a **product** of a rising part $x$ and a falling part $e^{-x/2}$. Early on the rising $x$ wins and the curve climbs; eventually the decaying exponential wins and it falls. The peak is the handoff. To differentiate a product you cannot just differentiate each piece — you need the **product rule** ("first-prime times second, plus first times second-prime"), and the exponential's derivative needs the **chain rule** (inside function $-x/2$):

$$f'(x) = \tfrac14\Big[\underbrace{1\cdot e^{-x/2}}_{(x)'\,e^{-x/2}} + \underbrace{x\cdot\big(-\tfrac12\big)e^{-x/2}}_{x\,(e^{-x/2})'}\Big] = \tfrac14\,e^{-x/2}\Big(1 - \tfrac{x}{2}\Big).$$

Set $f'(x)=0$. Since $e^{-x/2}$ is always positive (never zero), the only solution is $1 - \tfrac{x}{2}=0$, i.e. $x=2$. The sign of $f'$ runs $+$ (climbing) to $-$ (falling), so it is a **maximum** — the mode is $x=2$.

**The tempting wrong idea.** The classic slip is to differentiate the product *piece by piece*: $(x\,e^{-x/2})' \overset{?}{=} 1\cdot(-\tfrac12)e^{-x/2}$, dropping a whole term. Wrong — the derivative of a product is **not** the product of the derivatives; keep **both** terms. A second slip: forgetting the chain rule on $e^{-x/2}$ and writing its derivative as $e^{-x/2}$ instead of $-\tfrac12 e^{-x/2}$ (the inside $-x/2$ contributes its own derivative $-\tfrac12$ out front).

**Notation, one glyph at a time.** The three rules, named and read aloud:

$$(fg)' = f'g + fg' \qquad \text{read: ``derivative of a } \textbf{product}\text{.''}$$
$$\left(\frac{f}{g}\right)' = \frac{f'g - fg'}{g^2} \qquad \text{read: ``derivative of a } \textbf{quotient}\text{.''}$$
$$\frac{d}{dx}\,f\big(g(x)\big) = f'\big(g(x)\big)\,g'(x) \qquad \text{read: ``the } \textbf{chain rule}\text{ — outside derivative times inside derivative.''}$$

The symbol $\tfrac{d}{dx}$ reads **"the derivative with respect to $x$ of"** — an *instruction*, not a fraction. The prime $f'$ is shorthand for the same.

**The mode recipe, and the limit tool.** *Mode recipe:* to find where any density $f$ peaks, compute $f'$, set $f'=0$, solve, confirm $f'$ flips $+\to-$. Every mode problem is this. *The limit tool:* sometimes a limit collapses to the meaningless forms $\tfrac00$ or $\tfrac{\infty}{\infty}$. **L'Hôpital's rule** says: differentiate top and bottom *separately* and try again,

$$\text{if } \lim \frac{f}{g} \text{ is } \tfrac00 \text{ or } \tfrac{\infty}{\infty}, \quad \lim \frac{f(x)}{g(x)} = \lim \frac{f'(x)}{g'(x)}.$$

**Ramp the difficulty.**

- *Simplest:* the mode $x=2$, above.
- *The limit you'll use constantly:* $\displaystyle\lim_{x\to\infty} x^2 e^{-x/3}$. Written $\tfrac{x^2}{e^{x/3}}$ it is $\tfrac{\infty}{\infty}$. One L'Hôpital pass: $\tfrac{2x}{\frac13 e^{x/3}}$ — still $\tfrac{\infty}{\infty}$; a second pass: $\tfrac{2}{\frac19 e^{x/3}} \to 0$. The exponential outgrows any polynomial. **Exponential beats polynomial** — memorize it and you rarely even reach for the rule.
- *Why it matters:* every probability density on $[0,\infty)$ has a tail like $x^n e^{-x/\theta}$; this limit being $0$ is *why* that tail's area is finite (Concept 2) and why expectations exist.
- *Edge:* L'Hôpital applies **only** to $\tfrac00$ and $\tfrac{\infty}{\infty}$. Used on a limit that isn't indeterminate, it gives a wrong answer.

**Picture it.**

<figure>
<img src="../../assets/diagrams/ch08_deriv_rules.png" alt="Left panel: the curve f(x) = (1/4) x e^{-x/2} rising from the origin, cresting at x=2, then decaying; a red dashed horizontal tangent touches the crest where f'=0, labelled 'the mode'; the formula f'(x) = (1/4) e^{-x/2}(1 - x/2) is written above. Right panel: x^2 and e^{x/3} both rising, with e^{x/3} overtaking, annotated x^2 / e^{x/3} -> 0, exp beats poly." style="width:90%; max-width:740px; display:block; margin:1em auto;">
<figcaption>The mode is where the tangent goes flat ($f'=0$): here $x=2$. Right: the exponential outruns the polynomial, so $x^2 e^{-x/3}\to 0$ — which is what makes the density's tail area finite.</figcaption>
</figure>

**Consolidate.** You can differentiate products and compositions, find a density's mode by setting $f'=0$, and clear a $\tfrac00$ or $\tfrac{\infty}{\infty}$ limit with L'Hôpital — knowing in advance that exponential decay always beats polynomial growth.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Differentiation, Modes & Limits**

$$(fg)' = f'g + fg', \qquad \left(\tfrac{f}{g}\right)' = \tfrac{f'g - fg'}{g^2}, \qquad \tfrac{d}{dx}f(g(x)) = f'(g(x))\,g'(x).$$
$$\textbf{Mode:}\ \text{solve } f'(x)=0. \qquad \textbf{L'Hôpital } \left(\tfrac00,\tfrac{\infty}{\infty}\right):\ \lim\tfrac{f}{g}=\lim\tfrac{f'}{g'}. \qquad \lim_{x\to\infty} x^n e^{-x/\theta}=0.$$

*In plain terms:* the slope of a curve; zero slope marks a peak (the mode). When a limit jams at $\tfrac00$ or $\tfrac{\infty}{\infty}$, differentiate top and bottom and retry — and exponential decay always wins against polynomial growth.

*Recognition cue:* "most likely value / peak / mode" $\to$ set $f'=0$. A limit that evaluates to $\tfrac00$ or $\tfrac{\infty}{\infty}$ $\to$ L'Hôpital. A tail $x^n e^{-x/\theta}$ as $x\to\infty$ $\to$ it's $0$, no work needed.
:::

## Concept 2 — Integration & Improper Integrals (B.0.2)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Integration over $[0,\infty)$**

Find the constant $c$ that makes $f(x) = c\,e^{-x/7}$ ($x>0$) a valid probability density (total area $1$). Then write the survival probability $S(t) = \int_t^\infty \tfrac14 e^{-u/4}\,du$ as a clean formula in $t$.

If you wrote **$c = \tfrac17$** (because $\int_0^\infty e^{-x/7}\,dx = 7$) and **$S(t) = e^{-t/4}$** (and you can confirm $S(0)=1$), **skip to Concept 3**. If the upper limit of $\infty$ made you uneasy, or you wrote $S(t)=1-e^{-t/4}$, read on.
:::

**The idea.** An integral sums infinitely many infinitely-thin slices of area under a curve; pushing the upper limit to infinity is fine **as long as the tail decays**, and "total area $=1$" is exactly what makes a function a probability density.

**Concrete instance.** A continuous distribution spreads probability over a *range*, not single points, and "how much probability sits here" is an **area** under the density — an integral. Before any of that area means anything, the *whole* area must be $1$. Task: *Bill models encounter intensity by $f(x) = c\,e^{-x/7}$ for $x>0$; find the $c$ that makes the total area $1$.*

**Reason it through.** We need $\int_0^\infty c\,e^{-x/7}\,dx = 1$. The antiderivative of $e^{-x/7}$ is $-7e^{-x/7}$ (check: differentiate $-7e^{-x/7}$, the chain rule gives $-7\cdot(-\tfrac17)e^{-x/7}=e^{-x/7}$ ✓). But the upper limit is *infinity*, which we cannot plug in directly. So integrate up to a finite **wall** $b$, then let the wall slide out:

$$\int_0^\infty e^{-x/7}\,dx = \lim_{b\to\infty}\Big[-7e^{-x/7}\Big]_0^{b} = \lim_{b\to\infty}\Big(-7e^{-b/7} + 7\Big) = 0 + 7 = 7,$$

because $e^{-b/7}\to 0$ as the wall recedes (Concept 1: exponential decay wins). So $\int_0^\infty c\,e^{-x/7}\,dx = 7c$, and $7c=1$ gives $c=\tfrac17$.

**The tempting wrong idea.** Two traps. First, the **infinity panic**: *"you can't integrate to infinity."* You can — you take a **limit**, and as long as the tail $e^{-b/7}$ dies (it does), the area is finite. Second, the **survival-vs-CDF mix-up**. The **survival** $S(t)=\int_t^\infty f$ is the probability of landing *above* $t$; the **CDF** $F(t)=\int_0^t f$ is the probability *below* $t$. They satisfy $S = 1-F$, and it is dangerously easy to compute one and label it the other. Anchor on the endpoints: a survival has $S(0)=1$, $S(\infty)=0$; a CDF has $F(0)=0$, $F(\infty)=1$. If your formula fails that test, you computed the other one.

**Notation, one glyph at a time.** The **improper integral** over $[0,\infty)$ is *defined* as a limit:

$$\int_0^{\infty} f(x)\,dx \;=\; \lim_{b\to\infty}\int_0^{b} f(x)\,dx \qquad \text{read: ``integrate to a wall } b\text{, then slide } b \text{ to infinity.''}$$

The sign $\int$ is an elongated "S" for **sum**; $dx$ is the **width** of an infinitely thin slice; together $\int f(x)\,dx$ reads **"sum the slice heights $f(x)$ times their tiny widths $dx$."** The one integration move you reuse most (the next concept handles the other):

$$\int f\big(g(x)\big)\,g'(x)\,dx = \int f(u)\,du \quad(\textbf{$u$-substitution, reverses the chain rule}).$$

Spot an inside function $g(x)$ whose derivative $g'(x)$ is sitting in the integrand, set $u=g(x)$, and the integral collapses. *Example:* $\int_0^1 y^2 e^{y^3}\,dy$ — the inside is $y^3$, $du = 3y^2\,dy$, so it becomes $\tfrac13\int_0^1 e^u\,du = \tfrac13(e-1)$.

**The two facts you'll lean on.** From the work above, the exponential's total area over $[0,\infty)$ is just its scale:

$$\int_0^{\infty} e^{-x/\theta}\,dx = \theta, \qquad\text{hence}\qquad \int_0^\infty \tfrac1\theta e^{-x/\theta}\,dx = 1.$$

That second line is *why* $\tfrac1\theta e^{-x/\theta}$ is a valid density. And its survival tail is

$$S(t) = \int_t^\infty \tfrac1\theta e^{-u/\theta}\,du = \Big[-e^{-u/\theta}\Big]_t^\infty = e^{-t/\theta},$$

which indeed has $S(0)=1$ and $S(\infty)=0$ — a survival function, not a CDF.

**Ramp the difficulty.**

- *Simplest:* normalize $e^{-x/7}$, getting $c=\tfrac17$.
- *Survival tail:* $S(t)=\int_t^\infty \tfrac14 e^{-u/4}\,du = e^{-t/4}$ (the gate problem); confirm $S(0)=1$.
- *$u$-substitution twist:* $\int_0^1 y^2 e^{y^3}\,dy = \tfrac13(e-1)$, as above.
- *By-parts / the harder road:* $\int_0^\infty x^3 e^{-x/2}\,dx$ — grindable by parts, but that's exactly the labor the next two concepts eliminate.

**Picture it.**

<figure>
<img src="../../assets/diagrams/ch08_improper.png" alt="The density (1/theta) e^{-x/theta} over [0, infinity). The full shaded area under it equals 1 (normalization), labelled with the integral. A second region from a red dashed line at t rightward is hatched and labelled S(t) = integral from t to infinity of f = e^{-t/theta}, the survival tail. A dotted vertical wall at b is annotated 'wall b -> infinity; tail e^{-b/theta} -> 0'. Bill's Dragonite #149 sits in the clear upper-right margin." style="width:90%; max-width:760px; display:block; margin:1em auto;">
<figcaption>The full area under a density is $1$ (which fixes $c$); the tail area from $t$ rightward is the survival $S(t)$. The upper wall $b$ slides to infinity and the tail $e^{-b/\theta}$ vanishes — the dragon at the edge of the chart, the part that runs off to infinity.</figcaption>
</figure>

**Consolidate.** You can integrate over $[0,\infty)$ by taking a limit, find a density's normalizing constant by forcing the total area to $1$, compute a survival tail $S(t)$ (and tell it from the CDF by the endpoint test), and collapse a chain-rule integrand with $u$-substitution.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Improper Integrals, Normalizing & Survival**

$$\int_0^{\infty} f(x)\,dx = \lim_{b\to\infty}\int_0^{b} f(x)\,dx, \qquad \int_0^{\infty} e^{-x/\theta}\,dx = \theta, \qquad \int_0^\infty \tfrac1\theta e^{-x/\theta}\,dx = 1.$$
$$\textbf{$u$-sub:}\ \int f(g)\,g'\,dx=\int f(u)\,du. \quad \textbf{Normalize:}\ \int f = 1. \quad \textbf{Survival:}\ S(t)=\int_t^\infty f = 1-F(t),\ S(0)=1,\ S(\infty)=0.$$

*In plain terms:* integrate to a finite wall, then let it slide to infinity; if the tail decays, the area is finite. "Total area $=1$" defines a density; the tail area from $t$ rightward is survival.

*Recognition cue:* limits $0$ to $\infty$ with an $e^{-x/\theta}$ factor $\to$ a continuous distribution on $[0,\infty)$. Asked for a normalizing constant $\to$ set $\int f=1$. Endpoint test ($S(0)=1$ vs $F(0)=0$) tells survival from CDF.
:::

## Concept 3 — Integration by Parts, the Tabular Way (B.0.3)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Integration by Parts (tabular)**

Evaluate $\displaystyle\int x^{2}\, e^{-x}\, dx$ (an indefinite integral). If you can produce $-x^2 e^{-x} - 2x e^{-x} - 2e^{-x} + C$ **without** writing out two separate by-hand rounds — by laddering derivatives of $x^2$ against antiderivatives of $e^{-x}$ with alternating signs — **skip to Concept 4**. If "integration by parts" still means slow, error-prone substitution into $\int u\,dv = uv - \int v\,du$ each time, read on: there's a table that does it in one pass.
:::

**The idea.** Integration by parts reverses the **product rule**; when one factor is a **power of $x$** (which differentiates down to zero) and the other is an exponential (which integrates forever), you can lay the whole thing out as a **table** and read the answer off, instead of grinding round after round.

**Concrete instance.** Task: *evaluate $\int x^3 e^{-x/2}\,dx$.* By the textbook formula you would set $u=x^3$, $dv=e^{-x/2}\,dx$, integrate by parts, and be left with $\int x^2 e^{-x/2}\,dx$ — then do it *again*, and *again*, three rounds of bookkeeping with a sign to track each time. The **tabular** method does all three rounds at once.

**Reason it through.** The classic formula is

$$\int u\,dv = uv - \int v\,du \qquad (\textbf{integration by parts, reverses the product rule}).$$

Watch what happens when $u$ is a power: each round **differentiates** $u$ (so $x^3\to 3x^2\to 6x\to 6\to 0$) and **integrates** $dv$ (so $e^{-x/2}\to -2e^{-x/2}\to 4e^{-x/2}\to\cdots$). The signs alternate $+,-,+,-$. Tabular IBP just **records those two ladders side by side** and multiplies along the diagonals:

- Left column $D$: differentiate $x^3$ repeatedly until you hit $0$.
- Right column $I$: integrate $e^{-x/2}$ once for each row.
- Multiply each $D$-entry by the $I$-entry **one row down**, attaching signs $+,-,+,-,\dots$, and add.

$$\int x^3 e^{-x/2}\,dx = -2x^3 e^{-x/2} - 12x^2 e^{-x/2} - 48x\,e^{-x/2} - 96\,e^{-x/2} + C.$$

(Term by term: $+(x^3)(-2e^{-x/2})$; $-(3x^2)(4e^{-x/2})$; $+(6x)(-8e^{-x/2})$; $-(6)(16e^{-x/2})$. The ladder ends because $x^3$'s fourth derivative is $0$.)

**The tempting wrong idea.** Two slips. First, the **sign drift**: forgetting that the diagonal signs alternate, and writing all terms $+$. Anchor the first product as $+$ and strictly alternate. Second, **mis-pairing the rows**: each $D$-entry multiplies the $I$-entry *one row below it*, not the one beside it — the table is read on the **diagonal**, not the row. (Pair $x^3$ with $-2e^{-x/2}$, not with $e^{-x/2}$.)

**Notation, one glyph at a time.** Read the table top to bottom: **"$D$ goes down by differentiating until zero; $I$ goes down by integrating; take diagonal products with alternating signs."** The method works whenever the $D$-column eventually hits $0$ — i.e. whenever $u$ is a polynomial. (If neither factor ever differentiates to zero, fall back to the plain $\int u\,dv = uv - \int v\,du$ formula.)

**Why it matters for us.** Every continuous moment you compute — $E[X]=\int x f$, $E[X^2]=\int x^2 f$ — for an exponential or gamma density is a power-times-exponential integral, exactly this shape. Tabular IBP is the brute-force road to all of them. The *next* concept is the shortcut that skips even this.

**Ramp the difficulty.**

- *Simplest:* $\int x\,e^{-x}\,dx$. $D$: $x, 1, 0$; $I$: $e^{-x}, -e^{-x}, e^{-x}$. Diagonals $+,-$: $-x e^{-x} - e^{-x} + C$.
- *Twist (our integral):* $\int x^3 e^{-x/2}\,dx$, the four-row table above.
- *Definite version:* evaluate $\int_0^\infty x^3 e^{-x/2}\,dx$ by plugging the antiderivative into $[\,\cdot\,]_0^\infty$ — every $x^k e^{-x/2}$ term $\to 0$ at $\infty$ (exponential beats polynomial) and the only survivor at $0$ is the constant term, giving $0 - (-96) = 96$.
- *Edge:* if the non-power factor is $\sin$ or $\cos$ (which never differentiate to zero), the table **cycles** instead of terminating — a different trick. On Exam P the power-times-$e^{-x/\theta}$ case is the one that appears, and it always terminates.

**Picture it.**

<figure>
<img src="../../assets/diagrams/ch08_ibp_tabular.png" alt="A tabular integration-by-parts layout for the integral of x^3 e^{-x/2} dx. Left column D (red boxes): x^3, 3x^2, 6x, 6, 0 — derivatives of x^3. Right column I (blue boxes): e^{-x/2}, -2e^{-x/2}, 4e^{-x/2}, -8e^{-x/2}, 16e^{-x/2} — antiderivatives of e^{-x/2}. Grey diagonal arrows pair each D-row with the I-row one below, labelled with alternating signs +, -, +, -. The assembled answer -2x^3 e^{-x/2} - 12x^2 e^{-x/2} - 48x e^{-x/2} - 96 e^{-x/2} + C is boxed at the bottom." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>Tabular IBP: differentiate the power down to $0$ on the left, integrate the exponential on the right, multiply along the diagonals with alternating signs, and add. Three rounds of by-hand parts become one table.</figcaption>
</figure>

**Consolidate.** You can integrate a power-times-exponential by laddering derivatives against antiderivatives in a table, reading diagonal products with alternating signs — fast and slip-resistant — and evaluate the definite version by killing every term at $\infty$ and keeping the survivor at $0$.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Integration by Parts (Tabular)**

$$\int u\,dv = uv - \int v\,du. \qquad \textbf{Tabular (power $\times$ exp):}$$
$$\text{Column } D:\ \text{differentiate the power to } 0. \quad \text{Column } I:\ \text{integrate the exponential.}$$
$$\text{Answer} = \sum (\pm)\,(D\text{-entry})\times(I\text{-entry one row below}),\ \text{signs } +,-,+,-,\dots$$

*In plain terms:* reverse the product rule. When one factor is a polynomial, lay derivatives against antiderivatives in two columns and read diagonal products with alternating signs — no repeated by-hand rounds.

*Recognition cue:* an integral of a **polynomial times $e^{-x/\theta}$** (or times $e^{ax}$) with no shortcut available $\to$ tabular IBP. The $D$-column terminating at $0$ is what makes the table finite.
:::

## Concept 4 — The Gamma Identity (the Master Ball ⚪)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Gamma Integral**

Evaluate $\displaystyle\int_0^\infty x^{3}\, e^{-x/2}\, dx$ in **one line**, no integration by parts.

If you wrote **$\Gamma(4)\,2^4 = 3!\cdot 16 = 96$** (and you know the power on $x$ is $\alpha-1$, so $\alpha = 4$, **not** $3$), you own the most leveraged tool in the book — **skip to the Worked Examples**. If you reached for integration by parts, or you'd have written $\Gamma(3)\,2^3$, this is the section that saves you the most exam time you will ever save.
:::

**The idea.** Any integral of the shape "a power of $x$ times a decaying exponential, swept from $0$ to $\infty$" equals a gamma function times the scale raised to that power — so you **write the answer** instead of integrating.

**Concrete instance.** Concept 3 left you able to grind $\int_0^\infty x^3 e^{-x/2}\,dx$ out by parts (one table, then evaluate). This concept replaces even the table with one identity. Task: *evaluate $\int_0^\infty x^3 e^{-x/2}\,dx$* — Bill's cold-open integral.

**Reason it through.** There is a special function, $\Gamma(\alpha)$ ("the gamma function"), built to be the value of exactly this kind of integral. The key fact: for whole-number inputs it is just a **factorial**, $\Gamma(n)=(n-1)!$. The identity says the integral equals $\Gamma(\alpha)\,\theta^{\alpha}$, where $\alpha$ is the **power on $x$ plus one**, and $\theta$ is the **scale** in the exponential. In our integral the power on $x$ is $3$, so $\alpha=3+1=4$, and the exponential is $e^{-x/2}$, so $\theta=2$. Therefore

$$\int_0^\infty x^3 e^{-x/2}\,dx = \Gamma(4)\,2^4 = 3!\cdot 16 = 6\cdot 16 = 96.$$

One line. No parts.

**The tempting wrong idea.** The single most punished error is **off-by-one on $\alpha$**. The exponent on $x$ is $\alpha-1$, **not** $\alpha$ — so a power of $3$ means $\alpha=4$, and $\Gamma(4)=3!=6$. The trap is to match the power directly and write $\Gamma(3)\,2^3 = 2\cdot 8 = 16$, wrong by a factor of six. (Team Rocket makes exactly this mistake in a moment, and it costs them.) **Always set $\alpha=(\text{power on }x)+1$ before reaching for the factorial.**

**Notation, one glyph at a time.** The capital Greek **gamma**, $\Gamma$, names the function:

$$\Gamma(\alpha) = \int_0^\infty t^{\alpha-1} e^{-t}\,dt \qquad \text{read: ``gamma of alpha.''}$$

Two facts make it usable without ever evaluating that defining integral:

$$\Gamma(n) = (n-1)! \ \text{ for integer } n, \qquad \Gamma\!\left(\tfrac12\right) = \sqrt{\pi}, \qquad \Gamma(\alpha+1)=\alpha\,\Gamma(\alpha).$$

The letter $\theta$ ("theta") is the **scale**: the number under $x$ in $e^{-x/\theta}$.

**Derive it from the by-parts case.** This is not asserted — it is exactly the tabular IBP of Concept 3, packaged. Start with $\theta=1$ and integer $\alpha=n$. One round of parts on $\int_0^\infty x^n e^{-x}\,dx$ ($u=x^n$, $dv=e^{-x}dx$) gives

$$\int_0^\infty x^n e^{-x}\,dx = \Big[-x^n e^{-x}\Big]_0^\infty + n\int_0^\infty x^{n-1}e^{-x}\,dx = 0 + n\int_0^\infty x^{n-1}e^{-x}\,dx,$$

the boundary term vanishing because exponential beats polynomial (Concept 1). Each round peels off one factor; from the base case $\int_0^\infty e^{-x}\,dx = 1 = 0!$, repeating gives $\int_0^\infty x^n e^{-x}\,dx = n!$. Now restore the scale with $u=x/\theta$ ($x=\theta u$, $dx=\theta\,du$):

$$\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx = \int_0^\infty (\theta u)^{\alpha-1}e^{-u}\,\theta\,du = \theta^{\alpha}\int_0^\infty u^{\alpha-1}e^{-u}\,du = \boxed{\;\Gamma(\alpha)\,\theta^{\alpha}.\;}$$

The Master Ball is just tabular IBP, done in general and packaged, with the scale pulled out by a substitution.

**Ramp the difficulty.**

- *Simplest:* $\int_0^\infty x^3 e^{-x/2}\,dx = \Gamma(4)\,2^4 = 96$.
- *Normalizing constant:* find $c$ for $f(x)=c\,x\,e^{-x/3}$. Here $\int_0^\infty x\,e^{-x/3}\,dx = \Gamma(2)\,3^2 = 1!\cdot 9 = 9$, so $c=\tfrac19$.
- *Expectation:* $E[X]$ multiplies the density by an extra $x$, *raising the power by one*. For $f(x)=\tfrac19 x e^{-x/3}$, $E[X]=\tfrac19\int_0^\infty x^2 e^{-x/3}\,dx = \tfrac19\,\Gamma(3)\,3^3 = \tfrac19\cdot 2\cdot 27 = 6$.
- *Half-integer edge:* when $\alpha$ is a half-integer, use $\Gamma(\tfrac12)=\sqrt\pi$ and the step-down $\Gamma(\alpha+1)=\alpha\,\Gamma(\alpha)$ — e.g. $\Gamma(\tfrac32)=\tfrac12\Gamma(\tfrac12)=\tfrac{\sqrt\pi}{2}$. (This is the normal distribution's hidden normalizer.)

**Picture it.**

<figure>
<img src="../../assets/diagrams/ch08_gamma_integral.png" alt="The gamma integrand x^{alpha-1} e^{-x} plotted for alpha = 1, 2, 3, 4, each a different color and hatch, with the total shaded area under each curve labelled Gamma(alpha) = (alpha-1)!: areas 1, 1, 2, 6 respectively. The boxed identity integral from 0 to infinity of x^{alpha-1} e^{-x/theta} dx = Gamma(alpha) theta^alpha sits in the upper region. The real Master Ball item sprite is composited in the clear lower-right margin." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>The gamma integrand for several $\alpha$. The entire area under each curve is a factorial — no integration by parts required. The Master Ball catches <em>any</em> power-times-exponential integral on $[0,\infty)$ in one throw.</figcaption>
</figure>

**Consolidate.** The instant you see $\int_0^\infty x^{\text{power}} e^{-x/\theta}\,dx$, you now **stop**, read $\alpha=(\text{power})+1$ and $\theta$ off the page, and write $\Gamma(\alpha)\,\theta^\alpha = (\alpha-1)!\,\theta^\alpha$. This one move normalizes densities, computes means and second moments, and short-circuits half the integrals in the rest of the book.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Gamma Integral Identity (the Master Ball ⚪)**

$$\boxed{\int_0^{\infty} x^{\alpha-1} e^{-x/\theta}\, dx = \Gamma(\alpha)\,\theta^{\alpha}}$$
$$\Gamma(n) = (n-1)!\ (\text{integer } n), \qquad \Gamma\!\left(\tfrac12\right) = \sqrt{\pi}, \qquad \Gamma(\alpha+1) = \alpha\,\Gamma(\alpha).$$
$$\text{Special case } (\theta = 1): \quad \int_0^\infty x^n e^{-x}\,dx = n!.$$

*In plain terms:* power-of-$x$ times decaying-exponential over $[0,\infty)$ equals a gamma (a factorial, for whole numbers) times the scale to that power. You never integrate it by hand.

*Recognition cue:* the instant you see $\int_0^\infty x^{\text{power}} e^{-x/\theta}\,dx$, **stop** — don't do parts. Set $\alpha = (\text{power on } x) + 1$, read $\theta$ off the exponential, write $\Gamma(\alpha)\,\theta^{\alpha}$. **The trap is off-by-one on $\alpha$.**
:::

## Worked Examples — Faded Guidance

Three examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why* — the labor you're avoiding) before the **Trainer's Path** (the fast *how*), because the gamma shortcut is the load-bearing instrument of the chapter.

### Worked Example 1 — Bill's Lighthouse Integral (full narration; understanding-first)

**ARCHETYPE:** *gamma-integral evaluation (power $\times$ decaying exponential over $[0,\infty)$).*

**Setup.** Bill's monitor shows his "expected lifetime activity" integral,
$$I = \int_0^\infty x^{3}\,e^{-x/2}\,dx.$$
The door stays locked until you evaluate it in one line.

**Step 1 — Identify (which archetype, and read off the parameters).** This is $\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx$ — the gamma shape. Match the pattern: the power on $x$ is $3$, so $\alpha-1=3\Rightarrow\alpha=4$; the exponential scale is $\theta=2$.

**Step 2 — Trainer's Path (the fast how).** Apply the identity directly:
$$I = \Gamma(4)\,\theta^4 = 3!\cdot 2^4 = 6\cdot 16 = 96.$$
Done — about fifteen seconds.

**Step 3 — Professor's Path (the labor you avoided).** By tabular IBP (Concept 3), $\int x^3 e^{-x/2}\,dx = -2x^3 e^{-x/2} - 12x^2 e^{-x/2} - 48x e^{-x/2} - 96 e^{-x/2} + C$. Evaluate $[\,\cdot\,]_0^\infty$: every $x^k e^{-x/2}$ term dies at $\infty$ (exponential beats polynomial) and at $0$ only the constant term survives, giving $0 - (-96) = 96$. Same answer, the long way.

**Step 4 — Check & pitfall.** $\alpha=4$ is a positive integer, so $\Gamma(4)=3!=6$ — **not** $4!$. **The trap is off-by-one on $\alpha$:** the exponent on $x$ is $\alpha-1$, so $\alpha$ is one *more* than the power you see. Sanity: the answer is positive (an integrated activity), as it must be. *(Back-ref: Entries №03, №04.)*

### Worked Example 2 — Normalizing Bill's Encounter Model (partial guidance)

**ARCHETYPE:** *normalizing constant via the gamma identity.*

**Setup.** Bill models encounter intensity by $f(x)=c\,x\,e^{-x/3}$ for $x>0$. Find the $c$ that makes it a valid density.

**Identify.** A valid density integrates to $1$: $\int_0^\infty c\,x\,e^{-x/3}\,dx = 1$. The integral is gamma-shaped, power $1$ on $x$ (so $\alpha=2$), scale $\theta=3$. *Your move: evaluate the integral, then solve for $c$.*

$$\int_0^\infty x\,e^{-x/3}\,dx = \Gamma(2)\,3^2 = 1!\cdot 9 = 9 \quad\Longrightarrow\quad 9c=1 \quad\Longrightarrow\quad c=\tfrac19.$$

**Check & pitfall.** $\Gamma(2)=1!=1$, easy to misread as $2!$. With $c=\tfrac19$, $f\ge 0$ on its support and integrates to $1$ — a valid density. *(Back-ref: Entries №02, №04.)*

### Worked Example 3 — A Survival Tail and a Mode (light guidance)

**ARCHETYPE:** *improper-integral survival tail + mode by optimization.*

**Setup.** A fainted Pokémon's remaining recovery time has density $f(t)=\tfrac15 e^{-t/5}$ for $t>0$. (a) Find the survival $S(t)=P(T>t)$ as a clean formula and confirm $S(0)=1$. (b) Separately, find the mode of $g(x)=\tfrac14 x e^{-x/2}$.

**(a)** Survival is the tail integral:
$$S(t)=\int_t^\infty \tfrac15 e^{-u/5}\,du = \big[-e^{-u/5}\big]_t^\infty = 0-\big(-e^{-t/5}\big) = e^{-t/5}, \qquad S(0)=e^0=1.\ \checkmark$$

**(b)** Set $g'=0$: $g'(x)=\tfrac14 e^{-x/2}(1-\tfrac{x}{2})$, zero only when $1-\tfrac x2=0$, so **mode $=2$** (sign of $g'$ flips $+\to-$, a maximum).

**Check & pitfall.** $S(0)=1$ and $S$ decreasing — a survival, not a CDF. **The trap:** writing $S(t)=1-e^{-t/5}$, which is the *CDF* $F(t)$; survival is $1-F$, so always confirm $S(0)=1$, $S(\infty)=0$. *(Back-ref: Entries №01, №02.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — read $\alpha$ off the page**

For any $\int_0^\infty x^{p}e^{-x/\theta}\,dx$: the power $p$ is $\alpha-1$, so $\alpha=p+1$ and the answer is $\Gamma(p+1)\,\theta^{p+1}=p!\,\theta^{p+1}$ for integer $p$. Train yourself to write the answer *before* you'd have finished the first integration by parts. This single reflex saves more exam minutes than any other in the book.
:::

::: trainers-tip
**TRAINER'S TIP — survival vs. CDF, every time**

After integrating a tail, sanity-check the endpoints. A **survival** has $S(0)=1$, $S(\infty)=0$; a **CDF** has $F(0)=0$, $F(\infty)=1$. If your formula fails the endpoint test, you computed the *other* one — subtract from $1$.
:::

::: trainers-tip
**TRAINER'S TIP — calculator factorials on the TI-30XS**

Compute $\Gamma(n)=(n-1)!$ with the factorial key: type the number, then [math]{.kbd} → [!]{.keystroke}. Store $\sqrt\pi\approx 1.7725$ (for $\Gamma(\tfrac12)$) with [STO▸]{.kbd} so you never re-key it. Clearing memory before the exam is mandatory — do it at the Prometric desk.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:135px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Team Rocket, cracking Bill's integral to power a twerp-detector</figcaption>
</figure>

Jessie, James, and Meowth have tapped Bill's monitor and are trying to crack his energy integral $\int_0^\infty x^3 e^{-x/2}\,dx$ to power their balloon's twerp-detector.

"Easy!" crows Meowth. "Da power on $x$ is $3$, da scale is $2$ — so it's $\Gamma(3)\cdot 2^{3} = 2\cdot 8 = 16$!"

"Sixteen units of twerp-tracking power!" cheers James, flipping the switch. The detector glows feebly, points at a passing Magikarp, and sputters out.

The *correct* value was $96$ — they were off by a **factor of six**, and their underpowered gadget couldn't find a twerp standing next door. "Looks like Team Rocket's *underestimating* again!"

**Where it fails:** Meowth set $\alpha$ equal to the power on $x$. But the exponent on $x$ is $\alpha-1$, **not** $\alpha$ — so a power of $3$ means $\alpha=4$, and $\Gamma(4)=3!=6$, giving $6\cdot 16 = 96$. **Always set $\alpha=(\text{power on }x)+1$ before reaching for the factorial.** This is the exact off-by-one trap from Concept 4 — and the most-punished gamma-integral error on the exam.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal arithmetic of **pricing insurance.**

Actuaries integrate loss densities every single day. When a claim's severity is modeled as exponential or gamma — the two most common loss models in property-casualty work — computing the **expected claim**, the **expected payment above a deductible**, or a **limited expected value** *is* a gamma integral. A pricing actuary who recognizes $\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx = \Gamma(\alpha)\,\theta^\alpha$ on sight prices a policy in seconds; one who grinds it out by parts wastes billable hours and risks an arithmetic slip on a quote a client is waiting for. Differentiation matters just as much: the **mode** of a fitted loss curve is found by setting $f'=0$, and the limit "exponential beats polynomial" is the reason expected losses for these models are even finite.

*Series bridge:* this gamma shortcut and the loss-integration setup return in force on **CAS Exam 5 (Basic Ratemaking)** and the loss-models portion of **Exam FAM/ALTAM**; the improper-integral-as-tail idea underlies survival models throughout **Exam FAM** and the long-term-actuarial track.

*Transfer check:* could you solve this with **no Pokémon in it**? "A loss $X$ has density $f(x)=\tfrac19 x\,e^{-x/3}$ on $x>0$; find $E[X]$." Same gamma identity, answer $6$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Bill's Door (the HM Practical)

There is no gym leader here and no badge to win — only Bill, watching through the camera, and a single fused problem standing between you and the door.

**Bill's Challenge.** "One problem," Bill says, "that uses every instrument at once. Solve it and the door opens; you cross into the continuous wilds carrying the HM." A wild Pokémon's *replacement value* is modeled by the density
$$f(x) = \tfrac14\,x\,e^{-x/2}, \qquad x>0.$$
Three tasks, one breath each:
**(a)** Confirm $f$ is a valid density (integrates to $1$).
**(b)** Find the **mode** of $f$ (the most likely value).
**(c)** Compute $E[X]=\int_0^\infty x\,f(x)\,dx$.

**ARCHETYPE:** *integrative — gamma normalization + mode by optimization + gamma expectation.*

**Step 1 — Identify.** (a) and (c) are gamma-identity evaluations; (b) is an optimization (set $f'=0$).

**Step 2 — Trainer's Path.**

**(a)** Power on $x$ is $1$ ($\alpha=2$), scale $\theta=2$:
$$\int_0^\infty \tfrac14 x\,e^{-x/2}\,dx = \tfrac14\,\Gamma(2)\,2^2 = \tfrac14\cdot 1\cdot 4 = 1.\ \checkmark$$
Valid density.

**(b)** $f'(x) = \tfrac14 e^{-x/2}(1-\tfrac x2)$, zero only when $1-\tfrac x2=0$, so the **mode is $x=2$** (the sign of $f'$ flips $+\to-$).

**(c)** The integrand $x\cdot f(x)=\tfrac14 x^2 e^{-x/2}$ has power $2$ on $x$, so $\alpha=3$, $\theta=2$:
$$E[X] = \int_0^\infty \tfrac14 x^2 e^{-x/2}\,dx = \tfrac14\,\Gamma(3)\,2^3 = \tfrac14\cdot 2\cdot 8 = 4.$$

**Step 3 — Professor's Path (the cross-check).** This $f$ is the $\mathrm{Gamma}(\alpha=2,\theta=2)$ density you will meet by name in ch11. Its mean is $\alpha\theta = 2\cdot 2 = 4$ — matching (c) exactly — and its mode is $(\alpha-1)\theta = 1\cdot 2 = 2$, matching (b). The mean ($4$) sits to the *right* of the mode ($2$), as it must for a right-skewed density. Every piece agrees.

**Step 4 — Check & pitfall.** $E[X]=4=\alpha\theta$ is a clean cross-check; the mode $<$ mean ordering confirms the skew. The capstone trap is the gamma off-by-one in (a)/(c): read $\alpha=(\text{power})+1$, not the power itself.

> "That," Bill says, and the lock clicks open, "is wielding the instruments. The wilds past my door are continuous — but you read them now. Go."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~4 min/problem; faster on Route Trainers), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C8.1.** 🔴 *Lighthouse steps, dusk.* Evaluate a Caterpie's foraging integral $\displaystyle\int_0^\infty x^{2}e^{-x}\,dx$.

**C8.2.** 🟡 *Bill's monitor.* To normalize the encounter model, evaluate $\displaystyle\int_0^\infty x^{4}e^{-x/3}\,dx$.

**C8.3.** 🔴 *Calibrating intensity.* Find the constant $c$ making $f(x)=c\,e^{-x/7}$ ($x>0$) a valid density, and write its survival $S(t)$.

**C8.4.** 🔴 *Reading a peak.* A wild Pokémon's encounter density is $f(x)=\tfrac14 x\,e^{-x/2}$ ($x>0$). Find the *most likely* value (the mode) by optimization.

**C8.5.** 🟡 *Tail check.* Compute the survival probability $S(t)=\displaystyle\int_t^\infty \tfrac14 e^{-u/4}\,du$ as a formula in $t$, and state $S(0)$.

**C8.6.** 🟡 *Spot the inside function.* Evaluate $\displaystyle\int_0^1 y^2 e^{y^3}\,dy$ by $u$-substitution.

### Gym Battles (true exam difficulty)

**C8.7.** 🟡 *Bill's lighthouse integral.* For $\displaystyle\int_0^\infty x^{3}e^{-x/\theta}\,dx$ with scale $\theta=2$, evaluate the integral.

**C8.8.** 🔴 *Catch the Rocket slip (audit).* Team Rocket evaluates $\displaystyle\int_0^\infty x^{3}e^{-x/2}\,dx$ as "$\Gamma(3)\cdot 2^3 = 16$." Give the correct value and name the error.

**C8.9.** 🟡 *Expected value of a gamma shape.* For $f(x)=\tfrac19 x\,e^{-x/3}$ ($x>0$), compute $E[X]=\displaystyle\int_0^\infty x f(x)\,dx$.

**C8.10.** 🟡 *Catch the sloppy log (audit).* A field log claims $\displaystyle\int_0^\infty x^{2}e^{-x/5}\,dx = \Gamma(3)\cdot 5^{2} = 50$. Find the true value and name the slip.

**C8.11.** 🟡 *Tabular by parts.* Use tabular integration by parts to find the indefinite integral $\displaystyle\int x^{2}e^{-x}\,dx$.

**C8.12.** 🟡 *Exponential beats polynomial.* Evaluate $\displaystyle\lim_{x\to\infty} x^{2}e^{-x/3}$, and explain in one line why a tail of this shape integrates to a finite value.

**C8.13.** 🔵 *Gary's variance grab (rival-trap).* For the exponential $f(x)=\tfrac12 e^{-x/2}$ ($x>0$, mean $2$), Gary claims $E[X^2]=(E[X])^2=4$. Compute the true $E[X^2]=\int_0^\infty x^2 f(x)\,dx$ via the gamma identity, then $\mathrm{Var}(X)=E[X^2]-(E[X])^2$, and name Gary's error.

**C8.14.** 🔵 *Gary's normalizing shortcut (rival-trap, decision).* Gary insists the density $f(x)=c\,x^{2}e^{-x/2}$ ($x>0$) "must have $c=\tfrac12$ because that's the exponential constant." **Decide** whether he is right: find the true $c$, and state which integral identity settles it.

### Elite Challenge (integrative / stretch)

**C8.15.** 🔵 *Bill's dawn capstone.* For $f(x)=\tfrac{1}{2\theta^{3}}x^{2}e^{-x/\theta}$ ($x>0$, a $\mathrm{Gamma}(3,\theta)$): (a) verify it integrates to $1$; (b) show $E[X]=3\theta$; (c) show $E[X^2]=12\theta^2$ and hence $\mathrm{Var}(X)=3\theta^2$. Keep $\theta$ symbolic.

**C8.16.** 🔵 *Half-integer Master Ball.* Using $x=u^2$ ($dx=2u\,du$) and the known fact $\int_0^\infty e^{-u^2}\,du=\tfrac{\sqrt\pi}{2}$, show that $\Gamma(\tfrac12)=\int_0^\infty x^{-1/2}e^{-x}\,dx=\sqrt\pi$.

**C8.17.** 🔵 *Shortcut or grind? (decision).* You must evaluate $\displaystyle\int_0^\infty x^{3}e^{-x/4}\,dx$ on the clock. **Decide** between tabular integration by parts and the gamma identity, then give the value and justify the choice.

**C8.18.** 🔵 *Catch the survival/cdf swap (audit).* A solver integrates a density's tail and writes "$F(t)=e^{-t/5}$" for the cdf of an $\mathrm{Exp}(5)$. Use the endpoint test to decide whether that is the cdf, and give the correct cdf.
:::

## Answers

### Quick-Answer Table

| # | Answer | Archetype |
|---|---|---|
| C8.1 | $2$ | gamma evaluation |
| C8.2 | $5832$ | gamma evaluation |
| C8.3 | $c=\tfrac17$, $S(t)=e^{-t/7}$ | normalize + survival |
| C8.4 | mode $=2$ | mode by optimization |
| C8.5 | $S(t)=e^{-t/4}$, $S(0)=1$ | survival tail |
| C8.6 | $\tfrac13(e-1)\approx 0.573$ | $u$-substitution |
| C8.7 | $96$ | gamma evaluation |
| C8.8 | $96$ (off-by-one on $\alpha$) | audit |
| C8.9 | $6$ | gamma expectation |
| C8.10 | $250$ (forgot scale power) | audit |
| C8.11 | $-x^2 e^{-x}-2x e^{-x}-2e^{-x}+C$ | tabular IBP |
| C8.12 | $0$ | limit |
| C8.13 | $E[X^2]=8$, $\mathrm{Var}=4$ | rival-trap |
| C8.14 | $c=\tfrac{1}{16}$ (Gary wrong) | rival-trap / decision |
| C8.15 | $3\theta,\ 12\theta^2,\ 3\theta^2$ | integrative |
| C8.16 | $\sqrt\pi$ | half-integer gamma |
| C8.17 | $1536$; use the gamma identity | decision |
| C8.18 | $e^{-t/5}$ is survival; $F(t)=1-e^{-t/5}$ | audit |

**C8.1** — *Gamma evaluation (Entry №04).* Power on $x$ is $2\Rightarrow\alpha=3$, scale $\theta=1$: $\int_0^\infty x^2 e^{-x}\,dx = \Gamma(3)\,1^3 = 2! = 2.$

**C8.2** — *Gamma evaluation with scale (Entry №04).* Power $4\Rightarrow\alpha=5$, $\theta=3$: $\int_0^\infty x^4 e^{-x/3}\,dx = \Gamma(5)\,3^5 = 4!\cdot 243 = 24\cdot 243 = 5832.$

**C8.3** — *Normalize + survival (Entries №02, №04).* $\int_0^\infty c\,e^{-x/7}\,dx = c\cdot 7 = 1 \Rightarrow c=\tfrac17$ (here $\alpha=1$, $\theta=7$, $\Gamma(1)=1$). Survival: $S(t)=\int_t^\infty \tfrac17 e^{-u/7}\,du = e^{-t/7}$, with $S(0)=1$.

**C8.4** — *Mode by optimization (Entry №01).* $f(x)=\tfrac14 x e^{-x/2}$. Product + chain rule: $f'(x)=\tfrac14 e^{-x/2}(1-\tfrac x2)$. Since $e^{-x/2}>0$, need $1-\tfrac x2=0\Rightarrow x=2$. Sign of $f'$ runs $+\to-$, a max. **Mode $=2$.**

**C8.5** — *Survival tail (Entry №02).* $S(t)=\int_t^\infty \tfrac14 e^{-u/4}\,du = \big[-e^{-u/4}\big]_t^\infty = e^{-t/4}$, and $S(0)=e^0=1$.

**C8.6** — *$u$-substitution (Entry №02).* Inside function $y^3$, $du=3y^2\,dy$: $\int_0^1 y^2 e^{y^3}\,dy = \tfrac13\int_0^1 e^u\,du = \tfrac13(e-1)\approx 0.573.$

**C8.7** — *Gamma evaluation, off-by-one $\alpha$ (Entry №04).* Power $3\Rightarrow\alpha=4$, $\theta=2$: $\int_0^\infty x^3 e^{-x/2}\,dx = \Gamma(4)\,2^4 = 3!\cdot 16 = 96.$ (Same as WE 1 and Bill's integral.)

**C8.8** — *Audit: off-by-one on $\alpha$ (Entry №04, Team Rocket trap).* The exponent on $x$ is $\alpha-1$, so a power of $3$ gives $\alpha=4$, not $3$. Correct value $\Gamma(4)\,2^3$? — no: with $\theta=2$, $\Gamma(4)\,2^4 = 6\cdot 16 = 96$. Team Rocket used $\Gamma(3)\,2^3=16$, off by a factor of six. **True value $96$.**

**C8.9** — *Gamma expectation (Entry №04).* $E[X]=\int_0^\infty x\cdot\tfrac19 x e^{-x/3}\,dx = \tfrac19\int_0^\infty x^2 e^{-x/3}\,dx = \tfrac19\,\Gamma(3)\,3^3 = \tfrac19\cdot 2\cdot 27 = 6.$ (Cross-check: gamma mean $\alpha\theta=2\cdot 3=6$.)

**C8.10** — *Audit: scale power (Entry №04).* Power $2\Rightarrow\alpha=3$, scale $\theta=5$. The identity gives $\Gamma(3)\,\theta^{\alpha}=\Gamma(3)\,5^{3}=2\cdot 125=250$ — the log used $5^{2}$ (the power on $x$) instead of $5^{\alpha}=5^{3}$ for the scale exponent. **True value $250$.**

**C8.11** — *Tabular IBP (Entry №03).* $D$: $x^2, 2x, 2, 0$; $I$: $e^{-x}, -e^{-x}, e^{-x}, -e^{-x}$. Diagonal products with signs $+,-,+$: $+(x^2)(-e^{-x}) - (2x)(e^{-x}) + (2)(-e^{-x}) = -x^2 e^{-x} - 2x e^{-x} - 2e^{-x} + C.$ (Check: differentiate to recover $x^2 e^{-x}$.)

**C8.12** — *Exponential-beats-polynomial limit (Entry №01).* $\tfrac{x^2}{e^{x/3}}$ is $\tfrac{\infty}{\infty}$. Two L'Hôpital passes: $\to\tfrac{2x}{\frac13 e^{x/3}}\to\tfrac{2}{\frac19 e^{x/3}}\to 0$. Because the integrand decays faster than any polynomial grows, its tail area $\int_b^\infty$ vanishes as $b\to\infty$, so the total integral is finite. **Limit $=0$.**

**C8.13** — *Rival-trap: $E[X^2]\ne(E[X])^2$ (Entry №04).* Gary equated the second moment with the squared mean, which would force the variance to zero. Truth: $E[X^2]=\int_0^\infty x^2\cdot\tfrac12 e^{-x/2}\,dx = \tfrac12\,\Gamma(3)\,2^3 = \tfrac12\cdot 2\cdot 8 = 8.$ Then $\mathrm{Var}(X)=8-2^2=4$ (matching $\theta^2=4$ for an exponential). **$E[X^2]=8$, $\mathrm{Var}(X)=4$; Gary forgot the $+\mathrm{Var}$ term in $E[X^2]=\mathrm{Var}+(E[X])^2$.**

**C8.14** — *Rival-trap / decision (Entry №04).* Gary is **wrong**. The normalizing constant is *not* a fixed number — it depends on the kernel. The settling identity is the Master Ball: $\int_0^\infty x^2 e^{-x/2}\,dx = \Gamma(3)\,2^3 = 2\cdot 8 = 16$, so $c=\tfrac{1}{16}$ — not $\tfrac12$. (This is the $\mathrm{Gamma}(3,2)$ density.) **Decision: do not trust a "remembered" constant; evaluate the kernel integral. $c=\tfrac{1}{16}$.**

**C8.15** — *Integrative symbolic gamma (Entry №04).*
(a) $\int_0^\infty \tfrac{1}{2\theta^3}x^2 e^{-x/\theta}\,dx = \tfrac{1}{2\theta^3}\Gamma(3)\theta^3 = \tfrac{1}{2\theta^3}\cdot 2\cdot\theta^3 = 1.\ \checkmark$
(b) $E[X]=\tfrac{1}{2\theta^3}\int_0^\infty x^3 e^{-x/\theta}\,dx = \tfrac{1}{2\theta^3}\Gamma(4)\theta^4 = \tfrac{1}{2\theta^3}\cdot 6\cdot\theta^4 = 3\theta.$
(c) $E[X^2]=\tfrac{1}{2\theta^3}\Gamma(5)\theta^5 = \tfrac{1}{2\theta^3}\cdot 24\cdot\theta^5 = 12\theta^2$, so $\mathrm{Var}=12\theta^2-(3\theta)^2=3\theta^2.$ (These are the $\mathrm{Gamma}(3,\theta)$ mean $\alpha\theta$ and variance $\alpha\theta^2$.)

**C8.16** — *Half-integer gamma via substitution (Entry №04).* By definition $\Gamma(\tfrac12)=\int_0^\infty x^{-1/2}e^{-x}\,dx$. Substitute $x=u^2$, $dx=2u\,du$, $x^{-1/2}=u^{-1}$ (limits stay $0\to\infty$): $\Gamma(\tfrac12)=\int_0^\infty u^{-1}e^{-u^2}(2u\,du)=2\int_0^\infty e^{-u^2}\,du=2\cdot\tfrac{\sqrt\pi}{2}=\sqrt\pi.$

**C8.17** — *Decision: shortcut over grind (Entry №04).* The integrand is power-times-decaying-exponential over $[0,\infty)$ — **fire the Master Ball.** Power $3\Rightarrow\alpha=4$, $\theta=4$: $\int_0^\infty x^3 e^{-x/4}\,dx = \Gamma(4)\,4^4 = 6\cdot 256 = 1536.$ Tabular IBP would need four rows then a limit evaluation — same answer, far more time and slip risk. **Decision: use the gamma identity.**

**C8.18** — *Audit: survival vs. cdf endpoint test (Entry №02).* A cdf must satisfy $F(0)=0$ and $F(\infty)=1$. But $e^{-0/5}=1$, not $0$ — so $e^{-t/5}$ is the **survival** $S(t)$, not the cdf. The true cdf is $F(t)=1-S(t)=1-e^{-t/5}$ (giving $F(0)=0$, $F(\infty)=1$). The solver swapped survival for the cdf.

## Badge Earned — the HM "Calculus"

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map — Bill's lighthouse now passed, the path to the continuous wilds open to the south." style="width:60%; max-width:380px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>HM Acquired (not a badge) — Bill's Lighthouse cleared → the continuous wilds open!</strong></figcaption>
</figure>

There is no badge here — but you walk out with the **HM: Calculus**, and you do not put it down again. You clear the lighthouse when you can, unaided:

1. **Differentiate** products and compositions, **find a mode** by setting $f'=0$, and **resolve $\tfrac00$ / $\tfrac{\infty}{\infty}$ limits** via L'Hôpital / exponential-beats-polynomial. *(Prereq — TIA B.0.1.)*
2. **Integrate over $[0,\infty)$**, use **$u$-substitution**, **find a normalizing constant** by forcing $\int f=1$, and **distinguish survival from CDF** by the endpoint test ($S(0)=1$ vs $F(0)=0$). *(Prereq — TIA B.0.2.)*
3. **Integrate by parts, tabular-style** — differentiate the power to $0$, integrate the exponential, diagonal products with alternating signs. *(Prereq — TIA B.0.3.)*
4. **Evaluate any gamma integral on sight** — $\int_0^\infty x^{p}e^{-x/\theta}\,dx = \Gamma(p+1)\,\theta^{p+1}=p!\,\theta^{p+1}$ with $\alpha=p+1$ (no off-by-one). *(Prereq — the Master Ball.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 $\to$ re-read Concept 1 + C8.4 / C8.12. Miss item 2 $\to$ Concept 2 + WE 3 / C8.3, C8.5, C8.6. Miss item 3 $\to$ Concept 3 + C8.11. Miss item 4 $\to$ rebuild Concept 4, WE 1, and the Team Rocket trap, then retry C8.7, C8.8, C8.15.

*Onward — through Bill's door and into **the continuous wilds**, where the first smooth density is waiting and the area under the curve is, at last, a probability you can read.*
