---
name: writing-executive-memos
description: "Distils Cortex Suite operational progress into 1-page executive memos designed to travel upward through leadership. Use when asked to write an executive memo, leadership summary, upward update, monthly memo, or strategic summary for Jeni, Vicki, Rohith, or Andrew."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__jira__jira_get_sprints
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__outlook__outlook_get_calendar_events
  - Read
  - create_file
  - edit_file
  - task_list
---

# Writing Executive Memos — Cortex Suite

Distils Cortex Suite operational progress into 1-page executive memos designed to travel upward through leadership.

## Context

Executive memos are the key "natural visibility" artefact. They convert messy operational detail into clear strategic narrative. They are designed to be easy for Jeni (Shalini's manager) to include verbatim in her own leadership updates to Vicki Wood (GM), Rohith E (Head of Data), and Andrew McMullen (Group Exec DDAI) — naturally surfacing Shalini's work without requiring promotion.

The format makes leaders forward the memo because it is **useful**, not because it is promotional. A well-crafted executive memo answers the question a leader would ask before they ask it.

CPO/Head of Product roles require the ability to translate delivery into enterprise narrative. This skill builds and demonstrates that capability with every memo produced.

## Memo Principles

1. **One page maximum.** If it needs more, it needs splitting into separate memos.
2. **Lead with "what leaders should care about"** — not what was delivered. The headline answers "so what?", not "what happened?".
3. **Every data point needs context.** A number without context is noise. Always show: vs target, vs last period, or vs benchmark.
4. **Include a forward-looking insight.** What is coming? What decision is approaching? Leaders value foresight over hindsight.
5. **End with a clear ask or "no action required — for awareness".** Every memo shall have an explicit action line. Ambiguity about whether action is needed is unacceptable.
6. **Design for forwarding.** Assume the memo will be read by someone two levels up who has no context. Remove internal jargon, acronyms without definition, and team-specific references that a skip-level would not understand.

## Workflow

### Step 1 — Gather Inputs

Pull data from available sources in parallel:

- **JIRA sprint data**: Active sprint progress, velocity, blockers, completion rates
  ```
  jira_search_issues(jql="project = DME AND sprint in openSprints()", maxResults=50)
  jira_get_board_issues(boardId=106106, maxResults=50)
  jira_get_board_issues(boardId=106133, maxResults=50)
  ```
- **Roadmap progress**: Epic/initiative status, quarterly milestone tracking
- **Adoption metrics**: Consumer count, API call volumes, downstream system integrations
- **Risk/blocker status**: Active blockers, unresolved risks, dependency constraints
- **Stakeholder feedback**: Recent interactions, sentiment, requests received
- **Upcoming milestones**: Calendar events, committed dates, decision points
  ```
  outlook_get_calendar_events(startDate="<today>", endDate="<today+42d>")
  ```

### Step 2 — Identify the "So What"

Ask: **What is the single most important thing leadership should know this period?**

This becomes the headline. It shall not be a summary of activities — it shall be the one insight, outcome, or inflection point that matters most. Test by imagining a GM reading it between meetings: does it tell them something they need to know?

### Step 3 — Frame Strategically

Connect operational progress to enterprise strategy. Every memo shall link delivery to at least one of:

- **Customer outcomes** — how does this improve what customers experience?
- **AI adoption** — how does this advance the Group's AI and data capabilities?
- **Data-driven decisioning** — how does this enable better decisions at scale?
- **Operational efficiency** — how does this reduce cost, time, or risk?

Use the language of enterprise strategy, not project management. "Enabled real-time credit decisioning" not "completed sprint goal."

### Step 4 — Draft the Memo

Use the 6-section format below. Read the reference template from `reference/executive-memo-template.md` for the fillable skeleton.

Fill every section with concrete data. No placeholder text shall remain in the final output. Every claim shall be supported by evidence from JIRA, metrics, or provided context.

### Step 5 — Add the Forward Look

The Forward Look section shall never be empty or generic. It shall contain:

- What is coming in the next 4–6 weeks that leadership should anticipate
- Upcoming decisions that may require leadership input or endorsement
- Risks on the horizon — even if not yet materialised
- Milestones or deliverables approaching committed dates

Generic statements like "continued progress expected" are unacceptable. Be specific: "Cortex API v3 migration completes 15-May-2026; Digital Banker integration testing begins the following sprint."

### Step 6 — Polish

Remove every sentence that does not earn its place. Apply these tests:

- If a bullet can be cut without losing meaning, cut it.
- If a metric lacks context (vs target/trend/benchmark), add context or remove it.
- If the headline is activity-focused, rewrite it as outcome-focused.
- If the Forward Look is generic, make it specific.
- If the Action Required is ambiguous, clarify it.

Read the memo as though you are Andrew McMullen seeing it for the first time between meetings. Does every line tell you something you need to know?

## Memo Format

This is the primary output. One page, six sections, no exceptions.

```
# Cortex Suite — Executive Memo
**Period:** {week/month ending DD-MMM-YYYY}
**Author:** {name} | **Classification:** {Internal/Confidential}

## Headline
{One sentence: the single most important thing.
E.g., "Cortex adoption grew to 5 active consumers this quarter,
with Digital Banker integration reducing customer lookup time by 40%."}

## What Leaders Should Know
{3–5 bullets: strategic progress, outcomes, adoption movement.
Each bullet starts with a bold label.}
- **Adoption:** {metric with trend — e.g., "5 active consumers, up from 3 last quarter"}
- **Delivery:** {key milestone achieved or approaching — with date}
- **Risk:** {top risk with mitigation, or "No material risks this period"}
- **Opportunity:** {growth opportunity identified — what could be unlocked}

## By the Numbers
| Metric | Value | Trend | Context |
|--------|-------|-------|---------|
| {metric name} | {value} | {↑/↓/→} | {vs target / vs last period} |
| {metric name} | {value} | {↑/↓/→} | {vs target / vs last period} |
| {metric name} | {value} | {↑/↓/→} | {vs target / vs last period} |
{3–5 key metrics. Every row shall include context.}

## Forward Look
{2–3 sentences: what is coming in the next 4–6 weeks that leadership
should anticipate. Upcoming decisions, milestones, risks on the horizon.
Shall never be empty or generic.}

## Action Required
{Either a specific ask: "Seeking endorsement for..." / "Decision required by DD-MMM-YYYY on..."
OR "No action required — for awareness only."}
```

## Headline Writing Guide

The headline is the most important sentence in the memo. It determines whether the reader continues or files it.

### Headline Principles

- **Lead with the outcome, not the activity.** What changed, not what was done.
- **Include a number.** "Grew to 5 consumers" not "continued to grow." Specificity builds credibility.
- **Connect to something leadership cares about:** customer outcomes, risk reduction, efficiency gains, strategic capability enablement.
- **Keep it to one sentence.** If it needs two sentences, the memo needs splitting.

### Headline Examples

| ❌ Bad | ✅ Good | Why |
|--------|---------|-----|
| "Cortex Sprint 7 completed successfully" | "Cortex now powers credit decisioning for 3 lending products, replacing legacy FICO dependency" | Outcome vs activity |
| "Team delivered 12 stories this sprint" | "Customer Cortex adoption reached 5 downstream consumers, ahead of Q3 target of 4" | Strategic impact vs velocity |
| "Good progress on data quality" | "Data quality score improved from 7.2 to 8.6/10, driven by automated validation rules in the ADAPT pipeline" | Quantified with mechanism |
| "Transcat work continues" | "Transaction categorisation accuracy reached 94%, enabling the retirement of 2 manual reconciliation processes" | Measurable outcome with business impact |

## How This Creates Visibility

This memo format is engineered for natural upward flow:

- **Jeni can include it verbatim** in her own updates to Vicki, Rohith, and Andrew. No reformatting needed.
- **The "By the Numbers" table is quotable** in leadership meetings — GMs can reference specific metrics without digging through slides.
- **The "Forward Look" positions Shalini as someone thinking ahead**, not just reporting behind. Leaders notice people who anticipate.
- **The "Opportunity" bullet signals growth mindset** to leadership — not just maintaining, but identifying what could be unlocked.
- **The memo format itself signals CPO-level thinking:** strategic, concise, evidence-based. The artefact demonstrates the capability.
- **The "Action Required" line respects leaders' time** — they immediately know whether they need to do something or just absorb.

## Cadence

- **Primary cadence:** Monthly, aligned with Leadership Team reporting cycles.
- **Ad-hoc memos:** Produce for significant milestones, major risks materialising, strategic opportunities identified, or when a decision is needed between regular cycles.
- **Do not produce a memo when there is nothing meaningful to say.** A memo with no substantive content erodes credibility. If the month was steady-state, say so in one line to Jeni directly rather than producing a full memo.

## Squads & Data Sources

| Squad | Board ID | Project Key | Key People |
|---|---|---|---|
| Cortex Engineering | 106106 | DME | Sasi (Lead Eng), Cooper, Josh, Jolin, Jack, GK, Vinoth |
| Customer Insights DS | 106106 | DME | Tom (Lead DS), Rupa, Simran, Justin, Vivasha, Claudia, Richard |
| Project Hawkeye | 106133 | DME | Peter (Sr BA), Kadeeja (SM), GK, Phil Hood (Exec Mgr) |

## Stakeholder Context

| Stakeholder | Role | Why They Read This Memo |
|---|---|---|
| **Jeni Jose Mannanal** | Head of Data (Shalini's manager) | Includes in her own LT updates; needs it ready to forward |
| **Vicki Wood** | GM — DDAI | Scans for strategic progress and risks across her portfolio |
| **Rohith E** | Head of Data — DDAI | Tracks data product maturity and adoption |
| **Andrew McMullen** | Group Exec — DDAI | Looks for enterprise impact, risk, and investment signals |
| **Lu Luc** | Head of AI Services | Interested in AI/ML model integration and adoption |

## Architecture Reference

When referencing technical components, use these names (full name on first use with acronym, then acronym thereafter):

| Component | Full Name | Notes |
|-----------|-----------|-------|
| ADAPT | ADAPT Data Pipeline | Core ingestion pipeline |
| Snowflake | Snowflake Data Warehouse | Primary analytical store |
| Databricks | Databricks Analytics Platform | ML and analytics workloads |
| ADLS2 | Azure Data Lake Storage Gen2 | Raw and curated data layers |
| Cosmos DB | Azure Cosmos DB | Low-latency API backing store |
| Mesh APIs | Cortex Mesh APIs (Info API, CAP API, GCM) | Consumption layer |

## Writing Style

- Use clear, professional language appropriate for banking and financial services.
- Avoid jargon from consumer technology or startup culture. No "disrupt", "pivot", "hustle", "move fast and break things."
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym thereafter.
- Numbers under ten are written as words in prose; tables use numerals throughout.
- Percentages always use numerals: "5% improvement", not "five percent improvement."
- Use active voice. Name the actor: "Sasi delivered the API refactor" not "the API refactor was delivered."

## Quality Checklist

Before presenting any executive memo, verify:

- [ ] Fits on one page — if it exceeds one page, split or cut
- [ ] Headline is outcome-focused, not activity-focused
- [ ] Headline includes at least one number
- [ ] Every metric in "By the Numbers" has context (vs target, vs last period, or vs benchmark)
- [ ] "What Leaders Should Know" has 3–5 bullets, each with a bold label
- [ ] Forward Look is specific — no generic "continued progress expected"
- [ ] Forward Look references dates in DD-MMM-YYYY format
- [ ] Action Required is explicit — either a specific ask or "no action required"
- [ ] Designed for forwarding — no internal jargon a skip-level would not understand
- [ ] Every claim has supporting evidence (JIRA data, metrics, or stated source)
- [ ] Stakeholder names are current and correctly spelled
- [ ] All dates use DD-MMM-YYYY format
- [ ] "Shall" / "should" / "may" used correctly for requirement levels
- [ ] No placeholder text remains in the output
- [ ] Professional banking language — no startup jargon
