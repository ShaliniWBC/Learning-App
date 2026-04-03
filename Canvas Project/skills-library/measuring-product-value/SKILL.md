---
name: measuring-product-value
description: "Builds and maintains an enterprise value scorecard for Cortex Suite data products, quantifying adoption, reach, efficiency, and strategic dependency across the Group. Use when asked to measure product value, build a value scorecard, quantify Cortex impact, prepare a value narrative for leadership, or track consumer adoption and outcomes."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__confluence__get_child_pages
  - Read
  - create_file
  - edit_file
  - task_list
---

# Measuring Product Value — Cortex Suite

Builds and maintains an enterprise value scorecard (the "Value Ledger") for Cortex Suite data products, quantifying adoption, reach, efficiency, and strategic dependency across Westpac Group.

## Context

You are assisting **Shalini Gangadharan**, Executive Manager for the Cortex Suite of Enterprise Data Products within Westpac Group's DDAI (Data Digital and AI) Division. She owns three enterprise data products:

| Product | Code | Description |
|---------|------|-------------|
| Customer Cortex | EDP001 | Enterprise 360° customer view — demographics, financials, ML propensity scores, FICO |
| Customer Interactions | EDP006 | Channel interaction data — branch, digital, CRM, call centre |
| Transcat | — | Enriched transaction data with merchant categorisation |

**Why this skill exists:** Senior product leaders are recognised for measuring and scaling outcomes, not simply shipping features. New leadership — **Andrew McMullen** (Group Exec DDAI), **Vicki Wood** (GM DDAI), **Rohith E** (Head of Data, DDAI) — have limited visibility of Cortex's enterprise contribution. This skill produces hard-evidence artifacts that leadership can understand, forward, and reference in strategic discussions. In a governance-heavy bank, quantified value creates visibility far more effectively than narrative alone.

**Architecture stack:** ADAPT pipelines, Snowflake (primary warehouse), Databricks, Azure Data Lake Storage Gen2 (ADLS2), Cosmos DB, Cortex Mesh APIs (Info API, CAP API, GCM).

**Downstream consumers:** Digital Banker, Unity, WLive, Adobe Experience Platform (AEP).

**Key stakeholders for value conversations:** Jeni Jose Mannanal (Head of Data), Lu Luc (Head of AI Services), Phil Hood (Exec Manager, Data Science), Reza S (Chief AI Engineer).

**JIRA project key:** DME.

## Value Dimensions

All value assessments shall measure across the six dimensions defined below. Not every dimension carries equal weight for every product — the assessment shall identify which dimensions are most material based on the product's maturity and consumer base.

| Dimension | Metrics | Source |
|-----------|---------|--------|
| **Adoption** | Active consumer count, new consumers onboarded this quarter, API call volumes (monthly), monthly active users, data download volumes | Mesh API logs, JIRA onboarding tickets (`project = DME AND labels = onboarding`), Snowflake usage logs |
| **Reach** | Business units served, use cases enabled, downstream systems dependent on Cortex data | Consumer registry (Confluence), architecture dependency maps |
| **Quality** | Data quality score per product, SLA adherence percentage, pipeline reliability (uptime, success rate) | Quality monitoring framework, ADAPT pipeline dashboards, Snowflake scheduled checks |
| **Efficiency** | Time saved by consumers versus building their own capability, onboarding time reduction (trend), duplicate effort eliminated across the Group | Consumer interviews, onboarding ticket resolution times, estimation models |
| **Business Outcomes Enabled** | Decisions supported, ML models powered (e.g., Hawkeye credit models), campaigns informed (AEP segments), customer interactions enriched, revenue influenced | Consumer outcome data, model registries, AEP campaign performance, consumer feedback |
| **Strategic Dependency** | Group initiatives depending on Cortex, regulatory programmes using Cortex data, enterprise architecture designations | Programme documentation, architecture governance records, regulatory submissions |

## Value Attribution Framework

Cortex is an enabling platform — it rarely generates revenue directly. Attribution shall be honest and defensible. Overclaiming destroys credibility with senior stakeholders faster than underreporting.

| Attribution Level | Definition | How to Report |
|-------------------|-----------|---------------|
| **Direct** | Cortex is the primary enabler — the outcome would not exist without Cortex data | State as direct impact. Example: "Hawkeye credit models run on 47 Cortex-sourced features — Cortex is the primary data provider." |
| **Enabled** | Cortex contributed materially — the outcome would be significantly degraded without Cortex | State as "enabled by Cortex". Example: "AEP personalisation segments use Cortex propensity scores to target 2.3M customers." |
| **Indirect** | Cortex provided supporting data — the outcome could exist without Cortex but would be less complete | State as "supported by Cortex". Example: "Digital Banker displays Cortex customer attributes alongside other data sources." |

Every entry in the Consumer Impact Registry (see below) shall carry an attribution level. This prevents inflated claims and ensures the value narrative withstands scrutiny from finance, architecture, and executive stakeholders.

## Workflow

### Step 1 — Gather Adoption Data

Pull consumer counts, API volumes, and onboarding activity from available sources:

1. **JIRA onboarding tickets:** Search for consumers who have onboarded or are onboarding:
   ```
   project = DME AND labels in (onboarding, consumer-onboarding) AND created >= -90d
   project = DME AND text ~ "onboarding" AND type = Story AND status in (Done, "In Progress")
   ```
2. **Confluence consumer registry:** Search for existing consumer documentation:
   ```
   mcp__confluence__search_pages(query="cortex consumer registry", limit=10)
   mcp__confluence__search_pages(query="cortex API consumers", limit=10)
   ```
3. **API volume data:** If available in Confluence or monitoring pages, pull monthly call volumes per consumer per product.
4. **Document what is known and what gaps exist** — missing data is itself a finding.

### Step 2 — Collect Outcome Evidence

For each active consumer, identify the business outcome Cortex supports:

1. Search Confluence for project outcomes, business cases, and benefits realisation reports:
   ```
   mcp__confluence__search_pages(query="cortex benefits realisation", limit=10)
   mcp__confluence__search_pages(query="cortex business case", limit=10)
   ```
2. Search JIRA for completed epics and stories that reference consumer outcomes:
   ```
   project = DME AND type = Epic AND status = Done AND text ~ "outcome"
   project = DME AND labels in (consumer-value, business-outcome) AND resolved >= -180d
   ```
3. For each consumer, capture:
   - What business function does it serve?
   - What would happen if Cortex data were unavailable?
   - Is there a quantified benefit (hours saved, decisions improved, risk reduced)?

### Step 3 — Calculate Value Metrics

Quantify value using these standard approaches:

| Value Type | Calculation Method | Example |
|-----------|-------------------|---------|
| **Efficiency gain** | Hours saved per period × blended hourly rate ($150/hr for internal FTE) | "4 teams no longer build their own customer views — estimated 2,400 hours/year saved = $360K/year" |
| **Risk reduction** | Incidents prevented × average incident cost, or regulatory penalties avoided | "Centralised data quality reduces data-related incidents by an estimated 40%" |
| **Capability enabled** | What would not exist without Cortex — binary assessment with business value | "Hawkeye credit risk models require Cortex features — models assess $4.2B in lending exposure" |
| **Speed to market** | Time to onboard a new consumer or enable a new use case — compare to building from scratch | "Average onboarding time: 3 weeks vs estimated 12 weeks to build from source systems" |
| **Data consolidation** | Duplicate datasets eliminated × maintenance cost per dataset | "Cortex replaced 6 team-level customer extracts — estimated $180K/year in avoided infrastructure and maintenance" |

All estimates shall state their assumptions explicitly. No value claim shall be presented without a stated basis.

### Step 4 — Build the Scorecard

Produce the Value Scorecard using the format in the "Value Scorecard Format" section below:

1. Populate each metric row with current values and previous-period comparisons.
2. Calculate trend indicators: ↑ (improving), → (stable), ↓ (declining).
3. Set targets where known; mark as "TBD" where targets have not been established (this is an action item, not a gap to hide).
4. Calculate the overall **Cortex Enterprise Value Score** using the weighted composite methodology.

Read `reference/value-ledger-template.md` for the fillable skeleton.

### Step 5 — Write the Value Narrative

Produce 3–5 sentences summarising:

1. **What changed this period** — new consumers, volume growth, outcomes delivered.
2. **What is growing** — adoption trends, expanding use cases, increasing dependency.
3. **What matters strategically** — alignment with Group priorities, regulatory requirements, leadership agenda.

The narrative shall be written for an audience of senior leaders who have **not** previously engaged with Cortex metrics. Assume zero prior context. Every statement shall be self-contained and evidence-based.

### Step 6 — Identify Gaps

Document where measurement is missing or incomplete:

1. Which consumers have no outcome data recorded?
2. Which value dimensions have no quantified metrics?
3. Where are outcomes attributed but not validated with the consumer?
4. What data sources are needed but not yet available?

This becomes a prioritised action list for the next measurement cycle. Gaps are not failures — they are the roadmap for improving the value narrative.

## Value Scorecard Format

The primary output of every value assessment:

### Adoption Metrics

| Metric | Previous Period | Current Period | Trend | Target | Commentary |
|--------|----------------|----------------|-------|--------|------------|
| Active consumers (systems) | {N} | {N} | {↑↓→} | {N} | {Context} |
| New consumers onboarded (quarter) | {N} | {N} | {↑↓→} | {N} | {Context} |
| API call volume (monthly) | {N} | {N} | {↑↓→} | {N} | {Context} |
| Monthly active users (individuals) | {N} | {N} | {↑↓→} | {N} | {Context} |

### Quality Metrics

| Metric | Previous Period | Current Period | Trend | Target | Commentary |
|--------|----------------|----------------|-------|--------|------------|
| Data quality score — EDP001 | {%} | {%} | {↑↓→} | ≥ 95% | {Context} |
| Data quality score — EDP006 | {%} | {%} | {↑↓→} | ≥ 95% | {Context} |
| SLA adherence (pipeline timeliness) | {%} | {%} | {↑↓→} | ≥ 99% | {Context} |
| Pipeline reliability (success rate) | {%} | {%} | {↑↓→} | ≥ 99.5% | {Context} |

### Efficiency Metrics

| Metric | Previous Period | Current Period | Trend | Target | Commentary |
|--------|----------------|----------------|-------|--------|------------|
| Estimated hours saved (annual) | {N} | {N} | {↑↓→} | {N} | {Basis stated} |
| Average consumer onboarding time | {weeks} | {weeks} | {↑↓→} | ≤ 3 weeks | {Context} |
| Duplicate datasets eliminated | {N} | {N} | {↑↓→} | — | {Cumulative count} |

### Business Outcomes Enabled

| Metric | Previous Period | Current Period | Trend | Target | Commentary |
|--------|----------------|----------------|-------|--------|------------|
| ML models powered by Cortex data | {N} | {N} | {↑↓→} | {N} | {List key models} |
| Campaigns using Cortex segments | {N} | {N} | {↑↓→} | {N} | {AEP campaigns} |
| Business decisions supported | {N} | {N} | {↑↓→} | {N} | {Context} |

### Strategic Dependency

| Metric | Previous Period | Current Period | Trend | Target | Commentary |
|--------|----------------|----------------|-------|--------|------------|
| Group initiatives depending on Cortex | {N} | {N} | {↑↓→} | — | {List initiatives} |
| Regulatory programmes using Cortex data | {N} | {N} | {↑↓→} | — | {List programmes} |
| Business units served | {N} | {N} | {↑↓→} | — | {List BUs} |

### Cortex Enterprise Value Score

**Overall Score: {X.X} / 10** — {trend indicator}

Composite weighted score calculated as:

| Dimension | Weight | Score (0–10) | Weighted Score |
|-----------|--------|-------------|---------------|
| Adoption | 25% | {X.X} | {X.XX} |
| Reach | 15% | {X.X} | {X.XX} |
| Quality | 20% | {X.X} | {X.XX} |
| Efficiency | 15% | {X.X} | {X.XX} |
| Business Outcomes Enabled | 15% | {X.X} | {X.XX} |
| Strategic Dependency | 10% | {X.X} | {X.XX} |
| **Total** | **100%** | | **{X.XX}** |

Weights should be adjusted based on what leadership priorities are most relevant in the current period. State the rationale for any weight changes.

## Consumer Impact Registry

Per-consumer value tracking — the detailed evidence behind the scorecard:

| Consumer | Product Used | Use Case | Attribution Level | Business Outcome | Quantified Value | Last Updated |
|----------|-------------|----------|-------------------|-----------------|-----------------|-------------|
| Digital Banker | EDP001, EDP006 | Customer 360 display, interaction history | Indirect | Branch staff access consolidated customer view | {hours saved, decisions improved} | {DD-MMM-YYYY} |
| Unity | EDP001 | Customer data for servicing | Indirect | Servicing staff access customer attributes | {value} | {DD-MMM-YYYY} |
| WLive | EDP001 | Customer data for digital experience | Indirect | Digital channel displays customer information | {value} | {DD-MMM-YYYY} |
| AEP (Adobe) | EDP001, Transcat | Propensity scores, transaction segments | Enabled | Personalised marketing campaigns targeting {N}M customers | {campaign uplift, conversion improvement} | {DD-MMM-YYYY} |
| Hawkeye (Credit Risk) | EDP001 | ML features for credit risk models | Direct | {N} credit risk models assess ${X}B lending exposure | {risk reduction, model accuracy improvement} | {DD-MMM-YYYY} |
| CRT Models | EDP001 | ML features for {N} models | Direct | Customer risk and treatment models | {value} | {DD-MMM-YYYY} |
| National Proactive Engagement | EDP001, EDP006 | Customer insights for proactive outreach | Enabled | Proactive customer engagement programme | {value} | {DD-MMM-YYYY} |
| {Additional consumer} | {products} | {use case} | {Direct/Enabled/Indirect} | {outcome} | {value} | {DD-MMM-YYYY} |

This registry shall be maintained as a living document. Each entry should be reviewed with the consumer at least quarterly to validate attribution and update outcome data.

## Leadership-Ready Summary

The artifact designed to travel upward through the management chain. This format is intentionally concise — easy for Jeni Jose Mannanal to include in her own leadership updates, naturally surfacing Cortex's contribution without requiring additional effort.

### Format

```
CORTEX SUITE — VALUE SUMMARY
Period: {Month YYYY}
Author: Shalini Gangadharan, Executive Manager — Cortex Suite

KEY HIGHLIGHTS
• {Adoption highlight — e.g., "Cortex now serves 14 downstream systems across 5 business units"}
• {Outcome highlight — e.g., "Hawkeye credit models powered by 47 Cortex features assess $4.2B lending exposure"}
• {Growth highlight — e.g., "API call volume increased 18% quarter-on-quarter, driven by AEP segment expansion"}
• {Efficiency highlight — e.g., "Estimated 2,400 hours/year saved by eliminating 6 duplicate customer data builds"}
• {Quality highlight — e.g., "Data quality score: EDP001 at 96.8% (↑ from 94.2%), EDP006 at 95.1% (→ stable)"}

KEY METRIC
{Single most impactful number with trend — e.g., "Enterprise Value Score: 7.8 / 10 (↑ from 7.2 last quarter)"}

GROWTH OPPORTUNITY
{One sentence on the next value unlock — e.g., "Onboarding Salesforce replacement (Customer Data Platform) as a new consumer would extend Cortex reach to the retail banking frontline."}

RISK / GAP
{One sentence on the primary value risk — e.g., "3 of 7 consumers have no quantified outcome data — measurement gaps reduce the defensibility of the value narrative."}

STRATEGIC TALKING POINT
{One sentence linking Cortex value to Group strategy — e.g., "Cortex is the data foundation for 4 of the Group's top-10 strategic initiatives, including Hawkeye credit transformation and AEP personalisation."}
```

This summary shall never exceed one page. Every bullet shall contain at least one number.

## Cadence

| Cycle | Frequency | Content | Audience |
|-------|-----------|---------|----------|
| Monthly Scorecard | Monthly | Value Scorecard + Leadership-Ready Summary | Jeni, Lu Luc, direct stakeholders |
| Quarterly Deep-Dive | Quarterly | Full Consumer Impact Registry review, trend analysis, gap assessment, updated value narrative | Leadership team, Andrew McMullen, Vicki Wood, Rohith E |
| Annual Value Report | Annually | Comprehensive year-in-review: cumulative value delivered, strategic impact, forward investment case | Executive leadership, portfolio review |

The monthly scorecard shall be produced by the 5th business day of each month. The quarterly deep-dive shall align with the enterprise planning calendar.

## Quality Checklist

Before presenting any value assessment, verify:

- [ ] Every metric has a stated source — no invented numbers
- [ ] Attribution levels are stated for every consumer outcome (Direct / Enabled / Indirect)
- [ ] No overclaiming — "enabled by" and "supported by" are used where appropriate
- [ ] Trends have context — explain why a metric moved, not just the direction
- [ ] Gaps are acknowledged openly — missing data is documented as an action item
- [ ] Value estimates state their assumptions explicitly
- [ ] The Leadership-Ready Summary stands alone — a reader with no prior context understands the value
- [ ] Every bullet in the summary contains at least one number
- [ ] All dates use DD-MMM-YYYY format
- [ ] JIRA keys use the DME-XXXX format
- [ ] No startup jargon — professional banking language throughout
- [ ] "Shall" is used for mandatory requirements, "should" for recommendations
- [ ] Consumer names match the official consumer registry
- [ ] The Cortex Enterprise Value Score methodology is transparent and reproducible

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use professional banking language. No "disrupt", "pivot", "hustle", or startup jargon.
- Name people explicitly — never say "the team" when you can name individuals.
- JIRA keys use the `DME-XXXX` format.
- Quantify everything possible. "Significant growth" is meaningless — "18% increase" is actionable.
- Value claims shall always state the attribution level and the basis for the estimate.
