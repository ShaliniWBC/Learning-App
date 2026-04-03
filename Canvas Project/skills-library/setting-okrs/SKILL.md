---
name: setting-okrs
description: "Drafts, cascades, and scores OKRs for Cortex Suite data products. Use when planning quarterly objectives, reviewing OKR progress, or cascading strategy to squad-level key results."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - Read
  - create_file
  - edit_file
  - task_list
---

# Setting OKRs — Cortex Suite Data Products

Drafts and cascades Objectives and Key Results for Westpac Group's Cortex Suite data products, aligned to the enterprise OKR framework and quarterly planning cadence.

## Context

Westpac Group operates an enterprise OKR framework with a quarterly cadence aligned to the financial year (FY runs October–September). OKRs shall cascade from Group strategy through divisional priorities down to product, squad, and individual levels.

**Product Manager:** Shalini Gangadharan
**Portfolio:** Customer Cortex (EDP001), Customer Interactions (EDP006), Transcat
**Squads:** Cortex Engineering, Customer Insights DS, Project Hawkeye
**Key Stakeholders:** Carolyn McCann (GM), Damian McRae (GM), Lily Zhao (Strategy), Jeni (Manager)
**Architecture:** ADAPT, Snowflake, Databricks, ADLS2, Cosmos DB, Mesh APIs

## OKR Hierarchy

The agent shall respect the following cascade structure. Product OKRs (Shalini's level) shall demonstrably trace upward to divisional OKRs and downward to squad OKRs.

| Level | Owner | Scope | Typical Count |
|---|---|---|---|
| Enterprise Strategy | Group Executive | Westpac Group strategic priorities | 3–5 objectives |
| Divisional OKRs | GM (Carolyn, Damian) | Division-level outcomes | 3–5 objectives |
| Product OKRs | Product Manager (Shalini) | Data product outcomes | 3–5 per product |
| Squad OKRs | Squad Lead | Delivery-aligned outcomes | 2–4 per squad |
| Individual OKRs | Team Member | Personal contribution | 2–3 per person |

## Workflow

### Step 1 — Identify Planning Horizon

The agent shall confirm:
- Which quarter is being planned (e.g., Q2 FY26: Jan–Mar 2026)
- Whether this is a fresh draft, mid-quarter review, or end-of-quarter scoring
- Any known strategic shifts or re-prioritisations

### Step 2 — Gather Strategic Input

The agent shall:
1. Search Confluence for enterprise and divisional OKRs using `mcp__confluence__search_pages` with queries such as "OKR", "strategic priorities", "divisional objectives", and the relevant FY/quarter
2. Retrieve the current product roadmap commitments from Confluence or JIRA
3. Check JIRA for in-flight epics and their status using `mcp__jira__jira_search_issues`
4. Identify any commitments made to stakeholders (Carolyn, Damian, Lily, Jeni) that should be reflected

If strategic input is unavailable, the agent should ask the user to provide or confirm the divisional OKRs before proceeding.

### Step 3 — Draft Objectives

The agent shall draft 3–5 objectives per product, following these principles:
- Each objective shall be **outcome-focused**, not output-focused
- Objectives shall be qualitative, inspirational, and time-bound to the quarter
- Each objective shall clearly trace to a divisional OKR (document the link)
- Objectives shall be ambitious but achievable — stretch targets, not fantasy

### Step 4 — Define Key Results

For each objective, the agent shall define 2–4 key results:
- Each KR shall be **quantitative and measurable** with a specific target value
- Each KR shall include a **baseline** (current state) and a **target** (end-of-quarter goal)
- KRs shall be either binary (achieved/not achieved) or scored on a 0.0–1.0 scale
- KRs shall describe outcomes, not activities or deliverables

### Step 5 — Score and Health Check

The agent shall:
1. Apply the 0.0–1.0 scoring method (see Scoring Definitions below)
2. Assign a health status to each KR based on current or projected score
3. Calculate an overall objective score as the average of its KR scores
4. Flag any objectives where all KRs are below 0.4 for escalation discussion

### Step 6 — Cascade to Squads

The agent shall:
1. Map each product OKR to one or more squad-level OKRs
2. Ensure every product KR has at least one squad-level KR that contributes to it
3. Verify there is no duplication across squads for the same KR
4. Confirm coverage: no product KR should be unowned at squad level

**Squad mapping reference:**
- **Cortex Engineering** — platform reliability, pipeline performance, data freshness, infrastructure
- **Customer Insights DS** — model accuracy, insight adoption, analytical coverage, data quality
- **Project Hawkeye** — monitoring, alerting, anomaly detection, operational intelligence

### Step 7 — Review Narrative

At quarter-end, the agent shall produce a quarterly review narrative containing:
1. Scoring summary table (see OKR Table Format)
2. Highlights — objectives and KRs that met or exceeded targets
3. Misses — objectives and KRs that fell short, with root-cause commentary
4. Learnings — what the team shall carry forward
5. Adjustments — recommended changes for the next quarter's OKRs

## OKR Writing Rules

### Objectives — Shall Be

- **Qualitative:** Describe a desired future state, not a metric
- **Inspirational:** Motivate the team toward meaningful outcomes
- **Time-bound:** Scoped to the quarter
- **Outcome-focused:** Describe the change in the world, not the work done

### Objectives — Shall Not Be

- Output-focused ("Deliver X", "Build Y", "Ship Z")
- Business-as-usual activities dressed up as objectives
- Vague or unmeasurable ("Improve things", "Do better")

### Key Results — Shall Be

- **Quantitative:** Include a number, percentage, or binary pass/fail
- **Measurable:** Verifiable from an existing data source or system
- **Specific:** Include both baseline and target values
- **Outcome-oriented:** Describe the result, not the task

### Key Results — Shall Not Be

- Tasks or activities ("Complete migration", "Attend 5 meetings")
- Unmeasurable ("Improve stakeholder sentiment" without a survey score)
- Binary where a scale would be more informative

### Anti-Patterns to Avoid

| Anti-Pattern | Example | Better Alternative |
|---|---|---|
| KR is a task | "Deploy v2.0 to production" | "Reduce P1 incident rate from 4/month to 1/month" |
| Objective is BAU | "Maintain platform uptime" | "Establish Cortex as the most reliable data platform in the division" |
| Unmeasurable KR | "Improve data quality" | "Increase data quality score from 72% to 90% across EDP001 entities" |
| Sandbagged target | "Achieve 1% adoption increase" | "Grow active consumer count from 12 to 25 across Mesh APIs" |

## OKR Table Format

This is the primary output format. All OKR artefacts shall use this structure:

| Code | Objective / Key Result | Baseline | Target | Score | Status |
|---|---|---|---|---|---|
| **O1** | **[Objective statement]** | — | — | [avg] | [health] |
| O1-KR1 | [Key result statement] | [value] | [value] | [0.0–1.0] | 🟢/🟡/🔴 |
| O1-KR2 | [Key result statement] | [value] | [value] | [0.0–1.0] | 🟢/🟡/🔴 |
| **O2** | **[Objective statement]** | — | — | [avg] | [health] |
| O2-KR1 | [Key result statement] | [value] | [value] | [0.0–1.0] | 🟢/🟡/🔴 |
| O2-KR2 | [Key result statement] | [value] | [value] | [0.0–1.0] | 🟢/🟡/🔴 |

## Scoring Definitions

| Score Range | Health | Indicator | Meaning |
|---|---|---|---|
| 0.7–1.0 | On Track | 🟢 | KR is on pace or achieved; no intervention required |
| 0.4–0.69 | At Risk | 🟡 | KR requires attention; mitigations should be identified |
| 0.0–0.39 | Off Track | 🔴 | KR is unlikely to be met; escalation or scope change required |

**Scoring method:**
- **Binary KRs:** Score 1.0 if achieved, 0.0 if not
- **Scaled KRs:** Score = (Current Value − Baseline) ÷ (Target − Baseline), capped at 1.0
- **Objective score:** Average of its KR scores, rounded to two decimal places

## Quarterly Review Format

```markdown
# OKR Quarterly Review — [Product] — [Quarter] [FY]
**Review Date:** [DD-MMM-YYYY]
**Product Manager:** Shalini Gangadharan

## Scoring Summary
[Insert OKR Table with final scores]

## Overall Health
- Objectives On Track: [count] / [total]
- Objectives At Risk: [count] / [total]
- Objectives Off Track: [count] / [total]

## Highlights
- [Objective/KR that met or exceeded target, with context]

## Misses
- [Objective/KR that fell short, with root-cause analysis]

## Learnings
- [What the team should carry forward to next quarter]

## Adjustments for Next Quarter
- [Recommended changes to objectives, targets, or squad allocation]
```

## Data Product OKR Examples

> **Note:** The following are illustrative examples only. Actual OKRs shall be drafted based on current strategic priorities and real baseline data.

### Customer Cortex (EDP001) — Example

| Code | Objective / Key Result | Baseline | Target | Score | Status |
|---|---|---|---|---|---|
| **O1** | **Establish Customer Cortex as the trusted single source of customer data across the division** | — | — | — | — |
| O1-KR1 | Increase data quality score across core entities from 74% to 92% | 74% | 92% | — | — |
| O1-KR2 | Grow active Mesh API consumer count from 8 to 20 | 8 | 20 | — | — |
| O1-KR3 | Reduce data freshness lag from 24 hours to 4 hours for priority entities | 24h | 4h | — | — |
| **O2** | **Accelerate insight generation for customer-facing decision-making** | — | — | — | — |
| O2-KR1 | Increase the proportion of automated insights consumed by downstream applications from 30% to 60% | 30% | 60% | — | — |
| O2-KR2 | Reduce average time-to-insight for ad hoc analytical requests from 5 days to 2 days | 5d | 2d | — | — |

### Pipeline Reliability — Example

| Code | Objective / Key Result | Baseline | Target | Score | Status |
|---|---|---|---|---|---|
| **O1** | **Deliver enterprise-grade reliability for Cortex data pipelines** | — | — | — | — |
| O1-KR1 | Achieve 99.5% pipeline success rate across Databricks and Snowflake workloads | 96.2% | 99.5% | — | — |
| O1-KR2 | Reduce mean time to recovery for P1 pipeline incidents from 3 hours to 45 minutes | 3h | 45min | — | — |
| O1-KR3 | Decrease unplanned re-processing events from 12/quarter to 3/quarter | 12 | 3 | — | — |

## Quality Checklist

Before finalising any OKR set, the agent shall verify:

- [ ] Every objective traces to a divisional OKR (cascade link documented)
- [ ] Each objective has 2–4 key results
- [ ] Every KR has a baseline and a target value
- [ ] No KR is a task or activity — all are outcomes
- [ ] Objectives are qualitative and outcome-focused, not output-focused
- [ ] Scoring method is defined for each KR (binary or scaled)
- [ ] Squad-level OKRs cover all product KRs without duplication
- [ ] Date format uses DD-MMM-YYYY throughout
- [ ] Language is professional and appropriate for banking context
- [ ] OKR table format is used for all structured output
