#!/usr/bin/env python3
"""Regenerate the chapter set to the v2 chapter map (MASTER_PLAN_V2.md Part 6).

16 chapters (ch00..ch15) + 2 checkpoints, teaching-first skeleton, tier metadata.
Overwrites existing chapter files with v2 stubs (Draft-1 is preserved in drafts/).
The comprehensive workflow then rewrites each stub to the masterful standard.

Run: python tools/scaffold_v2.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH = ROOT / "book" / "chapters"
CH.mkdir(parents=True, exist_ok=True)

STUB = "<!-- status: stub -->"

# (filebase, title, type_class, tier, outcomes, draft1_source, maps_to, kind)
CHAPTERS = [
    ("ch00_orientation", "Orientation — How to Use This Book & How to Read the Math",
     "type-normal", "C", "orientation", "", "Pallet Town — the decision to set out", "chapter"),
    ("ch01_toolkit_numbers", "The Toolkit I — Numbers, Variables, Functions & Notation",
     "type-normal", "C", "prereq", "ch01_trainer_school", "Trainer School, part one", "chapter"),
    ("ch02_toolkit_calculus", "The Toolkit II — Series & Calculus for Probability",
     "type-normal", "B", "prereq", "ch01_trainer_school", "Trainer School, part two", "chapter"),
    ("ch03_outcomes", "The Space of Possible Outcomes",
     "type-normal", "C", "1a", "ch02_route_1", "Route 1 — the Spearow swarm", "chapter"),
    ("ch04_counting", "Counting the Uncountable",
     "type-rock", "B", "1b", "ch03_pewter_city", "Viridian Forest → Pewter, Brock", "chapter"),
    ("ch05_bayes", "Reasoning From Evidence",
     "type-water", "A", "1c,1d,1e,1f,1g", "ch04_cerulean_city", "Cerulean, Misty — the proving ground", "chapter"),
    ("ch05x_checkpoint_a", "Checkpoint A — The Rocket Hideout",
     "type-normal", "C", "review", "", "Spaced-retrieval review of Topic 1", "checkpoint"),
    ("ch06_random_variables", "Variables of Fortune",
     "type-electric", "A", "2a", "ch05_vermilion_city", "S.S. Anne, part one — the RV language", "chapter"),
    ("ch07_center_spread", "Center & Spread",
     "type-electric", "A", "2b,2c,2d", "ch05_vermilion_city", "Vermilion, Lt. Surge — expectation/variance/MGF/Darth Vader", "chapter"),
    ("ch08_discrete", "The Named Patterns I — Discrete Distributions",
     "type-grass", "B", "2d2", "ch06_celadon_city", "Lavender Tower & Celadon Game Corner, Erika", "chapter"),
    ("ch09_continuous", "The Named Patterns II — Continuous Distributions & Transformations",
     "type-psychic", "B", "2d3", "ch07_saffron_city", "Saffron, Sabrina", "chapter"),
    ("ch10_pricing", "Pricing the Risk",
     "type-poison", "A", "2e,2f", "ch08_fuchsia_safari", "Fuchsia, Safari Zone, Koga — highest weight", "chapter"),
    ("ch10x_checkpoint_b", "Checkpoint B — The Univariate World",
     "type-normal", "C", "review", "", "Spaced-retrieval review of Topic 2", "checkpoint"),
    ("ch11_joint", "Two Fates Entwined",
     "type-fire", "A", "3a,3b", "ch09_cinnabar_island", "Cinnabar — joint/marginal/conditional", "chapter"),
    ("ch12_double_expectation", "Expectation Within Expectation",
     "type-ground", "A", "3c,3d", "ch10_viridian_gym", "Viridian Gym, Giovanni", "chapter"),
    ("ch13_covariance", "Combining Forces",
     "type-normal", "A", "3e,3g,3h", "ch11_victory_road", "Victory Road", "chapter"),
    ("ch14_order_clt", "Order From Chaos",
     "type-psychic", "A", "3f,3i", "ch12_indigo_plateau", "Indigo Plateau approach — order stats & CLT", "chapter"),
    ("ch15_champion", "Champion's Challenge — Exam Strategy & Mock Exams",
     "type-normal", "B", "all", "ch13_champions_challenge", "The League — strategy + 3 mocks", "chapter"),
]

BOXES = """\
<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
"""


def chapter_md(base, title, tcls, tier, outcomes, src, maps_to, kind) -> str:
    num = base[2:4]
    head = f"""<!--
  file: {base}
  tier: {tier}
  outcomes: {outcomes}
  draft1_source: drafts/chapters_draft1/{src}.md
  maps_to: {maps_to}
  status: stub
-->
{STUB}

# {title} {{.{tcls}}}
"""
    if kind == "checkpoint":
        return head + f"""
## Checkpoint — Spaced Retrieval

*(A short, no-new-content review: retrieval prompts and a few mixed problems that force
recall across the topics just finished. Per MASTER_PLAN_V2 Part 6 / doctrine rule 8.)*

## Mixed Retrieval Problems

## Answer Key
"""
    return head + f"""
## Cold Open

## Where You Are — 60-Second Retrieval

*(Retrieve the prior chapter's load-bearing idea before starting.)*

## Oak's Briefing — Learning Outcomes & Test-Out Gate

> **Do you already own this chapter?** *(Skip gate — pass the bar, move on.)*

## The Teaching

*(FOR EACH concept, in difficulty order: a "Do you already own this?" micro-check, then the
nine-beat Concept Lesson Arc (one-sentence idea → concrete instance → reason in words →
dismantle the wrong idea → notation one glyph at a time → derive the formula → ramp →
picture/table → consolidate), then the Pokédex Entry + Recognition Cue. Tier {tier}.)*

## Worked Examples — Faded Guidance

*(full → partial → independent; Tier-A first example understanding-first.)*

## Trainer's Tips

## Team Rocket's Trap

## From Kanto to the Real World

## The Gym Battle (Capstone)

## The Gym Challenge (Problem Set)

::: problem-set
### Route Trainers (mechanics)

### Gym Battles (true SOA difficulty)

### Elite Challenge (integrative / stretch)
:::

## Answer Key

::: answer-key
:::

## Badge Earned — Mastery Checklist

---

{BOXES}
"""


def main() -> None:
    # remove old chapter files not in the v2 set
    keep = {b[0] for b in CHAPTERS}
    for f in CH.glob("*.md"):
        if f.stem not in keep:
            f.unlink()
            print(f"  removed {f.name}")
    for c in CHAPTERS:
        path = CH / f"{c[0]}.md"
        path.write_text(chapter_md(*c))
        print(f"  wrote {c[0]}.md  (tier {c[3]})")


if __name__ == "__main__":
    main()
