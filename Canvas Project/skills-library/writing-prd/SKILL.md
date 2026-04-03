---
name: writing-prd
description: "Writes Product Requirements Documents for Cortex Suite enterprise data products. Use when asked to write a PRD, product requirements, feature spec, or requirements document for Customer Cortex, Customer Interactions, Transcat, or any Cortex data product."
---

# Writing PRDs for Cortex Suite Data Products

Produces enterprise-grade Product Requirements Documents for Westpac's Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat).

## Context

You are assisting a Product Manager who leads the Cortex Suite within Westpac Group's Enterprise Data & Analytics function. All PRDs must reflect:

- **Enterprise data product context** — not consumer SaaS. These are internal data platforms consumed by downstream systems and teams.
- **Banking governance requirements** — data classification, RBAC, regulatory compliance, change management.
- **Cortex architecture** — ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.
- **Downstream consumers** — Digital Banker, Unity, WLive, AEP (Adobe Experience Platform), Salesforce (being decommissioned).
- **Westpac standards** — use professional banking language. No startup jargon. No "disrupt", "pivot", "hustle", "move fast and break things".

## Workflow

### Step 1: Gather Context

Before drafting anything, ask clarifying questions. Do NOT jump straight to writing.

**Always ask:**
1. What is the feature/capability being requested?
2. Which Cortex product does this relate to? (Customer Cortex, Customer Interactions, Transcat, or cross-product)
3. Is there an existing JIRA epic? If yes, get the key (e.g., CRTX-1234).
4. Who requested this? (Stakeholder name, team, channel)
5. What is the target delivery timeframe?
6. Are there any known constraints or dependencies?

**If a JIRA epic is referenced:**
- Use `mcp__jira__jira_get_issue` to pull the epic summary, description, status, and linked issues.
- Use `mcp__jira__jira_search_issues` with JQL `"Epic Link" = <EPIC-KEY>` or `parent = <EPIC-KEY>` to find child stories/tasks.

**If a Confluence page is referenced or the topic is known:**
- Use `mcp__confluence__search_pages` to find existing documentation, design decisions, or prior PRDs on the topic.
- Read relevant pages for context before drafting.

### Step 2: Draft the PRD

Use the template structure below. Read `reference/prd-template.md` for the fillable skeleton.

Adapt section depth to the size of the feature:
- **Small enhancement**: Lighter sections, 3–5 pages equivalent
- **Major capability**: Full depth, 8–15 pages equivalent
- **Platform change**: Full depth plus architecture appendix

### Step 3: Review & Iterate

After drafting:
1. Present a summary of what was written and key decisions made.
2. Call out any sections where assumptions were made and flag them for review.
3. Ask if the PM wants to adjust scope, add detail, or restructure.

## PRD Section Structure

Every PRD must include these sections in order:

### 1. Document Header

| Field | Value |
|-------|-------|
| **Title** | [Feature/Capability Name] |
| **Version** | [e.g., 0.1 Draft] |
| **Author** | [PM Name] |
| **Status** | Draft / In Review / Approved |
| **Date** | [Created date] |
| **Parent Epic** | [JIRA key with link, e.g., CRTX-1234] |
| **Product** | Customer Cortex / Customer Interactions / Transcat |
| **Data Classification** | [Restricted / Confidential / Internal] |

### 2. Problem Statement

Address three questions:
- **What problem are we solving?** — Be specific. Reference data quality issues, capability gaps, or business process friction.
- **Who is affected?** — Name the personas: downstream system consumers, internal analysts, business stakeholders, end customers (indirectly).
- **What is the cost of inaction?** — Quantify where possible: manual effort hours, data quality incidents, missed revenue, regulatory exposure.

### 3. Strategic Alignment

- **OKR Mapping**: Which Objective and Key Result does this serve? Reference the specific OKR code if available.
- **Cortex Product Vision**: How does this advance the product roadmap? Where does it sit on the maturity curve?
- **Enterprise Strategy Fit**: How does this align with broader Westpac data strategy (e.g., data mesh, cloud migration, customer 360)?

### 4. User Stories & Acceptance Criteria

Write user stories in standard format with data-product-specific personas:

```
As a [persona],
I want [capability],
So that [outcome].

Acceptance Criteria:
- Given [context], when [action], then [result]
- ...
```

**Standard Cortex personas to consider:**
- Digital Banker API consumer
- Unity platform consumer
- WLive dashboard user
- AEP segment builder
- Data analyst (SQL/Snowflake direct)
- Data scientist (Databricks notebook user)
- Data product owner
- Data governance officer
- Downstream application developer (Mesh API consumer)

### 5. Scope

Structure as three clear lists:

**In Scope:**
- Numbered list of what this PRD covers

**Out of Scope:**
- Numbered list of what this PRD explicitly does NOT cover (and why)

**Future Considerations:**
- Items that may be addressed in subsequent iterations

### 6. Data Requirements

| Attribute | Detail |
|-----------|--------|
| **Source System(s)** | [e.g., Core Banking, CRM, Digital channels] |
| **Key Attributes** | [List critical data fields] |
| **Data Quality Expectations** | [Completeness, accuracy, timeliness thresholds] |
| **SCD Handling** | [Type 1 / Type 2 / Type 3 — specify per entity] |
| **Refresh Cadence** | [Real-time / Near-real-time / Daily / Weekly] |
| **Volume Estimates** | [Row counts, growth rate] |
| **Retention Policy** | [Per data classification and regulatory requirements] |

### 7. Technical Approach

High-level only — this is not a TDD. Include:

- **Architecture Overview**: Which layers are affected? (Ingestion → Raw → Curated → Consumption)
- **Pipeline Design**: ADAPT pipeline changes, new DAGs, Snowflake transformations, Databricks notebooks.
- **Storage**: ADLS2 paths, Snowflake schemas, Cosmos DB collections affected.
- **API Contract Changes**: New/modified Mesh API endpoints, payload changes, versioning approach.
- **Integration Points**: Which downstream systems need changes? (Digital Banker, Unity, WLive, AEP, Salesforce)
- **Data Flow Diagram**: Describe the flow in text — Amp can render as a diagram description.

### 8. Dependencies & Assumptions

**Dependencies:**
- Cross-team dependencies (name the team and what's needed)
- Architecture dependencies (platform changes required)
- Data source dependencies (new feeds, schema changes)
- External vendor dependencies

**Assumptions:**
- Numbered list of assumptions that underpin this PRD
- Flag any that need validation

### 9. Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| **Performance** | [e.g., API response < 200ms p95] |
| **Availability** | [e.g., 99.9% uptime] |
| **Data Freshness** | [e.g., < 15 min latency from source] |
| **Volume** | [e.g., 50M records, 10% monthly growth] |
| **Data Classification** | [Restricted / Confidential / Internal] |
| **Concurrency** | [Expected concurrent users/consumers] |
| **Recovery** | [RPO/RTO targets] |

### 10. Stakeholders & Approvals

**RACI Matrix:**

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Requirements sign-off | | | | |
| Architecture review | | | | |
| Data governance review | | | | |
| Security review | | | | |
| Testing sign-off | | | | |
| Go-live approval | | | | |

### 11. Estimation

Provide effort estimates by stream with confidence levels.

| Stream | Estimate | Confidence | Notes |
|--------|----------|------------|-------|
| Data Engineering | [e.g., 3–5 sprints] | Medium | |
| Data Science | [e.g., 1 sprint] | High | |
| Testing / QA | [e.g., 2 sprints] | Low | Depends on test data availability |
| Release Management | [e.g., 1 sprint] | Medium | |
| **Total** | [range] | [overall] | |

**Confidence definitions:**
- **High**: Well-understood scope, team has done similar work, estimates based on actuals.
- **Medium**: Scope mostly understood, some unknowns remain, estimates based on analogous work.
- **Low**: Significant unknowns, new technology/patterns, estimates are rough order of magnitude.

### 12. Risks & Mitigations

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|------|------------|--------|------------|-------|
| 1 | | L/M/H | L/M/H | | |

### 13. Success Metrics

Define measurable KPIs:
- **Adoption**: [e.g., X downstream systems consuming within 3 months]
- **Quality**: [e.g., Data quality score > 95%]
- **Performance**: [e.g., Pipeline SLA met 99% of runs]
- **Business Outcome**: [e.g., Reduction in manual effort by X hours/week]

Include measurement method and review cadence.

### 14. Appendix

- **JIRA Ticket Breakdown**: Table mapping stories/tasks to this PRD's scope
- **Data Dictionary**: Key entities and attributes with definitions
- **Architecture Diagrams**: Text description of diagrams (for rendering)
- **Glossary**: Define acronyms and Cortex-specific terminology
- **Change Log**: Track PRD revisions

## Writing Style Guidelines

- Use clear, professional language appropriate for banking/financial services.
- Avoid jargon from consumer tech/startup culture.
- Be precise about data terminology — distinguish between attributes, entities, measures, dimensions.
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Version numbers follow semantic convention: Major.Minor (e.g., 1.0, 1.1, 2.0).

## Output Format

- Output the PRD as a single Markdown document.
- Use the header table format shown in the template.
- Include a table of contents after the header.
- Use horizontal rules (`---`) between major sections.
- Tables must be properly formatted Markdown tables.

## Tools Available

When writing PRDs, use these tools as needed:
- **JIRA**: Pull epic details, child stories, sprint context via `mcp__jira__jira_get_issue` and `mcp__jira__jira_search_issues`.
- **Confluence**: Search for existing docs, design decisions, prior PRDs via `mcp__confluence__search_pages` and `mcp__confluence__get_page`.
- **File system**: Read existing documents or data dictionaries from the workspace.
