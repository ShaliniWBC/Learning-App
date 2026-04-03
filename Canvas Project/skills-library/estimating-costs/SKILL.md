---
name: estimating-costs
description: "Produces cost and effort estimates for Cortex Suite initiatives using analogous estimation with confidence levels, resource matrices, and boundary definitions. Use when asked to estimate costs, size effort, produce budgetary guidance, or build a resource plan for a delivery initiative."
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

# Cost & Effort Estimation Skill

Produces structured cost and effort estimates for Cortex Suite delivery initiatives using analogous estimation, confidence levels, and per-stream breakdowns.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite at Westpac Group. She owns three enterprise data products:

| Product | Code | Description |
|---------|------|-------------|
| Customer Cortex | EDP001 | Customer 360 data product |
| Customer Interactions | EDP006 | Interaction history and channel data |
| Transcat | — | Transaction categorisation |

**Team composition (~15 people across ~3 squads):**

| Person | Role | Notes |
|--------|------|-------|
| Sasi | Lead Engineer | Architecture and engineering decisions |
| Cooper | Engineer | Exits after Sprint 6 — plan for handover |
| Josh | Grad Engineer | Ramping up — apply 0.6 FTE for estimation |
| Jolin | Grad Engineer | Ramping up — apply 0.6 FTE for estimation |
| Jack | Analyst | AEP integration focus |
| GK | SME / Solution Designer | Architecture inputs, shared allocation |
| Tom | Lead Data Scientist | DS team lead |
| Rupa | Data Scientist | Check leave cover |
| Simran | Data Scientist | |
| Justin | Data Scientist | Sole EDB contributor — SPOF risk |
| Vivasha | Data Scientist | |
| Claudia | Data Scientist | |
| Richard | Data Scientist | |
| Vinoth | Data Scientist | Part-time — apply 0.5 FTE |
| Peter | Senior BA | Hawkeye focus |
| Kadeeja | Scrum Master | Sprint ceremonies and facilitation |

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

**JIRA project key:** DME.

**Historical references:**
- **Hawkeye Budgetary Guidance** (DME-9222) — estimates across 3 streams (Engineering, Data Science, Testing/QA).
- **Account Scrutiny** — $122K approved project. Use as an analogue for medium-complexity initiatives.

## Estimation Methodology

All estimates shall follow the **analogous estimation** approach:

1. **Use historical actuals** — calibrate every estimate against completed work of similar scope and complexity. Search JIRA and Confluence for prior actuals before producing new estimates.
2. **Estimate in ranges** — every effort figure shall include three values: Optimistic, Likely, and Pessimistic. Single-point estimates are not acceptable.
3. **Apply confidence levels** — every stream estimate shall carry a High, Medium, or Low confidence rating with clear justification.
4. **Define boundaries** — every estimate shall explicitly state what is included, what is excluded, and what assumptions underpin the numbers.
5. **State caveats** — every estimate shall list conditions that could materially change the figures.

## Workflow

### Step 1 — Scope the Estimate

Before estimating, establish:

1. **What is being estimated?** — Feature, initiative, project, or budgetary guidance.
2. **JIRA reference** — Epic, initiative, or story keys (e.g., DME-9222).
3. **Delivery context** — New build, enhancement to existing product, integration, or migration.
4. **Audience** — SteerCo (summary), delivery team (detailed), or finance (cost-focused).
5. **Timeline constraints** — Fixed deadline, sprint-based delivery, or flexible.

If a JIRA key is provided, use `mcp__jira__jira_get_issue` to pull the epic description, linked issues, and current status. Use `mcp__jira__jira_search_issues` with JQL `parent = <EPIC-KEY>` to find child stories and their effort data.

### Step 2 — Gather Analogues

Search for completed work of similar scope:

1. Use `mcp__jira__jira_search_issues` with JQL patterns:
   ```
   project = DME AND status = Done AND type = Epic AND resolved >= -6m
   project = DME AND labels in (budgetary-guidance, estimation) AND status = Done
   ```
2. Use `mcp__confluence__search_pages` to find prior estimation documents, budgetary guidance, or project proposals.
3. For each analogue, note: scope, actual effort (person-days), team size, duration, and any known overruns.
4. If no analogues are found, state this explicitly and note that the estimate is based on expert judgement with Low confidence.

### Step 3 — Decompose by Stream

Break the work into four delivery streams:

| Stream | Scope Includes |
|--------|---------------|
| **Engineering** | Pipeline development, API changes, infrastructure, schema changes, environment setup |
| **Data Science** | Model development, feature engineering, notebook development, ML training, validation |
| **Testing / QA** | Test planning, test case development, execution, regression, UAT coordination |
| **Release Management** | Release planning, change management, deployment, post-release validation, documentation |

Not every initiative requires all four streams. State which streams are applicable and which are not.

### Step 4 — Size Each Stream

For each applicable stream:

1. Estimate person-days in three values: Optimistic, Likely, Pessimistic.
2. Assign a confidence level (High / Medium / Low) with justification.
3. Identify key assumptions that underpin the estimate.
4. Note risks that could push the estimate towards the pessimistic end.
5. Reference the analogue used for calibration.

**Overhead factor:** Apply a 20% overhead factor to account for ceremonies, meetings, admin, and context switching. This shall be shown as a separate line item, not hidden in stream estimates.

### Step 5 — Build Resource Matrix

Map estimated effort to named individuals:

1. List every person who shall contribute, with their role and FTE allocation per sprint.
2. Flag capacity constraints: leave, shared allocation, ramp-up periods, exit dates.
3. Identify single points of failure (SPOF) and recommend mitigation.
4. Show FTE values as decimals (0.0–1.0) per sprint.
5. Note total available person-days per sprint (1 sprint = 10 business days × FTE).

**Known constraints to apply:**
- Cooper: exits after Sprint 6. Any work assigned beyond Sprint 6 shall name a replacement.
- Josh and Jolin: graduates ramping up — apply 0.6 FTE unless the PM advises otherwise.
- Vinoth: part-time — apply 0.5 FTE.
- GK: shared allocation — confirm FTE with the PM before committing.

### Step 6 — Calculate Costs

Convert person-days to dollar estimates:

1. Apply day rates per stream (ask the PM for current rates, or use placeholder rates clearly marked as indicative).
2. Add infrastructure and licence costs where applicable (see Architecture Cost Considerations below).
3. Add a contingency percentage — recommended: 15% for High confidence, 25% for Medium, 40% for Low.
4. Show the total as a range (Optimistic to Pessimistic) including contingency.

### Step 7 — Produce Caveats & Boundaries

Generate the boundary definition using the template in section 10 below. Every estimate shall include:

1. Numbered list of items **in scope** of the estimate.
2. Numbered list of items **out of scope** (to be estimated separately).
3. Numbered assumptions.
4. Numbered caveats — conditions that could change the estimate.

### Step 8 — Format for Audience

Produce the estimate in the appropriate format:

- **SteerCo / Finance:** Executive summary table with stream totals, cost range, confidence, and key caveats. One page maximum.
- **Delivery Team:** Full breakdown with per-person allocation, sprint-level detail, and task decomposition.
- **Combined:** Both sections in a single document (use `reference/estimation-template.md` as the skeleton).

Save the completed estimate as a markdown file named `{Initiative-Name}-Estimate.md` in the workspace root or a location the PM specifies.

## Effort Estimation Table Format

The primary output table for every estimate:

| Stream | Optimistic (days) | Likely (days) | Pessimistic (days) | Confidence | Key Assumptions |
|--------|--------------------|---------------|---------------------|------------|-----------------|
| Engineering | | | | High / Med / Low | |
| Data Science | | | | High / Med / Low | |
| Testing / QA | | | | High / Med / Low | |
| Release Management | | | | High / Med / Low | |
| Overhead (20%) | | | | — | Ceremonies, admin, context switching |
| **Total** | **X** | **Y** | **Z** | **Overall** | |

## Confidence Level Definitions

| Level | Definition | Expected Variance |
|-------|-----------|-------------------|
| **High** | Well-understood scope. Team has completed analogous work. Estimate is calibrated against actuals. | ±15% |
| **Medium** | Scope mostly understood, some unknowns remain. Estimate is based on similar (not identical) work. | ±30% |
| **Low** | Significant unknowns. New technology, patterns, or integrations. Rough order of magnitude. | ±50% or more |

When reporting overall confidence, use the **lowest** stream confidence as the overall level. A single Low-confidence stream makes the entire estimate Low confidence.

## Resource Matrix Format

| Person | Role | Sprint N | Sprint N+1 | Sprint N+2 | Sprint N+3 | Sprint N+4 | Notes |
|--------|------|----------|------------|------------|------------|------------|-------|
| Sasi | Lead Engineer | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | Architecture lead |
| Cooper | Engineer | 0.8 | 0.8 | — | — | — | Exits after Sprint 6 |
| Josh | Grad Engineer | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | Ramping up |
| Jolin | Grad Engineer | 0.6 | 0.6 | 0.6 | 0.6 | 0.6 | Ramping up |
| Tom | Lead DS | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | DS team lead, split across initiatives |
| Vinoth | Data Scientist | 0.5 | 0.5 | 0.5 | 0.5 | 0.5 | Part-time allocation |
| {Name} | {Role} | {FTE} | {FTE} | {FTE} | {FTE} | {FTE} | {Leave, shared, ramp-up} |
| **Total FTE** | | **X.X** | **X.X** | **X.X** | **X.X** | **X.X** | |

FTE values: 0.0 = not allocated, 1.0 = full-time. Use "—" for sprints where a person is unavailable.

## Cost Calculation Format

| Stream | Person-Days (Likely) | Day Rate ($) | Stream Cost ($) | Notes |
|--------|----------------------|--------------|-----------------|-------|
| Engineering | | | | |
| Data Science | | | | |
| Testing / QA | | | | |
| Release Management | | | | |
| **Subtotal (Labour)** | **X** | | **$X** | |
| Infrastructure | — | — | | See architecture costs |
| Licences | — | — | | |
| Contingency (X%) | — | — | | Based on confidence level |
| **Grand Total** | | | **$X** | |

Show three columns (Optimistic / Likely / Pessimistic) when the audience requires a range view.

## Architecture Cost Considerations

When estimating Cortex Suite initiatives, account for these platform-specific cost drivers:

| Cost Driver | What to Estimate | Typical Triggers |
|-------------|-----------------|------------------|
| **ADAPT pipeline development** | Development and testing effort for new or modified pipelines | New data source, schema change, new consumption pattern |
| **Snowflake compute credits** | Warehouse sizing, query volume, transformation complexity | New curated layer tables, complex joins, materialised views |
| **Databricks cluster costs** | Notebook development, ML model training, feature engineering | New models, retraining pipelines, large dataset processing |
| **Azure Data Lake (ADLS2)** | Storage volume, data retention, replication | New raw/curated data, increased retention requirements |
| **Cosmos DB throughput** | Request Units per second (RU/s), document size, indexing | New API endpoints, increased query volume, new collections |
| **Mesh API hosting** | Compute, scaling, API gateway costs | New endpoints, increased consumer count, higher throughput |
| **Environment provisioning** | Dev, Test, Staging, Prod setup and maintenance | New product or major architectural change |

If infrastructure costs cannot be quantified, state them as a caveat with a placeholder range.

## Boundary Definition Template

Every estimate shall include this structure:

**In Scope of This Estimate:**
1. [Specific deliverable or work item]
2. [Specific deliverable or work item]
3. [Specific deliverable or work item]

**Out of Scope (shall be estimated separately):**
1. [Item] — [Reason for exclusion]
2. [Item] — [Reason for exclusion]

**Assumptions:**
1. [Assumption that underpins the estimate]
2. [Assumption that underpins the estimate]
3. Team capacity remains stable for the duration of the delivery (no unplanned attrition)

**Caveats:**
1. Estimate assumes no change to the ADAPT pipeline framework version during delivery
2. Estimate assumes existing Snowflake warehouse capacity is sufficient
3. [Project-specific caveat]
4. Estimate is valid for 30 calendar days from the date of issue — re-estimation shall be required if delivery does not commence within this period

## Estimation Anti-Patterns

Avoid these common estimation failures:

| Anti-Pattern | Why It Fails | Correct Approach |
|-------------|-------------|-----------------|
| Single-point estimate | Creates false precision; no visibility of risk | Always use Optimistic / Likely / Pessimistic ranges |
| "The team" without names | Hides capacity assumptions; prevents accountability | Name individuals with FTE allocations |
| No confidence level | Stakeholders cannot assess estimate reliability | Assign High / Medium / Low with variance bands |
| Missing boundaries | Scope creep; disagreements on what was covered | Use the Boundary Definition Template for every estimate |
| Testing effort omitted | Underestimation by 20–30% | Testing / QA is a mandatory stream |
| Release effort omitted | Last-mile costs not visible until too late | Release Management is a mandatory stream |
| No overhead factor | Estimates assume 100% productivity | Apply 20% overhead for ceremonies, admin, and context switching |
| No analogue reference | Estimate is based on intuition, not data | Search JIRA and Confluence for completed similar work |

## Quality Checklist

Before presenting any estimate, verify:

- [ ] Every stream has Optimistic / Likely / Pessimistic values (no single-point estimates)
- [ ] Every stream has a confidence level with justification
- [ ] Resource matrix names specific individuals with FTE allocations
- [ ] Known capacity constraints are reflected (Cooper exit, grad ramp-up, Vinoth part-time)
- [ ] Boundary definition is complete (In Scope, Out of Scope, Assumptions, Caveats)
- [ ] Overhead factor (20%) is included as a separate line
- [ ] Contingency percentage matches the confidence level
- [ ] Infrastructure and licence costs are addressed (even if noted as "to be confirmed")
- [ ] At least one analogue is referenced (or absence of analogues is stated)
- [ ] Estimate is formatted for the stated audience (SteerCo vs delivery team)
- [ ] All dates use DD-MMM-YYYY format
- [ ] JIRA keys use the DME-XXXX format
- [ ] No startup jargon — professional banking language throughout

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use professional banking language. No "disrupt", "pivot", "hustle", or startup jargon.
- Name people explicitly — never say "the team" when you can name individuals.
- JIRA keys use the `DME-XXXX` format.
