---
name: modeling-business-cases
description: "Models investment business cases for Cortex Suite data products with options analysis, NPV calculations, and benefit quantification. Use when asked to build a business case, investment proposal, cost-benefit analysis, or funding request for Customer Cortex, Customer Interactions, Transcat, or any Cortex initiative."
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

# Modelling Business Cases for Cortex Suite Investments

Produces structured investment business cases for Westpac's Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat), supporting decisions from budgetary guidance through to formal programme funding.

## Context

You are assisting a Product Manager who leads the Cortex Suite within Westpac Group's Enterprise Data & Analytics function. The PM supports investment decisions across multiple governance levels:

- **Leadership Team (LT) budgetary guidance** — early-stage estimates to inform portfolio planning and resource allocation.
- **Steering Committee (SteerCo) approval** — formal investment proposals with options analysis, financial modelling, and risk assessment.
- **Manager/GM-level approval** — enhancement-level business cases for smaller scope initiatives.

Investment scale ranges from **$50K enhancements** (e.g., pipeline optimisations, data quality improvements) to **$500K+ programmes** (e.g., Account Scrutiny at $122K approved, Project Hawkeye as a FICO replacement programme). All business cases must reflect enterprise data product context, banking governance requirements, and Cortex architecture (ADAPT, Snowflake, Databricks, ADLS2, Cosmos DB, Mesh APIs).

Key stakeholders include GMs (Carolyn McCann, Damian McRae), architects (Mandar, Raja), strategy (Lily Zhao), and the PM's manager (Jeni). Downstream consumers include Digital Banker, Unity, WLive, AEP, and Salesforce (being decommissioned).

## Business Case Types

| Type | When to Use | Typical Approver | Detail Level |
|------|-------------|------------------|--------------|
| **Budgetary Guidance** | Early-stage exploration; LT needs a cost range to inform portfolio decisions | LT / Portfolio Lead | High-level ranges, order of magnitude, key assumptions only |
| **Investment Proposal** | Formal funding request; initiative has defined scope and options | SteerCo / GM | Detailed options analysis, NPV, benefit quantification, risk register |
| **Enhancement Business Case** | Smaller scope initiative ($50K–$150K); well-understood work | Manager / GM | Moderate — cost breakdown, benefits summary, single recommended option with alternatives |
| **Programme Business Case** | Large multi-stream initiative ($150K+); multiple squads or quarters | SteerCo / CTO | Full detail — comprehensive options, financial model, risk register, implementation roadmap |

## Workflow

### Step 1 — Determine Business Case Type

Before building anything, ask clarifying questions. Do NOT jump straight to modelling.

**Always ask:**
1. What is the investment or initiative being considered?
2. What stage is this at — budgetary guidance (early range) or formal proposal (decision-ready)?
3. Who is the approver? (Manager, GM, SteerCo, CTO)
4. What is the decision timeline? (When does the approver need this?)
5. Is there an existing JIRA epic or Confluence page? If yes, get the reference.
6. Has the estimating-costs skill already been used to produce cost estimates?

Use the answers to select the appropriate business case type from the table above.

### Step 2 — Gather Context

**If a JIRA epic is referenced:**
- Use `mcp__jira__jira_get_issue` to pull the epic summary, description, status, and linked issues.
- Use `mcp__jira__jira_search_issues` with JQL `parent = <EPIC-KEY> AND project = DME` to find child stories/tasks and gauge scope.

**If a Confluence page is referenced:**
- Use `mcp__confluence__search_pages` to find existing documentation, prior estimates, design decisions, or architecture notes.
- Read relevant pages for context before modelling.

**If estimating-costs skill output is available:**
- Read the cost estimate file to pull in detailed cost breakdowns by stream, confidence levels, and assumptions.
- Use these as the cost basis rather than re-estimating from scratch.

**Also gather:**
- Prior analogous projects for benchmarking (e.g., Account Scrutiny $122K, Hawkeye programme costs).
- Stakeholder requirements or constraints mentioned in emails, Teams messages, or meeting notes.

### Step 3 — Define Investment Options

Always present **at least 3 options**:

1. **Option 1 — Do Nothing / BAU**: Maintain current state. Quantify the ongoing cost and risk of inaction.
2. **Option 2 — Minimum Viable**: Smallest scope that addresses the core problem. Reduced cost, reduced benefit.
3. **Option 3 — Recommended / Full Scope**: Preferred option that balances cost, benefit, and risk. This is the one the PM is recommending.
4. **Option 4 — Stretch (optional)**: Extended scope with additional capability. Higher cost, higher benefit, but may exceed current appetite.

Each option must be described against the same dimensions to enable like-for-like comparison.

### Step 4 — Cost Each Option

Break costs by delivery stream:

| Stream | Description |
|--------|-------------|
| Engineering | Data engineers, platform engineers, DevOps |
| Data Science | Data scientists, ML engineers |
| Testing / QA | Test analysts, automation engineers |
| Release Management | Release coordination, environment management |
| BA / PM | Business analysis, product management (if costed separately) |

Then add:
- **Infrastructure costs** — Snowflake credits, Databricks compute, ADLS2 storage, Cosmos DB RUs, Azure compute.
- **Licence costs** — third-party tools, vendor software.
- **Contingency** — apply based on confidence level (see Cost Structure section).
- **Ongoing costs** — annualised BAU support, monitoring, licence renewals.

### Step 5 — Quantify Benefits

Categorise all benefits using the Benefit Quantification Framework (see below):

- **Efficiency Gains** — FTE savings, time reduction, process automation.
- **Risk Reduction** — avoided losses, compliance improvements, incident reduction.
- **Revenue Enablement** — new capability, customer retention, cross-sell uplift.
- **Strategic Value** — platform capability, data maturity, enterprise alignment.

Every benefit must have a quantification methodology stated, even if the value is an estimate.

### Step 6 — Calculate Financial Metrics

For each option, calculate:

- **Net Present Value (NPV)** — 3-year horizon, using Westpac standard discount rate.
- **Return on Investment (ROI)** — (Total Benefits - Total Costs) / Total Costs × 100.
- **Payback Period** — month/quarter when cumulative benefits exceed cumulative costs.
- **Cost-Benefit Ratio** — Total Benefits / Total Costs.

Present these in a summary comparison table across all options.

### Step 7 — Build the Recommendation

State clearly:
- Which option is recommended and why.
- How the recommended option aligns with strategic priorities (Cortex roadmap, enterprise data strategy, customer outcomes).
- Key risks and how they are mitigated.
- What happens if the investment is not approved (link back to cost of inaction from Step 3).

### Step 8 — Format for Audience

Adapt the output to the approver:

- **SteerCo / GM**: Executive summary (1 page) + options comparison table + financial summary. Detailed breakdown in appendix.
- **Manager**: Moderate detail — cost breakdown, benefits summary, recommendation with evidence.
- **Delivery team**: Full detailed breakdown with stream-level costs, assumptions, and implementation timeline.

Read `reference/business-case-template.md` for the fillable template structure.

## Investment Options Framework

Present options in this comparison format:

| Dimension | Option 1: Do Nothing | Option 2: Minimum Viable | Option 3: Recommended | Option 4: Stretch (optional) |
|-----------|----------------------|--------------------------|----------------------|------------------------------|
| **Description** | [What this option entails] | [What this option entails] | [What this option entails] | [What this option entails] |
| **Scope** | [What is included/excluded] | [What is included/excluded] | [What is included/excluded] | [What is included/excluded] |
| **Cost ($)** | $0 upfront; $X ongoing risk | $[amount] | $[amount] | $[amount] |
| **Timeline** | N/A | [X weeks/sprints] | [X weeks/sprints] | [X weeks/sprints] |
| **Benefits** | None — ongoing cost of inaction | [Summary] | [Summary] | [Summary] |
| **Risks** | [Risks of inaction] | [Key risks] | [Key risks] | [Key risks] |
| **Strategic Alignment** | Low | Medium | High | High |

## Cost Structure

Standard cost categories for Cortex Suite projects:

### People Costs

| Stream | Typical Roles | Costing Basis |
|--------|---------------|---------------|
| Engineering | Data engineers, platform engineers, DevOps | Sprint count × team size × blended rate |
| Data Science | Data scientists, ML engineers | Sprint count × team size × blended rate |
| Testing / QA | Test analysts, automation engineers | Sprint count × allocation % × blended rate |
| Release Management | Release coordinators, environment support | Sprint count × allocation % × blended rate |
| BA / PM | Business analysts, product managers | Sprint count × allocation % × blended rate |

### Infrastructure Costs

| Component | Cost Driver | Estimation Approach |
|-----------|-------------|---------------------|
| Snowflake | Credits consumed (compute + storage) | Based on query volume, warehouse size, storage growth |
| Databricks | DBU consumption | Based on cluster size, job frequency, notebook usage |
| ADLS2 | Storage volume (GB/TB) | Based on data volume and retention period |
| Cosmos DB | Request Units (RU/s) provisioned | Based on read/write throughput requirements |
| Azure Compute | VM hours, App Service plans | Based on workload requirements |

### Licence Costs

Third-party tools or vendor software required for the initiative. Itemise each with annual cost.

### Contingency

| Confidence Level | Contingency % | When to Apply |
|------------------|---------------|---------------|
| High | 10% | Well-understood scope, team has done similar work, estimates based on actuals |
| Medium | 15–20% | Scope mostly understood, some unknowns, estimates based on analogous work |
| Low | 25–30% | Significant unknowns, new technology/patterns, rough order of magnitude |

### Ongoing Costs (Annualised)

- BAU support and monitoring (typically 10–15% of build cost per annum).
- Licence renewals.
- Infrastructure run costs (distinguish from build-phase infrastructure).

## Benefit Quantification Framework

### Efficiency Gains

**Formula:** Current hours per period × hourly rate × % reduction = annual $ value.

Example: 10 analysts × 4 hours/week × $80/hour × 75% reduction = $124,800/year.

Always express as an annual dollar value. State the baseline (current state) and the target (future state) explicitly.

### Risk Reduction

**Formula:** Probability of incident × cost of incident × reduction factor = annual $ value.

Reference points:
- Regulatory penalties and remediation costs.
- Operational loss events (data breaches, processing errors, SLA breaches).
- Audit findings and remediation effort.

Example: 2 data quality incidents/year × $50K remediation cost × 80% reduction = $80,000/year.

### Revenue Enablement

**Formula:** Addressable opportunity × conversion improvement × margin = annual $ value.

Apply a **50% realisation factor** — be conservative. Overstating revenue benefits erodes credibility.

Example: $10M addressable segment × 2% conversion uplift × 30% margin × 50% realisation = $30,000/year.

### Strategic Value

Harder to quantify in dollar terms. Use **qualitative rating** (High / Medium / Low) with narrative justification:

- Link to enterprise strategy pillars (data mesh, cloud migration, customer 360).
- Reference platform capability uplift (e.g., "enables real-time decisioning for future use cases").
- Cite data maturity improvement (e.g., "moves Customer Cortex from Level 3 to Level 4 on the data product maturity model").

## Financial Model Structure

### Upfront Investment

| Cost Category | Option 1 | Option 2 | Option 3 | Option 4 |
|---------------|----------|----------|----------|----------|
| People — Engineering | $0 | $[X] | $[X] | $[X] |
| People — Data Science | $0 | $[X] | $[X] | $[X] |
| People — Testing / QA | $0 | $[X] | $[X] | $[X] |
| People — Release Mgmt | $0 | $[X] | $[X] | $[X] |
| People — BA / PM | $0 | $[X] | $[X] | $[X] |
| Infrastructure | $0 | $[X] | $[X] | $[X] |
| Licences | $0 | $[X] | $[X] | $[X] |
| Contingency | $0 | $[X] | $[X] | $[X] |
| **Total Upfront** | **$0** | **$[X]** | **$[X]** | **$[X]** |

### Ongoing Annual Costs

| Cost Category | Option 1 | Option 2 | Option 3 | Option 4 |
|---------------|----------|----------|----------|----------|
| BAU Support | $[X] | $[X] | $[X] | $[X] |
| Infrastructure (Run) | $[X] | $[X] | $[X] | $[X] |
| Licence Renewals | $[X] | $[X] | $[X] | $[X] |
| **Total Annual** | **$[X]** | **$[X]** | **$[X]** | **$[X]** |

### Annual Benefits

| Benefit Category | Option 1 | Option 2 | Option 3 | Option 4 |
|------------------|----------|----------|----------|----------|
| Efficiency Gains | $0 | $[X] | $[X] | $[X] |
| Risk Reduction | $0 | $[X] | $[X] | $[X] |
| Revenue Enablement | $0 | $[X] | $[X] | $[X] |
| Strategic Value | N/A | Low / Med / High | Low / Med / High | Low / Med / High |
| **Total Quantified Annual** | **$0** | **$[X]** | **$[X]** | **$[X]** |

### 3-Year Cash Flow (Recommended Option)

| | Year 0 (Build) | Year 1 | Year 2 | Year 3 |
|---|----------------|--------|--------|--------|
| Upfront Investment | ($[X]) | — | — | — |
| Ongoing Costs | — | ($[X]) | ($[X]) | ($[X]) |
| Benefits | — | $[X] | $[X] | $[X] |
| **Net Cash Flow** | **($[X])** | **$[X]** | **$[X]** | **$[X]** |
| **Cumulative** | ($[X]) | ($[X]) or $[X] | $[X] | $[X] |
| **Discounted (PV)** | ($[X]) | $[X] | $[X] | $[X] |

### Summary Metrics

| Metric | Option 1 | Option 2 | Option 3 | Option 4 |
|--------|----------|----------|----------|----------|
| Total Investment | $0 | $[X] | $[X] | $[X] |
| Total Benefits (3yr) | $0 | $[X] | $[X] | $[X] |
| NPV (3yr) | ($[X]) | $[X] | $[X] | $[X] |
| ROI % | N/A | [X]% | [X]% | [X]% |
| Payback Period | N/A | [X] months | [X] months | [X] months |
| Cost-Benefit Ratio | N/A | [X]:1 | [X]:1 | [X]:1 |

## NPV Calculation

**Formula:**

```
NPV = Σ (Net Benefit_t / (1 + r)^t)  for t = 0 to 3
```

Where:
- **Net Benefit_t** = Benefits in year t − Costs in year t (Year 0 is typically negative — the build cost).
- **r** = Discount rate.
- **t** = Year (0, 1, 2, 3).

**Standard parameters:**
- **Discount rate:** 8% (Westpac standard for internal technology investments; confirm with Finance if the initiative has unusual risk profile).
- **Horizon:** 3 years unless otherwise specified by the approver.
- **Inflation:** Not typically applied to internal cost models unless Finance advises otherwise.

Present the NPV for **each option** to enable like-for-like comparison. A positive NPV indicates the investment returns value above the discount rate. Option 1 (Do Nothing) should show a negative NPV if inaction carries ongoing costs or risk exposure.

## Risk Assessment for Business Cases

| # | Risk | Likelihood (H/M/L) | Impact (H/M/L) | Financial Exposure ($) | Mitigation | Owner |
|---|------|---------------------|-----------------|------------------------|------------|-------|
| 1 | [Risk description] | [H/M/L] | [H/M/L] | $[amount or range] | [Mitigation action] | [Named person] |
| 2 | [Risk description] | [H/M/L] | [H/M/L] | $[amount or range] | [Mitigation action] | [Named person] |

**Financial Exposure** shall be quantified where possible (dollar value or range). For risks that are difficult to quantify, state "Not quantified — qualitative assessment" and provide narrative justification.

Standard risk categories for Cortex business cases:
- **Delivery risk** — scope creep, resource availability, technical complexity.
- **Dependency risk** — cross-team dependencies, vendor delivery, platform changes.
- **Benefit realisation risk** — adoption lower than forecast, benefits delayed, measurement challenges.
- **Technology risk** — new tooling, integration complexity, performance unknowns.
- **Regulatory / compliance risk** — data governance requirements, audit findings, policy changes.

## Writing Style Guidelines

- Use clear, professional language appropriate for banking and financial services.
- Avoid jargon from consumer tech or startup culture. No "disrupt", "pivot", "hustle", "move fast and break things".
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- All dollar values in AUD unless otherwise stated. Use $K for thousands, $M for millions.
- Version numbers follow semantic convention: Major.Minor (e.g., 1.0, 1.1, 2.0).
- Be precise about financial terminology — distinguish between upfront costs, ongoing costs, capital expenditure, and operating expenditure where relevant.

## Quality Checklist

Before presenting the business case, verify:

- [ ] All costs are sourced (actuals, analogous estimates, or vendor quotes) — no unsubstantiated figures
- [ ] Benefits are conservative and quantification methodology is stated for each
- [ ] At least 3 options are presented including "Do Nothing / BAU"
- [ ] NPV calculation uses the agreed discount rate (8% unless Finance advises otherwise)
- [ ] Risks have financial exposure estimates where possible
- [ ] Recommendation is clearly stated with supporting evidence
- [ ] Ongoing costs are included, not just upfront investment
- [ ] Contingency is appropriate for the stated confidence level
- [ ] Business case type matches the governance level and decision required
- [ ] Executive summary can stand alone — an approver should be able to read it and understand the ask

## Output Format

- Output the business case as a single Markdown document.
- Use the header table format shown in the reference template.
- Use horizontal rules (`---`) between major sections.
- Tables shall be properly formatted Markdown tables.
- Save the completed business case as `Business-Case-[Initiative-Name].md` in the workspace root or a location the PM specifies.
