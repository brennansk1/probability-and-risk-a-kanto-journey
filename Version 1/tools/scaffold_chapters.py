#!/usr/bin/env python3
"""Generate professional chapter + appendix skeletons for the textbook.

Each chapter gets the standard 10-part architecture (DESIGN.md), a type-colored
heading, a metadata header, and inline templates for the five Pokemon-styled
callout boxes so the writing workflow has the exact syntax to fill. Idempotent:
will NOT overwrite a file that has progressed past the stub marker.

Run: python tools/scaffold_chapters.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH_DIR = ROOT / "book" / "chapters"
APX_DIR = ROOT / "book" / "appendices"
CH_DIR.mkdir(parents=True, exist_ok=True)
APX_DIR.mkdir(parents=True, exist_ok=True)

STUB_MARKER = "<!-- status: stub -->"

# (num, slug, title, type_class, topic, outcomes, badge, maps_to)
CHAPTERS = [
    (1, "trainer_school", "Trainer School, Pallet Town — The Tools of the Trade",
     "type-normal", "Prerequisite calculus & algebra", "prereq",
     "Toolkit Cleared (Trainer's License)",
     "The night before Ash gets his first Pokemon; up late in Oak's lab."),
    (2, "route_1", "Pallet Town & Route 1 — The Space of All Possible Outcomes",
     "type-normal", "General Probability", "1a", "Boulder Badge",
     "Ash receives Pikachu; the Spearow swarm on Route 1."),
    (3, "pewter_city", "Viridian Forest & Pewter City — Counting the Uncountable",
     "type-rock", "General Probability", "1b", "Counting Badge (Brock)",
     "Viridian Forest maze into Brock's Pewter Gym."),
    (4, "cerulean_city", "Cerulean City — Reasoning From Evidence",
     "type-water", "General Probability", "1c-1g", "Cascade Badge",
     "Cerulean mysteries; Misty's gym; Bill's lighthouse."),
    (5, "vermilion_city", "S.S. Anne & Vermilion City — Variables of Fortune",
     "type-electric", "Univariate Random Variables", "2a-2d", "Thunder Badge",
     "The S.S. Anne voyage and Lt. Surge's gym."),
    (6, "celadon_city", "Lavender Town & Celadon City — The Named Patterns of Chance (Discrete)",
     "type-grass", "Univariate Random Variables (discrete)", "2d2", "Rainbow Badge",
     "Lavender's Pokemon Tower and Celadon's Game Corner; Erika's gym."),
    (7, "saffron_city", "Saffron City & the Normal World — Continuous Patterns & the Bell Curve",
     "type-psychic", "Univariate Random Variables (continuous)", "2d3", "Marsh Badge",
     "Sabrina's reality-warping psychic gym."),
    (8, "fuchsia_safari", "Fuchsia City & the Safari Zone — Pricing the Risk",
     "type-poison", "Univariate Random Variables (loss models)", "2e-2f", "Soul Badge",
     "The Safari Zone's limited balls; Koga's gym. HIGHEST EXAM WEIGHT."),
    (9, "cinnabar_island", "Cinnabar Island — Two Fates Entwined (Joint Distributions)",
     "type-fire", "Multivariate Random Variables", "3a-3b", "Volcano Badge",
     "The Pokemon Mansion research logs; Blaine's riddle gym."),
    (10, "viridian_gym", "Viridian Gym & the Giovanni Confrontation — Expectation Within Expectation",
     "type-ground", "Multivariate Random Variables", "3c-3d", "Earth Badge",
     "Giovanni revealed as Team Rocket's boss."),
    (11, "victory_road", "Victory Road — Combining Forces (Covariance, Correlation & Sums)",
     "type-normal", "Multivariate Random Variables", "3e,3g,3h", "Victory Road Cleared",
     "The gauntlet before the League; the team combines."),
    (12, "indigo_plateau", "The Indigo Plateau — Order from Chaos (Order Statistics & the CLT)",
     "type-psychic", "Multivariate Random Variables", "3f,3i", "League Finalist",
     "The Elite Four and the League tournament field."),
    (13, "champions_challenge", "Champion's Challenge — Becoming a Master (Exam Strategy & Mocks)",
     "type-normal", "Exam execution & integrative review", "all", "Indigo League Champion",
     "The final battle against Champion Gary; three full mock exams."),
]

APPENDICES = [
    ("a_formula_sheet", "Appendix A — Master Formula Sheet & Shortcut Catalog"),
    ("b_distribution_tables", "Appendix B — Distribution Reference Tables"),
    ("c_normal_table", "Appendix C — The Provided Normal Table & Symmetry Techniques"),
    ("d_calculator_guide", "Appendix D — Calculator Guide (TI-30XS MultiView & BA II Plus)"),
    ("e_exam_day", "Appendix E — Exam-Day Logistics & Psychology"),
    ("f_cross_reference", "Appendix F — Cross-Reference to ACTEX/Broverman/Finan & SOA Samples"),
    ("g_glossary", "Appendix G — Glossary (Kanto term ↔ formal term)"),
    ("h_answer_keys", "Appendix H — Consolidated Answer Keys"),
    ("i_risk_primer", "Appendix I — \"Risk and Insurance\" Study-Note Primer"),
]

BOX_TEMPLATES = """\
<!-- ============================================================
     CALLOUT BOX TEMPLATES (Pandoc fenced divs). Delete unused.
     Styled by book/theme.css — see FORMATTING.md sec. 5.
     ============================================================ -->

::: cold-open
**▶ EPISODE**

(250-500 words, second person, present tense. End on the unanswered question
Ash cannot yet solve.)
:::

::: pokedex-entry
**POKÉDEX ENTRY — <concept>**

$$ <formula> $$

*In plain terms:* (one or two sentences, no symbols).

*Recognition cue:* when you see ___, reach for this.
:::

::: trainers-tip
**TRAINER'S TIP**

(1-3 sentences of pure exam craft: a calculator keystroke, a pacing cue, an
archetype tell.)
:::

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

(Jessie/James/Meowth commit the canonical error in-character, ~80-150 words.)

**The fix:** (one sentence naming the error and the guardrail.)
:::

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

(80-160 words connecting the concept to actual actuarial/insurance practice;
name a concrete application. Optional one-line "Series bridge:" pointer.)
:::
"""


def chapter_body(num, slug, title, type_class, topic, outcomes, badge, maps_to) -> str:
    full_title = f"Chapter {num}: {title}"
    return f"""<!--
  chapter: {num}
  slug: {slug}
  topic: {topic}
  outcomes: {outcomes}
  badge: {badge}
  maps_to: {maps_to}
  status: stub
-->
{STUB_MARKER}

# {full_title} {{.{type_class}}}

## Cold Open

*(Episode scene — see template below.)*

## Oak's Briefing — Learning Outcomes

By the end of this chapter you will be able to:

- *(verb)* ... **[Topic {outcomes}]**

> Cross-reference: Appendix F (manual sections + SOA sample questions).

## The Theory (Pokédex Entries)

*(Boxed definitions/theorems/formulas. Each: the entry, plain meaning, recognition cue.)*

## Worked Examples

*(3-5 in-world tasks. Each uses the six-part skeleton: Setup → Archetype tag →
Identify → Trainer's Path → Professor's Path (if it differs) → Check & pitfall.)*

### Worked Example {num}.1 — <title>

**Setup (in-world).** ...

**ARCHETYPE:** *<recognition label>*

**Identify.** ...

**Trainer's Path.** ...

**Check & pitfall.** ...

## Trainer's Tips

## Team Rocket's Trap

## The Gym Battle (Capstone)

*(The chapter's hardest single problem, fully solved.)*

## The Gym Challenge (Problem Set)

> **Test-out instructions.** Think you know this chapter? Work this set timed,
> then check the answer key. Hit the mastery bar (80%+ with correct method) and
> you may skip ahead.

### Route Trainers (mechanics)

### Gym Battles (true SOA difficulty)

### Elite Challenge (integrative / stretch)

## Answer Key

*(Full worked solution per problem, archetype-labeled, back-referenced. Quick-answer
table at the end.)*

## Badge Earned — Mastery Checklist

You earn the **{badge}** when you can, unaided:

1. ...
2. ...
3. ...

> **Gym rematch:** if a checklist item fails, revisit — ...

---

{BOX_TEMPLATES}
"""


def appendix_body(slug, title) -> str:
    return f"""<!--
  appendix: {slug}
  status: stub
-->
{STUB_MARKER}

# {title}

*(Reference content — to be filled by the writing workflow. See DESIGN.md Part 2.)*
"""


def write_if_stub(path: Path, content: str) -> str:
    if path.exists():
        existing = path.read_text()
        if STUB_MARKER not in existing:
            return "skip (has progressed past stub)"
    path.write_text(content)
    return "written"


def main() -> None:
    for c in CHAPTERS:
        num = c[0]
        path = CH_DIR / f"ch{num:02d}_{c[1]}.md"
        status = write_if_stub(path, chapter_body(*c))
        print(f"  ch{num:02d}_{c[1]}.md : {status}")
    for slug, title in APPENDICES:
        path = APX_DIR / f"appendix_{slug}.md"
        status = write_if_stub(path, appendix_body(slug, title))
        print(f"  appendix_{slug}.md : {status}")


if __name__ == "__main__":
    main()
