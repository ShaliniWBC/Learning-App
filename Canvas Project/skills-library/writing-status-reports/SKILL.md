---
name: writing-status-reports
description: "Produces recurring status reports for Cortex Suite by pulling live JIRA sprint data and formatting for the target audience. Use when asked to write a status report, weekly update, manager update, sponsor update, sprint review summary, or product health report."
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

# Writing Status Reports — Cortex Suite

Produces recurring status reports for Westpac's Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat) by pulling live JIRA sprint data and formatting to the target audience's expectations.

## Context

The Product Manager produces multiple recurring reports at different cadences for different audiences. Each has a distinct format, level of detail, and purpose. Reports shall be data-driven — pulled from JIRA boards and sprint data — not manually assembled from memory or anecdote. Every metric shall trace back to a JIRA query, every RAG status shall be justified, and every forward-looking statement shall reference concrete milestones or dates.

## Squads & JIRA Boards

| Squad | Board ID | Project Key | Key People |
|---|---|---|---|
| Cortex Engineering | 106106 | DME | Sasi (Lead Eng), Cooper, Josh, Jolin, Jack, GK, Vinoth |
| Customer Insights DS | 106106 | DME | Tom (Lead DS), Rupa, Simran, Justin, Vivasha, Claudia, Richard |
| Project Hawkeye | 106133 | DME | Peter (Sr BA), Kadeeja (SM), GK, Phil Hood (Exec Mgr) |

## Report Types

| Type | Audience | Cadence | Format | Detail Level | Key Content |
|------|----------|---------|--------|-------------|-------------|
| Weekly LT Update | Leadership Team | Weekly | Bullet-point summary | High-level | Achievements, blockers, upcoming milestones, RAG status per product |
| Fortnightly Manager Update | Jeni (manager) | Fortnightly | Structured narrative | Medium | Sprint health, team capacity, risks, decisions needed, stakeholder pulse |
| Hawkeye Sponsor Update | Programme sponsors | Fortnightly/Monthly | Formal report | Detailed | Programme milestones, budget tracking, risk register, decisions required |
| Sprint Review Summary | Squads + stakeholders | Per sprint | Structured summary | Medium | What was delivered, what carried over, velocity trend, demo highlights |
| Monthly Product Health | LT / GMs (Carolyn McCann, Damian McRae) | Monthly | Dashboard-style | High-level | Product KPIs, quality scores, adoption metrics, roadmap progress |

## Workflow

### Step 1 — Determine Report Type

Before pulling any data, establish:

1. **Which report** is being produced? (See Report Types table above.)
2. **Which period** does it cover? (Sprint number, week ending date, month.)
3. **Any special items** to highlight? (Escalations, wins, personnel changes, stakeholder requests.)

If the user has not specified the report type, ask before proceeding.

### Step 2 — Pull JIRA Data

Fetch sprint data from both boards using these JQL patterns:

```
# Active sprint issues — Board 106106 (Engineering + DS)
project = DME AND sprint in openSprints()

# Active sprint issues — Board 106133 (Hawkeye)
project = DME AND sprint in openSprints()

# Recently completed items (current week)
project = DME AND status changed to Done DURING (startOfWeek(), now())

# Carry-over candidates (closed sprint, not done)
project = DME AND sprint in closedSprints() AND status != Done

# Blockers
project = DME AND status = Blocked
```

When using `jira_get_board_issues`, pass `fields: ["summary", "status", "assignee", "priority", "labels", "sprint", "story_points"]` to minimise payload.

When using `jira_search_issues`, pass `fields: ["summary", "status", "assignee", "priority", "labels", "sprint"]`.

### Step 3 — Calculate Metrics

Compute the following from the JIRA data:

| Metric | Formula | Notes |
|--------|---------|-------|
| Sprint Completion % | (stories Done ÷ stories Committed) × 100 | Count by story, not by story points |
| Velocity | Story points completed per sprint | Track 3-sprint rolling average |
| Carry-over Rate | (stories carried ÷ stories committed) × 100 | Flag if > 20% |
| Blocker Count | Count of issues with status = Blocked | Include duration if available |
| Blocker Resolution Time | Average days from Blocked to unblocked | Use status change history |
| Scope Change Count | Stories added after sprint start | Compare sprint start vs current scope |

### Step 4 — Determine RAG Status

Assign a RAG status per product/initiative using these thresholds:

| RAG | Criteria |
|-----|----------|
| 🟢 Green | On track. No active blockers. Sprint completion ≥ 80%. No scope/timeline risk. |
| 🟡 Amber | Minor risks. 1–2 active blockers. Sprint completion 60–79%. Slight delay (< 1 week). Mitigation in progress. |
| 🔴 Red | Major blockers (≥ 3 or unresolved > 5 days). Sprint completion < 60%. Delay > 1 week. Budget or scope impact. Escalation required. |

Every RAG status shall include a one-sentence justification. Never assign a colour without explanation.

### Step 5 — Draft Report

Read the appropriate template from `reference/status-report-templates.md` and fill in every section. Apply these principles:

- Lead with **outcomes**, not activities ("Delivered API integration for Digital Banker" not "Worked on API").
- Quantify everything possible.
- Name people and JIRA tickets — never "the team" and "various items".
- "No blockers" is a valid and valuable data point — state it explicitly.

### Step 6 — Add Forward Look

Every report shall include a forward-looking section. This section shall never be empty.

- Reference upcoming milestones with dates (DD-MMM-YYYY).
- Note decisions required and from whom.
- Flag risks on the horizon, even if not yet materialised.
- Check the calendar using `outlook_get_calendar_events` for upcoming stakeholder meetings, demos, or deadlines.

### Step 7 — Review & Verify

Before presenting the report, run through the Quality Checklist at the end of this skill. Verify:

- All data points trace to JIRA queries.
- RAG statuses are justified with criteria from Step 4.
- Stakeholder names are spelled correctly.
- Dates are in DD-MMM-YYYY format.
- No placeholder text remains.

## Weekly LT Update Format

The most frequent report. Shall be concise, scannable, and outcome-focused.

```
# Cortex Suite — Weekly Update
**Week Ending:** {DD-MMM-YYYY}
**Author:** {name}

## Overall Status: {🟢/🟡/🔴}
{One-sentence justification for overall RAG.}

### Achievements This Week
- {Outcome-focused bullet — name people, reference JIRA tickets}
- {Outcome-focused bullet — quantify where possible}
- {Outcome-focused bullet}

### In Progress
| Initiative | Status | Owner | Target Date | Notes |
|-----------|--------|-------|-------------|-------|
| {Initiative} | {🟢/🟡/🔴} | {Person} | {DD-MMM-YYYY} | {Brief note} |

### Blockers & Risks
| # | Issue | Impact | Action | Owner | Due |
|---|-------|--------|--------|-------|-----|
| 1 | {Description} | {Impact statement} | {Mitigation action} | {Person} | {DD-MMM-YYYY} |
| — | {If none: "No active blockers this week."} | | | | |

### Upcoming (Next 2 Weeks)
- {DD-MMM-YYYY} — {Milestone or deadline}
- {DD-MMM-YYYY} — {Decision point or deliverable}

### Decisions / Escalations
- {Numbered list of decisions or escalations}
- {If none: "No decisions required this week."}
```

## Fortnightly Manager Update Format

More detailed than the LT update. Provides Jeni with operational visibility and flags items needing her input.

```
# Cortex Suite — Fortnightly Manager Update
**Period:** {DD-MMM-YYYY} to {DD-MMM-YYYY}
**Author:** {name}
**Overall Status:** {🟢/🟡/🔴} — {One-sentence justification}

## Sprint Health Summary

| Squad | Sprint | Committed | Completed | Completion % | Velocity (3-sprint avg) | Carry-over | Trend |
|-------|--------|-----------|-----------|-------------|------------------------|-----------|-------|
| Cortex Engineering | {N} | {X} | {Y} | {Z%} | {V} | {C} | {↑/↓/→} |
| Customer Insights DS | {N} | {X} | {Y} | {Z%} | {V} | {C} | {↑/↓/→} |
| Project Hawkeye | {N} | {X} | {Y} | {Z%} | {V} | {C} | {↑/↓/→} |

## Team & Capacity

| Person | Squad | Status | Notes |
|--------|-------|--------|-------|
| {Name} | {Squad} | {Available / On Leave / Ramping Down} | {Leave dates, constraints} |

{Note any exits, new joiners, or capacity constraints affecting delivery.}

## Key Achievements
- **{Achievement}** — {Description with JIRA reference DME-XXXX}. {Person} delivered {outcome}.
- **{Achievement}** — {Description with JIRA reference DME-XXXX}.

## Risks & Issues

| ID | Description | Likelihood | Impact | RAG | Mitigation | Owner |
|----|-------------|-----------|--------|-----|-----------|-------|
| R1 | {Risk description} | {High/Med/Low} | {High/Med/Low} | {🟢/🟡/🔴} | {Action} | {Person} |

{If none: "No active risks or issues this period."}

## Stakeholder Pulse
- **{Stakeholder/Group}**: {Recent interaction, sentiment, commitments made or requested.}
- **{Stakeholder/Group}**: {Recent interaction, sentiment.}

## Decisions Needed from Manager
1. {Decision description — what, why, options, recommendation}
2. {If none: "No decisions required this period."}

## Forward Look (Next 4 Weeks)
| Date | Milestone / Event | Squad | Notes |
|------|------------------|-------|-------|
| {DD-MMM-YYYY} | {Description} | {Squad} | {Dependencies or risks} |
```

## Hawkeye Sponsor Update Format

Formal programme report for sponsors. Shall be comprehensive and self-contained.

```
# Project Hawkeye — Sponsor Update
**Period:** {DD-MMM-YYYY} to {DD-MMM-YYYY}
**Author:** {name}
**Programme Status:** {🟢/🟡/🔴} — {One-sentence justification}

## Programme Status Dashboard

| Milestone | Target Date | Status | Notes |
|-----------|-------------|--------|-------|
| {Milestone 1} | {DD-MMM-YYYY} | {🟢/🟡/🔴} | {Brief status} |
| {Milestone 2} | {DD-MMM-YYYY} | {🟢/🟡/🔴} | {Brief status} |

## Budget Summary

| Category | Approved | Spent to Date | Forecast | Variance |
|----------|---------|--------------|---------|---------|
| {Category} | ${X} | ${Y} | ${Z} | {+/-$V} |
| **Total** | **${X}** | **${Y}** | **${Z}** | **{+/-$V}** |

## Key Achievements
- {Achievement with JIRA references and named people}
- {Achievement with quantified impact}

## Risk Register

| ID | Risk | Likelihood | Impact | RAG | Mitigation | Owner | Review Date |
|----|------|-----------|--------|-----|-----------|-------|-------------|
| R1 | {Description} | {H/M/L} | {H/M/L} | {🟢/🟡/🔴} | {Action} | {Person} | {DD-MMM-YYYY} |

## Issues Log

| ID | Issue | Raised | Impact | Resolution | Owner | Status |
|----|-------|--------|--------|-----------|-------|--------|
| I1 | {Description} | {DD-MMM-YYYY} | {Impact} | {Action} | {Person} | {Open/Closed} |

{If none: "No open issues this period."}

## Decisions Required from Sponsors
1. **{Decision}**: {Context, options, recommendation, deadline for decision.}
2. {If none: "No sponsor decisions required this period."}

## Next Period Plan
| Activity | Owner | Target Date | Dependencies |
|----------|-------|-------------|-------------|
| {Activity} | {Person} | {DD-MMM-YYYY} | {Dependencies} |
```

## Sprint Review Summary Format

Per-sprint summary for squads and stakeholders. Focuses on delivery and velocity trends.

```
# Sprint Review Summary
**Sprint:** {N}
**Date Range:** {DD-MMM-YYYY} to {DD-MMM-YYYY}
**Squad:** {Squad Name}

## Sprint Goals vs Actuals

| # | Goal | Planned Tickets | Completed | Status |
|---|------|----------------|-----------|--------|
| G1 | {Goal description} | {X} | {Y} | {✅ Met / ⚠️ Partial / ❌ Missed} |
| G2 | {Goal description} | {X} | {Y} | {✅ Met / ⚠️ Partial / ❌ Missed} |

## Velocity Trend (Last 5 Sprints)

| Sprint | Committed (SP) | Completed (SP) | Completion % |
|--------|---------------|----------------|-------------|
| {N-4} | {X} | {Y} | {Z%} |
| {N-3} | {X} | {Y} | {Z%} |
| {N-2} | {X} | {Y} | {Z%} |
| {N-1} | {X} | {Y} | {Z%} |
| {N} | {X} | {Y} | {Z%} |

**3-Sprint Rolling Average:** {V} story points

## Carry-Over Items

| JIRA | Title | Assignee | Reason for Carry-Over |
|------|-------|----------|----------------------|
| DME-XXXX | {Title} | {Person} | {Reason — blocked, scope change, capacity} |

{If none: "No carry-over items. All committed stories were completed."}

## Demo / Showcase Highlights
- **{Feature/Deliverable}**: {What was demonstrated, audience reaction, feedback received.}

## Retrospective Themes (High-Level)
- **What went well:** {Theme}
- **What to improve:** {Theme}
- **Action items:** {Specific action with owner}
```

## Monthly Product Health Format

Dashboard-style report for LT and GMs. Covers all three products at a glance.

```
# Cortex Suite — Monthly Product Health Report
**Month:** {Month YYYY}
**Author:** {name}

## Product Health Dashboard

| Product | Status | Quality Score | Adoption | Roadmap Progress | Key Metric |
|---------|--------|-------------|----------|-----------------|------------|
| Customer Cortex (EDP001) | {🟢/🟡/🔴} | {X/10} | {trend} | {X% of Q milestones} | {e.g., API uptime 99.8%} |
| Customer Interactions (EDP006) | {🟢/🟡/🔴} | {X/10} | {trend} | {X% of Q milestones} | {e.g., data freshness < 4 hrs} |
| Transcat | {🟢/🟡/🔴} | {X/10} | {trend} | {X% of Q milestones} | {e.g., categorisation accuracy 94%} |

## Key Achievements This Month
- {Outcome with quantified impact}
- {Outcome with JIRA references}

## Delivery Metrics

| Metric | This Month | Last Month | Trend | Target |
|--------|-----------|-----------|-------|--------|
| Sprint Completion % | {X%} | {Y%} | {↑/↓/→} | ≥ 80% |
| Velocity (avg SP/sprint) | {X} | {Y} | {↑/↓/→} | {target} |
| Blocker Count | {X} | {Y} | {↑/↓/→} | 0 |
| Carry-over Rate | {X%} | {Y%} | {↑/↓/→} | ≤ 20% |

## Risks & Escalations
| # | Risk / Escalation | Impact | Status | Owner |
|---|------------------|--------|--------|-------|
| 1 | {Description} | {Impact} | {Open/Mitigated/Closed} | {Person} |

{If none: "No active risks or escalations."}

## Roadmap Progress
| Initiative | Q Target | Status | Notes |
|-----------|---------|--------|-------|
| {Initiative} | {Description} | {🟢/🟡/🔴} | {Brief update} |

## Forward Look
- {Key milestones for next month with dates}
- {Decisions or dependencies}
```

## Writing Principles

- **Lead with outcomes, not activities.** "Delivered API integration for Digital Banker" not "Worked on API".
- **Quantify everything possible.** Story points, percentages, days, counts.
- **RAG status must be justified.** Never assign a colour without a one-sentence explanation tied to the thresholds in Step 4.
- **Name people and JIRA tickets.** Never "the team" and "various items". Say "Sasi completed DME-1234" and "Cooper resolved the ADAPT pipeline blocker (DME-1235)".
- **"No blockers" is a valid data point.** State it explicitly — it gives leadership confidence.
- **Forward look shall never be empty.** There is always something on the horizon.
- **Use professional banking language.** No startup jargon. No "disrupt", "pivot", "hustle". Use "shall" for mandatory, "should" for recommended, "may" for optional.
- **All dates in DD-MMM-YYYY format** (e.g., 28-Mar-2026).
- **Use active voice.** Name the actor: "Sasi shall review the schema" not "the schema will be reviewed".

## Architecture Reference

When referencing technical components in reports, use these names:

| Component | Full Name | Notes |
|-----------|-----------|-------|
| ADAPT | ADAPT Data Pipeline | Core ingestion pipeline |
| Snowflake | Snowflake Data Warehouse | Primary analytical store |
| Databricks | Databricks Analytics Platform | ML and analytics workloads |
| ADLS2 | Azure Data Lake Storage Gen2 | Raw and curated data layers |
| Cosmos DB | Azure Cosmos DB | Low-latency API backing store |
| Mesh APIs | Cortex Mesh APIs (Info API, CAP API, GCM) | Consumption layer |

## Quality Checklist

Before presenting any status report, verify:

- [ ] Report type matches what was requested
- [ ] All data points trace to JIRA queries (no invented numbers)
- [ ] RAG statuses are justified with criteria from Step 4
- [ ] Every person named is spelled correctly
- [ ] All dates are in DD-MMM-YYYY format
- [ ] Achievements are outcome-focused, not activity-focused
- [ ] Blockers section is explicit ("No active blockers" or listed with impact)
- [ ] Forward look section is populated — never empty
- [ ] JIRA references use `DME-XXXX` format
- [ ] No placeholder text remains in the output
- [ ] "Shall" / "should" / "may" used correctly for requirement levels
- [ ] Tone matches the target audience (concise for LT, detailed for manager, formal for sponsors)
- [ ] Metrics are calculated using the standard formulas from Step 3
