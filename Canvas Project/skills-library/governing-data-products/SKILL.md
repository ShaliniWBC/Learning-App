---
name: governing-data-products
description: "Produces data governance artefacts for Cortex Suite enterprise data products. Use when asked to create data contracts, quality SLAs, RBAC matrices, lineage documents, classification registers, or compliance checklists for Customer Cortex, Customer Interactions, Transcat, or any Cortex data product."
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

# Governing Data Products — Cortex Suite

Produces data product governance artefacts for Westpac's Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat).

## Context

You are assisting a Product Manager who leads the Cortex Suite within Westpac Group's Enterprise Data & Analytics function. All governance artefacts must reflect:

- **Enterprise data product context** — these are internal data platforms governed under data mesh principles, operating with a data-as-a-product mindset. Each product has defined producers, consumers, and contractual obligations.
- **Regulated banking environment** — APRA prudential standards, Privacy Act, Consumer Data Right, and internal Westpac data governance policies apply to all artefacts produced.
- **Cortex architecture** — ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.
- **Downstream consumers** — Digital Banker, Unity, WLive, AEP (Adobe Experience Platform), Salesforce (being decommissioned).
- **Westpac standards** — use professional banking language. No startup jargon. No "disrupt", "pivot", "hustle", "move fast and break things".

## Governance Artefact Types

| Artefact | Purpose | When to Produce | Audience |
|----------|---------|-----------------|----------|
| **Data Contract** | Defines the interface between producer and consumer — schema, quality guarantees, SLAs, and change management | When onboarding a new consumer or changing schema | Data engineers, consuming teams, governance officers |
| **Data Quality SLA** | Defines quality thresholds, measurement methods, and remediation procedures | During product setup or SLA review | Data product owners, data engineers, consumers |
| **RBAC Matrix** | Defines access permissions by role across data products and attributes | During security review or new consumer onboarding | Security officers, data governance, consuming teams |
| **Data Lineage Document** | Traces data from source systems through transformation to consumption endpoints | During architecture review or audit | Architects, auditors, data governance officers |
| **Data Classification Register** | Classifies data elements by sensitivity level per Westpac standards | During product setup or regulatory review | Data governance officers, security, compliance |
| **Compliance Checklist** | Verifies regulatory compliance across applicable standards | During release or audit preparation | Compliance officers, auditors, product owners |

## Workflow

### Step 1 — Identify Artefact Needed

Determine:
1. Which governance artefact is required?
2. Which Cortex product does this relate to? (Customer Cortex, Customer Interactions, Transcat, or cross-product)
3. What triggered this need? (New consumer onboarding, audit, schema change, regulatory review, periodic SLA review)
4. Is there an existing JIRA epic or Confluence page? If yes, gather the reference.

### Step 2 — Gather Context

**If a JIRA epic is referenced:**
- Use `mcp__jira__jira_get_issue` to pull the epic summary, description, status, and linked issues.
- Use `mcp__jira__jira_search_issues` with JQL to find related governance or compliance tickets.

**If a Confluence page is referenced or the topic is known:**
- Use `mcp__confluence__search_pages` to find existing governance documentation, data contracts, architecture decisions, or prior artefacts.
- Use `mcp__confluence__get_page` to read relevant pages for context before drafting.

**Always gather:**
- Data product metadata (entities, attributes, schemas, refresh cadence)
- Existing governance artefacts for the same product
- Consumer requirements and integration specifications
- Applicable regulatory obligations

### Step 3 — Draft Artefact

Use the appropriate template from `reference/data-governance-template.md`. Read the template before drafting and follow the structure precisely.

Adapt depth to the complexity of the governance need:
- **Single consumer onboarding**: Data contract + RBAC matrix
- **Product setup**: Full suite — contract, quality SLA, classification register, RBAC matrix
- **Audit preparation**: Lineage document, compliance checklist, classification register
- **Schema change**: Updated data contract, lineage impact assessment

### Step 4 — Validate

Cross-reference the drafted artefact against:
- **Architecture** — ADAPT pipeline definitions, Snowflake schema structures, Mesh API contracts
- **Downstream consumer requirements** — verify the artefact addresses all consuming systems' needs
- **Regulatory requirements** — confirm alignment with APRA CPS 220, CPS 234, CDR, Privacy Act
- **Existing governance artefacts** — ensure consistency with previously published contracts and SLAs

### Step 5 — Review

1. Present a summary of the artefact and key decisions made.
2. Identify gaps — flag sections where assumptions were made or information is incomplete.
3. Flag items requiring sign-off from an architect, data governance officer, or security officer.
4. Ask if the PM wants to adjust scope, add detail, or restructure.

## Data Contract Structure

A data contract shall contain the following sections:

### Producer

| Field | Value |
|-------|-------|
| **Product Name** | [e.g., Customer Cortex EDP001] |
| **Producer Team** | [Team name] |
| **Product Owner** | [Name and role] |
| **Contact** | [Email or channel] |

### Consumer

| Field | Value |
|-------|-------|
| **Consuming System** | [e.g., Digital Banker, Unity, WLive] |
| **Consumer Team** | [Team name] |
| **Consumer Contact** | [Name, email, or channel] |
| **Integration Method** | [Mesh API / Direct Snowflake query / File export] |

### Schema

| Entity | Attribute | Data Type | Nullable | Description | Classification |
|--------|-----------|-----------|----------|-------------|----------------|
| | | | Yes / No | | Restricted / Confidential / Internal |

### Quality Guarantees

| Dimension | Threshold | Measurement Method |
|-----------|-----------|-------------------|
| **Completeness** | [e.g., ≥ 99.5% for mandatory fields] | [Method] |
| **Accuracy** | [e.g., ≥ 99.0% against source] | [Method] |
| **Freshness** | [e.g., ≤ 15 minutes from source event] | [Method] |

### SLA

| Field | Value |
|-------|-------|
| **Availability** | [e.g., 99.9% during business hours] |
| **Latency** | [e.g., API response < 200ms p95] |
| **Support Hours** | [e.g., Mon–Fri 08:00–18:00 AEST] |
| **Incident Response** | [e.g., P1 within 30 minutes, P2 within 2 hours] |

### Change Management

| Field | Value |
|-------|-------|
| **Breaking Change Policy** | [e.g., 30-day notice with migration support] |
| **Notification Period** | [e.g., 14 days for non-breaking, 30 days for breaking] |
| **Versioning** | [e.g., Semantic versioning — Major.Minor] |
| **Deprecation Policy** | [e.g., Prior version supported for 90 days post-release] |

### Security

| Field | Value |
|-------|-------|
| **Data Classification** | [Restricted / Confidential / Internal / Public] |
| **Encryption at Rest** | [e.g., AES-256 via Azure Storage Service Encryption] |
| **Encryption in Transit** | [e.g., TLS 1.2 minimum] |
| **Access Method** | [e.g., Azure AD RBAC, service principal, Mesh API key] |

## Data Quality SLA Format

| Dimension | Metric | Threshold | Measurement Method | Remediation | Owner |
|-----------|--------|-----------|-------------------|-------------|-------|
| **Completeness** | Percentage of non-null values for mandatory fields | ≥ 99.5% | Automated profiling per pipeline run | Re-run pipeline; escalate to source if systemic | [Name] |
| **Accuracy** | Percentage of values matching source of truth | ≥ 99.0% | Sample-based reconciliation (daily) | Root cause analysis; source team engagement | [Name] |
| **Timeliness** | Time from source event to consumption availability | ≤ [X] minutes/hours | Pipeline monitoring dashboard | Escalate pipeline failure; invoke SLA breach process | [Name] |
| **Consistency** | Cross-entity referential integrity score | ≥ 99.0% | Automated constraint checks | Data engineering investigation; schema review | [Name] |
| **Uniqueness** | Percentage of records free from unintended duplicates | 100% | Deduplication check per load | Automated deduplication; root cause if recurring | [Name] |
| **Validity** | Percentage of values conforming to defined domain rules | ≥ 99.5% | Rule-based validation per pipeline run | Reject invalid records; notify source team | [Name] |

## RBAC Matrix Format

| Role | Data Product | Access Level | Entities / Attributes | Justification | Approved By | Expiry |
|------|-------------|-------------|----------------------|---------------|-------------|--------|
| [e.g., Data Analyst — Campaign] | Customer Cortex | Read | Customer demographics, segments | Campaign targeting analysis | [Governance Officer] | [DD-MMM-YYYY or Ongoing] |
| [e.g., Data Engineer — Cortex] | Customer Cortex | Read/Write | All entities | Pipeline development and maintenance | [Governance Officer] | Ongoing |
| [e.g., API Consumer — Digital Banker] | Customer Cortex | Read (API) | Customer summary, interaction history | Real-time customer profile rendering | [Governance Officer] | Ongoing |

## Data Classification

Westpac standard classification levels shall be applied:

| Classification | Description | Examples | Handling Requirements |
|---------------|-------------|----------|----------------------|
| **Restricted** | Highly sensitive data requiring the strictest controls | Credit data, PII (name, address, date of birth, TFN), financial transactions, account balances | Encrypted at rest and in transit; access logged; RBAC enforced; no bulk export without approval |
| **Confidential** | Internal data with limited distribution | Internal analytics outputs, model scores, propensity predictions, segment assignments | Encrypted at rest; access controlled by team/role; no external sharing |
| **Internal** | Data for internal use without significant sensitivity | Operational metadata, pipeline run logs, documentation, data catalogues | Standard access controls; available to authenticated internal users |
| **Public** | Data approved for external distribution | Published data product catalogues, public API documentation | No special controls required |

## Regulatory Considerations

All governance artefacts should address the following regulatory obligations where applicable:

### APRA CPS 220 — Risk Management

- Data products shall have documented risk assessments covering data quality, availability, and integrity risks.
- Risk appetite statements should reference the data product's role in downstream decision-making.

### APRA CPS 234 — Information Security

- Information assets (data products) shall be classified by sensitivity and criticality.
- Access controls shall be commensurate with the classification level.
- Security testing and vulnerability assessment requirements shall be documented.

### Consumer Data Right (CDR)

- Data products containing CDR-designated data shall identify affected attributes.
- Consent management and data sharing obligations shall be documented.
- Data retention and deletion requirements under CDR shall be specified.

### Privacy Act

- Personal information handling shall comply with the Australian Privacy Principles (APPs).
- Purpose limitation, collection minimisation, and disclosure controls shall be documented.
- Cross-border data transfer restrictions shall be identified where applicable.

## Quality Checklist

Before presenting any governance artefact, verify:

- [ ] Artefact type is appropriate for the governance need and trigger
- [ ] Data product name and version are correctly identified
- [ ] All data elements are classified per Westpac standards
- [ ] RBAC permissions follow least-privilege principle
- [ ] Quality thresholds are measurable and have defined remediation paths
- [ ] Change management procedures specify notification periods and versioning
- [ ] Regulatory obligations (APRA CPS 220, CPS 234, CDR, Privacy Act) are addressed where applicable
- [ ] Downstream consumer requirements are reflected in SLAs and contracts
- [ ] Architecture references (ADAPT, Snowflake, Databricks, ADLS2, Mesh APIs) are accurate
- [ ] All dates use DD-MMM-YYYY format
- [ ] "Shall" is used for mandatory requirements, "should" for recommendations
- [ ] No section contains placeholder text or is left empty without explanation
- [ ] Items requiring architect or governance officer sign-off are explicitly flagged

## Writing Style

- Use clear, professional language appropriate for banking/financial services.
- Avoid jargon from consumer tech/startup culture.
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Version numbers follow semantic convention: Major.Minor (e.g., 1.0, 1.1, 2.0).

## Output Format

- Output governance artefacts as Markdown documents.
- Use the header table format shown in the templates.
- Tables shall be properly formatted Markdown tables.
- Use horizontal rules (`---`) between major sections.
- Save completed artefacts with descriptive filenames (e.g., `Data-Contract-CustomerCortex-DigitalBanker-v1.0.md`).
