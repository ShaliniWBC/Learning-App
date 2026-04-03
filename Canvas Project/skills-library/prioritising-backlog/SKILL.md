---
name: prioritising-backlog
description: "Scores and prioritises product backlog items for Cortex Suite using WSJF, RICE, MoSCoW, and value-effort frameworks. Use when asked to prioritise the backlog, rank items, run a backlog refinement, or prepare prioritised input for sprint planning."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__jira__jira_get_sprints
  - mcp__jira__jira_get_transitions
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - Read
  - create_file
  - edit_file
  - task_list
---

# Prioritising Backlog — Cortex Suite Data Products

Scores and prioritises product backlog items for Westpac's Cortex Suite of Enterprise Data Products, applying structured frameworks to produce stack-ranked backlogs that feed into sprint planning and quarterly roadmap decisions.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite within Westpac Group's DDAI (Data Digital and AI) Division. Shalini manages three product backlogs across two JIRA boards, requiring structured prioritisation to ensure the highest-value work enters each sprint.

**Products:**

- **Customer Cortex (EDP001)** — enterprise 360° customer data product
- **Customer Interactions (EDP006)** — channel interaction and engagement data product
- **Transcat** — transaction categorisation capability

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

**Downstream consumers:** Digital Banker, Unity, WLive, AEP (Adobe Experience Platform), Salesforce (being decommissioned).

Backlog refinement is a recurring activity — weekly or bi-weekly — and shall produce a prioritised, scored list of items ready for sprint planning. Cross-product prioritisation is common, as items from different products compete for the same squad capacity.

### Squads & JIRA Boards

| Squad | Board ID | Project Key | Lead |
|---|---|---|---|
| Cortex Engineering | 106106 | DME | Sasi (Lead Eng) |
| Customer Insights DS | 106106 | DME | Tom (Lead DS) |
| Project Hawkeye | 106133 | DME | — |

**Team members:** Cooper, Josh, Jolin, Jack, GK (Engineering); Rupa, Simran, Justin, Vivasha, Claudia, Richard (DS); Peter (Sr BA); Kadeeja (SM); Vinoth.

## Prioritisation Frameworks

Select the appropriate framework based on the prioritisation context. The agent shall recommend the best fit but defer to the PM's preference.

| Framework | Best For | Inputs Required | Output |
|---|---|---|---|
| **WSJF** (Weighted Shortest Job First) | SAFe-aligned comparison of items of different sizes; cross-product backlog ranking | Business Value, Time Criticality, Risk Reduction, Job Size | Priority score per item |
| **RICE** (Reach, Impact, Confidence, Effort) | Consumer-facing features; data product enhancements with measurable reach | Reach, Impact (1–3), Confidence (%), Effort (person-sprints) | Priority score per item |
| **MoSCoW** (Must/Should/Could/Won't) | Sprint-level scope decisions; time-boxed delivery planning | Stakeholder input, dependencies, deadline constraints | Categorised list |
| **Value vs Effort** (2×2 Quadrant) | Quick visual prioritisation for planning sessions; stakeholder alignment | Relative value, relative effort | Quadrant placement |

When in doubt, default to **WSJF** for cross-product backlog prioritisation and **MoSCoW** for sprint-level scope decisions.

## Workflow

### Step 1 — Scope the Prioritisation

Before scoring, the agent shall clarify:

1. **Which board(s)?** Board 106106 (Cortex Engineering + Customer Insights DS), Board 106133 (Project Hawkeye), or both.
2. **Backlog scope:** Single product (EDP001, EDP006, or Transcat), cross-product, or a specific epic.
3. **Planning horizon:** Next sprint, next two sprints, or quarterly.
4. **Framework preference:** WSJF, RICE, MoSCoW, Value vs Effort, or agent recommendation.
5. **Constraints:** Known deadlines, regulatory mandates, capacity limitations.

### Step 2 — Pull Backlog Items

Fetch candidate items from JIRA:

```
mcp__jira__jira_search_issues(
  jql="project = DME AND status in ('To Do', 'Open', 'Backlog') AND issuetype in (Story, Task, Bug)",
  fields=["summary", "priority", "labels", "story points", "assignee", "sprint", "epic"],
  maxResults=50
)
```

For board-specific pulls:

```
mcp__jira__jira_get_board_issues(boardId=106106, fields=["summary", "status", "assignee", "priority", "labels", "sprint"])
mcp__jira__jira_get_board_issues(boardId=106133, fields=["summary", "status", "assignee", "priority", "labels", "sprint"])
```

### Step 3 — Enrich Items

For each backlog item, the agent shall identify:

| Enrichment Field | Source | Purpose |
|---|---|---|
| **Business value driver** | PM input, labels, epic context | Determines scoring weight |
| **Requesting stakeholder** | JIRA reporter, linked Confluence pages | Identifies accountability |
| **Dependencies** | Linked issues, blockers in JIRA | Affects sequencing |
| **Deadline constraints** | Labels, fix versions, stakeholder commitments | Identifies non-discretionary items |
| **Downstream consumer impact** | Labels, product mapping | Determines reach |
| **Technical complexity** | Story points, assignee expertise | Informs effort estimates |

Items with regulatory or contractual deadlines shall be flagged as **Non-discretionary** and placed at the top of the backlog regardless of score.

### Step 4 — Apply Framework

Score each item using the selected framework (see detailed scoring models below). For each item, the agent shall:

1. Assign scores for each framework component.
2. Calculate the composite priority score.
3. Document the scoring rationale — a brief explanation of why each score was assigned.

Present the scored list to the PM before proceeding to stack ranking.

### Step 5 — Stack Rank

Produce an ordered list with scores, grouped by priority tier:

| Tier | Score Range (WSJF) | Score Range (RICE) | Meaning |
|---|---|---|---|
| **P1 Critical** | ≥ 5.0 | Top 10% | Must be in the next sprint; delay has material business impact |
| **P2 High** | 3.0–4.9 | Next 20% | Should be in the next 1–2 sprints |
| **P3 Medium** | 1.5–2.9 | Next 30% | Important but can wait 2–3 sprints |
| **P4 Low** | < 1.5 | Bottom 40% | Backlog — schedule when capacity allows |

Non-discretionary items bypass scoring but shall still be tier-assigned for sequencing purposes.

### Step 6 — Identify Conflicts

The agent shall scan for and flag:

| Conflict Type | Detection Method | Resolution Guidance |
|---|---|---|
| **High score + blocker** | Item scores P1/P2 but has open blockers | Escalate blocker; consider unblocking work as priority |
| **Conflicting stakeholder priorities** | Two stakeholders request conflicting items for the same sprint | Present trade-off to PM with scoring rationale |
| **Capacity constraint** | Total committed points exceed squad velocity | Defer lowest-tier items; flag capacity gap |
| **Cross-squad dependency** | Item requires work from multiple squads | Coordinate sequencing; flag in sprint planning |
| **Resource contention** | Same person assigned to multiple P1 items | Recommend primary/secondary assignment |

### Step 7 — Produce Recommendation

The agent shall produce a final prioritisation document containing:

1. **Prioritised backlog** — scored, ranked, and tiered (see output format below).
2. **Items recommended for next sprint** — with rationale for inclusion.
3. **Items to defer** — with reasons (capacity, dependencies, lower priority).
4. **Conflicts and trade-offs** — flagged items requiring PM decision.
5. **Backlog health indicators** — metrics on overall backlog state.

Save the output as a markdown file named `Backlog-Prioritisation-{scope}-{DD-MMM-YYYY}.md` in the workspace root (or a location the PM specifies).

## WSJF Scoring Model

**WSJF Score = (Business Value + Time Criticality + Risk Reduction) ÷ Job Size**

| Component | Scale | Definition |
|---|---|---|
| **Business Value** | 1–13 (Fibonacci) | Revenue impact, customer value, strategic alignment. 1 = marginal business impact; 13 = critical to enterprise strategy or major revenue driver |
| **Time Criticality** | 1–13 (Fibonacci) | Deadline pressure, cost of delay, competitive urgency. 1 = fully flexible timeline; 13 = immovable regulatory or contractual deadline |
| **Risk Reduction / Opportunity Enablement** | 1–13 (Fibonacci) | Technical risk reduction, platform enablement, unblocks other work. 1 = no risk reduction; 13 = eliminates critical technical debt or unblocks multiple initiatives |
| **Job Size** | 1–13 (Fibonacci) | Estimated effort in story points or person-days. 1 = trivial (< 1 day); 13 = very large (> 2 sprints of dedicated effort) |

**Scoring guidance:**

- Use Fibonacci values (1, 2, 3, 5, 8, 13) to force meaningful differentiation.
- Score components independently — do not let one dimension influence another.
- A high WSJF score means the item delivers disproportionate value relative to its size.
- Items with Job Size = 1 should be scrutinised — they may be quick wins or may be under-estimated.

**WSJF Scoring Table:**

| # | JIRA | Title | Product | Business Value | Time Criticality | Risk Reduction | CoD | Job Size | WSJF | Rank |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | DME-XXXX | {Title} | {Product} | {BV} | {TC} | {RR} | {BV+TC+RR} | {JS} | {CoD÷JS} | {rank} |

## RICE Scoring Model

**RICE Score = (Reach × Impact × Confidence) ÷ Effort**

| Component | Scale | Definition |
|---|---|---|
| **Reach** | Count per quarter | Number of downstream consumers, users, or use cases affected. E.g., 5 downstream systems, 200 analysts, 50,000 end customers |
| **Impact** | Multiplier | 3 = Massive (transformative change); 2 = High (significant improvement); 1 = Medium (noticeable improvement); 0.5 = Low (minor improvement); 0.25 = Minimal (barely perceptible) |
| **Confidence** | Percentage | 100% = High (validated with data); 80% = Medium (informed estimate); 50% = Low (speculative or early-stage) |
| **Effort** | Person-sprints | Total effort required. 1 person-sprint = 1 person × 1 sprint (2 weeks). E.g., 2 people for 3 sprints = 6 person-sprints |

**RICE Scoring Table:**

| # | JIRA | Title | Product | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---|---|---|---|---|---|---|---|---|---|
| 1 | DME-XXXX | {Title} | {Product} | {R} | {I} | {C%} | {E} | {R×I×C÷E} | {rank} |

## MoSCoW Categorisation

Apply MoSCoW when making sprint-level scope decisions within a fixed time-box.

| Category | Definition | Decision Rule |
|---|---|---|
| **Must Have** | Non-negotiable for the sprint/release. Failure to deliver makes the sprint a failure. | Regulatory mandates, contractual commitments, items blocking critical downstream work |
| **Should Have** | Important but the sprint is still viable without them. High value, high urgency. | High-scoring WSJF/RICE items that fit within remaining capacity |
| **Could Have** | Desirable if capacity allows. Lower urgency or value. | Items that improve quality of life but are not time-critical |
| **Won't Have (this time)** | Explicitly out of scope for this sprint. Acknowledged and deferred. | Items that were considered but did not make the cut — document the reason |

**MoSCoW Output Table:**

| Category | JIRA | Title | Product | Rationale |
|---|---|---|---|---|
| **Must** | DME-XXXX | {Title} | {Product} | {Why it is non-negotiable} |
| **Should** | DME-XXXX | {Title} | {Product} | {Why it is important} |
| **Could** | DME-XXXX | {Title} | {Product} | {Why it is desirable} |
| **Won't** | DME-XXXX | {Title} | {Product} | {Why it is deferred} |

## Value vs Effort Quadrant

Use for quick visual prioritisation during planning sessions or stakeholder alignment meetings.

```
                        HIGH VALUE
                            │
            Q1: Quick Wins  │  Q2: Strategic Bets
            Do first        │  Plan carefully
            ────────────────┼────────────────
            Q3: Fill-ins    │  Q4: Deprioritise
            Do if capacity  │  Defer or drop
            allows          │
                            │
                        LOW VALUE
          LOW EFFORT ◄──────┼──────► HIGH EFFORT
```

| Quadrant | Value | Effort | Action | Guidance |
|---|---|---|---|---|
| **Q1 — Quick Wins** | High | Low | Do first | Immediate value with minimal investment. Schedule in the current or next sprint. |
| **Q2 — Strategic Bets** | High | High | Plan carefully | Significant value but requires substantial investment. Break into smaller deliverables; sequence across sprints. |
| **Q3 — Fill-ins** | Low | Low | Do if capacity allows | Low risk, low reward. Use to fill sprint capacity gaps or assign to ramping team members. |
| **Q4 — Deprioritise** | Low | High | Defer or drop | Poor return on investment. Defer indefinitely or remove from the backlog. |

**Value vs Effort Output Table:**

| # | JIRA | Title | Product | Value (H/M/L) | Effort (H/M/L) | Quadrant | Action |
|---|---|---|---|---|---|---|---|
| 1 | DME-XXXX | {Title} | {Product} | {H/M/L} | {H/M/L} | {Q1/Q2/Q3/Q4} | {Recommendation} |

## Prioritised Backlog Output Format

This is the primary output table. All prioritisation artefacts shall include this structure:

| Rank | JIRA | Title | Product | Score | Framework | Tier | Dependencies | Recommended Sprint | Rationale |
|---|---|---|---|---|---|---|---|---|---|
| 1 | DME-XXXX | {Title} | {Product} | {score} | {WSJF/RICE} | P1 Critical | {Dependency list} | Sprint {N} | {Brief scoring rationale} |
| 2 | DME-XXXX | {Title} | {Product} | {score} | {WSJF/RICE} | P1 Critical | None | Sprint {N} | {Rationale} |
| 3 | DME-XXXX | {Title} | {Product} | {score} | {WSJF/RICE} | P2 High | {Dependencies} | Sprint {N+1} | {Rationale} |

## Backlog Health Indicators

The agent shall assess and report on overall backlog health using these metrics:

| Indicator | Healthy | Warning | Action Required |
|---|---|---|---|
| **Total backlog items** | < 100 | 100–200 | > 200: conduct bulk grooming session; archive stale items |
| **Items with no priority set** | < 5% of backlog | 5–20% | > 20%: schedule bulk triage session |
| **Items untouched > 6 months** | < 10 items | 10–30 | > 30: review for relevance; close or re-scope |
| **Items with no assignee** | Acceptable for backlog items | Flag for sprint candidates | Sprint candidates must have an assignee before commitment |
| **Items with no story points** | Acceptable for backlog items | Flag for sprint candidates | Must be sized before entering a sprint |
| **Items with no epic link** | < 10% | 10–25% | > 25%: items may be orphaned; link to epics or archive |
| **Bug-to-feature ratio** | < 20% bugs | 20–40% bugs | > 40%: quality issues require dedicated remediation sprint |

**Backlog Health Summary:**

| Metric | Current Value | Status | Recommendation |
|---|---|---|---|
| Total items | {count} | {🟢/🟡/🔴} | {Action if needed} |
| No priority | {count} ({%}) | {🟢/🟡/🔴} | {Action if needed} |
| Stale (> 6 months) | {count} | {🟢/🟡/🔴} | {Action if needed} |
| Unsized | {count} ({%}) | {🟢/🟡/🔴} | {Action if needed} |
| No epic link | {count} ({%}) | {🟢/🟡/🔴} | {Action if needed} |
| Bug ratio | {%} | {🟢/🟡/🔴} | {Action if needed} |

## Refinement Session Guide

### Pre-Session Preparation

The agent shall prepare the following before a refinement session:

1. Pull the current backlog using the JQL queries in Step 2.
2. Pre-score the top 15–20 candidate items using the selected framework.
3. Identify items requiring discussion (ambiguous scope, missing information, conflicting priorities).
4. Prepare the backlog health summary.
5. Flag any items approaching deadline constraints.

### During the Session

1. Review the top 10–15 items with the PM and squad leads.
2. Score collaboratively — present pre-scores and adjust based on team input.
3. Identify cross-squad dependencies and flag for coordination.
4. Size unsized items (story points) — items entering a sprint shall have estimates.
5. Apply MoSCoW for sprint-level scope decisions if the session feeds directly into sprint planning.

### Post-Session Actions

1. Update JIRA priorities to reflect agreed scoring and ranking.
2. Communicate changes to affected stakeholders.
3. Feed the prioritised backlog into the sprint planning skill.
4. Archive or close items agreed for removal.
5. Document decisions and rationale in the output artefact.

## Cortex-Specific Prioritisation Factors

Beyond framework scores, the agent shall consider these Cortex-specific factors when recommending priorities:

| Factor | Weight | Guidance |
|---|---|---|
| **Downstream consumer impact** | High | Items affecting Digital Banker, Unity, WLive, or AEP should receive higher Reach/Business Value scores. More consumers affected = higher priority. |
| **Regulatory / compliance deadlines** | Non-negotiable | Regulatory items bypass scoring and are automatically P1. Flag with deadline and mandate source. |
| **Platform dependencies** | Medium–High | ADAPT changes, Snowflake migrations, or Databricks upgrades may block multiple items. Prioritise the unblocking work. |
| **Data quality impact** | High | Items that improve data quality across multiple consumers should score higher on Risk Reduction / Opportunity Enablement. |
| **Salesforce decommissioning** | Time-critical | Items related to Salesforce migration have a fixed timeline. Score Time Criticality accordingly. |
| **Cross-product enablement** | Medium | Items in EDP001 that unblock EDP006 or Transcat should receive higher Risk Reduction scores. |
| **Technical debt reduction** | Medium | Prioritise if debt is causing production incidents or slowing delivery velocity. |

## JIRA Queries

Use these JQL patterns to gather backlog data:

```
# All open backlog items
project = DME AND status in ("To Do", "Open", "Backlog") AND issuetype in (Story, Task, Bug)

# Backlog items by product label
project = DME AND status in ("To Do", "Open", "Backlog") AND labels = "customer-cortex"
project = DME AND status in ("To Do", "Open", "Backlog") AND labels = "customer-interactions"
project = DME AND status in ("To Do", "Open", "Backlog") AND labels = "transcat"

# Items with no priority set
project = DME AND priority = None AND status != Done

# Stale items (created more than 180 days ago, not updated)
project = DME AND status in ("To Do", "Open", "Backlog") AND updated <= -180d

# Items with no story points
project = DME AND "Story Points" is EMPTY AND status in ("To Do", "Open", "Backlog")

# Items approaching a fix version deadline
project = DME AND fixVersion is not EMPTY AND status in ("To Do", "Open", "Backlog")
```

When using `jira_search_issues` or `jira_get_board_issues`, pass `fields: ["summary", "status", "assignee", "priority", "labels", "fixVersions", "sprint", "story points"]` to minimise payload.

## Quality Checklist

Before presenting the prioritised backlog, the agent shall verify:

- [ ] Prioritisation scope is confirmed (board, product, horizon)
- [ ] Framework selection is justified and agreed with the PM
- [ ] Every scored item has a documented rationale — not just a number
- [ ] Non-discretionary items (regulatory, contractual) are flagged and placed at the top
- [ ] Scoring uses the correct scale for the selected framework
- [ ] Stack ranking is consistent with scores — no manual overrides without documented reason
- [ ] Dependencies are identified and sequencing is valid
- [ ] Backlog health indicators are assessed and reported
- [ ] Conflicts and trade-offs are flagged for PM decision
- [ ] Items recommended for sprint have assignees and story point estimates
- [ ] Deferred items have clear reasons for deferral
- [ ] All dates use DD-MMM-YYYY format
- [ ] Language is professional and appropriate for banking context — no startup jargon
- [ ] Output follows the Prioritised Backlog Output Format table structure
