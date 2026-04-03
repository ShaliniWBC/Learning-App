---
name: generating-presentations
description: "Structures slide-by-slide presentation content for executive forums, programme updates, sprint reviews, and architecture reviews for Cortex Suite. Use when asked to create a presentation, build slides, prepare a deck, or draft slide content for SteerCo, LT, sprint review, or architecture forum."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - Read
  - create_file
  - edit_file
  - task_list
---

# Presentation Content Skill

Structures slide-by-slide presentation content for executive forums, programme updates, sprint reviews, and architecture reviews for the Cortex Suite of Enterprise Data Products.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite at Westpac Group. She presents at multiple forums — Steering Committee, Leadership Team meetings, sprint reviews, and architecture forums — across three enterprise data products.

Amp cannot create PPTX files directly. This skill produces structured slide-by-slide content in markdown that the PM shall transfer to PowerPoint. Each slide has a clear title, key message, body content, visual guidance, and speaker notes.

| Product | Code | Description |
|---------|------|-------------|
| Customer Cortex | EDP001 | Enterprise 360° customer view (demographics, financials, ML propensity scores, FICO) |
| Customer Interactions | EDP006 | Channel interaction data (branch, digital, CRM, call centre) |
| Transcat | — | Enriched transaction data with merchant categorisation |

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

**Key stakeholders:** Carolyn McCann (GM), Damian McRae (GM), Jeni (Manager), Mandar and Raja (Architects), Lily Zhao (Strategy), Leadership Team.

## Presentation Types

| Type | Audience | Typical Slides | Duration | Tone |
|------|----------|----------------|----------|------|
| SteerCo Update | GMs, executive sponsors | 8–12 slides | 20–30 min | Formal, decision-focused |
| LT Strategic Review | Leadership Team | 6–10 slides | 15–20 min | Strategic, outcome-focused |
| Sprint Review / Demo | Squads + stakeholders | 5–8 slides | 15 min | Collaborative, show-don't-tell |
| Architecture Review | Architects, tech leads | 10–15 slides | 30–45 min | Technical, detailed |
| Investment Proposal | GMs, Finance | 8–12 slides | 20–30 min | Business-case focused |
| Team All-Hands | All squads | 6–10 slides | 15–20 min | Motivational, transparent |

## Workflow

### Step 1 — Determine Presentation Context

Before drafting any slides, establish:

1. **Which forum?** — SteerCo, LT, sprint review, architecture review, investment proposal, or all-hands.
2. **Who is the audience?** — Name specific stakeholders from the table above.
3. **Duration?** — How many minutes are allocated? This determines slide count (~2 minutes per slide).
4. **Key message or decision?** — The single most important thing the audience should take away.
5. **Date of presentation?** — For the title slide and any timeline references.

If the PM does not specify, default to the SteerCo Update format.

### Step 2 — Gather Content

Pull data from available sources in parallel:

- **JIRA**: Active sprint status, blockers, velocity, epic progress for relevant initiatives.
  ```
  mcp__jira__jira_search_issues(jql="project = DME AND sprint in openSprints()", maxResults=50)
  mcp__jira__jira_get_board_issues(boardId=106106, maxResults=50)
  ```
- **Confluence**: Prior updates, decision logs, architecture decision records, programme pages.
  ```
  mcp__confluence__search_pages(query="cortex status update", limit=10)
  ```
- **Other skill outputs**: Use outputs from `presenting-to-executives`, `estimating-costs`, or `modeling-business-cases` as source material when the PM references them.

### Step 3 — Define Slide Sequence

Build the narrative arc for the presentation. Every presentation shall follow a logical flow:

**Setup → Context → Body → Conclusion → Ask**

Select the appropriate narrative structure from the Narrative Structures table below, then map each slide to a position in the arc. Number every slide and note its purpose before drafting content.

### Step 4 — Draft Slide Content

For each slide, produce all four elements:

1. **Title** — states the conclusion, not the topic.
2. **Key Message** — one sentence that captures the "so what" of this slide.
3. **Body Content** — bullet points, tables, or structured text (maximum 5 bullets, maximum 2 lines per bullet).
4. **Speaker Notes** — what the presenter should say (3–5 sentences, adding context beyond the slide).

Use the Slide Content Format below for consistent output.

### Step 5 — Add Data Visualisation Guidance

For each slide that presents data, describe what chart or visual would work best. Do not generate images — describe the visual so the PM can create it in PowerPoint. Reference the Data Visualisation Guidance table below.

### Step 6 — Review

Before presenting the draft, verify:

1. **Narrative flow** — slides tell a coherent story from start to finish.
2. **One-slide-one-message rule** — no slide tries to make two points.
3. **"So what" test** — every slide answers "why does this matter?"
4. **Slide count** — matches allocated time (~2 minutes per slide).
5. **Data context** — every data point has comparison (vs target, vs previous period, vs benchmark).

## Slide Content Format

All slide output shall follow this structure:

```
---
## Slide {N}: {Title — state the conclusion, not the topic}
**Key Message:** {One sentence — the "so what" of this slide}

**Content:**
{Bullet points, tables, or structured text — maximum 5 bullets}

**Visual Guidance:** {What chart/diagram/image would work here — describe for PowerPoint creation}

**Speaker Notes:**
{What to say when presenting this slide — 3–5 sentences that add value beyond the slide content}
---
```

## Narrative Structures

Select the structure that best fits the presentation purpose:

| Structure | Flow | Best For |
|-----------|------|----------|
| Situation–Complication–Resolution (SCR) | Set context → state the problem → present the solution | SteerCo decisions, investment proposals |
| What–So What–Now What | State facts → explain significance → propose action | LT updates, status presentations |
| Problem–Options–Recommendation | Define problem → show options → recommend one | Architecture reviews, vendor decisions |
| Show–Tell–Ask | Demo/evidence → explain → request action | Sprint reviews, showcase presentations |

## Executive Presentation Rules

1. **One slide = one message.** If a second point is needed, add a second slide.
2. **Title states the conclusion, not the topic.** "Customer Cortex adoption grew 23%" — not "Adoption Update."
3. **Maximum 5 bullet points per slide**, maximum 2 lines per bullet.
4. **Every data point needs context** — vs target, vs previous period, vs benchmark.
5. **Tables over paragraphs. Charts over tables** where possible.
6. **Slide numbers and classification footer** on every slide.
7. **Second slide shall be Executive Summary** — the entire presentation in 4–5 bullets.
8. **Penultimate slide shall be Decisions Required / Ask** — clear, numbered, actionable.
9. **No orphan data** — every number shall have a source or reference.
10. **No slide shall exceed readable density** — if the audience cannot absorb it in 2 minutes, split it.

## Standard Slide Templates

Common slide patterns to select from when building the sequence:

| Slide Type | When to Use | Structure |
|------------|-------------|-----------|
| Title Slide | Opening | Presentation title, subtitle, author, date, classification |
| Executive Summary | Second slide | 4–5 bullets summarising the entire presentation |
| RAG Dashboard | Programme status | RAG table with initiatives, status, owner, commentary |
| Options Comparison | Decision slides | Side-by-side table comparing 3–4 options with cost, risk, timeline |
| Timeline / Roadmap | Planning slides | Horizontal timeline with milestones and key dates |
| Financial Summary | Investment slides | Cost/benefit table with totals and variance commentary |
| Risk Matrix | Risk slides | Likelihood × impact matrix or risk register table |
| Ask / Decision Slide | Penultimate | Numbered list of decisions required with clear framing |
| Next Steps | Final content slide | Action, owner, due date table |
| Appendix Divider | Signals detail follows | "Appendix" title with list of what follows |

## Data Visualisation Guidance

When a slide contains data, recommend the appropriate visual:

| Data Type | Recommended Visual | Notes |
|-----------|--------------------|-------|
| Trend over time | Line chart | Maximum 3 series; label endpoints |
| Comparison across categories | Horizontal bar chart | Sorted by value; label bars directly |
| Status across initiatives | RAG table | Colour-coded with commentary column |
| Part-to-whole | Pie chart (max 5 segments) or stacked bar | Avoid 3D effects |
| Process / flow | Flowchart or architecture diagram | Describe for Mermaid rendering if needed |
| Timeline / milestones | Gantt-style or horizontal timeline | Key dates labelled; group by workstream |
| Financial comparison | Grouped bar chart or waterfall chart | Show budget vs actual vs forecast |
| Risk distribution | Heat map (likelihood × impact) | 3×3 or 5×5 grid with initiatives plotted |

## Westpac Presentation Conventions

- Data classification on every slide: Restricted, Confidential, or Internal.
- Slide numbers in footer.
- "Westpac Group" branding context — the PM shall apply corporate template in PPTX.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Currency in AUD with $ prefix.
- Use "shall" for commitments in speaker notes; "should" for recommendations.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- No startup jargon — professional banking language throughout. No "disrupt", "pivot", "hustle", or "move fast and break things."
- Numbers under ten written as words in prose; tables use numerals throughout.
- Percentages always use numerals: "5% improvement", not "five percent improvement."

## Quality Checklist

Before presenting any slide deck draft, verify:

- [ ] Every slide has exactly one key message
- [ ] Narrative flows logically — a reader would understand without the speaker
- [ ] Executive Summary slide captures the full story in 4–5 bullets
- [ ] Ask / Decision slide is specific, numbered, and actionable
- [ ] Data visualisation guidance is practical and appropriate for each data slide
- [ ] Speaker notes add value beyond the slide content (not just repeating bullets)
- [ ] Total slide count matches allocated presentation time (~2 min per slide)
- [ ] No slide has more than 5 bullets or exceeds readable density
- [ ] All dates use DD-MMM-YYYY format
- [ ] Classification footer is noted on every slide
- [ ] Every data point has context (vs target, vs prior period, vs benchmark)
- [ ] Slide titles state conclusions, not topics
- [ ] RAG statuses are justified — Green with open risks is a contradiction
- [ ] No startup jargon — professional banking language throughout
