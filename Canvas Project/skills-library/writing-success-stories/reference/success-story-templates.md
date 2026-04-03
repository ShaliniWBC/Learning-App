# Success Story Templates — Cortex Suite

Reference templates for each success story format. Read the appropriate template, replace all `{placeholder}` markers with actual content, and remove any guidance text in parentheses.

---

## Template 1: 1-Page Case Study

```
# {Action-Oriented Title}
Example: "How Digital Banker Reduced Onboarding Time by 67% with Cortex"

| Field | Value |
|-------|-------|
| **Consumer** | {Consumer name — e.g., Digital Banker, Unity, WLive, AEP} |
| **Cortex Product(s)** | {Customer Cortex EDP001 / Customer Interactions EDP006 / Transcat} |
| **Date** | {DD-MMM-YYYY} |
| **Author** | {Author name} |

## The Challenge

{2–3 sentences describing the consumer's problem in business terms.
Frame the cost of inaction — what happened if this was not solved.
Lead with the consumer's pain, not Cortex's capabilities.}

## Why Cortex

{2–3 sentences explaining why Cortex was the right solution.
Note what alternatives existed and why they were insufficient.
Establish Cortex's strategic positioning for this use case.}

## The Implementation

{1 paragraph covering:
- Timeline: {start date} to {go-live date} ({duration})
- Key architectural decisions (e.g., API vs batch, real-time vs near-real-time)
- Integration pattern used (e.g., Mesh API, direct Snowflake access, event-driven)
- Team members involved: {names and roles}
- Any notable challenges overcome during delivery}

## The Outcome

{Quantified results — include at least 2–3 metrics:}

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| {Metric 1 — e.g., Onboarding Time} | {e.g., 6 weeks} | {e.g., 2 weeks} | {e.g., 67% reduction} |
| {Metric 2 — e.g., Data Freshness} | {e.g., 48 hours} | {e.g., 15 minutes} | {e.g., 99.5% improvement} |
| {Metric 3 — e.g., Manual Effort} | {e.g., 40 hrs/month} | {e.g., 2 hrs/month} | {e.g., 95% reduction} |

{Include a direct quote from the consumer if available:}

> "{Consumer quote about the impact}" — {Consumer name, role}

## The Reusable Pattern

{1 paragraph describing the key insight other teams can learn from this implementation.
What did this prove? What pattern emerged?
Frame as a transferable lesson, not a specific solution.}

**Pattern**: {One-sentence summary of the reusable pattern — e.g., "Cortex Mesh APIs can serve real-time scoring use cases with sub-200ms latency when backed by Cosmos DB."}

## Where Else This Works

- **{Team/Consumer 1}**: {Why this pattern applies to them — 1 sentence}
- **{Team/Consumer 2}**: {Why this pattern applies to them — 1 sentence}
- **{Team/Consumer 3}**: {Why this pattern applies to them — 1 sentence}
```

---

## Template 2: 3-Slide Story Outline

Use this outline to build a visual presentation. Each slide maps to a section below.

```
## Slide 1 — Title & Problem

**Title**: {Action-oriented title — same as case study}
**Subtitle**: {Cortex Suite | Consumer: {name} | {DD-MMM-YYYY}}

**Content**:
- {Consumer name} needed: {1-sentence problem statement}
- Cost of inaction: {what happened without a solution}
- Key question: {the question this implementation answered}

**Visual**: {Suggest a visual — e.g., before/after diagram, timeline, process flow}

## Slide 2 — Solution & Implementation

**Content**:
- Why Cortex: {1–2 bullets on why Cortex was chosen}
- Integration pattern: {e.g., Mesh API, Snowflake direct, event-driven}
- Timeline: {start} → {go-live} ({duration})
- Team: {key people involved}

**Visual**: {Suggest a visual — e.g., architecture diagram, integration flow}

## Slide 3 — Outcome & Where Else

**Content**:
- Key metric 1: {before} → {after} ({improvement})
- Key metric 2: {before} → {after} ({improvement})
- Consumer quote: "{quote}" — {name}
- Reusable pattern: {one-sentence pattern summary}

**Where else this works**:
- {Team 1}: {why}
- {Team 2}: {why}

**Visual**: {Suggest a visual — e.g., metrics dashboard, comparison chart}
```

---

## Template 3: Quick Win Post

For Teams channels, intranet posts, and newsletters. Shall be conversational but professional — no startup jargon.

```
## 🏆 {Headline — action-oriented, outcome-focused}
Example: "Digital Banker Goes Live with Real-Time Customer Scoring via Cortex"

**What happened**: {1 paragraph — what was delivered, for whom, and when.
Name the consumer and the Cortex product. Include the go-live date in DD-MMM-YYYY format.}

**Why it matters**: {1 paragraph — the business outcome in quantified terms.
What changed for the consumer? How does this benefit Westpac?
Include at least one specific metric.}

**The team**: {1 paragraph — name the people who delivered this.
Credit specific contributions. This builds visibility for the team, not just the product.}

**What's next**: {1 paragraph — where else this pattern could be applied.
Name specific teams or use cases. Signal growth thinking.}

**Learn more**: {Link to the full case study on Confluence, if available.}
```

---

## Template 4: Reusable Pattern

For architecture forums, integration playbooks, and other product teams. Technical focus with enough context for teams unfamiliar with Cortex.

```
# Reusable Pattern: {Pattern Name}
Example: "Real-Time Customer Scoring via Cortex Mesh API"

| Field | Value |
|-------|-------|
| **Pattern Name** | {Descriptive name for the integration pattern} |
| **Origin** | {Consumer implementation where this pattern was first used} |
| **Cortex Product(s)** | {Customer Cortex EDP001 / Customer Interactions EDP006 / Transcat} |
| **Date Documented** | {DD-MMM-YYYY} |
| **Author** | {Author name} |
| **Status** | {Proven / Experimental / Proposed} |

## Problem Statement

{2–3 sentences describing the class of problem this pattern solves.
Frame generically — not tied to the original consumer.
Example: "Multiple downstream consumers require real-time access to customer propensity scores
but currently rely on batch extracts with 24–48 hour latency."}

## Pattern Description

{1–2 paragraphs describing the integration pattern in technical terms.
Include:
- Architecture components involved (e.g., Mesh API, Cosmos DB, Snowflake, ADLS2)
- Data flow (source → transformation → serving layer → consumer)
- Key design decisions and rationale
- Performance characteristics (latency, throughput, availability)}

## Architecture Diagram

{Describe the architecture or reference an attached diagram.}

```
{Source} → {Processing Layer} → {Serving Layer} → {Consumer}
Example:
Snowflake → Databricks (ML scoring) → Cosmos DB → Mesh API (Info API) → Consumer App
```

## Implementation Guide

### Prerequisites
- {Prerequisite 1 — e.g., consumer must be onboarded to Cortex API gateway}
- {Prerequisite 2 — e.g., data domain must be registered in Cortex catalogue}

### Steps
1. {Step 1 — e.g., Define data contract with Cortex team}
2. {Step 2 — e.g., Configure API access via Mesh API gateway}
3. {Step 3 — e.g., Implement consumer-side integration}
4. {Step 4 — e.g., Validate in ADAPT non-production environment}
5. {Step 5 — e.g., Production go-live with monitoring}

### Estimated Timeline
| Phase | Duration | Notes |
|-------|----------|-------|
| Design & Contract | {X weeks} | {Assumes data domain already exists} |
| Build & Integration | {X weeks} | {Dependent on consumer complexity} |
| Testing & Validation | {X weeks} | {Includes UAT with consumer} |
| Go-Live | {X days} | {Phased rollout recommended} |

## Proven Results

{Reference the original implementation that proved this pattern:}

| Metric | Result | Context |
|--------|--------|---------|
| {Metric 1} | {Value} | {From {Consumer} implementation, {DD-MMM-YYYY}} |
| {Metric 2} | {Value} | {From {Consumer} implementation, {DD-MMM-YYYY}} |

## Applicability

This pattern is suitable for teams that:
- {Criterion 1 — e.g., require sub-second access to customer data}
- {Criterion 2 — e.g., currently consume batch extracts with unacceptable latency}
- {Criterion 3 — e.g., need enriched customer profiles combining multiple data domains}

### Candidate Teams / Use Cases
| Team / Consumer | Use Case | Fit |
|----------------|----------|-----|
| {Team 1} | {Their use case} | {High / Medium} |
| {Team 2} | {Their use case} | {High / Medium} |
| {Team 3} | {Their use case} | {High / Medium} |

## Limitations & Considerations

- {Limitation 1 — e.g., not suitable for bulk data extraction; use Snowflake direct for batch}
- {Limitation 2 — e.g., requires Cosmos DB provisioning; lead time of 2–3 weeks}
- {Consideration 1 — e.g., rate limiting applies; discuss volume requirements with Cortex team}

## Contact

For questions about this pattern, contact:
- **Product**: {Product Manager name}
- **Architecture**: {Solution Designer / Architect name}
- **Engineering**: {Lead Engineer name}

## JIRA References

| JIRA Key | Summary | Relevance |
|----------|---------|-----------|
| DME-XXXX | {Title} | {Original implementation ticket} |
| DME-XXXX | {Title} | {Architecture decision record} |
```
