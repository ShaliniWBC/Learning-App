---
name: managing-roadmaps
description: "Builds and maintains product roadmaps for Cortex Suite enterprise data products across strategic, tactical, and delivery views. Use when asked to create a roadmap, prioritise initiatives, plan quarters, map dependencies, or produce a Now/Next/Later view."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__jira__jira_get_sprints
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - Read
  - create_file
  - edit_file
  - task_list
---

# Managing Roadmaps for Cortex Suite

Builds and maintains product roadmaps for Westpac's Cortex Suite of Enterprise Data Products — spanning strategic half-yearly views through to sprint-level delivery plans.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite within Westpac Group's Enterprise Data & Analytics function. The Cortex Suite comprises:

- **Customer Cortex (EDP001)** — enterprise customer data product
- **Customer Interactions (EDP006)** — interaction and engagement data product
- **Transcat** — transaction categorisation capability

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

**Downstream consumers:** Digital Banker, Unity, WLive, AEP (Adobe Experience Platform), Salesforce (being decommissioned).

Enterprise data product roadmaps operate on quarterly planning cycles and shall align with Westpac's enterprise data strategy. Roadmaps must reflect cross-product dependencies, platform constraints, and the needs of multiple downstream consumer groups.

### Squads & JIRA Boards

| Squad | Board ID | Project Key | Lead |
|---|---|---|---|
| Cortex Engineering | 106106 | DME | Sasi (Lead Eng) |
| Customer Insights DS | 106106 | DME | Tom (Lead DS) |
| Project Hawkeye | 106133 | DME | — |

**Team members:** Cooper, Josh, Jolin, Jack, GK (Engineering); Rupa, Simran, Justin, Vivasha, Claudia, Richard (DS); Peter (Sr BA); Kadeeja (SM); Vinoth.

### Key Stakeholders

| Stakeholder | Role | Roadmap Interest |
|---|---|---|
| **Carolyn McCann** | General Manager | Strategic alignment, investment priority |
| **Damian McRae** | General Manager | Delivery confidence, resource allocation |
| **Jeni** | Shalini's Manager | Quarterly planning, capacity, risks |
| **Mandar** | Architect | Architecture feasibility, platform roadmap |
| **Raja** | Architect | Technical standards, integration patterns |
| **Lily Zhao** | Strategy Team | Enterprise strategy alignment, investment cases |

## Roadmap Views

| View | Time Horizon | Audience | Granularity | Refresh Cadence |
|---|---|---|---|---|
| **Strategic** | 6–12 months | GMs, LT, Strategy (Carolyn, Damian, Lily) | Initiative-level | Half-yearly |
| **Tactical** | Current + next quarter | Squad leads, architects (Sasi, Tom, Mandar, Raja) | Epic-level | Quarterly |
| **Delivery** | Current + next sprint | Engineers, data scientists | Story-level | Per sprint |
| **Stakeholder** | Tailored per consumer | Downstream consumer teams (Digital Banker, Unity, WLive, AEP) | Feature-level | As requested |

Select the appropriate view based on the audience and purpose. A single request may require multiple views.

## Workflow

### Step 1 — Determine Roadmap Type

Before building, clarify:

1. **Which view?** Strategic, Tactical, Delivery, or Stakeholder (see table above).
2. **Time horizon?** Current quarter, next quarter, half-year, or full year.
3. **Audience?** Name specific stakeholders or consumer groups.
4. **Which products?** All Cortex Suite, single product, or cross-product.
5. **Purpose?** Quarterly planning, SteerCo input, stakeholder alignment, dependency mapping.

### Step 2 — Gather Current State

Pull data from available sources in parallel:

- **JIRA epics and sprints:**
  ```
  mcp__jira__jira_search_issues(jql="project = DME AND issuetype = Epic AND status != Done", maxResults=50)
  mcp__jira__jira_get_board_issues(boardId=106106, maxResults=50)
  mcp__jira__jira_get_board_issues(boardId=106133, maxResults=50)
  mcp__jira__jira_get_sprints(boardId=106106, state="active")
  mcp__jira__jira_get_sprints(boardId=106133, state="active")
  ```

- **Confluence strategy documents:**
  ```
  mcp__confluence__search_pages(query="cortex roadmap", limit=10)
  mcp__confluence__search_pages(query="cortex strategy", limit=10)
  mcp__confluence__search_pages(query="data product quarterly plan", limit=10)
  ```

- **Current roadmap artefacts:** Check workspace for existing roadmap files.

Compile: active epics, their status (RAG), assigned squad, current sprint placement, and any documented strategic themes.

### Step 3 — Prioritise Initiatives

Apply RICE or WSJF (see Prioritisation Frameworks below). For each candidate initiative:

1. Score using the selected framework.
2. Rank by composite score, highest first.
3. Note any mandatory items (regulatory, contractual) that override scoring — mark these as **Non-discretionary**.

Present the scored and ranked list before proceeding to time-horizon allocation.

### Step 4 — Map Dependencies

For each initiative, identify:

| Dependency Type | Description | Example |
|---|---|---|
| **Cross-product** | Between Cortex products | EDP006 enrichment depends on EDP001 entity resolution |
| **Cross-team** | Between squads | DS model requires Engineering pipeline changes |
| **Platform** | Infrastructure or architecture | Databricks cluster upgrade required before streaming work |
| **External** | Outside Cortex team | Digital Banker API version upgrade blocks consumption |
| **Data source** | Upstream feed changes | Core Banking schema migration affects ingestion |

Express dependencies as: `{Initiative A} → blocks → {Initiative B}` with a brief description.

### Step 5 — Allocate to Time Horizons

Use the Now/Next/Later framework (see section below) to bucket initiatives:

1. **Now** — current quarter: committed work, resourced, in-flight or ready to start.
2. **Next** — next quarter: scoped, prioritised, dependencies identified, not yet resourced.
3. **Later** — future quarters: directionally agreed, not yet scoped in detail.

Validate allocation against:
- Squad capacity (available people × sprint velocity)
- Dependency sequencing (blocked items cannot be in "Now" if blocker is in "Next")
- Strategic priority (higher-scored items should appear earlier)

### Step 6 — Draft the Roadmap

Read the reference template at `reference/roadmap-template.md` and populate all sections with concrete data. The output shall follow the Roadmap Structure defined below.

Save the completed roadmap as a markdown file named `Roadmap-{Product/Suite}-{Quarter}-v{X.Y}.md` in the workspace root (or a location the PM specifies).

### Step 7 — Identify Conflicts

Before presenting, scan for:

| Conflict Type | Detection Method |
|---|---|
| **Capacity overload** | Total committed story points > squad velocity × available sprints |
| **Dependency clash** | Initiative A depends on B, but A is scheduled before B |
| **Deadline risk** | Committed delivery date at risk based on current velocity |
| **Resource contention** | Same person assigned as primary on two parallel initiatives |
| **Scope creep** | More items in "Now" than capacity supports |

Flag each conflict with a recommended resolution.

## Prioritisation Frameworks

### RICE Framework

**Reach × Impact × Confidence ÷ Effort = RICE Score**

| Factor | Definition (Data Product Context) | Scale |
|---|---|---|
| **Reach** | Number of downstream consumers or use cases affected per quarter | Count (e.g., 5 downstream systems, 200 analysts) |
| **Impact** | Degree of improvement for each reached consumer | 3 = Massive, 2 = High, 1 = Medium, 0.5 = Low, 0.25 = Minimal |
| **Confidence** | How certain are we about Reach, Impact, and Effort estimates? | 100% = High, 80% = Medium, 50% = Low |
| **Effort** | Person-sprints required to deliver (1 person-sprint = 1 person × 1 sprint) | Numeric (e.g., 6 person-sprints) |

**RICE Scoring Table:**

| # | Initiative | Product | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---|---|---|---|---|---|---|---|---|
| 1 | {Initiative} | {Product} | {R} | {I} | {C%} | {E} | {R×I×C÷E} | {rank} |

### WSJF Framework

**Cost of Delay ÷ Job Duration = WSJF Score**

| Factor | Definition (Data Product Context) | Scale |
|---|---|---|
| **Business Value** | Revenue impact, cost avoidance, or strategic importance | 1 (Low) – 10 (Critical) |
| **Time Criticality** | Regulatory deadline, market window, or stakeholder commitment | 1 (Flexible) – 10 (Immovable deadline) |
| **Risk Reduction / Opportunity Enablement** | Reduces technical debt, unblocks other initiatives, or enables future capabilities | 1 (Marginal) – 10 (Transformative) |
| **Cost of Delay** | Business Value + Time Criticality + Risk Reduction | Sum of above three |
| **Job Duration** | Relative size in sprints | 1 (XS, 1 sprint) – 10 (XL, 10+ sprints) |

**WSJF Scoring Table:**

| # | Initiative | Product | Business Value | Time Criticality | Risk Reduction | CoD | Job Duration | WSJF | Rank |
|---|---|---|---|---|---|---|---|---|---|
| 1 | {Initiative} | {Product} | {BV} | {TC} | {RR} | {CoD} | {JD} | {CoD÷JD} | {rank} |

## Roadmap Structure

The output roadmap shall contain these sections in order:

### 1. Header

| Field | Value |
|---|---|
| **Product** | {Cortex Suite / Customer Cortex / Customer Interactions / Transcat} |
| **Period** | {Q1 FY26 / H1 FY26 / etc.} |
| **View** | {Strategic / Tactical / Delivery / Stakeholder} |
| **Author** | Shalini Gangadharan, Product Manager — Cortex Suite |
| **Version** | {X.Y} |
| **Date** | {DD-MMM-YYYY} |
| **Status** | {Draft / In Review / Approved} |

### 2. Strategic Themes

List three to five themes that anchor the roadmap for the period. Each theme shall have a one-line description and link to the enterprise strategy.

| # | Theme | Description | Strategic Alignment |
|---|---|---|---|
| T1 | {Theme Name} | {One-line description} | {Link to enterprise strategy pillar} |

### 3. Initiative Table

| # | Initiative | Product | Priority Score | Framework | Quarter | Squad | Owner | Dependencies | Status | JIRA Epic |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {score} | {RICE/WSJF} | {Q} | {Squad} | {Person} | {Dependency list} | {🟢/🟡/🔴} | DME-XXXX |

### 4. Dependency Map

Text-based description of cross-initiative dependencies:

```
{Initiative A} → blocks → {Initiative B} : {reason}
{Initiative C} → blocks → {Initiative D} : {reason}
{External: Platform Upgrade} → blocks → {Initiative E} : {reason}
```

### 5. Capacity Summary

| Squad | Available Sprints | Velocity (avg pts/sprint) | Total Capacity (pts) | Committed (pts) | Utilisation | Buffer |
|---|---|---|---|---|---|---|
| Cortex Engineering | {N} | {V} | {N×V} | {committed} | {%} | {remaining} |
| Customer Insights DS | {N} | {V} | {N×V} | {committed} | {%} | {remaining} |
| Project Hawkeye | {N} | {V} | {N×V} | {committed} | {%} | {remaining} |

Target utilisation should be 70–80% to allow for unplanned work and technical debt.

### 6. Risks & Trade-offs

| # | Risk / Trade-off | Impact | Likelihood | Mitigation | Owner | Due Date |
|---|---|---|---|---|---|---|
| 1 | {Description} | {L/M/H} | {L/M/H} | {Action} | {Person} | {DD-MMM-YYYY} |

### 7. Change Log

| Version | Date | Author | Changes |
|---|---|---|---|
| {X.Y} | {DD-MMM-YYYY} | {Name} | {What moved in/out/changed and why} |

## Now / Next / Later Framework

### Bucket Definitions

| Bucket | Time Horizon | Entry Criteria | Exit Criteria |
|---|---|---|---|
| **Now** | Current quarter | Prioritised, resourced, dependencies resolved or managed, JIRA epics created with stories | Delivered to production OR moved to "Next" with documented reason |
| **Next** | Next quarter | Scored and ranked, scope defined at epic level, dependencies identified, squad capacity tentatively allocated | Promoted to "Now" at quarterly planning OR deprioritised to "Later" with reason |
| **Later** | Future quarters (2+) | Directionally agreed by PM and stakeholders, aligned to strategic themes, high-level effort estimate exists | Promoted to "Next" when strategic priority and capacity align OR removed with documented rationale |

### Bucket Rules

1. **Now** items shall not exceed squad capacity. If capacity is exceeded, the lowest-priority item moves to "Next."
2. **Next** items shall have a named owner and at least epic-level scope. Items without an owner remain in "Later."
3. **Later** items are not commitments. They represent strategic intent and may be removed without formal change control.
4. Items shall only move backwards (Now → Next, Next → Later) with a documented reason in the Change Log.
5. Non-discretionary items (regulatory, contractual) bypass scoring but shall still be capacity-checked.

### Now / Next / Later View

| Bucket | Initiative | Product | Owner | Dependencies | Status |
|---|---|---|---|---|---|
| **Now** | {Initiative} | {Product} | {Person} | {Dependencies} | {🟢/🟡/🔴} |
| **Next** | {Initiative} | {Product} | {Person} | {Dependencies} | Scoped |
| **Later** | {Initiative} | {Product} | {Person} | {Dependencies} | Directional |

## Conventions

- **JIRA keys** use the `DME-XXXX` format.
- **Name people explicitly** — "Sasi to deliver pipeline changes" not "the engineering team will deliver."
- **RAG status definitions:**

| Status | Definition |
|---|---|
| 🟢 **Green** | On track — delivery within committed quarter, no unresolved blockers |
| 🟡 **Amber** | At risk — 1–2 sprint delay likely, or dependency not yet confirmed; recovery plan in place |
| 🔴 **Red** | Off track — committed quarter at risk without intervention; escalation required |

- All dates in **DD-MMM-YYYY** format (e.g., 28-Mar-2026).
- Use **"shall"** for mandatory requirements, **"should"** for recommendations, **"may"** for optional items.
- Version numbers follow **Major.Minor** convention (e.g., 1.0, 1.1, 2.0).
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- Use professional banking language. No startup jargon — no "disrupt", "pivot", "hustle", "move fast and break things."
- Capacity should target **70–80% utilisation** to allow for unplanned work.
- Non-discretionary items (regulatory, contractual) shall be flagged separately from discretionary priorities.

## JIRA Queries

Use these JQL patterns to gather roadmap data:

```
# All open epics
project = DME AND issuetype = Epic AND status != Done

# Epics by label/component for a specific product
project = DME AND issuetype = Epic AND labels = "customer-cortex"

# Current sprint items
sprint in openSprints() AND project = DME

# Items in a specific quarter (using fix version or label)
project = DME AND fixVersion = "Q3-FY26"
```

When using `jira_get_board_issues`, pass `fields: ["summary", "status", "assignee", "priority", "labels", "fixVersions", "sprint"]` to minimise payload.

## Quality Checklist

Before presenting the roadmap, verify:

- [ ] Roadmap view matches the stated audience and purpose
- [ ] Every initiative has a named owner (not a team name)
- [ ] Priority scores are calculated and ranked consistently
- [ ] Dependencies are mapped and sequencing is valid (no blocked items before their blockers)
- [ ] Capacity is not overcommitted (target 70–80% utilisation)
- [ ] "Now" bucket does not exceed available capacity
- [ ] Non-discretionary items are flagged and capacity-accounted
- [ ] RAG statuses are justified — Green with open blockers is a contradiction
- [ ] Change Log documents what moved in/out since the last version
- [ ] All dates use DD-MMM-YYYY format
- [ ] No filler text — every row in the initiative table represents a real, scoped initiative
- [ ] Strategic themes link to enterprise strategy
