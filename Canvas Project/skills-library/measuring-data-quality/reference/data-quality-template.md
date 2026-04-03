# Data Quality Assessment — [Product Name]

---

## 1. Document Header

| Field | Value |
|-------|-------|
| **Title** | [Product Name] — Data Quality Assessment |
| **Version** | 0.1 Draft |
| **Author** | Shalini Gangadharan |
| **Date** | [DD-MMM-YYYY] |
| **Status** | Draft / In Review / Approved |
| **JIRA Reference** | [DME-XXXX — link to epic or assessment ticket] |
| **Product** | [Customer Cortex / Customer Interactions / Transcat / Cross-Product] |
| **Assessment Trigger** | [New product release / SLA breach / Consumer complaint / Regulatory audit / Periodic review] |

---

## 2. Executive Summary

[2–3 paragraphs summarising: which product was assessed, how many entities and attributes were evaluated, the overall product quality score with RAG status, key findings (best and worst performing areas), and recommended actions.]

**Bottom Line:**
- **Product Quality Score:** [X.X%] [🟢/🟡/🔴]
- **Entities Assessed:** [N]
- **Attributes Assessed:** [N]
- **Critical Issues Found:** [N]
- **Assessment Date:** [DD-MMM-YYYY]

---

## 3. Scope

### Entities Assessed

| # | Entity | Layer | Description | Downstream Consumers |
|---|--------|-------|-------------|---------------------|
| 1 | [e.g., dim_customer] | [Curated / Consumption] | [Brief description] | [Digital Banker, Unity, etc.] |
| 2 | [e.g., fact_interaction] | [Curated / Consumption] | [Brief description] | [WLive, AEP, etc.] |
| 3 | [e.g., ref_merchant_category] | [Reference] | [Brief description] | [Transcat consumers] |

### Dimensions Assessed

| Dimension | Applicable | Weight | Rationale |
|-----------|-----------|--------|-----------|
| Completeness | Yes / No | [X%] | [Why this weight] |
| Accuracy | Yes / No | [X%] | [Why this weight] |
| Timeliness | Yes / No | [X%] | [Why this weight] |
| Consistency | Yes / No | [X%] | [Why this weight] |
| Uniqueness | Yes / No | [X%] | [Why this weight] |
| Validity | Yes / No | [X%] | [Why this weight] |
| **Total** | | **100%** | |

### Out of Scope

1. [Entity or dimension] — [Reason for exclusion]
2. [Entity or dimension] — [Reason for exclusion]

---

## 4. Quality Scorecard

### Entity: [Entity Name 1]

| Attribute | Dimension | Metric | Threshold | Current | Status | Trend | Weight |
|-----------|-----------|--------|-----------|---------|--------|-------|--------|
| [attribute_name] | Completeness | % non-null | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |
| [attribute_name] | Accuracy | % matching source | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |
| [attribute_name] | Uniqueness | % unique on key | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |
| [attribute_name] | Validity | % conforming to rules | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |
| [attribute_name] | Timeliness | % within SLA | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |
| [attribute_name] | Consistency | % consistent cross-dataset | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |

**Entity Quality Score:** [X.X%] [🟢/🟡/🔴]

### Entity: [Entity Name 2]

| Attribute | Dimension | Metric | Threshold | Current | Status | Trend | Weight |
|-----------|-----------|--------|-----------|---------|--------|-------|--------|
| [attribute_name] | [Dimension] | [Metric] | ≥ [X%] | [X.X%] | [🟢/🟡/🔴] | [↑/→/↓] | [1/2/3] |

**Entity Quality Score:** [X.X%] [🟢/🟡/🔴]

### Product Quality Summary

| Entity | Entity Weight | Entity Score | Weighted Score | Status |
|--------|--------------|-------------|----------------|--------|
| [Entity 1] | [X] | [X.X%] | [X.X] | [🟢/🟡/🔴] |
| [Entity 2] | [X] | [X.X%] | [X.X] | [🟢/🟡/🔴] |
| [Entity 3] | [X] | [X.X%] | [X.X] | [🟢/🟡/🔴] |
| **Product Total** | **[ΣW]** | | **[X.X%]** | **[🟢/🟡/🔴]** |

> **[Product Name] Quality Score: [X.X%] [🟢/🟡/🔴]**
> Based on [N] entities, [N] attributes assessed on [DD-MMM-YYYY].

---

## 5. Quality Rules Catalogue

| Rule ID | Entity | Attribute | Rule Type | Rule Definition | Severity |
|---------|--------|-----------|-----------|-----------------|----------|
| DQ-[PRD]-001 | [entity] | [attribute] | Not Null | `[attribute]` shall not be null | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-002 | [entity] | [attribute] | Referential Integrity | `[attribute]` shall exist in `[parent_table]` | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-003 | [entity] | [attribute] | Range Check | `[attribute]` shall be between [min] and [max] | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-004 | [entity] | [attribute] | Format Check | `[attribute]` shall match pattern [NNN-NNN / etc.] | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-005 | [entity] | [attribute] | Freshness Check | `[attribute]` shall be within [X hours] of current timestamp | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-006 | [entity] | [attr1], [attr2] | Cross-Field | `[attr1]` shall be ≤ `[attr2]` | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-007 | [entity] | [attribute] | Domain Check | `[attribute]` shall exist in [reference set] | [Block / Quarantine / Flag / Log] |
| DQ-[PRD]-008 | [entity] | — | Statistical Anomaly | Daily record count shall not vary by more than ±[X%] from 30-day rolling average | [Flag / Log] |

**Severity Definitions:**
- **Block**: Pipeline shall halt; records shall not proceed to downstream layers.
- **Quarantine**: Affected records shall be moved to a quarantine table; pipeline continues for clean records.
- **Flag**: Records shall be marked with a quality flag; pipeline continues.
- **Log**: Issue shall be logged to the monitoring table; no pipeline impact.

---

## 6. Monitoring Framework

### Real-Time Checks (ADAPT Pipeline Gates)

| # | Rule ID | Check Description | Action on Failure | Notes |
|---|---------|-------------------|-------------------|-------|
| 1 | DQ-[PRD]-001 | [Not null check on primary key] | Quarantine | [Notes] |
| 2 | DQ-[PRD]-002 | [Referential integrity check] | Quarantine | [Notes] |

### Daily Batch Checks (Snowflake Scheduled Tasks)

| # | Rule ID | Check Description | Alert Threshold | Notification Target | Notes |
|---|---------|-------------------|-----------------|---------------------|-------|
| 1 | DQ-[PRD]-003 | [Completeness % for mandatory fields] | < [X%] | [Person / channel] | [Notes] |
| 2 | DQ-[PRD]-004 | [Accuracy sampling against source] | < [X%] | [Person / channel] | [Notes] |
| 3 | DQ-[PRD]-008 | [Record count anomaly detection] | ± [X%] variance | [Person / channel] | [Notes] |

### Weekly Quality Report

| Item | Detail |
|------|--------|
| **Generated** | Every Monday, 08:00 AEST |
| **Source** | `dq_monitoring.daily_scores` (7-day window) |
| **Content** | Entity-level scorecard, 7-day trend, issues flagged |
| **Distribution** | [Shalini, Sasi, squad members] |
| **Format** | Markdown report / Confluence page |

### Monthly Quality Review

| Item | Detail |
|------|--------|
| **Scheduled** | First Thursday of each month |
| **Content** | Product-level quality score, 30-day trend, resolved/open issues, remediation progress |
| **Audience** | Product stakeholders, data governance, downstream consumer representatives |
| **Format** | Presentation-ready summary with scorecard and commentary |

---

## 7. Issues Register

| # | Entity | Attribute | Dimension | Current | Threshold | Gap | Root Cause Category | Impact | Severity | JIRA |
|---|--------|-----------|-----------|---------|-----------|-----|---------------------|--------|----------|------|
| 1 | [entity] | [attribute] | [dimension] | [X.X%] | [X%] | [X.X pp] | [Source system defect / Pipeline defect / Schema mismatch / Timing issue / Duplicate ingestion / Business rule gap] | [Which consumers affected, how] | [P1/P2/P3/P4] | [DME-XXXX] |
| 2 | [entity] | [attribute] | [dimension] | [X.X%] | [X%] | [X.X pp] | [Root cause] | [Impact] | [P1/P2/P3/P4] | [DME-XXXX] |

---

## 8. Remediation Plan

| Priority | Issue # | Action | Owner | Target Date | Status | Dependencies |
|----------|---------|--------|-------|-------------|--------|-------------|
| 1 | [#] | [Specific remediation action] | [Person name] | [DD-MMM-YYYY] | Not Started / In Progress / Done | [Any blockers] |
| 2 | [#] | [Specific remediation action] | [Person name] | [DD-MMM-YYYY] | Not Started / In Progress / Done | [Any blockers] |
| 3 | [#] | [Specific remediation action] | [Person name] | [DD-MMM-YYYY] | Not Started / In Progress / Done | [Any blockers] |

**Prioritisation criteria:**
1. P1 and P2 severity issues shall be remediated first.
2. Within the same severity, prioritise by number of downstream consumers affected.
3. Quick wins (< 2 days effort) should be addressed within the current sprint regardless of severity.

---

## 9. Incident Log

| # | Date | Severity | Entity | Description | Records Affected | Root Cause | Resolution | Resolved Date | JIRA |
|---|------|----------|--------|-------------|-----------------|------------|------------|---------------|------|
| 1 | [DD-MMM-YYYY] | [P1/P2/P3/P4] | [entity] | [Brief description] | [N records / X%] | [Root cause] | [What was done] | [DD-MMM-YYYY] | [DME-XXXX] |

---

## 10. Assumptions & Caveats

### Assumptions

1. Quality metrics are calculated against the curated layer unless otherwise stated.
2. Accuracy checks use the source system of record as the authoritative reference.
3. Timeliness SLAs are measured from source system event time to curated layer availability.
4. [Additional assumption]

### Caveats

1. Quality scores represent a point-in-time assessment and may vary with data volume fluctuations.
2. Accuracy sampling is based on [X%] of records — full-population accuracy checks may yield different results.
3. Assessment is valid for 30 calendar days from the date of issue.
4. [Additional caveat]

---

## 11. Appendix

### A. RAG Threshold Definitions

| Status | Threshold | Interpretation |
|--------|-----------|---------------|
| 🟢 Green | ≥ 95% | Quality meets or exceeds expectations |
| 🟡 Amber | 85% – 94% | Quality below target — monitoring and improvement required |
| 🔴 Red | < 85% | Quality critically below target — remediation required |

### B. Attribute Weight Definitions

| Weight | Label | Criteria |
|--------|-------|----------|
| 3 | Critical | Directly affects customer-facing systems or regulatory reporting |
| 2 | Important | Used in operational decisions or analytics |
| 1 | Standard | Used for supplementary or internal purposes |

### C. Incident Severity Definitions

| Severity | Definition | Response Time | Escalation |
|----------|-----------|---------------|-----------|
| P1 — Critical | > 5% records affected, customer-facing impact | 1 hour | GM notification |
| P2 — Major | 1–5% records affected, operational impact | 4 hours | Team lead notification |
| P3 — Minor | < 1% records affected, no customer impact | Next business day | JIRA ticket |
| P4 — Cosmetic | Metadata/documentation only | Within sprint | Backlog |

### D. Glossary

| Term | Definition |
|------|-----------|
| ADAPT | Westpac's enterprise data pipeline framework |
| ADLS2 | Azure Data Lake Storage Gen2 |
| AEP | Adobe Experience Platform |
| Cortex | Westpac's suite of Enterprise Data Products |
| DQ | Data Quality |
| EDP | Enterprise Data Product |
| RAG | Red / Amber / Green status indicator |
| RCA | Root Cause Analysis |
| SLA | Service Level Agreement |
| Transcat | Transaction Categorisation |

### E. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DD-MMM-YYYY] | Shalini Gangadharan | Initial assessment |
