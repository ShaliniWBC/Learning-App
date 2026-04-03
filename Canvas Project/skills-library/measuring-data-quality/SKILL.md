---
name: measuring-data-quality
description: "Builds data quality measurement frameworks and monitoring scorecards for Cortex Suite enterprise data products. Use when asked to measure data quality, build a quality scorecard, define quality rules, investigate data quality issues, or set up data quality monitoring for Customer Cortex, Customer Interactions, or Transcat."
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

# Data Quality Measurement Skill

Builds data quality measurement frameworks and monitoring scorecards for Cortex Suite enterprise data products.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite at Westpac Group. She owns three enterprise data products:

| Product | Code | Description |
|---------|------|-------------|
| Customer Cortex | EDP001 | Customer 360 data product |
| Customer Interactions | EDP006 | Interaction history and channel data |
| Transcat | — | Transaction categorisation |

Data quality is a **core product attribute** for enterprise data products. Quality is not aspirational — it is a contractual obligation to downstream consumers. Poor data quality directly impacts customer outcomes, operational decisions, and regulatory compliance.

**Architecture stack:** ADAPT pipelines, Snowflake (primary warehouse), Databricks, Azure Data Lake Storage Gen2 (ADLS2), Cosmos DB, Mesh APIs.

**Downstream consumers:** Digital Banker, Unity, WLive, Adobe Experience Platform (AEP).

**JIRA project key:** DME.

## Data Quality Dimensions

All quality assessments shall use the six standard dimensions defined below:

| Dimension | Definition | Measurement Approach | Example for Cortex |
|-----------|-----------|----------------------|-------------------|
| **Completeness** | The degree to which mandatory data fields are populated | % of non-null values for mandatory fields across the assessed entity | Customer Cortex: `email_address` populated for 98.7% of active customers |
| **Accuracy** | The degree to which data values correctly represent the real-world entity | % of values matching the authoritative source system | Customer Cortex: `date_of_birth` matches Core Banking source for 99.4% of records |
| **Timeliness** | The degree to which data is available within the agreed SLA window | % of records delivered and available within the defined SLA | Customer Interactions: 99.1% of interaction records available within 15 minutes of event |
| **Consistency** | The degree to which data values are consistent across related datasets | % of records consistent across related entities and cross-referenced datasets | Transcat: `merchant_category` consistent between raw and curated layers for 97.8% of records |
| **Uniqueness** | The degree to which records are free from unintended duplication | % of records without duplicates on the defined primary/composite key | Customer Cortex: 99.99% unique on `customer_id` (composite: source_system + source_id) |
| **Validity** | The degree to which data values conform to defined business rules and formats | % of values conforming to the defined domain, format, and business rules | Customer Interactions: `channel_code` value exists in the approved reference data set for 99.6% of records |

Not every dimension applies equally to every entity. The assessment shall identify which dimensions are most critical for each entity based on downstream consumer requirements.

## Workflow

### Step 1 — Scope the Assessment

Before measuring anything, establish:

1. **Which data product?** — Customer Cortex, Customer Interactions, Transcat, or cross-product.
2. **Which entities?** — Specific tables, views, or API payloads to assess (e.g., `dim_customer`, `fact_interaction`, `ref_merchant_category`).
3. **What triggered the assessment?** — New product release, SLA breach, consumer complaint, regulatory audit, periodic review, or proactive health check.
4. **Who are the downstream consumers?** — Which systems and teams consume this data, and what are their quality expectations?
5. **JIRA reference** — Any related epic, incident, or quality ticket (e.g., DME-XXXX).

If a JIRA key is provided, use `mcp__jira__jira_get_issue` to pull the issue description, status, and linked issues. Use `mcp__jira__jira_search_issues` with JQL patterns to find related quality incidents:

```
project = DME AND labels in (data-quality, quality-issue, dq-breach) AND status != Done
project = DME AND text ~ "data quality" AND created >= -90d
```

### Step 2 — Define Metrics

For each entity in scope:

1. **Select relevant dimensions** — not all six dimensions apply to every entity. Prioritise based on downstream consumer requirements.
2. **Define specific metrics** — one or more measurable metrics per dimension per entity/attribute.
3. **Set thresholds** — minimum acceptable quality level per metric. Use these defaults unless the PM provides overrides:

| Dimension | Default Threshold | Rationale |
|-----------|------------------|-----------|
| Completeness | ≥ 98% | Mandatory fields shall be populated for operational use |
| Accuracy | ≥ 99% | Financial services data shall be accurate |
| Timeliness | ≥ 99% | SLA compliance is contractual |
| Consistency | ≥ 97% | Cross-dataset consistency allows for transformation lag |
| Uniqueness | ≥ 99.9% | Duplicate records create material downstream errors |
| Validity | ≥ 99% | Invalid values break downstream processing |

4. **Assign weights** — weight each dimension by business criticality for the entity. Default weighting:
   - Accuracy: 25%, Completeness: 20%, Timeliness: 20%, Uniqueness: 15%, Validity: 10%, Consistency: 10%.

### Step 3 — Gather Baselines

Search for existing quality data before building from scratch:

1. Use `mcp__confluence__search_pages` to find existing quality reports, data dictionaries, or SLA documentation.
2. Use `mcp__jira__jira_search_issues` to find quality-related incidents, bugs, and remediation work:
   ```
   project = DME AND type = Bug AND labels in (data-quality) AND resolved >= -6m
   project = DME AND text ~ "quality score" AND type = Story
   ```
3. Review current monitoring — check if automated quality checks exist in ADAPT pipelines or Snowflake scheduled tasks.
4. Document what is already measured and what gaps exist.

### Step 4 — Build Scorecard

Produce the quality scorecard using the format in the "Quality Scorecard Format" section below. For each entity:

1. List every assessed attribute with its dimension, metric, threshold, and current value.
2. Calculate the per-attribute status using RAG thresholds.
3. Calculate per-entity and per-product scores using the weighted average methodology in "Quality Score Calculation".
4. Identify trend direction where historical data is available (↑ improving, → stable, ↓ declining).

Read `reference/data-quality-template.md` for the fillable skeleton.

### Step 5 — Identify Issues

For every attribute or entity scoring below threshold:

1. **Document the gap** — current value versus threshold, number of affected records.
2. **Categorise the root cause** — use these standard categories:

| Root Cause Category | Description | Example |
|--------------------|-------------|---------|
| Source system defect | Data is incorrect or missing at the source | Core Banking sends null `date_of_birth` for migrated accounts |
| Pipeline defect | Transformation or loading logic introduces errors | ADAPT pipeline truncates `address_line_2` at 50 characters |
| Schema mismatch | Source schema change not reflected in pipeline | New `channel_code` value added upstream, not in reference data |
| Timing issue | Data arrives outside the SLA window | Batch job delayed by upstream dependency |
| Duplicate ingestion | Same records loaded multiple times | Replay of failed batch without deduplication |
| Business rule gap | Rule not defined or incorrectly defined | Validation allows future dates for `account_open_date` |

3. **Assess impact** — which downstream consumers are affected and how.
4. **Assign severity** — use the incident classification in section 9 below.

### Step 6 — Define Monitoring

For each metric in the scorecard, define the monitoring approach:

1. **Check type** — automated rule, manual review, or statistical anomaly detection.
2. **Frequency** — real-time, daily, weekly, or monthly (see Monitoring Framework below).
3. **Alert threshold** — the value at which an alert shall be triggered (should be at or above the scorecard threshold).
4. **Notification target** — who receives the alert (individual, team channel, or escalation group).
5. **Remediation workflow** — what happens when an alert fires (auto-quarantine, manual review, incident creation).

### Step 7 — Produce Report

Generate the quality assessment report containing:

1. **Executive summary** — product quality score, overall RAG status, key findings, and recommended actions.
2. **Quality scorecard** — full scorecard table per entity.
3. **Issues register** — all attributes below threshold with root cause, impact, and severity.
4. **Monitoring recommendations** — proposed monitoring rules and frequencies.
5. **Remediation plan** — prioritised list of actions to improve quality scores.

Save the completed assessment as a markdown file named `{Product-Name}-Quality-Assessment.md` in the workspace root or a location the PM specifies.

## Quality Scorecard Format

The primary output of every quality assessment:

| Entity | Attribute | Dimension | Metric | Threshold | Current | Status | Trend |
|--------|-----------|-----------|--------|-----------|---------|--------|-------|
| dim_customer | customer_id | Uniqueness | % unique on composite key | ≥ 99.9% | 99.99% | 🟢 | → |
| dim_customer | email_address | Completeness | % non-null for active customers | ≥ 98% | 98.7% | 🟢 | ↑ |
| dim_customer | date_of_birth | Accuracy | % matching Core Banking source | ≥ 99% | 99.4% | 🟢 | → |
| dim_customer | address_line_1 | Completeness | % non-null | ≥ 98% | 96.2% | 🟡 | ↓ |
| fact_interaction | interaction_ts | Timeliness | % available within 15 min SLA | ≥ 99% | 99.1% | 🟢 | → |
| fact_interaction | channel_code | Validity | % in approved reference set | ≥ 99% | 99.6% | 🟢 | ↑ |
| ref_merchant_cat | category_code | Consistency | % consistent raw vs curated | ≥ 97% | 97.8% | 🟢 | → |

**Overall Product Quality Score:** [Weighted average] — [RAG status]

**RAG Thresholds:**

| Status | Threshold | Interpretation |
|--------|-----------|---------------|
| 🟢 Green | ≥ 95% | Quality meets or exceeds expectations |
| 🟡 Amber | 85% – 94% | Quality below target — monitoring and improvement required |
| 🔴 Red | < 85% | Quality critically below target — remediation required |

## Quality Score Calculation

### Per-Attribute Score

Each attribute score is its measured value expressed as a percentage:

```
Attribute Score = Current Value (already a %)
```

For example, if `email_address` completeness is 98.7%, the attribute score is 98.7.

### Per-Entity Score

Weighted average of all attribute scores for the entity, weighted by business criticality:

```
Entity Score = Σ (Attribute Score × Weight) / Σ Weights
```

Assign weights per attribute based on:
- **Critical** (weight 3): Attributes that directly affect customer-facing systems or regulatory reporting.
- **Important** (weight 2): Attributes used in operational decisions or analytics.
- **Standard** (weight 1): Attributes used for supplementary or internal purposes.

### Per-Product Score

Weighted average of all entity scores for the product:

```
Product Score = Σ (Entity Score × Entity Weight) / Σ Entity Weights
```

Entity weights should reflect the entity's importance to downstream consumers and business operations.

**Present the product score prominently:**

> **Customer Cortex Quality Score: 94.2% 🟡**
> Based on 4 entities, 28 attributes assessed on 28-Mar-2026.

## Data Quality Rules

Common rule patterns for Cortex Suite data products:

| Rule Type | Description | Example |
|-----------|-------------|---------|
| **Not Null** | Mandatory fields shall be populated | `customer_id` shall not be null |
| **Referential Integrity** | Foreign key references shall exist in the parent table | `account_id` in `fact_transaction` shall exist in `dim_account` |
| **Range Check** | Numeric values shall fall within defined bounds | `age` shall be between 18 and 120 |
| **Format Check** | Values shall match the defined format pattern | BSB format shall be NNN-NNN (three digits, hyphen, three digits) |
| **Freshness Check** | Data shall be updated within the defined SLA | `last_updated` shall be within 24 hours of the current timestamp |
| **Cross-Field Consistency** | Related fields shall be logically consistent | `account_open_date` shall be ≤ `account_close_date` |
| **Domain Check** | Values shall exist in the approved reference data set | `state_code` shall be in {NSW, VIC, QLD, SA, WA, TAS, NT, ACT} |
| **Statistical Anomaly** | Record counts and distributions shall not deviate beyond threshold | Daily record count shall not vary by more than ±20% from the 30-day rolling average |
| **Cross-Dataset Consistency** | Values shall match across related datasets | `customer_name` in Customer Cortex shall match `customer_name` in Customer Interactions |

When defining rules, specify:
- **Rule ID** — unique identifier (e.g., DQ-CC-001)
- **Entity and attribute** — what the rule applies to
- **Rule type** — from the table above
- **Rule definition** — precise, testable statement using "shall"
- **Severity** — what happens when the rule fails (block, quarantine, flag, log)

## Monitoring Framework

Data quality monitoring shall operate at four levels:

### Real-Time Checks (Pipeline Validation Gates)

- Executed within ADAPT pipelines as transformation steps complete.
- Checks: not null on primary keys, referential integrity, format validation.
- Action on failure: quarantine affected records, continue pipeline, raise alert.
- Scope: critical attributes only — checks shall not add more than 5% to pipeline execution time.

### Daily Batch Checks (Snowflake Scheduled Queries)

- Executed as Snowflake scheduled tasks after daily refresh completes.
- Checks: completeness percentages, accuracy sampling, freshness validation, duplicate detection.
- Action on failure: log to quality monitoring table, raise alert if below threshold.
- Output: daily quality metrics written to `dq_monitoring.daily_scores`.

### Weekly Quality Reports (Automated Scorecard Generation)

- Generated every Monday from the daily quality metrics.
- Content: entity-level scorecard, trend analysis (7-day), issues flagged during the week.
- Distribution: product team (Shalini, Sasi, relevant squad members).
- Format: markdown report or Confluence page update.

### Monthly Quality Reviews (Stakeholder Presentation)

- Comprehensive quality assessment across all entities and dimensions.
- Content: product-level quality score, trend analysis (30-day), resolved and open issues, remediation progress.
- Audience: product stakeholders, data governance, downstream consumer representatives.
- Format: presentation-ready summary with scorecard and commentary.

## Incident Classification

When quality breaches occur, classify severity as follows:

| Severity | Definition | Response Time | Escalation |
|----------|-----------|---------------|-----------|
| **P1 — Critical** | > 5% of records affected AND customer-facing impact (Digital Banker, Unity, WLive, AEP displaying incorrect data) | 1 hour | GM notification, war room established |
| **P2 — Major** | 1–5% of records affected OR operational impact (internal reports, analytics, or operational processes affected) | 4 hours | Team lead notification, incident ticket created |
| **P3 — Minor** | < 1% of records affected, no customer-facing or operational impact | Next business day | Logged in JIRA, addressed within current sprint |
| **P4 — Cosmetic** | Metadata, documentation, or labelling issues only — no data impact | Within sprint | Addressed as part of backlog grooming |

**Incident response requirements:**

- P1 and P2 incidents shall have a JIRA ticket created immediately with the label `data-quality`.
- P1 incidents shall include a root cause analysis (RCA) document within 5 business days of resolution.
- All incidents shall be reviewed in the monthly quality review.

## Quality Checklist

Before presenting any quality assessment, verify:

- [ ] Assessment scope is clearly defined (product, entities, trigger)
- [ ] All six dimensions have been considered (with justification for any excluded)
- [ ] Thresholds are defined for every metric (using defaults or PM-provided overrides)
- [ ] Scorecard includes current values, not placeholders
- [ ] RAG status is correctly calculated against thresholds
- [ ] Overall product quality score is calculated using weighted averages
- [ ] Issues are categorised with root cause, impact, and severity
- [ ] Monitoring recommendations include frequency, alert thresholds, and notification targets
- [ ] Remediation plan is prioritised by severity and business impact
- [ ] All dates use DD-MMM-YYYY format
- [ ] JIRA keys use the DME-XXXX format
- [ ] No startup jargon — professional banking language throughout
- [ ] "Shall" is used for mandatory requirements, "should" for recommendations

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use professional banking language. No "disrupt", "pivot", "hustle", or startup jargon.
- Name people explicitly — never say "the team" when you can name individuals.
- JIRA keys use the `DME-XXXX` format.
- Quality scores shall always include the RAG emoji (🟢, 🟡, 🔴) for visual clarity.
