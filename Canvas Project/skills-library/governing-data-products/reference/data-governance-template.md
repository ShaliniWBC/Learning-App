# Data Governance Artefact Template — Cortex Suite

---

## Document Header

| Field | Value |
|-------|-------|
| **Artefact Type** | [Data Contract / Data Quality SLA / RBAC Matrix / Data Lineage Document / Data Classification Register / Compliance Checklist] |
| **Version** | 0.1 Draft |
| **Author** | [Author Name] |
| **Status** | Draft / In Review / Approved |
| **Date** | [DD-MMM-YYYY] |
| **Data Product** | [Customer Cortex EDP001 / Customer Interactions EDP006 / Transcat] |
| **Related JIRA** | [JIRA-KEY — link to epic or ticket] |
| **Data Classification** | [Restricted / Confidential / Internal] |
| **Next Review Date** | [DD-MMM-YYYY] |

---

## Table of Contents

1. [Data Contract](#1-data-contract)
2. [Data Quality SLA](#2-data-quality-sla)
3. [RBAC Matrix](#3-rbac-matrix)
4. [Data Lineage](#4-data-lineage)
5. [Data Classification Register](#5-data-classification-register)
6. [Compliance Checklist](#6-compliance-checklist)
7. [Approvals](#7-approvals)
8. [Change Log](#8-change-log)

---

## 1. Data Contract

### 1.1 Producer

| Field | Value |
|-------|-------|
| **Product Name** | [e.g., Customer Cortex EDP001] |
| **Producer Team** | [Team name] |
| **Product Owner** | [Name and role] |
| **Contact** | [Email or channel] |

### 1.2 Consumer

| Field | Value |
|-------|-------|
| **Consuming System** | [e.g., Digital Banker / Unity / WLive / AEP / Salesforce] |
| **Consumer Team** | [Team name] |
| **Consumer Contact** | [Name, email, or channel] |
| **Integration Method** | [Mesh API / Direct Snowflake query / File export / Event stream] |

### 1.3 Schema

| Entity | Attribute | Data Type | Nullable | Description | Classification |
|--------|-----------|-----------|----------|-------------|----------------|
| [Entity name] | [Attribute name] | [VARCHAR / INTEGER / TIMESTAMP / etc.] | Yes / No | [Description] | Restricted / Confidential / Internal |
| | | | | | |
| | | | | | |

### 1.4 Quality Guarantees

| Dimension | Threshold | Measurement Method |
|-----------|-----------|-------------------|
| **Completeness** | [e.g., ≥ 99.5% for mandatory fields] | [Automated profiling per pipeline run] |
| **Accuracy** | [e.g., ≥ 99.0% against source of truth] | [Sample-based reconciliation] |
| **Freshness** | [e.g., ≤ 15 minutes from source event] | [Pipeline monitoring dashboard] |

### 1.5 Service Level Agreement

| Field | Value |
|-------|-------|
| **Availability** | [e.g., 99.9% during business hours AEST] |
| **Latency** | [e.g., API response < 200ms p95] |
| **Support Hours** | [e.g., Mon–Fri 08:00–18:00 AEST] |
| **Incident Response** | [e.g., P1 within 30 minutes, P2 within 2 hours] |
| **Escalation Path** | [e.g., L1 → Data Engineering → Product Owner → Governance Officer] |

### 1.6 Change Management

| Field | Value |
|-------|-------|
| **Breaking Change Policy** | [e.g., 30-day notice with migration support] |
| **Notification Period** | [e.g., 14 days for non-breaking, 30 days for breaking] |
| **Versioning** | [e.g., Semantic versioning — Major.Minor] |
| **Deprecation Policy** | [e.g., Prior version supported for 90 days post-release] |
| **Communication Channel** | [e.g., Confluence page, email distribution list] |

### 1.7 Security

| Field | Value |
|-------|-------|
| **Data Classification** | [Restricted / Confidential / Internal / Public] |
| **Encryption at Rest** | [e.g., AES-256 via Azure Storage Service Encryption] |
| **Encryption in Transit** | [e.g., TLS 1.2 minimum] |
| **Access Method** | [e.g., Azure AD RBAC, service principal, Mesh API key] |
| **Audit Logging** | [e.g., All access logged to Azure Monitor] |

---

## 2. Data Quality SLA

| Dimension | Metric | Threshold | Measurement Method | Remediation | Owner |
|-----------|--------|-----------|-------------------|-------------|-------|
| **Completeness** | Percentage of non-null values for mandatory fields | ≥ [X]% | [e.g., Automated profiling per pipeline run] | [e.g., Re-run pipeline; escalate to source if systemic] | [Name] |
| **Accuracy** | Percentage of values matching source of truth | ≥ [X]% | [e.g., Sample-based reconciliation (daily)] | [e.g., Root cause analysis; source team engagement] | [Name] |
| **Timeliness** | Time from source event to consumption availability | ≤ [X] minutes/hours | [e.g., Pipeline monitoring dashboard] | [e.g., Escalate pipeline failure; invoke SLA breach process] | [Name] |
| **Consistency** | Cross-entity referential integrity score | ≥ [X]% | [e.g., Automated constraint checks] | [e.g., Data engineering investigation; schema review] | [Name] |
| **Uniqueness** | Percentage of records free from unintended duplicates | [X]% | [e.g., Deduplication check per load] | [e.g., Automated deduplication; root cause if recurring] | [Name] |
| **Validity** | Percentage of values conforming to defined domain rules | ≥ [X]% | [e.g., Rule-based validation per pipeline run] | [e.g., Reject invalid records; notify source team] | [Name] |

### SLA Breach Process

1. **Detection**: [Describe how breaches are detected — automated alerting, dashboard threshold triggers]
2. **Notification**: [Who is notified and within what timeframe]
3. **Investigation**: [Root cause analysis process and responsible team]
4. **Remediation**: [Corrective action and timeline]
5. **Post-Incident Review**: [Review cadence and documentation requirements]

---

## 3. RBAC Matrix

| Role | Data Product | Access Level | Entities / Attributes | Justification | Approved By | Expiry |
|------|-------------|-------------|----------------------|---------------|-------------|--------|
| [e.g., Data Analyst — Campaign] | [Product name] | Read | [Specific entities/attributes] | [Business justification] | [Governance Officer name] | [DD-MMM-YYYY or Ongoing] |
| [e.g., Data Engineer — Cortex] | [Product name] | Read/Write | [Specific entities/attributes or "All entities"] | [Business justification] | [Governance Officer name] | Ongoing |
| [e.g., API Consumer — Digital Banker] | [Product name] | Read (API) | [Specific entities/attributes] | [Business justification] | [Governance Officer name] | Ongoing |
| [e.g., Data Scientist — Models] | [Product name] | Read | [Specific entities/attributes] | [Business justification] | [Governance Officer name] | [DD-MMM-YYYY] |
| | | | | | | |

### Access Review Schedule

| Review Type | Frequency | Responsible | Last Completed | Next Due |
|-------------|-----------|-------------|----------------|----------|
| Quarterly access review | Quarterly | [Governance Officer] | [DD-MMM-YYYY] | [DD-MMM-YYYY] |
| Leaver/mover access revocation | Event-driven | [Security team] | N/A | N/A |
| Privileged access review | Monthly | [Security Officer] | [DD-MMM-YYYY] | [DD-MMM-YYYY] |

---

## 4. Data Lineage

### 4.1 Source Systems

| Source System | Description | Data Extracted | Extraction Method | Frequency |
|---------------|-------------|---------------|-------------------|-----------|
| [e.g., Core Banking] | [Description] | [Key entities/attributes] | [CDC / Batch / API / Event] | [Real-time / Daily / Hourly] |
| | | | | |

### 4.2 Transformation Layers

| Layer | Platform | Description | Key Transformations |
|-------|----------|-------------|-------------------|
| **Ingestion** | ADAPT | [Raw data landing] | [e.g., Schema validation, deduplication] |
| **Raw** | ADLS2 | [Immutable raw storage] | [e.g., Partitioning, format conversion] |
| **Curated** | Snowflake / Databricks | [Business-ready transformations] | [e.g., SCD Type 2, joins, aggregations] |
| **Consumption** | Snowflake / Cosmos DB / Mesh API | [Consumer-facing views and APIs] | [e.g., Materialised views, API projections] |

### 4.3 Data Flow

```
[Source System] → [ADAPT Pipeline] → [ADLS2 Raw Zone] → [Databricks/Snowflake Curated] → [Consumption Layer]
                                                                                              ├── Mesh API → Digital Banker
                                                                                              ├── Snowflake View → Unity
                                                                                              ├── Snowflake View → WLive
                                                                                              └── Export → AEP
```

[Replace the above with the specific data flow for this data product. Describe each transformation step, including business logic applied.]

### 4.4 Lineage Metadata

| Field | Value |
|-------|-------|
| **Last Validated** | [DD-MMM-YYYY] |
| **Validated By** | [Name and role] |
| **Lineage Tool** | [e.g., Manual documentation / Azure Purview / Custom] |
| **Known Gaps** | [List any undocumented transformation steps] |

---

## 5. Data Classification Register

| Entity | Attribute | Classification | Rationale | PII | CDR Designated | Handling Requirements |
|--------|-----------|---------------|-----------|-----|----------------|----------------------|
| [Entity name] | [Attribute name] | Restricted / Confidential / Internal / Public | [Why this classification] | Yes / No | Yes / No | [Specific controls required] |
| | | | | | | |
| | | | | | | |

### Classification Definitions

| Classification | Description | Examples |
|---------------|-------------|----------|
| **Restricted** | Highly sensitive data requiring the strictest controls | Credit data, PII, financial transactions, account balances |
| **Confidential** | Internal data with limited distribution | Analytics outputs, model scores, segment assignments |
| **Internal** | Data for internal use without significant sensitivity | Operational metadata, pipeline logs, documentation |
| **Public** | Data approved for external distribution | Published catalogues, public API documentation |

### Classification Review

| Field | Value |
|-------|-------|
| **Last Reviewed** | [DD-MMM-YYYY] |
| **Reviewed By** | [Governance Officer name] |
| **Next Review Due** | [DD-MMM-YYYY] |
| **Review Trigger** | [Scheduled / Schema change / Regulatory update] |

---

## 6. Compliance Checklist

### APRA CPS 220 — Risk Management

- [ ] Data product risk assessment is documented and current
- [ ] Risk appetite statement references the data product's role in downstream decision-making
- [ ] Material risk events have defined escalation paths
- [ ] Risk register is maintained and reviewed quarterly

### APRA CPS 234 — Information Security

- [ ] Information assets (data products) are classified by sensitivity and criticality
- [ ] Access controls are commensurate with the classification level
- [ ] Security testing has been conducted within the last 12 months
- [ ] Vulnerability assessment results are documented and remediated
- [ ] Third-party access (if any) is governed by appropriate agreements

### Consumer Data Right (CDR)

- [ ] CDR-designated data attributes are identified in the classification register
- [ ] Consent management obligations are documented
- [ ] Data sharing procedures comply with CDR rules
- [ ] Data retention and deletion requirements are specified
- [ ] N/A — this data product does not contain CDR-designated data

### Privacy Act — Australian Privacy Principles (APPs)

- [ ] Personal information handling complies with APPs
- [ ] Purpose limitation is documented (data collected only for stated purposes)
- [ ] Collection minimisation is applied (only necessary data is collected)
- [ ] Disclosure controls are in place (data shared only with authorised parties)
- [ ] Cross-border data transfer restrictions are identified (if applicable)
- [ ] N/A — this data product does not contain personal information

### Westpac Internal Standards

- [ ] Data classification aligns with Westpac Group Data Classification Standard
- [ ] RBAC follows least-privilege principle
- [ ] Data retention policy complies with Westpac records management requirements
- [ ] Change management procedures comply with Westpac Change Governance Framework
- [ ] Incident response procedures are documented and tested

---

## 7. Approvals

| Approval | Name | Role | Date | Status |
|----------|------|------|------|--------|
| **Data Product Owner** | [Name] | [Role] | [DD-MMM-YYYY] | Pending / Approved |
| **Data Governance Officer** | [Name] | [Role] | [DD-MMM-YYYY] | Pending / Approved |
| **Security Officer** | [Name] | [Role] | [DD-MMM-YYYY] | Pending / Approved |
| **Architecture Review** | [Name] | [Role] | [DD-MMM-YYYY] | Pending / Approved |
| **Compliance Officer** | [Name] | [Role] | [DD-MMM-YYYY] | Pending / Approved |

---

## 8. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DD-MMM-YYYY] | [Name] | Initial draft |
| | | | |

---

## Glossary

| Acronym / Term | Definition |
|----------------|------------|
| ADAPT | Westpac's data pipeline orchestration framework |
| ADLS2 | Azure Data Lake Storage Gen2 |
| AEP | Adobe Experience Platform |
| APP | Australian Privacy Principle |
| CDR | Consumer Data Right |
| CPS 220 | APRA Prudential Standard — Risk Management |
| CPS 234 | APRA Prudential Standard — Information Security |
| Cortex | Westpac's suite of Enterprise Data Products |
| EDP | Enterprise Data Product |
| Mesh API | Data product consumption API layer |
| PII | Personally Identifiable Information |
| RBAC | Role-Based Access Control |
| SCD | Slowly Changing Dimension |
| SLA | Service Level Agreement |
| Transcat | Transaction Categorisation |
