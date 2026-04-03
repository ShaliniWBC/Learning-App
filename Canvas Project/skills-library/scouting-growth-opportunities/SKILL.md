---
name: scouting-growth-opportunities
description: "Identifying and scoring new Cortex adoption opportunities across Westpac Group business units, producing ranked growth pipelines with value hypotheses and engagement strategies. Use when scouting new consumers, expanding Cortex adoption, building a growth pipeline, identifying use cases for Customer Cortex, Customer Interactions, or Transcat, or preparing for leadership updates on platform growth."
allowed-tools:
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_issue
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__outlook__outlook_search_emails
  - mcp__outlook__outlook_get_calendar_events
  - mcp__outlook__teams_search_messages
  - Read
  - create_file
  - edit_file
  - task_list
---

# Scouting Growth Opportunities — Cortex Suite

Identifies, scores, and prioritises new adoption opportunities for Cortex Suite data products across Westpac Group, producing a ranked growth pipeline with value hypotheses, entry strategies, and leadership-ready summaries.

## Context

The agent supports **Shalini Gangadharan**, Executive Manager / Product Manager for the Cortex Suite of Enterprise Data Products within Westpac Group's DDAI (Data, Digital and AI) Division. The Cortex Suite comprises:

- **Customer Cortex (EDP001)** — enterprise 360° customer view (demographics, financials, ML propensity scores, FICO)
- **Customer Interactions (EDP006)** — channel interaction data (branch, digital, CRM, call centre)
- **Transaction Categorisation (Transcat)** — enriched transaction data with merchant categorisation

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs (Info API, CAP API, GCM), RCMS v3.

**Current downstream consumers:** Digital Banker, Unity, WLive, Adobe Experience Platform (AEP), Salesforce (being decommissioned).

**Leadership landscape:**

| Stakeholder | Role | Relevance to Growth |
|---|---|---|
| Andrew McMullen | Group Executive, DDAI | Sets divisional priorities; growth pipeline visibility |
| Vicki Wood | General Manager, DDAI | Operational leadership; platform adoption metrics |
| Rohith E | Head of Data, DDAI | Data product strategy; cross-product synergies |
| Jeni Jose Mannanal | Head of Data, DDAI (Manager) | Direct line manager |
| Reza S | Chief AI Engineer | AI/ML adoption pathways |
| Phil Hood | Executive Manager, Data Science | Hawkeye and model-driven use cases |

Growth requires proactively identifying new use cases and consumers rather than waiting for teams to discover Cortex. Every new consumer adoption creates legitimate, value-driven exposure to new stakeholders and leadership. This skill helps the PM operate at Head of Product altitude — driving enterprise product growth across the Group, not merely maintaining a platform.

**Shalini's relevant background:** MIT Sloan, P&L ownership as Senior PM for Investment Products, built Deposit products from inception, championed digital origination platform that doubled new accounts, presented at Westpac TechX. This skill leverages that commercial and product growth experience.

## Growth Opportunity Dimensions

Every candidate opportunity shall be scored across six dimensions:

| # | Dimension | Weight | What to Assess |
|---|-----------|--------|----------------|
| 1 | **Strategic Fit** | 25% | Alignment with Group priorities — customer outcomes, AI adoption, data-driven decisioning, cloud migration |
| 2 | **Business Value** | 25% | Quantifiable impact — efficiency gains, risk reduction, revenue uplift, cost avoidance |
| 3 | **Data Readiness** | 15% | Does Cortex already hold the data the target team needs, or is enrichment/new ingestion required? |
| 4 | **Sponsorship Likelihood** | 15% | Is there an accessible sponsor who would champion adoption? Existing relationship, shared stakeholder, or warm pathway? |
| 5 | **Speed to Value** | 10% | How quickly can the target team onboard and demonstrate results? API-ready vs. bespoke build |
| 6 | **Regulatory / Governance Complexity** | 10% | Compliance requirements, data classification barriers, privacy constraints, model risk governance |

Weights may be adjusted if the PM specifies different priorities. Any adjustment shall be documented with rationale.

Each dimension shall be scored from 1 (low attractiveness / high difficulty) to 5 (high attractiveness / low difficulty). The weighted total determines pipeline ranking.

| Weighted Score | Priority Tier | Action |
|----------------|---------------|--------|
| 4.0–5.0 | **Tier 1 — Pursue Now** | Initiate engagement within the current quarter |
| 3.0–3.9 | **Tier 2 — Develop** | Build relationship and refine value hypothesis; engage within 1–2 quarters |
| 2.0–2.9 | **Tier 3 — Monitor** | Track for changes in readiness or strategic priority; revisit quarterly |
| <2.0 | **Tier 4 — Park** | Not viable under current conditions; document and archive |

## Workflow

### Step 1 — Scan for Opportunities

The agent shall gather signals from multiple sources to identify teams, initiatives, or business units that may benefit from Cortex data products.

**Internal sources to scan:**

1. **Confluence** — search for pages mentioning "customer data", "customer 360", "customer attributes", "propensity", "segmentation", "customer view", "data enrichment", "transaction data"
   ```
   mcp__confluence__search_pages(query="customer data", limit=25)
   mcp__confluence__search_pages(query="customer 360 view", limit=25)
   mcp__confluence__search_pages(query="propensity model", limit=25)
   ```
2. **JIRA** — search for cross-project dependencies referencing Cortex data, or epics in other projects that mention customer analytics
   ```
   mcp__jira__jira_search_issues(jql="text ~ 'customer cortex' AND project != DME", maxResults=25)
   mcp__jira__jira_search_issues(jql="text ~ 'customer 360' AND project != DME", maxResults=25)
   ```
3. **Outlook & Teams** — search for recent discussions about customer data needs, data requests, or platform enquiries
   ```
   mcp__outlook__outlook_search_emails(query="customer data request", maxResults=10)
   mcp__outlook__teams_search_messages(query="cortex data", maxResults=20)
   ```
4. **Organisational signals** — new teams, new initiatives, leadership priorities, internal job postings mentioning customer analytics or data engineering
5. **Architecture forums** — teams going through architecture review with data requirements that Cortex could serve
6. **AEP migration** — teams needing customer data for marketing automation on Adobe Experience Platform
7. **Salesforce decommissioning** — teams previously consuming customer data via Salesforce that need an alternative source

### Step 2 — Identify Target Business Units

The agent shall map Westpac Group divisions and product teams against Cortex capabilities. Priority targets include:

- Teams using **fragmented customer data** from multiple sources instead of a consolidated view
- Teams **building their own customer views** — duplicating capability that Cortex already provides
- Teams with **ML or analytics initiatives** that need curated feature data
- Teams **migrating off legacy platforms** (Teradata, Salesforce) that need a modern data source
- Teams with **new digital propositions** requiring customer context (e.g., personalisation, next-best-action)
- **Regulatory or compliance initiatives** that need authoritative customer data (e.g., KYC, AML, responsible lending)

For each candidate, the agent shall document:

| Field | Detail |
|---|---|
| Business Unit / Team | Name and division |
| Current State | How they source customer data today |
| Pain Point | What problem Cortex could solve |
| Known Contacts | Any existing relationships or shared stakeholders |
| Trigger Event | What is making this relevant now (new initiative, platform migration, regulatory change) |

### Step 3 — Score Each Opportunity

For each candidate identified in Step 2, the agent shall:

1. Score each of the six dimensions from 1 to 5 with brief evidence
2. Calculate the weighted total
3. Assign a Priority Tier
4. Flag any dimension scoring 1 or 2 as a risk to be addressed in the entry strategy

### Step 4 — Build Value Hypotheses

For each Tier 1 and Tier 2 opportunity, the agent shall articulate a value hypothesis:

> "If **[team]** used Cortex for **[use case]**, they would gain **[quantified benefit]** because **[reason / evidence]**."

The value hypothesis shall be:

- **Specific** — names the team, the data product, and the use case
- **Quantified where possible** — FTE savings, time reduction, risk avoidance, or revenue impact
- **Evidence-based** — grounded in what is known about the team's current state and Cortex's capabilities
- **Testable** — the hypothesis can be validated through a pilot or proof of concept

### Step 5 — Design Entry Strategy

For each Tier 1 and Tier 2 opportunity, the agent shall recommend an engagement approach:

1. **Who to approach** — the specific stakeholder (name and role) who is most likely to champion adoption
2. **Value-led reason** — the conversation opener framed around their problem, not Cortex's capabilities
3. **Warm pathway** — how to reach them (shared stakeholder introduction, architecture forum, existing meeting)
4. **First meeting format** — recommended format (15-minute informal chat, demo session, architecture review slot)
5. **Evidence to bring** — relevant case study from existing consumers, data availability confirmation, or prototype

### Step 6 — Produce Growth Pipeline

The agent shall compile the ranked pipeline using the Opportunity Scoring Table (below) and save it as a Markdown document. This pipeline becomes a recurring artefact for leadership updates.

## Opportunity Scoring Table

Primary output format for the growth pipeline:

| Rank | Business Unit / Team | Use Case | Strategic Fit (25%) | Business Value (25%) | Data Readiness (15%) | Sponsorship (15%) | Speed (10%) | Governance (10%) | Total Score | Tier | Value Hypothesis |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {team} | {use case} | {1–5} | {1–5} | {1–5} | {1–5} | {1–5} | {1–5} | {weighted} | {1–4} | {hypothesis} |
| 2 | {team} | {use case} | {1–5} | {1–5} | {1–5} | {1–5} | {1–5} | {1–5} | {weighted} | {1–4} | {hypothesis} |

## Entry Strategy Templates

The agent shall adapt these templates based on the engagement pathway:

### Warm Introduction via Shared Stakeholder

> "[Stakeholder] mentioned your team is working on [initiative]. Cortex already provides [relevant capability] — for example, [existing consumer] uses it for [similar use case]. Happy to share how that works and whether it could help accelerate your timeline."

### Problem-Led Outreach

> "I noticed [team] is building [capability/data pipeline]. We solved a similar problem for [existing consumer] using [specific Cortex product] — it saved them [quantified benefit]. Would it be worth a 15-minute conversation to see if there is overlap?"

### Data Dependency Pathway

> "[Team] is currently consuming raw data from [source]. Cortex already curates and enriches this data with [specific enrichments] — could save your team [estimated] weeks of data engineering and provide ongoing quality assurance."

### Architecture Forum Entry

> "During the architecture review for [initiative], we identified a dependency on customer data attributes. Cortex provides these via the [specific API] — [existing consumer] onboarded in [timeframe]. Shall we walk through the integration pattern?"

### Platform Migration Pathway

> "With the Salesforce decommissioning / Teradata migration, [team] will need an alternative source for [data type]. Cortex already serves this to [N] downstream consumers via Mesh APIs with [SLA]. Can we discuss the transition?"

## Where to Look for Signals

Practical sources for identifying adoption opportunities:

| Source | What to Search | Signal |
|---|---|---|
| Confluence | "customer data", "customer 360", "customer attributes", "propensity", "segmentation" | Teams documenting customer data requirements |
| JIRA | Cross-project dependencies mentioning Cortex; epics with "customer analytics" | Teams with data dependencies Cortex could fulfil |
| Org Announcements | New teams, new initiatives, leadership communications | Emerging capability builds that need customer data |
| Job Postings | Roles mentioning customer analytics, data engineering, ML feature engineering | Teams investing in data capabilities Cortex provides |
| Architecture Forums | Architecture review papers, design reviews with data components | Teams going through design with data needs |
| AEP Programme | Adobe Experience Platform onboarding teams | Marketing automation teams needing customer data |
| Salesforce Decommission | Teams currently consuming via Salesforce | Forced migration creates adoption window |
| Data Science Community | Model development, feature store discussions, ML pipeline designs | Teams needing curated features for model training |

## Cortex Capability Map

What Cortex can offer to new consumers:

| Capability | Product | Data Available | Example Use Case |
|---|---|---|---|
| Customer demographics & firmographics | EDP001 | Name, address, contact, segment, lifecycle stage | Customer onboarding, KYC, marketing segmentation |
| Financial position & product holdings | EDP001 | Account balances, product portfolio, credit exposure | Relationship depth analysis, cross-sell targeting |
| ML propensity scores | EDP001 | Churn, cross-sell, next-best-action, attrition scores | Proactive retention, campaign targeting, personalisation |
| FICO / credit decisioning attributes | Hawkeye | Credit scores, risk grades, application decisioning | Credit origination, risk assessment, portfolio management |
| Channel interaction history | EDP006 | Branch visits, digital sessions, call centre contacts, CRM interactions | Customer journey analysis, channel optimisation, service improvement |
| Transaction categorisation & merchant enrichment | Transcat | Categorised transactions, merchant identification, spending patterns | Financial wellness, budgeting tools, spending insights, affordability assessment |

## How This Creates Visibility

Each growth pipeline activity generates legitimate, value-driven exposure:

1. **New consumer conversations** put the PM in front of new business unit leadership — building cross-Group relationships
2. **Growth pipeline** becomes a standing agenda item in LT and leadership updates — demonstrating proactive product management
3. **Successful onboardings** become case studies for leadership forums, TechX presentations, and divisional showcases
4. **Proactive growth positioning** signals Head of Product / CPO behaviour to senior leadership — driving enterprise platform adoption, not waiting for demand
5. **Cross-functional engagement** with architecture, data science, and business teams builds the broad stakeholder network required for senior product roles
6. **Quantified adoption metrics** (consumers onboarded, data volumes served, use cases enabled) provide concrete evidence for career progression discussions

## Cadence

- **Monthly** — run the full workflow (Steps 1–6) to refresh the pipeline
- **Fortnightly** — review Tier 1 opportunities and update engagement status
- **Quarterly** — present pipeline summary to manager and leadership; review Tier 2 and 3 for promotion or archival
- **Ad hoc** — when a new organisational signal is identified (restructure, new initiative, platform migration), run a targeted scan

## Conventions

1. The agent **shall** use professional banking language appropriate for Westpac Group
2. All dates **shall** use DD-MMM-YYYY format (e.g., 28-Mar-2026)
3. The agent **shall** use "shall" for mandatory requirements and "should" for recommendations
4. The agent **shall not** use startup jargon — no "disrupt", "pivot", "hustle", "growth hacking", "move fast and break things"
5. Value hypotheses **shall** be specific, quantified where possible, and testable
6. Entry strategies **should** be framed around the target team's problem, not Cortex's features
7. The agent **shall** name stakeholders explicitly where known
8. Opportunity scores **shall** include brief evidence for each dimension
9. The agent **should** cross-reference JIRA and Confluence for context on identified opportunities
10. All artefacts **shall** be saved to the appropriate project directory

## Quality Checklist

Before presenting any growth pipeline or opportunity assessment, the agent shall verify:

- [ ] Opportunity scan has covered at least four signal sources (Confluence, JIRA, Teams, organisational signals)
- [ ] Each opportunity has been scored across all six dimensions with evidence
- [ ] Value hypotheses are specific, quantified where possible, and testable
- [ ] Entry strategies are value-led (framed around the target team's problem)
- [ ] Tier 1 opportunities have named stakeholders and recommended engagement pathways
- [ ] Cortex capability alignment is documented for each opportunity
- [ ] Pipeline is ranked by weighted score with Priority Tier assigned
- [ ] All dates use DD-MMM-YYYY format
- [ ] Language is professional — no startup jargon or informal language
- [ ] Pipeline summary is suitable for inclusion in a leadership update
- [ ] No speculative opportunities without supporting evidence or signal
- [ ] Artefact has been saved to the specified location

## Output Format

- Output the growth pipeline as a single Markdown document
- Use the Opportunity Scoring Table format for the ranked pipeline
- Include the value hypothesis and entry strategy for each Tier 1 and Tier 2 opportunity
- Save as `Cortex-Growth-Pipeline-[DD-MMM-YYYY].md` in the workspace root or a location the PM specifies
- Read `reference/growth-pipeline-template.md` for the fillable output template
