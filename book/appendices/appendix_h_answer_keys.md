<!--
  file: appendix_h_answer_keys
  kind: appendix
  letter: H
  title: Answer Index — every problem's final answer, on one page per chapter
  purpose: a consolidated quick-answer index for fast self-checking; one scannable table per chapter listing problem id, final answer, archetype, and SOA outcome(s); full step-by-step solutions live in each chapter's own "## Answers" section, so nothing is duplicated; every answer here is machine-verified by the seed-151 harness (sims/verify_examples.py)
  sources: problems/bank.d/ch00.yaml … ch19.yaml (generated index), syllabus/outcomes.yaml (outcome codes)
  plan: MASTER_PLAN_V3 §23 (appendix spec), §28 (problem-bank schema)
-->

# Appendix H — The Answer Index {.type-normal}

> **What this is.** A single consolidated **answer index** for the whole problem bank — all **450** problems across ch00–ch19, one table per chapter. Each row gives you four things: the **problem id** (e.g. `C3.14`, `M2.17`), its **final answer**, its **archetype**, and the **SOA outcome(s)** it discharges. Use it to *self-check fast*: work a problem on paper, then scan down to its row and confirm the final number. Nothing more.
>
> **Where the full solutions live.** This index deliberately carries **no worked steps**. Every chapter already prints its own complete, step-by-step solutions in its **"## Answers"** section — re-deriving each result from scratch, with the shortcut used and the trap (if any) called out. Reproducing ~450 solutions here would bloat the book and invite drift between two copies of the same work. So when a row tells you *what* the answer is and you need *why*, turn back to that chapter's **## Answers**. Think of this appendix as the back-of-the-envelope key; the chapter is the worked solution manual.
>
> **Machine-verified.** Every answer in every row below is checked by the **seed-151 verification harness** (`sims/verify_examples.py`): each problem in the bank ships a self-contained Python predicate that recomputes its result and asserts it matches the printed answer. If a row here disagreed with the harness, the build would have failed. So you can trust these final values as ground truth — if your paper answer differs, the error is yours to find (which is exactly the point).

---

## H.0 How to read a row {.unnumbered}

Each chapter heading shows the Kanto leg it covers and its problem count. Within a table:

- **Problem** — the bank id. `C{n}.{k}` ids belong to chapter *n* (e.g. `C12.3`); `Q7.*` are Checkpoint A's review set; `M1.*` / `M2.*` / `M3.*` are the three mock exams in ch19 (Mock A / B / C). Rows follow the chapter's own running order, so they line up one-for-one with that chapter's **## Answers**.
- **Final answer** — the value(s) you should land on. Multi-part problems list each part, semicolon-separated. For the ch19 mocks the answer is the **lettered option plus its value** (e.g. `C (0.40)`), matching the five-option exam format.
- **Archetype** — how the problem is built. For ch00–ch18: **standard** (a clean drill), **audit** (spot the planted error in someone's work — 55 of these), **rival_trap** (Gary/Team Rocket states a plausible-but-wrong result you must refute — 34), or **decision** (compute, then *choose* an action — 27). For ch19 the column instead shows the SOA **topic** the question is weighted into (`topic1` General, `topic2` Univariate, `topic3` Multivariate), since the mocks carry topic tags rather than narrative archetypes.
- **Outcome(s)** — the SOA Exam P learning-outcome code(s) the problem discharges (`1a`…`3i`, per `syllabus/outcomes.yaml`). Calculus-prerequisite drills (ch08, and ch00's primer) are tagged `prereq` — they underwrite Topic 2/3 without mapping to a graded outcome.

**Readiness reminder.** By the time the index is a *checking* tool rather than a *learning* one, you should be getting these right under **6-minute pacing** — the SOA's ~180 minutes / 30 questions budget. If you can scan a row, recognize the archetype, and confirm your answer in seconds, you are ready. If you are still looking up *why*, you are revising, not rehearsing — and that is fine, but it is a different mode. Treat a clean run down a chapter's column under the clock as your green light.

---

## H.1 The index, chapter by chapter {.unnumbered}

### ch00 — Orientation {.unnumbered}

*Pallet Town. 4 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C0.1 | 0.135 | standard | prereq |
| C0.2 | 14 | audit | prereq |
| C0.3 | 0.375 | standard | prereq |
| C0.4 | 0.5 | standard | prereq |

### ch01 — Fundamentals of Probability {.unnumbered}

*Route 1. 22 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C1.1 | 0.9 | standard | 1a |
| C1.2 | 0.45 | standard | 1a |
| C1.3 | 0.60; mutually exclusive, NOT independent | standard | 1d, 1e |
| C1.4 | 0.20; 0.70 | standard | 1e |
| C1.5 | 0.4, 0.3, 0.2, 0.1 (sum 1.0) | standard | 1a, 1e |
| C1.6 | 0.875 | standard | 1e |
| C1.7 | 0.28 | standard | 1a, 1e |
| C1.8 | P(A and B)=0.25; NOT independent (0.25 != 0.20) | audit | 1d, 1e |
| C1.9 | 0.85; 0.60; 0.15 | standard | 1e |
| C1.10 | 0.80; none 0.20 | standard | 1e |
| C1.11 | p = 0.10; exactly one 0.90 | standard | 1e |
| C1.12 | 0.17; 0.3111 | standard | 1d, 1e |
| C1.13 | P(T or L) in [0.40, 0.75]; P(T and L) in [0, 0.35] | standard | 1e |
| C1.14 | 0.25; 0.70 | standard | 1e |
| C1.15 | 0.2 = 0.2 -> independent; Gary wrong | rival_trap | 1d, 1e |
| C1.16 | 0.95; none 0.05 | standard | 1e |
| C1.17 | (a) 1.0; (b) no; (c) multiplied disjoint events; misread union as a guarantee | audit | 1d, 1e |
| C1.18 | q = 0.70; none ~= 5.3e-7; pure-F 0.13 | standard | 1e |
| C1.19 | (a) 0.3; (b) independent; (c) impossible (would need 1.1 > 1) | standard | 1d, 1e |
| C1.20 | A ~= 0.0687; B 0.85 -> stand | decision | 1e |
| C1.21 | P(nothing) = 0.10; Meowth dropped the 'nothing' outcome (masses summed to 0.90) | audit | 1a |
| C1.22 | 0.57; Gary double-counted the 0.18 overlap | rival_trap | 1e |

### ch02 — Conditional Probability & Bayes {.unnumbered}

*Viridian -> Cerulean. 26 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C2.1 | 0.4 | standard | 1c |
| C2.2 | 0.5 | standard | 1c |
| C2.3 | 0.98 | standard | 1e |
| C2.4 | 0.46 | standard | 1e |
| C2.5 | 0.185 | standard | 1f |
| C2.6 | 0.0137 | standard | 1g |
| C2.7 | 0.3 | standard | 1c |
| C2.8 | P(A and B)=0.25; NOT independent (0.25 != 0.20) | audit | 1e |
| C2.22 | both 0.45; at least one 0.90 | decision | 1e |
| C2.9 | 0.39 | standard | 1f, 1g |
| C2.10 | 0.0732 | audit | 1g |
| C2.11 | 0.533 | standard | 1c, 1e |
| C2.12 | 0.14 | standard | 1e |
| C2.13 | 0.514 | rival_trap | 1f, 1g |
| C2.14 | 0.1106 | standard | 1g |
| C2.15 | 1.0 | standard | 1g |
| C2.16 | P(A\|B)=0.4286; P(A\|B^c)=0.1765 | standard | 1f, 1g |
| C2.17 | 0.571 | standard | 1f, 1g |
| C2.18 | pairwise independent (1/4 = 1/2*1/2); not mutual (1/4 != 1/8) | standard | 1e |
| C2.19 | 0.833 | standard | 1c, 1g |
| C2.20 | 0.938 | standard | 1g |
| C2.21 | (a) 0.4286 -> no; (b) 0.9310 -> yes | decision | 1g |
| C2.23 | 0.375 | audit | 1c |
| C2.24 | NOT independent (0 != 0.09); disjoint is the opposite of independent | rival_trap | 1e |
| C2.25 | 0.41 | audit | 1f |
| C2.26 | A: 7/15 = 0.4667; B is more reliable (1 > 0.4667) | decision | 1c, 1e |

### ch03 — Discrete RVs & Moments {.unnumbered}

*S.S. Anne -> Vermilion. 24 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C3.1 | mode 0, median 0 | standard | 2a, 2b, 2c |
| C3.2 | 1.7 | standard | 2b, 2c |
| C3.3 | 1.55 | standard | 2a, 2b, 2c |
| C3.4 | Var = 1.4275, sigma ~ 1.195 | standard | 2c |
| C3.5 | E[Y] = 13.6, Var(Y) = 22.84 | standard | 2c |
| C3.6 | E[X] = 4.5, Var(X) = 5.25 | standard | 2c, 2d |
| C3.7 | 25th = 1, 75th = 3 | standard | 2a, 2b, 2c |
| C3.26 | mean 2; Var_A = 4 > Var_B = 1; pick B | decision | 2c |
| C3.8 | E[W] = 2.5 (Meowth confused mode with mean) | audit | 2a, 2b, 2c |
| C3.9 | E[V] = 18.5, Var(V) = 142.75, sigma ~ 11.95 | standard | 2b, 2c |
| C3.10 | 2.0 | standard | 2a, 2b, 2c |
| C3.11 | E[X] = 1.1, Var(X) = 0.49; pmf 0.2, 0.5, 0.3 | standard | 2c, 2d |
| C3.12 | E[X] = 5.5, Var(X) = 5.25 | standard | 2c, 2d |
| C3.13 | Eevee E[D] = 2.3 < 3; Gary wrong | rival_trap | 2b, 2c |
| C3.14 | E[X^2] = 6.05 (not 4.6225) | standard | 2b, 2c |
| C3.15 | mode 0, median 1, mean 1.29 | standard | 2a, 2b, 2c |
| C3.16 | Var = 1 (not 10) | audit | 2c |
| C3.17 | E[Y] = 8.4, Var(Y) = 2.44 | standard | 2c |
| C3.18 | E[X] = 2, M_X(0) = 1 | standard | 2c, 2d |
| C3.19 | E[X]=1.35, E[Y]=13.5, Var(Y)=122.75 | standard | 2a, 2b, 2c |
| C3.20 | (n+1)/2 and (n^2-1)/12; at n=6: 3.5 and 35/12 | standard | 2c, 2d |
| C3.21 | (a) Pikachu; (b) Raichu | decision | 2c |
| C3.23 | Var(Y) = 45 (Gary forgot to square the 3) | rival_trap | 2c |
| C3.24 | E[X] = 1.5 (Jessie dropped the S(0) term) | audit | 2a, 2b, 2c |

### ch04 — Combinatorics {.unnumbered}

*Viridian Forest -> Pewter. 20 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C4.1 | 10000 | standard | 1b |
| C4.2 | 210 | standard | 1b |
| C4.3 | 35 | standard | 1b |
| C4.4 | 120 | standard | 1b |
| C4.5 | 60 | standard | 1b |
| C4.6 | 0.3456 | standard | 1b, 2d |
| C4.26 | (i) hypergeometric = 0.30; (ii) binomial = 0.288 | decision | 1b, 2d |
| C4.7 | 0.4762 | standard | 1b, 2d |
| C4.8 | 20 | audit | 1b |
| C4.9 | 0.9667 | standard | 1b, 2d |
| C4.10 | 35 | standard | 1b |
| C4.11 | 180 | standard | 1b |
| C4.12 | 0.8824 | standard | 1b, 2d |
| C4.13 | Gary 0.2646 (binomial, wrong); correct 0.30 (hypergeometric) | rival_trap | 1b, 2d |
| C4.14 | 84 | audit | 1b |
| C4.15 | 3024 | standard | 1b |
| C4.24 | 0.3333 | audit | 1b, 2d |
| C4.16 | P(>=2)=405/1287~=0.3147; P(<=1)=882/1287~=0.6853 | standard | 1b, 2d |
| C4.17 | 0.2 | rival_trap | 1b |
| C4.18 | (a) 11880; (b) 1/33~=0.0303; (c) 5/11~=0.4545 | standard | 1b, 2d |

### ch05 — Key Discrete Distributions {.unnumbered}

*Lavender Town -> Celadon. 25 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C5.1 | 1/0.3 = 3.333 (valid since \|r\| < 1) | standard | 2d |
| C5.2 | e^2 = 7.389 | standard | 2d |
| C5.3 | 0.85^5 = 0.4437 | standard | 2d |
| C5.4 | E = 6.667, Var = 37.78 | standard | 2d |
| C5.5 | 0.224 | standard | 2d |
| C5.6 | mean 12, variance 12 | standard | 2d |
| C5.7 | 0.1382 | standard | 2d |
| C5.26 | add rates: Poisson(3), mean 3 | decision | 2d |
| C5.8 | 0.2 (memoryless; gambler's fallacy) | audit | 2d |
| C5.9 | 1 - 4 e^{-3} = 0.8009 | standard | 2d |
| C5.10 | 0.0699 (lambda = 15) | standard | 2d |
| C5.11 | Poisson(8), mean 8 | standard | 2d |
| C5.12 | 0.8^4 = 0.4096 | standard | 2d |
| C5.13 | 0.1406 (geometric, not binomial) | rival_trap | 2d |
| C5.14 | Poisson(2), mean 2 | standard | 2d |
| C5.15 | E = 9.33; P(X=1) = 0.0227 | standard | 2d |
| C5.16 | 1 - 0.9^5 = 0.4095 (not ~1) | audit | 2d |
| C5.18 | Poisson(2), P(2) = 0.2707 | standard | 2d |
| C5.24 | 0.0699 (not ~1; rescale to lambda = 15) | audit | 2d |
| C5.19 | Poisson(2); 1 - e^{-6} = 0.9975 | standard | 2d |
| C5.20 | q/p; 4.0 | standard | 2d |
| C5.21 | (a) 1.156 (geometric); (b) 3.47 (negbin) | decision | 2d |
| C5.23 | Poisson(4), P(2) = 0.1465 | rival_trap | 2d |
| C5.22 | 0.1055 | standard | 2d |
| C5.25 | negbin: E = 7.5, Var = 18.75 | decision | 2d, 2b |

### ch06 — Deductibles & Limits (Discrete) {.unnumbered}

*Fuchsia / Safari Zone. 19 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C6.1 | 0.86 | standard | 2e |
| C6.2 | 1.911 | standard | 2f |
| C6.3 | 1.4 | standard | 2e |
| C6.4 | 1.15 | standard | 2e |
| C6.5 | 0.63 | standard | 2e |
| C6.6 | 0.6 | standard | 2e |
| C6.7 | 0.04 | standard | 2e |
| C6.8 | 0.37 (not 0) | audit | 2e |
| C6.9 | 0.296 | standard | 2e |
| C6.10 | 1.184 | standard | 2f |
| C6.11 | 0.37 (both roads) | standard | 2e |
| C6.12 | 1.17 | standard | 2e |
| C6.13 | 1.64 (per payment); Gary confused per-loss with per-payment | rival_trap | 2f |
| C6.14 | 0.82 | standard | 2e |
| C6.15 | A 0.41, B 1.15; choose A | decision | 2e |
| C6.16 | 0.41 (not -0.44) | audit | 2e |
| C6.17 | E[X^4]=1.52, E[X^1]=0.70; per loss 0.738; per payment 1.64; identity 1.52+0.04=1.56 | standard | 2e, 2f |
| C6.18 | 0.70; Gary's d*P(X>d) shortcut wrong | rival_trap | 2e |
| C6.19 | 1.64 (not 0.547); divided by F(2)=0.75 instead of P(X>2)=0.25 | audit | 2f |

### ch07 — Checkpoint A {.unnumbered}

*the route campfire. 12 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| Q7.1 | (a) 0.8, (b) 0.2 | standard | 1a, 1e |
| Q7.2 | 1/3 ~ 0.333 | standard | 1f, 1g |
| Q7.3 | E[W] = 1.5 (Meowth confused mode with mean) | audit | 2a, 2c |
| Q7.4 | 0.24576 | standard | 1b, 2d |
| Q7.5 | 12/55 ~ 0.2182 | standard | 1b, 2d |
| Q7.6 | E[X] = 4 (Gary's 3 omits the catching throw) | rival_trap | 2d |
| Q7.7 | P(N=0) = e^{-2} ~ 0.1353, E[N] = 2 | standard | 2d |
| Q7.8 | Poisson(4.0); P(0) = e^{-4} ~ 0.0183 (clerk multiplied instead of adding) | audit | 2d |
| Q7.9 | E[X] = 1.0, Var(X) = 0.9 | standard | 2c, 2d |
| Q7.10 | 0.7 (in \$100s) | standard | 2e, 2f |
| Q7.11 | E[X]=1.4, E[X^2]=1.1, E[(X-2)+]=0.3; 1.1+0.3=1.4 | standard | 2e, 2f |
| Q7.12 | (a) 1/0.3 ~ 3.333; (b) E=1.2, P(>=1)=0.7599; use geometric | decision | 1c, 2d |

### ch08 — The Calculus Toolkit {.unnumbered}

*Bill's Lighthouse. 18 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C8.1 | 2 | standard | prereq |
| C8.2 | 5832 | standard | prereq |
| C8.3 | c = 1/7; S(t) = e^{-t/7} | standard | prereq |
| C8.4 | mode = 2 | standard | prereq |
| C8.5 | S(t) = e^{-t/4}; S(0) = 1 | standard | prereq |
| C8.6 | (1/3)(e - 1) = 0.5728 | standard | prereq |
| C8.7 | 96 | standard | prereq |
| C8.8 | 96 (off-by-one: alpha = power + 1 = 4, not 3) | audit | prereq |
| C8.9 | 6 | standard | prereq |
| C8.10 | 250 (log used 5^2 instead of 5^alpha = 5^3) | audit | prereq |
| C8.11 | -x^2 e^{-x} - 2x e^{-x} - 2 e^{-x} + C | standard | prereq |
| C8.12 | 0 (exponential beats polynomial) | standard | prereq |
| C8.13 | E[X^2] = 8, Var(X) = 4 (Gary forgot E[X^2] = Var + (E[X])^2) | rival_trap | prereq |
| C8.14 | c = 1/16 (Gary wrong; the gamma integral settles it) | rival_trap | prereq |
| C8.15 | (a) integrates to 1; (b) E[X] = 3 theta; (c) E[X^2] = 12 theta^2, Var = 3 theta^2 | standard | prereq |
| C8.16 | Gamma(1/2) = sqrt(pi) | standard | prereq |
| C8.17 | 1536; use the gamma identity (one line beats four by-parts rounds) | decision | prereq |
| C8.18 | e^{-t/5} is the survival, not the cdf; true cdf F(t) = 1 - e^{-t/5} | audit | prereq |

### ch09 — Densities & CDFs {.unnumbered}

*Saffron / Sabrina. 19 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C9.1 | P(0.5<X<1.5)=0.5; P(X=1)=0 | standard | 2a |
| C9.2 | c=2/9; P(X<2)=4/9~0.444 | standard | 2a |
| C9.3 | F(x)=x^2; P(0.3<X<0.6)=0.27 | standard | 2a |
| C9.4 | f(x)=(1/5)e^{-x/5}; P(X>5)=e^{-1}~0.3679 | standard | 2a |
| C9.5 | total=1; P(Y<=5)=1; P(Y=0)=0.3 | standard | 2a |
| C9.6 | P(X=1)=0 (height read as probability) | audit | 2a |
| C9.7 | matters only for (ii), the discrete one, by the mass 0.2 | decision | 2a |
| C9.8 | c=1/8; F=x^2/16; P(1<X<3)=0.5; P(X=3)=0 | standard | 2a |
| C9.9 | valid (area=1); P(X<0.1)=0.4; P(X=0.1)=0 | standard | 2a |
| C9.10 | true 4/9~0.444 (integrated before normalizing) | audit | 2a |
| C9.11 | k=3/8; P(X<1)=1/8=0.125 (Gary skipped the constant) | rival_trap | 2a |
| C9.12 | k=0.3; F=0.4+0.15y^2 on (0,2]; P(Y<=1)=0.55 | standard | 2a |
| C9.13 | f(x)=2(1+x)^{-3}; P(X>1)=0.25 | standard | 2a |
| C9.14 | P(X=1)=0 (height isn't a probability; a point carries none) | rival_trap | 2a |
| C9.15 | P(Y=0)=P(Y<=0)=0.4 (mixed law: the mass is real) | audit | 2a |
| C9.16 | c=1/6; P(X<2)=1/3 (the claimed 0.5 is inconsistent) | standard | 2a |
| C9.17 | mass2=0.1; (0.5,0.4,0.1) total 1; yes, P(Y<=2)=1 vs P(Y<2)=0.9 | decision | 2a |
| C9.18 | c=2/3; F(1)=2/3; P(0.5<X<1.5)=7/12~0.583 | standard | 2a |
| C9.19 | area=1; F=x^3/8; f=F' ok; median=2^{2/3}~1.587 | standard | 2a |

### ch10 — Continuous Moments {.unnumbered}

*Saffron / Silph Co.. 23 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C10.1 | E[X]=3, Var(X)=3 | standard | 2c |
| C10.2 | 4/3 ~ 1.333 | standard | 2c |
| C10.3 | 5 | standard | 2c |
| C10.4 | E[X^2]=2.4, Var(X)=0.15 | standard | 2c |
| C10.5 | E[Y]=8, Var(Y)=2.4 | standard | 2c |
| C10.6 | 1.0 | standard | 2c, 2d |
| C10.7 | E[X^2]=3 (not 2.25) | standard | 2c |
| C10.26 | mean 4; Var_A=4/3 < Var_B=16/3; pick A | decision | 2c |
| C10.8 | E[X]=3 (not 5) | audit | 2c, 2d |
| C10.9 | E=1/3, E[X^2]=1/6, Var=1/18 | standard | 2c |
| C10.10 | 4 | standard | 2c |
| C10.11 | E=7, E[X^2]=140, Var=91 | standard | 2c, 2d |
| C10.12 | 2.0 | standard | 2c |
| C10.13 | E[X]=1.5 < 2; Gary wrong (mode != mean) | rival_trap | 2c |
| C10.14 | 2.4 (not 2.25) | standard | 2c |
| C10.15 | E[X wedge 9] = 5.625 | standard | 2c, 2d |
| C10.16 | Var=0.15 (not 2.4) | audit | 2c |
| C10.17 | E[Y]=9, Var(Y)=16 | standard | 2c |
| C10.24 | E[X]=6 (integrate S, not F) | audit | 2c |
| C10.19 | 4; 12; 144 | standard | 2c |
| C10.20 | 1.5 both ways | standard | 2c |
| C10.21 | ~2.94; full mean too high by ~5.06 | decision | 2c, 2d |
| C10.23 | Var(Y)=36 (Gary forgot the square) | rival_trap | 2c |

### ch11 — Key Continuous Distributions {.unnumbered}

*the continuous wilds. 19 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C11.1 | P=0.375; E[X]=6; Var(X)=64/12=5.3333 | standard | 2d |
| C11.2 | P(X>6)=0.3679; P(X<=3)=0.3935 | standard | 2d |
| C11.3 | E[X]=6; Var(X)=18; f(x)=(1/9) x e^{-x/3} | standard | 2d |
| C11.4 | E[X]=0.4 (below 1/2); Var(X)=0.04 | standard | 2d |
| C11.5 | true 0.375 (recorder divided by 10, not the width 8) | audit | 2d |
| C11.6 | Y~Uniform(2,10); E[Y]=6; Var(Y)=64/12=5.3333 | standard | 2d |
| C11.7 | A remaining = 10; B remaining = 2; keep A | decision | 2d |
| C11.8 | P(extra>15)=0.4724; expected additional=20 min | standard | 2d |
| C11.9 | c=1/16; Gamma(2,4); E[X]=8 | standard | 2d |
| C11.10 | P(X=5)=0 (Meowth read a density as a probability) | audit | 2d |
| C11.11 | T~Exponential(6); E[T]=6 | standard | 2d |
| C11.12 | E[X]=6, Var(X)=12 (Gary dropped theta^2) | rival_trap | 2d |
| C11.13 | P(X>0.5)=0.875; E[X]=0.75 | standard | 2d |
| C11.14 | expected remaining = 6 (not 2; memoryless, not fixed) | rival_trap | 2d |
| C11.15 | E[X]=6, Var(X)=12 (log swapped mean and variance) | audit | 2d |
| C11.16 | 25th = 4; 75th = 8 | standard | 2d |
| C11.17 | 0.5; 0.3679; 0.5; window=0.0920; elapsed time irrelevant | decision | 2d |
| C11.18 | (a) Gamma(3,2), E=6, Var=12; (b) 0.0803; (c) 6 = 3*2 (means add) | audit | 2d |
| C11.19 | P(X>4)=0.03125; E[X]=5/3=1.6667 | standard | — |

### ch12 — Normal & the CLT {.unnumbered}

*the Grand Gathering. 19 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C12.1 | 0.9332 | standard | 2d |
| C12.2 | 0.0228 | standard | 2d |
| C12.3 | 0.8705 | standard | 2d |
| C12.4 | 0.1151 | standard | 2d |
| C12.5 | ~95%; ~68% | standard | 2d |
| C12.6 | 82.8 | standard | 2d |
| C12.7 | 0.7745 | standard | 2d |
| C12.8 | 0.1587 | standard | 3i |
| C12.9 | 0.0475 | standard | 3i |
| C12.10 | 0.1056 | audit | 3i |
| C12.11 | 0.0562 | standard | 3i |
| C12.12 | 0.0062 | rival_trap | 3i |
| C12.13 | 0.8531 | standard | 3i |
| C12.14 | 0.0668 | rival_trap | 2d |
| C12.15 | 60 | audit | 3i |
| C12.16 | 0.7286 | standard | 3i |
| C12.17 | 3748 | decision | 2d, 3i |
| C12.18 | ~95%; not 'almost surely' | audit | 2d, 3i |
| C12.19 | 458 | decision | 3i |

### ch13 — Continuous Deductibles & Review {.unnumbered}

*Cinnabar Lab. 19 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C13.1 | 7.408 | standard | 2e |
| C13.2 | 10.0 | standard | 2f |
| C13.3 | 5.507 | standard | 2e |
| C13.4 | 6.4 | standard | 2e |
| C13.5 | 4.693 | standard | 2e |
| C13.6 | 7.0 | standard | 2e |
| C13.7 | 4.493 | standard | 2e |
| C13.8 | 2.21 (not 0) | audit | 2e |
| C13.9 | 2.953 | standard | 2e |
| C13.10 | 4.405 | standard | 2f |
| C13.11 | 4.693 (both roads) | standard | 2e |
| C13.12 | per loss 6.065; per payment 10 | standard | 2e, 2f |
| C13.13 | 10 (per payment); Gary confused per-loss with per-payment | rival_trap | 2f |
| C13.14 | 3.691 | standard | 2e |
| C13.15 | A 6.703, B 3.297; choose B | decision | 2e |
| C13.16 | 6.703 (not 6) | audit | 2e |
| C13.17 | 9.077; +35.4% | standard | 2e |
| C13.18 | 3.691; Gary's d*S(d) shortcut wrong | rival_trap | 2e |
| C13.19 | 10 (not 20.33); divided by F(4) instead of S(4) | audit | 2f |

### ch14 — Joint Distributions {.unnumbered}

*Pokemon Mansion logs. 22 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C14.1 | c = 4, f_X(x) = 2x | standard | 3a |
| C14.2 | valid pmf; P(X=1) = 3/7 ≈ 0.4286 | standard | 3a |
| C14.3 | P(Y>X) = 1/2; X ~ Uniform(0,1) | standard | 3a |
| C14.4 | f_X(x) = 3(1-x)^2 on 0<x<1 | standard | 3a |
| C14.5 | independent; X~Exp(mean 1), Y~Exp(mean 1/2) | decision | 3b |
| C14.6 | P(Y=2 \| X=2) = 1/3 | standard | 3b |
| C14.23 | k = 1/3 (the note is wrong) | audit | 3a |
| C14.7 | integrates to 1; independent; E[X] = 0.75 | standard | 3a, 3b |
| C14.8 | P(Y < 1/2) = 5/12 ≈ 0.4167 | standard | 3a |
| C14.9 | P(Y > 1/2 \| X = 1/4) = 4/5 = 0.80 | standard | 3b |
| C14.10 | 1/16 = 0.0625 (Team Rocket's product route is wrong) | audit | 3a, 3b |
| C14.11 | f_X(x) = 12x(1-x)^2; E[X] = 0.40 | standard | 3a |
| C14.12 | f(x,y) = x + y on [0,1]^2 | standard | 3a |
| C14.15 | P(X < 1/2) = 7/16 = 0.4375 | standard | 3a |
| C14.16 | dependent (Gary is wrong; rectangle is necessary, not sufficient) | rival_trap | 3b |
| C14.24 | E[Y \| X = 1/4] = 7/10 = 0.70 (Gary is wrong) | rival_trap | 3b |
| C14.13 | f_X(x) = (3/8)x^2; E[Y] = 0.75 | standard | 3a, 3b |
| C14.14 | P(X+Y < 2) = 1 - 3*e^(-2) ≈ 0.5940 | standard | 3a, 3b |
| C14.17 | E[XY] = 4/9 ≈ 0.4444 | standard | 3a |
| C14.18 | P(\|X - Y\| < 1/2) = 3/4 = 0.75 | standard | 3a |
| C14.19 | P(X < Y) = 3/5 = 0.60 | standard | 3b |
| C14.25 | P(X+Y > 3/2) = 1/8 = 0.125 (clerk under-reserves) | audit | 3a |

### ch15 — Joint Moments & Covariance {.unnumbered}

*Victory Road. 22 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C15.1 | 13 | standard | 3g |
| C15.2 | Var(X+Y)=17, Var(X-Y)=9 | standard | 3g |
| C15.3 | 24 | standard | 3e |
| C15.4 | Cov=1 (move together) | standard | 3e |
| C15.5 | 38 | standard | 3g, 3h |
| C15.6 | Normal(4, 13) | standard | 3h |
| C15.7 | Poisson(4); E=Var=4 | standard | 3h |
| C15.20 | A=7, B=19; send Pairing A | decision | 3e, 3g |
| C15.8 | Cov=0.16, rho~0.467 | standard | 3e |
| C15.9 | 9 | standard | 3g |
| C15.10 | 48 (Gary's 20 is wrong) | rival_trap | 3g, 3h |
| C15.11 | -1/144 ~ -0.00694 | standard | 3e |
| C15.12 | Cov=0 but dependent (Gary wrong) | rival_trap | 3e |
| C15.13 | ~0.212 | standard | 3h |
| C15.14 | Gamma(5,4); E=20, Var=80 | standard | 3h |
| C15.15 | Var=235; benefit=90 (note's 325 wrong) | audit | 3e, 3g |
| C15.21 | SD=10 (not 14) | audit | 3g |
| C15.22 | Binom(10,0.3); E=3, Var=2.1 (note's p wrong) | audit | 3h |
| C15.16 | Var(T)=54; Corr(X_i,T)~0.612 | standard | 3e, 3g |
| C15.17 | E[T]=6, Var(T)=15 | standard | 3g, 3h |
| C15.18 | ~11.106 | standard | 3e, 3g |
| C15.19 | E[XY]=17, E[(X+Y)^2]=81 | standard | 3e, 3g |

### ch16 — Conditional & Double Expectation {.unnumbered}

*Viridian Gym. 18 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C16.1 | 6 | standard | 3c |
| C16.2 | 24.6 | standard | 3c |
| C16.3 | 30.5 | standard | 3c |
| C16.4 | 9.667 | standard | 3d |
| C16.5 | Var(g)=38, Var(X)=47.667 | standard | 3d |
| C16.6 | 6 | standard | 3c |
| C16.7 | 65 | audit | 3c |
| C16.8 | E[S]=40 > 36 (over budget) | decision | 3c |
| C16.9 | E[X]=6, Var(X)=18.5 (setting choice dominates) | standard | 3d |
| C16.10 | E[X]=4, Var(X)=18.667 | standard | 3c, 3d |
| C16.11 | E[S]=12, Var(S)=56 | standard | 3c, 3d |
| C16.12 | E[N]=6, Var(N)=18 (overdispersed) | standard | 3c, 3d |
| C16.13 | E[X]=200, Var(X)=20800 (Gary dropped Term 2) | rival_trap | 3d |
| C16.14 | E[X]=1.75, Var(X)≈1.993 | standard | 3c, 3d |
| C16.15 | E[S]=150, Var(S)=13750 (dropped Var(N)mu^2=13500) | audit | 3c, 3d |
| C16.16 | Var(X)=104 (changed case) | rival_trap | 3d |
| C16.17 | E[X]=58.6, Var(X)≈2969.24, ≈52% from tier (dossier wrong) | audit | 3c, 3d |
| C16.18 | E[S]=2000, Var(S)=800000, CV=0.447, P(S>2600)≈0.251 (breach > 1 in 4) | decision | 3c, 3d |

### ch17 — Order Statistics {.unnumbered}

*the Elite Four. 17 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C17.1 | P(max<=0.8) = 0.8^5 = 0.32768 ~ 0.328 | standard | 3f |
| C17.2 | min ~ Exponential(rate 3/10); mean = 10/3 ~ 3.33 s | standard | 3f |
| C17.3 | true 0.5^8 = 1/256 ~ 0.0039 (log used 0.5^4; raise F(x)=x^2, not x) | audit | 3f |
| C17.4 | E[max] = (9/10)*20 = 18 | standard | 3f |
| C17.5 | true 0.8^5 = 0.328 (log used n*F=4, an impossible 'probability'; it is [F]^n) | audit | 3f |
| C17.6 | series = 0.729; parallel = 0.999 | standard | 3f |
| C17.7 | E[min] = 1/3 ~ 0.333; f_min(x) = 2(1-x) | standard | 3f |
| C17.8 | (i) E[max] = 0.75; (ii) P(max>0.9) = 0.271 | standard | 3f |
| C17.9 | (i) Exponential(0.325); (ii) mean 40/13 ~ 3.08; (iii) 0.377 | standard | 3f |
| C17.10 | E[X_(2)] = 2/5 = 0.4; f(x) = 12 x (1-x)^2 | standard | 3f |
| C17.11 | true 0.5^6 = 1/64 ~ 0.0156 (Gary used n*F = 3, impossible; it is [F]^n) | rival_trap | 3f |
| C17.12 | Exponential(1/2), mean 2 min; P(open>4) = e^{-2} ~ 0.135 | standard | 3f |
| C17.13 | E[max] = 10*(1+1/2+1/3) = 110/6 ~ 18.33 yr | standard | 3f |
| C17.14 | series = 0.684; parallel = 0.999 | audit | 3f |
| C17.15 | E[range] = (n-1)/(n+1) = 9/11 ~ 0.818 | standard | 3f |
| C17.16 | true mean = 2 min (Gary averaged means; add the rates) | rival_trap | 3f |
| C17.17 | (i) 0.99; (ii) 0.9405; (iii) Exponential(3/10), mean 10/3 ~ 3.33 yr | decision | 3f |

### ch18 — Checkpoint B {.unnumbered}

*Indigo Plateau, eve. 12 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| C18.1 | f_X(x)=x+1/2; E[X]=7/12≈0.5833 | standard | 3a, 3b |
| C18.2 | Cov(X,Y)=0.205 (positive) | standard | 3c, 3e |
| C18.3 | 33 | standard | 3g |
| C18.4 | E[S]=40, Var(S)=500 | standard | 3c, 3d |
| C18.5 | E[X]=38, Var(X)=120 (arena choice dominates) | standard | 3d |
| C18.6 | F_M(x)=x^4; E[M]=4/5=0.8 | standard | 3f |
| C18.7 | W ~ Expo(mean=6); E[W]=6 s | standard | 3f |
| C18.8 | Cov(X,Y)=0 yet X,Y are dependent (Y=X^2); zero cov ≠ independence | audit | 3e |
| C18.9 | Var(X+Y)=80 (Gary dropped 2Cov=30) | rival_trap | 3g, 3e |
| C18.10 | E[S]=120, Var(S)=3000 (dropped Var(N)mu^2=2400) | audit | 3c, 3d |
| C18.11 | L ~ Expo(mean=2); E[L]=2 min | standard | 3f |
| C18.12 | E[X]=43.5, Var(X)=1786.85, ≈51% from tier | standard | 3c, 3d |

### ch19 — Mock Exams (M1 / M2 / M3) {.unnumbered}

*Indigo Plateau / the Championship. 90 problems.*

| Problem | Final answer | Archetype | Outcome(s) |
|---------|--------------|-----------|------------|
| M1.1 | C (0.40) | topic1 | 1a, 1d |
| M1.2 | B (0.162) | topic1 | 1c, 1f |
| M1.3 | D (336) | topic1 | 1b |
| M1.4 | C (2/9 ~ 0.2222) | topic1 | 1a, 1d |
| M1.5 | D (0.784) | topic1 | 1f, 1g |
| M1.6 | C (~0.52) | topic1 | 1c, 1e |
| M1.7 | C (0.30) | topic1 | 1d |
| M1.8 | C (~0.330) | topic1 | 1b |
| M1.9 | D (~0.801) | topic2 | 2d |
| M1.10 | D (8) | topic2 | 2d, 2c |
| M1.11 | B (0.1024) | topic2 | 2d |
| M1.12 | A (0.0668) | topic2 | 2d |
| M1.13 | C (4) | topic2 | 2d, 2c |
| M1.14 | C (~2.43) | topic2 | 2e, 2f |
| M1.15 | C (~8.33) | topic2 | 2d, 2c |
| M1.16 | C (~0.549) | topic2 | 2d |
| M1.17 | C (~0.163) | topic2 | 2d, 3i |
| M1.18 | B (~3.15) | topic2 | 2e, 2f |
| M1.19 | B (3.0) | topic2 | 2d |
| M1.20 | B (1/9) | topic2 | 2a, 2b |
| M1.21 | B (~2.92) | topic2 | 2c, 2d |
| M1.22 | C (2.0) | topic2 | 2c |
| M1.23 | C (0.5) | topic3 | 3a, 3b |
| M1.24 | D (~0.833) | topic3 | 3f |
| M1.25 | B (13) | topic3 | 3c, 3e, 3g |
| M1.26 | C (~3.11) | topic3 | 3c, 3d |
| M1.27 | B (0.0228) | topic3 | 3e, 3g, 3i |
| M1.28 | A (2.0) | topic3 | 3f |
| M1.29 | C (200) | topic3 | 3c, 3d |
| M1.30 | C (~0.251) | topic3 | 3c, 3d, 3i |
| M2.1 | B (~0.41) | topic1 | 1a, 1d |
| M2.2 | B (0.40) | topic1 | 1c, 1g |
| M2.3 | B (924) | topic1 | 1b |
| M2.4 | B (0.42) | topic1 | 1c, 1e |
| M2.5 | B (~0.46) | topic1 | 1f |
| M2.6 | C (0.90) | topic1 | 1d, 1e |
| M2.7 | B (0.504) | topic1 | 1a |
| M2.8 | B (~0.234) | topic1 | 1b |
| M2.9 | A (~0.138) | topic2 | 2d |
| M2.10 | C (1.0) | topic2 | 2c, 2d |
| M2.11 | B (0.7745) | topic2 | 2d |
| M2.12 | C (~0.406) | topic2 | 2d |
| M2.13 | E (18) | topic2 | 2c, 2d |
| M2.14 | C (~13.52) | topic2 | 2e, 2f |
| M2.15 | B (~0.1353) | topic2 | 2a, 2b |
| M2.16 | C (82.8) | topic2 | 2d |
| M2.17 | A (~0.0475) | topic2 | 2d, 3i |
| M2.18 | C (0.40) | topic2 | 2c, 2d |
| M2.19 | C (~0.406) | topic2 | 2d, 2c |
| M2.20 | B (3) | topic2 | 2c, 2d |
| M2.21 | D (3.8) | topic2 | 2e, 2f |
| M2.22 | D (4/3) | topic2 | 2c, 2d |
| M2.23 | B (x + 1/2) | topic3 | 3a, 3b |
| M2.24 | C (1) | topic3 | 3c, 3e |
| M2.25 | C (~0.667) | topic3 | 3c, 3d |
| M2.26 | D (17) | topic3 | 3g, 3h |
| M2.27 | C (27) | topic3 | 3c, 3d |
| M2.28 | B (0.125) | topic3 | 3f |
| M2.29 | B (independent; f_X = 2x) | topic3 | 3a, 3b |
| M2.30 | C (~0.1587) | topic3 | 3c, 3d, 3i |
| M3.1 | C (0.40) | topic1 | 1a, 1d |
| M3.2 | C (0.625) | topic1 | 1c, 1f |
| M3.3 | D (1680) | topic1 | 1b |
| M3.4 | B (~0.133) | topic1 | 1c, 1e |
| M3.5 | C (~0.684) | topic1 | 1d, 1e |
| M3.6 | B (independent) | topic1 | 1g |
| M3.7 | C (0.40) | topic1 | 1a, 1b |
| M3.8 | B (~0.087) | topic1 | 1b |
| M3.9 | C (5.0) | topic2 | 2d, 2c |
| M3.10 | B (0.04) | topic2 | 2c, 2d |
| M3.11 | C (~0.175) | topic2 | 2d |
| M3.12 | B (4) | topic2 | 2c |
| M3.13 | B (~0.95) | topic2 | 2d |
| M3.14 | C (5.0) | topic2 | 2e, 2f |
| M3.15 | D (6) | topic2 | 2c, 2d |
| M3.16 | B (3.5) | topic2 | 2a, 2b |
| M3.17 | C (~0.1056) | topic2 | 2d, 3i |
| M3.18 | C (16) | topic2 | 2c, 2d |
| M3.19 | D (4) | topic2 | 2d |
| M3.20 | E (36) | topic2 | 2c |
| M3.21 | B (~6.93) | topic2 | 2d, 2c |
| M3.22 | C (0.375) | topic2 | 2d |
| M3.23 | B (0.5) | topic3 | 3a, 3b |
| M3.24 | D (6) | topic3 | 3c, 3d |
| M3.25 | B (~3.33) | topic3 | 3f |
| M3.26 | B (13) | topic3 | 3g, 3h |
| M3.27 | C (20) | topic3 | 3c, 3d |
| M3.28 | C (~0.239) | topic3 | 3c, 3i |
| M3.29 | B (0.20) | topic3 | 3e, 3g |
| M3.30 | B (~0.328) | topic3 | 3f, 3i |
