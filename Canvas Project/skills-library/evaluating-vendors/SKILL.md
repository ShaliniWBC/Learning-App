---
name: evaluating-vendors
description: "Produces build-vs-buy assessments and vendor evaluation scorecards for Cortex Suite technology decisions. Use when asked to evaluate a vendor, compare platforms, assess build vs buy, review a vendor renewal, or produce a technology selection recommendation."
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

# Vendor Evaluation & Build-vs-Buy Assessment Skill

Produces build-vs-buy assessments and vendor evaluation scorecards for Cortex Suite technology decisions, supporting procurement governance, architecture review, and Steering Committee approval.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite at Westpac Group. She owns three enterprise data products:

| Product | Code | Description |
|---------|------|-------------|
| Customer Cortex | EDP001 | Customer 360 data product |
| Customer Interactions | EDP006 | Interaction history and channel data |
| Transcat | — | Transaction categorisation |

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake Storage Gen2 (ADLS2), Cosmos DB, Mesh APIs.

**Active vendor-related initiatives:**
- **Project Hawkeye** — FICO replacement programme. Requires vendor evaluation for decisioning engine alternatives.
- **AEP Integration** — Adobe Experience Platform (AEP) integration with Cortex data products.
- **Salesforce Decommissioning** — Salesforce being retired; downstream consumers migrating to alternative platforms.

**Key stakeholders:**

| Stakeholder | Role | Relevance to Vendor Decisions |
|-------------|------|-------------------------------|
| **Carolyn McCann** | General Manager | Executive sponsor — approves vendor investments |
| **Damian McRae** | General Manager | Executive sponsor — approves vendor investments |
| **Mandar** | Architect | Architecture governance — assesses technical fit and integration |
| **Raja** | Architect | Architecture governance — assesses platform standards and security |

**JIRA project key:** DME.

Vendor decisions in enterprise banking require procurement governance, architecture review, security assessment, and Steering Committee approval. Every evaluation shall reflect these governance requirements.

## Evaluation Types

| Type | When to Use | Output |
|------|-------------|--------|
| **Build vs Buy** | Deciding whether to build a capability in-house or procure from a vendor | Decision brief with build-vs-buy matrix and recommendation |
| **Vendor Comparison** | Comparing 2–4 vendors for a specific capability | Weighted scorecard with TCO analysis |
| **Platform Assessment** | Evaluating a specific platform for fit within the Cortex architecture | Assessment report with technical fit analysis |
| **Renewal Review** | Assessing whether to renew, replace, or decommission an existing vendor | Recommendation paper with exit cost analysis |

## Workflow

### Step 1 — Define Evaluation Scope

Before evaluating, establish:

1. **What capability is being evaluated?** — Specific function or platform (e.g., decisioning engine, customer data platform, analytics tooling).
2. **What problem is being solved?** — Business need, capability gap, or risk being addressed.
3. **What evaluation type applies?** — Build vs Buy, Vendor Comparison, Platform Assessment, or Renewal Review (see table above).
4. **What constraints apply?**
   - Budget envelope (approved or indicative)
   - Timeline (decision deadline, implementation window)
   - Architecture constraints (must integrate with ADAPT, Snowflake, Azure ecosystem)
   - Regulatory constraints (data sovereignty, APRA compliance)
5. **Who is the decision-maker?** — SteerCo, GM, or architecture review board.
6. **Is there an existing JIRA epic or Confluence page?** If yes, get the reference.

If a JIRA key is provided, use `mcp__jira__jira_get_issue` to pull context. Use `mcp__confluence__search_pages` to find prior assessments, architecture decision records, or vendor evaluations.

### Step 2 — Establish Evaluation Criteria

Define weighted evaluation criteria. Use the standard criteria below unless the PM specifies otherwise:

| Criteria Category | Default Weight | What It Covers |
|-------------------|---------------|----------------|
| **Functional Fit** | 30% | Feature coverage, capability alignment, gap analysis |
| **Technical Fit** | 25% | Architecture compatibility, integration effort, scalability, performance |
| **Cost** | 20% | Licence, implementation, ongoing, hidden costs (TCO) |
| **Risk** | 10% | Vendor lock-in, data sovereignty, support model, exit complexity |
| **Strategic Alignment** | 10% | Alignment with Cortex roadmap, enterprise data strategy, Westpac direction |
| **Vendor Viability** | 5% | Financial stability, market position, customer base, product roadmap |

Weights shall total 100%. Adjust weights with justification if the initiative has specific priorities (e.g., a regulatory-driven initiative may weight Risk higher).

### Step 3 — Gather Information

Collect evidence for scoring from multiple sources:

1. **Vendor documentation** — Product datasheets, architecture guides, API documentation, pricing models.
2. **Architecture review inputs** — Request assessment from Mandar and Raja on technical fit, integration patterns, and security posture.
3. **Reference checks** — Customer references, analyst reports (Gartner, Forrester), industry case studies in banking and financial services.
4. **Internal sources:**
   - Use `mcp__confluence__search_pages` to find prior vendor assessments, architecture decision records, or procurement evaluations.
   - Use `mcp__jira__jira_search_issues` to find related initiatives or vendor-related epics.
5. **Proof of concept outcomes** — If a PoC has been conducted, incorporate results and findings.
6. **Procurement inputs** — Existing vendor agreements, contract terms, enterprise licensing arrangements.

### Step 4 — Score Options

Apply the weighted scoring model:

1. Score each option 1–5 against each criteria category using the scoring definitions below.
2. Calculate weighted scores (Score × Weight).
3. Document the evidence or rationale for each score — no unsupported scores.
4. Identify scoring differentiators — criteria where options diverge significantly.

**Scoring Scale:**

| Score | Definition |
|-------|-----------|
| **5** | Excellent — fully meets or exceeds requirements with no gaps |
| **4** | Good — meets most requirements with minor gaps that are manageable |
| **3** | Adequate — meets core requirements but with notable gaps or workarounds required |
| **2** | Weak — partially meets requirements; significant gaps or risks |
| **1** | Poor — does not meet requirements; fundamental gaps or incompatibilities |

### Step 5 — Analyse Total Cost of Ownership

Produce a 3-year TCO comparison for each option. Use the TCO Framework in section below. Include:

1. **Upfront costs** — Licence fees, implementation, integration development, data migration.
2. **Ongoing costs** — Annual subscription, support fees, infrastructure, internal maintenance effort.
3. **Hidden costs** — Integration development and maintenance, staff training and certification, data migration and cleansing, customisation and configuration, exit or migration costs if switching later.
4. **Internal effort** — FTE allocation for implementation, ongoing support, and vendor management.

If the estimating-costs skill has produced cost estimates for the build option, read that output and incorporate directly.

### Step 6 — Assess Risks

Evaluate each option against the following risk categories:

1. **Vendor lock-in** — Proprietary formats, APIs, data structures that impede future switching.
2. **Data sovereignty** — Where data is stored, processed, and accessed. Australian data residency requirements.
3. **Regulatory compliance** — APRA Prudential Standard CPS 234 (Information Security), CPS 231 (Outsourcing), APS 220 (Credit Risk Management where applicable).
4. **Support model** — SLA guarantees, support hours (Australian business hours), escalation paths, dedicated account management.
5. **Exit strategy** — Data portability, contract termination terms, migration effort if decommissioning.
6. **Security posture** — Encryption (at rest and in transit), RBAC, audit logging, penetration testing, SOC 2 / ISO 27001 certification.

Each risk shall have a likelihood (High/Medium/Low), impact (High/Medium/Low), and a proposed mitigation with named owner.

### Step 7 — Build vs Buy Analysis

If the evaluation includes an in-house build option:

1. Use the Build vs Buy Matrix (see section below) to structure the comparison.
2. For the build option, reference the estimating-costs skill output if available, or produce a high-level effort estimate using analogous work.
3. Compare the build TCO against vendor TCO over a 3-year horizon.
4. Assess strategic factors: IP ownership, customisation flexibility, dependency on internal capacity.
5. Consider opportunity cost — what else could the team deliver if they are not building this capability?

### Step 8 — Produce Recommendation

Deliver a clear recommendation:

1. **State the recommended option** — Which vendor, or build, and why.
2. **Summarise the evidence** — Reference scorecard totals, TCO comparison, and risk assessment.
3. **Address the second-best option** — Why it was not recommended despite its strengths.
4. **Propose risk mitigations** — Specific actions to address the top risks of the recommended option.
5. **Outline the implementation approach** — High-level phases, timeline, and resource requirements.
6. **Define the decision ask** — What the approver is being asked to do (approve, endorse, note).

Save the completed evaluation as a markdown file named `Vendor-Evaluation-[Capability-Name].md` in the workspace root or a location the PM specifies.

## Weighted Scorecard Format

The primary output for vendor comparisons:

| Criteria | Weight | Option A Score (1–5) | Option A Weighted | Option B Score (1–5) | Option B Weighted | Option C Score (1–5) | Option C Weighted |
|----------|--------|----------------------|-------------------|----------------------|-------------------|----------------------|-------------------|
| Functional Fit | 30% | | | | | | |
| Technical Fit | 25% | | | | | | |
| Cost | 20% | | | | | | |
| Risk | 10% | | | | | | |
| Strategic Alignment | 10% | | | | | | |
| Vendor Viability | 5% | | | | | | |
| **Total** | **100%** | | **X.XX** | | **X.XX** | | **X.XX** |

**Weighted Score Calculation:** Score (1–5) × Weight (decimal) = Weighted Score. Maximum possible total = 5.00.

**Scoring Evidence:** For each cell, provide a 1–2 sentence rationale in a supporting evidence table or footnotes. No score shall be awarded without justification.

## TCO Framework

3-year total cost comparison:

| Cost Category | Year 1 ($) | Year 2 ($) | Year 3 ($) | Total ($) |
|---------------|------------|------------|------------|-----------|
| Licence / Subscription | | | | |
| Implementation | | | | |
| Integration Development | | | | |
| Training & Certification | | | | |
| Support & Maintenance | | | | |
| Infrastructure | | | | |
| Exit / Migration (if applicable) | | | | |
| Internal Effort (FTE) | | | | |
| **Total** | **$X** | **$X** | **$X** | **$X** |

Produce one TCO table per option to enable like-for-like comparison. All values in AUD. Use $K for thousands, $M for millions.

## Build vs Buy Matrix

Structured comparison for build-vs-buy decisions:

| Dimension | Build (In-House) | Buy (Vendor) | Notes |
|-----------|------------------|--------------|-------|
| **Time to Value** | [Longer — development + testing + hardening] | [Shorter — configuration + integration] | [Compare sprint/month estimates] |
| **Upfront Cost** | [Development effort + infrastructure] | [Licence + implementation + integration] | [Reference TCO Year 1] |
| **Ongoing Cost** | [Maintenance, support, enhancements — internal FTE] | [Subscription + support fees + internal vendor management] | [Reference TCO Years 2–3] |
| **Customisation** | [Full control — built to specification] | [Configuration within vendor constraints; customisation may be limited or costly] | [Assess flexibility requirements] |
| **IP Ownership** | [Westpac owns the IP and codebase] | [Vendor owns the IP; Westpac has usage rights per licence] | [Strategic consideration] |
| **Risk** | [Delivery risk, team dependency, maintenance burden] | [Vendor dependency, lock-in, data sovereignty] | [Assess which risk profile is preferable] |
| **Maintenance** | [Ongoing internal effort; competes with feature delivery] | [Vendor maintains; internal effort for integration upkeep] | [Factor in team capacity] |
| **Strategic Fit** | [Aligns if capability is a differentiator] | [Aligns if capability is commodity or best-of-breed is available] | [Is this a differentiating or commodity capability?] |

## Banking-Specific Evaluation Criteria

Every vendor evaluation for Westpac shall assess these factors:

### Data Sovereignty
- Data shall reside in Australian data centres unless an explicit exemption is approved.
- Processing shall occur within Australian jurisdiction.
- Assess vendor's data centre locations and confirm Australian availability.
- Evaluate data residency controls and contractual guarantees.

### APRA Regulatory Compliance
- **CPS 234 (Information Security)** — Vendor shall meet or exceed Westpac's information security standards.
- **CPS 231 (Outsourcing)** — Material outsourcing arrangements require APRA notification and ongoing oversight.
- **APS 220 (Credit Risk Management)** — Applicable where the vendor provides credit decisioning or risk modelling capability (e.g., Project Hawkeye FICO replacement).
- Assess vendor's audit and compliance certification (SOC 2 Type II, ISO 27001).

### Architecture Integration
- Compatibility with ADAPT pipeline framework for data ingestion and transformation.
- Integration with Snowflake for analytical workloads and data warehousing.
- Compatibility with Databricks for data science and ML workflows.
- Storage alignment with ADLS2 for raw and curated data layers.
- API compatibility with Mesh API layer for data product consumption.
- Cosmos DB integration where real-time or low-latency access is required.

### Security and Access Control
- Role-Based Access Control (RBAC) aligned with Westpac's identity management.
- Encryption at rest (AES-256 minimum) and in transit (TLS 1.2 minimum).
- Comprehensive audit logging with tamper-proof log retention.
- Support for Westpac's security scanning and penetration testing requirements.
- Integration with Westpac's Single Sign-On (SSO) and identity provider.

### Vendor Financial Stability
- Assess vendor's financial position — revenue, profitability, funding status.
- Evaluate market position — analyst rankings (Gartner Magic Quadrant, Forrester Wave).
- Review customer base — number of enterprise banking customers, Australian references.
- Assess product roadmap alignment with Cortex Suite direction.

### Exit Strategy and Data Portability
- Contractual provisions for data extraction upon termination.
- Standard data export formats (CSV, Parquet, JSON — no proprietary-only formats).
- Transition assistance period and associated costs.
- Intellectual property rights to configurations, customisations, and integrations built during the engagement.

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- All dollar values in AUD unless otherwise stated. Use $K for thousands, $M for millions.
- Use professional banking language. No "disrupt", "pivot", "hustle", or startup jargon.
- Name people explicitly — never say "the team" when you can name individuals.
- JIRA keys use the `DME-XXXX` format.

## Quality Checklist

Before presenting any vendor evaluation, verify:

- [ ] Evaluation type is stated (Build vs Buy, Vendor Comparison, Platform Assessment, or Renewal Review)
- [ ] All criteria have scores with documented evidence — no unsupported scores
- [ ] Weighted scorecard totals are arithmetically correct
- [ ] TCO covers 3 years including hidden costs (integration, training, exit)
- [ ] Data sovereignty assessment is complete (Australian data residency confirmed or flagged)
- [ ] APRA regulatory compliance has been assessed (CPS 234, CPS 231, APS 220 where applicable)
- [ ] Architecture integration assessment addresses ADAPT, Snowflake, Databricks, ADLS2, Cosmos DB, and Mesh APIs
- [ ] Security assessment covers RBAC, encryption, audit logging, and SSO integration
- [ ] Exit strategy and data portability are evaluated
- [ ] Risk register includes mitigations with named owners and due dates
- [ ] Recommendation is clearly stated with the decision ask (approve, endorse, note)
- [ ] Build vs buy analysis references estimating-costs skill output where applicable
- [ ] All dates use DD-MMM-YYYY format
- [ ] No startup jargon — professional banking language throughout
