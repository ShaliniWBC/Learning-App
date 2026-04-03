# PRD Template — Cortex Suite Enterprise Data Products

---

## 1. Document Header

| Field | Value |
|-------|-------|
| **Title** | [Feature/Capability Name] |
| **Version** | 0.1 Draft |
| **Author** | [PM Name] |
| **Status** | Draft |
| **Date** | [DD-MMM-YYYY] |
| **Parent Epic** | [JIRA-KEY — link to epic] |
| **Product** | [Customer Cortex / Customer Interactions / Transcat] |
| **Data Classification** | [Restricted / Confidential / Internal] |

---

## Table of Contents

1. [Problem Statement](#2-problem-statement)
2. [Strategic Alignment](#3-strategic-alignment)
3. [User Stories & Acceptance Criteria](#4-user-stories--acceptance-criteria)
4. [Scope](#5-scope)
5. [Data Requirements](#6-data-requirements)
6. [Technical Approach](#7-technical-approach)
7. [Dependencies & Assumptions](#8-dependencies--assumptions)
8. [Non-Functional Requirements](#9-non-functional-requirements)
9. [Stakeholders & Approvals](#10-stakeholders--approvals)
10. [Estimation](#11-estimation)
11. [Risks & Mitigations](#12-risks--mitigations)
12. [Success Metrics](#13-success-metrics)
13. [Appendix](#14-appendix)

---

## 2. Problem Statement

### What problem are we solving?

[Describe the specific problem, capability gap, or data quality issue. Be concrete — reference incidents, manual workarounds, or missed opportunities.]

### Who is affected?

[List the personas and teams impacted. Include both direct consumers and indirectly affected parties.]

- **Downstream system consumers**: [e.g., Digital Banker, Unity, WLive]
- **Internal analysts**: [e.g., Campaign analytics, Risk reporting]
- **Business stakeholders**: [e.g., Customer division, Marketing]
- **End customers**: [Indirect impact — describe how]

### What is the cost of inaction?

[Quantify where possible.]

- Hours of manual effort per week/month: [X]
- Data quality incidents per quarter: [X]
- Revenue/customer impact: [describe]
- Regulatory exposure: [describe if applicable]

---

## 3. Strategic Alignment

### OKR Mapping

| Level | Objective | Key Result |
|-------|-----------|------------|
| Enterprise | [Objective] | [Key Result this serves] |
| Product | [Objective] | [Key Result this serves] |

### Cortex Product Vision Alignment

[Describe how this feature/capability advances the Cortex product roadmap. Where does it sit on the maturity curve?]

### Enterprise Strategy Fit

[Describe alignment with broader Westpac data strategy — data mesh, cloud migration, customer 360, etc.]

---

## 4. User Stories & Acceptance Criteria

### Story 1: [Short title]

```
As a [persona],
I want [capability],
So that [outcome].
```

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

### Story 2: [Short title]

```
As a [persona],
I want [capability],
So that [outcome].
```

**Acceptance Criteria:**
- [ ] Given [context], when [action], then [result]
- [ ] Given [context], when [action], then [result]

<!-- Add more stories as needed. Consider these personas:
- Digital Banker API consumer
- Unity platform consumer
- WLive dashboard user
- AEP segment builder
- Data analyst (SQL/Snowflake direct)
- Data scientist (Databricks notebook user)
- Data product owner
- Data governance officer
- Downstream application developer (Mesh API consumer)
-->

---

## 5. Scope

### In Scope

1. [Item]
2. [Item]
3. [Item]

### Out of Scope

1. [Item] — [Reason]
2. [Item] — [Reason]

### Future Considerations

1. [Item — potential future iteration]
2. [Item — potential future iteration]

---

## 6. Data Requirements

| Attribute | Detail |
|-----------|--------|
| **Source System(s)** | [e.g., Core Banking, CRM, Digital channels] |
| **Key Attributes** | [List critical data fields/entities] |
| **Data Quality Expectations** | [Completeness %, accuracy %, timeliness SLA] |
| **SCD Handling** | [Type 1 / Type 2 / Type 3 — specify per entity] |
| **Refresh Cadence** | [Real-time / Near-real-time / Daily / Weekly] |
| **Volume Estimates** | [Row counts, growth rate] |
| **Retention Policy** | [Per data classification and regulatory requirements] |

### Key Entities & Attributes

| Entity | Attribute | Type | Description | Source |
|--------|-----------|------|-------------|--------|
| | | | | |

---

## 7. Technical Approach

### Architecture Overview

[Describe which layers are affected: Ingestion → Raw → Curated → Consumption. Keep high-level — this is not a TDD.]

### Pipeline Design

[ADAPT pipeline changes, new DAGs, Snowflake transformations, Databricks notebooks required.]

### Storage

[ADLS2 paths, Snowflake schemas, Cosmos DB collections affected.]

### API Contract Changes

[New/modified Mesh API endpoints, payload changes, versioning approach. Specify if breaking change.]

### Integration Points

| System | Integration Type | Change Required | Impact |
|--------|-----------------|-----------------|--------|
| Digital Banker | API | [Describe] | [L/M/H] |
| Unity | API | [Describe] | [L/M/H] |
| WLive | Direct query | [Describe] | [L/M/H] |
| AEP | Segment export | [Describe] | [L/M/H] |
| Salesforce | [Decommissioning] | [Describe] | [L/M/H] |

### Data Flow

[Describe the end-to-end data flow in text. Include source → ingestion → transformation → storage → consumption layers.]

---

## 8. Dependencies & Assumptions

### Dependencies

| # | Dependency | Team/System | Type | Status | Impact if Delayed |
|---|-----------|-------------|------|--------|-------------------|
| 1 | | | Cross-team / Architecture / Data source / Vendor | | |

### Assumptions

1. [Assumption — flag if needs validation]
2. [Assumption — flag if needs validation]

---

## 9. Non-Functional Requirements

| Requirement | Target | Measurement Method |
|-------------|--------|--------------------|
| **Performance** | [e.g., API response < 200ms p95] | [How measured] |
| **Availability** | [e.g., 99.9% uptime] | [How measured] |
| **Data Freshness** | [e.g., < 15 min latency from source] | [How measured] |
| **Volume** | [e.g., 50M records, 10% monthly growth] | [How measured] |
| **Data Classification** | [Restricted / Confidential / Internal] | [Per Westpac policy] |
| **Concurrency** | [Expected concurrent users/consumers] | [How measured] |
| **Recovery (RPO)** | [Recovery Point Objective] | [How measured] |
| **Recovery (RTO)** | [Recovery Time Objective] | [How measured] |

---

## 10. Stakeholders & Approvals

### RACI Matrix

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Requirements sign-off | | | | |
| Architecture review | | | | |
| Data governance review | | | | |
| Security review | | | | |
| Testing sign-off | | | | |
| Go-live approval | | | | |

### Key Stakeholders

| Name | Role | Team | Interest |
|------|------|------|----------|
| | | | |

---

## 11. Estimation

| Stream | Estimate (Sprints) | Confidence | Notes |
|--------|--------------------|------------|-------|
| Data Engineering | [X–Y] | [High/Medium/Low] | |
| Data Science | [X–Y] | [High/Medium/Low] | |
| Testing / QA | [X–Y] | [High/Medium/Low] | |
| Release Management | [X–Y] | [High/Medium/Low] | |
| **Total** | **[X–Y]** | **[Overall]** | |

**Confidence Definitions:**
- **High**: Well-understood scope, team has done similar work, estimates based on actuals.
- **Medium**: Scope mostly understood, some unknowns remain, estimates based on analogous work.
- **Low**: Significant unknowns, new technology/patterns, rough order of magnitude.

---

## 12. Risks & Mitigations

| # | Risk | Likelihood | Impact | Mitigation | Owner | Status |
|---|------|------------|--------|------------|-------|--------|
| 1 | | L / M / H | L / M / H | | | Open |
| 2 | | L / M / H | L / M / H | | | Open |

---

## 13. Success Metrics

| Metric | Target | Measurement Method | Review Cadence |
|--------|--------|--------------------|----------------|
| **Adoption** | [e.g., X downstream systems consuming within 3 months] | | [Monthly] |
| **Data Quality** | [e.g., Quality score > 95%] | | [Weekly] |
| **Performance** | [e.g., Pipeline SLA met 99% of runs] | | [Daily] |
| **Business Outcome** | [e.g., Reduction in manual effort by X hours/week] | | [Quarterly] |

---

## 14. Appendix

### A. JIRA Ticket Breakdown

| Ticket Key | Summary | Type | Status | Sprint |
|------------|---------|------|--------|--------|
| | | Story / Task / Bug | | |

### B. Data Dictionary

| Field Name | Data Type | Description | Source | Classification |
|------------|-----------|-------------|--------|----------------|
| | | | | |

### C. Architecture Diagrams

[Describe diagrams in text for rendering. Include data flow, system context, and integration diagrams as needed.]

### D. Glossary

| Acronym/Term | Definition |
|--------------|------------|
| ADAPT | [Westpac's data pipeline framework] |
| ADLS2 | Azure Data Lake Storage Gen2 |
| AEP | Adobe Experience Platform |
| Cortex | Westpac's suite of Enterprise Data Products |
| EDP | Enterprise Data Product |
| Mesh API | Data product consumption API layer |
| SCD | Slowly Changing Dimension |
| Transcat | Transaction Categorisation |

### E. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DD-MMM-YYYY] | [Name] | Initial draft |
