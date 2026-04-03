---
name: analysing-incidents
description: "Produces post-incident reviews for Cortex Suite data pipeline failures, SLA breaches, and production issues. Use when asked to analyse an incident, conduct root cause analysis, write a PIR, or document a production issue."
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

# Incident Analysis Skill

Produces structured post-incident reviews for Cortex Suite data pipeline failures, SLA breaches, and production issues using root cause analysis, impact assessment, and preventive action tracking.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite at Westpac Group. She owns three enterprise data products:

| Product | Code | Description |
|---------|------|-------------|
| Customer Cortex | EDP001 | Customer 360 data product |
| Customer Interactions | EDP006 | Interaction history and channel data |
| Transcat | — | Transaction categorisation |

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

**Downstream consumers:** Digital Banker, Unity, WLive, Adobe Experience Platform (AEP).

**JIRA project key:** DME.

These enterprise data products serve critical downstream systems across Westpac Group. When incidents occur, they require structured root cause analysis, stakeholder communication, and preventive action tracking. Every incident shall be documented to a standard that satisfies both engineering and governance audiences.

## Incident Severity Classification

| Severity | Definition | Response Target | Communication | Examples |
|----------|-----------|-----------------|---------------|----------|
| **P1 — Critical** | Customer-facing data product unavailable; >5% records affected | 1 hour | GM + Leadership Team notification | ADAPT pipeline total failure, Mesh API outage affecting Digital Banker |
| **P2 — Major** | Degraded service; 1–5% records affected; SLA breach confirmed | 4 hours | Manager + downstream team notification | Snowflake transform failure, data quality breach in Customer Cortex |
| **P3 — Minor** | Limited impact; <1% records affected; no customer impact | Next business day | Team internal only | Delayed data refresh, minor data anomaly in staging |
| **P4 — Cosmetic** | Documentation or metadata only; no data or service impact | Within sprint | No external communication required | Dashboard formatting, data catalogue update |

## Workflow

### Step 1 — Classify the Incident

Establish the facts before analysis:

1. **What happened?** — Describe the failure in precise terms (e.g., "ADAPT pipeline for EDP001 raw-to-curated transform failed at 03:42 AEST").
2. **When did it happen?** — Exact timestamp of onset and detection (use DD-MMM-YYYY HH:MM AEST format).
3. **What systems are affected?** — List every pipeline, database, API, and downstream consumer impacted.
4. **What is the severity?** — Apply the classification table above. If uncertain, default to the higher severity until confirmed otherwise.
5. **Who detected it?** — Monitoring alert, downstream consumer report, manual observation, or scheduled check.

If a JIRA key is provided, use `mcp__jira__jira_get_issue` to pull the incident ticket details. Use `mcp__jira__jira_search_issues` with JQL `project = DME AND type = Bug AND labels = incident` to find related incidents.

### Step 2 — Build Timeline

Construct a chronological event log from detection to resolution:

1. Record every significant event with timestamp, actor, and system.
2. Include: detection, triage, escalation, investigation milestones, fix attempts (successful and unsuccessful), restoration, and confirmation.
3. Use the timeline table format defined in the PIR Structure section below.
4. Flag any delays between events that exceeded expected response times.

### Step 3 — Identify Root Cause

Apply the **5 Whys** technique to distinguish the root cause from contributing factors:

1. Start with the problem statement — a single sentence describing what went wrong.
2. Ask "Why?" iteratively, recording each answer. Stop when further "Why?" answers point to systemic or process-level causes.
3. Not every incident requires exactly five levels. Stop when the root cause is actionable.
4. Distinguish clearly between:
   - **Root cause** — the fundamental reason the incident occurred.
   - **Contributing factors** — conditions that made the incident more likely or more severe, but did not directly cause it.
5. Use the 5 Whys template defined in section 7 below.

Search Confluence for prior incident reports: use `mcp__confluence__search_pages` with queries such as "post-incident review", "PIR", or the system name to find patterns.

### Step 4 — Assess Impact

Quantify the incident's impact across all dimensions:

| Dimension | Detail |
|-----------|--------|
| **Duration** | Total time from onset to full restoration (HH:MM) |
| **Records Affected** | Count or percentage of records impacted |
| **Systems Impacted** | List of upstream sources, pipelines, databases, APIs, and downstream consumers |
| **SLA Breach** | Yes / No — if Yes, which SLA and by how much |
| **Customer Impact** | Direct or indirect impact on Westpac customers (describe or state None) |
| **Financial Impact** | Quantifiable cost or revenue impact (describe or state Not Assessed) |

### Step 5 — Document Resolution

Record the resolution in detail:

1. **What fixed it?** — Describe the specific action or change that resolved the incident.
2. **Who fixed it?** — Name the individual(s) who applied the fix.
3. **When was service restored?** — Exact timestamp of restoration (DD-MMM-YYYY HH:MM AEST).
4. **Was data recovered or reprocessed?** — If data loss occurred, document the recovery process and confirm completeness.
5. **Was a workaround applied?** — If the fix is temporary, document the permanent resolution plan.

### Step 6 — Define Prevention

Identify preventive actions to reduce the likelihood or impact of recurrence:

1. Each action shall have a named owner and a due date (DD-MMM-YYYY format).
2. Classify each action into one of four categories:

| Type | Description | Examples |
|------|-------------|----------|
| **Process** | Changes to procedures, runbooks, or escalation paths | Updated on-call rotation, revised SLA monitoring process |
| **Technical** | Code, configuration, or infrastructure changes | Schema validation gate, retry logic, auto-scaling rules |
| **Monitoring** | New or improved alerts, dashboards, or health checks | Pipeline failure alert, data freshness dashboard |
| **Training** | Knowledge sharing, documentation, or skill development | Runbook update, cross-training on ADAPT pipelines |

3. Create a JIRA ticket for each action using the DME project key, or reference an existing ticket.

### Step 7 — Produce PIR

Generate the Post-Incident Review document using the structure defined below. Read the reference template at `reference/pir-template.md` and fill in every section.

Save the completed PIR as `PIR-{Incident-ID}-{Short-Title}.md` in the workspace root or a location the PM specifies.

## Post-Incident Review Structure

The PIR is the primary output of this skill. It shall contain these sections in this exact order:

### 1. Header

```
# Post-Incident Review: {Incident Title}
**Incident ID:** {JIRA key or reference}
**Severity:** {P1 / P2 / P3 / P4}
**Date of Incident:** {DD-MMM-YYYY}
**Author:** {Name}
**Status:** {Draft / Under Review / Final}
**Review Date:** {DD-MMM-YYYY}
```

### 2. Executive Summary

A concise paragraph of 3–5 sentences covering:
- What happened
- What was the impact
- How it was resolved
- The key learning or preventive action

### 3. Timeline

| Time (AEST) | Event | Actor | System |
|-------------|-------|-------|--------|
| DD-MMM-YYYY HH:MM | Description of event | Person or team | System or component |

### 4. Impact Assessment

| Dimension | Detail |
|-----------|--------|
| Duration | |
| Records Affected | |
| Systems Impacted | |
| SLA Breach | |
| Customer Impact | |
| Financial Impact | |

### 5. Root Cause Analysis

Present the 5 Whys chain, followed by:
- **Root Cause Statement:** One sentence identifying the fundamental cause.
- **Contributing Factors:** Bullet list of conditions that made the incident more likely or severe.

### 6. Resolution

- Actions taken to resolve the incident
- Restoration confirmation
- Data recovery status (if applicable)

### 7. Prevention Actions

| # | Action | Type | Owner | Due Date | JIRA |
|---|--------|------|-------|----------|------|
| 1 | Description | Process / Technical / Monitoring / Training | Person name | DD-MMM-YYYY | DME-XXXX |

### 8. Lessons Learned

**What went well:**
- Bullet points

**What did not go well:**
- Bullet points

**What should change:**
- Bullet points

### 9. Appendix

References to supporting material:
- Monitoring logs and alert screenshots
- Pipeline execution logs
- Data quality reports
- Related JIRA tickets and Confluence pages

## 5 Whys Template

Use this structure for root cause analysis:

```
**Problem Statement:** {What happened — single sentence}

**Why 1:** {Immediate cause — why did the failure occur?}
**Why 2:** {Why did the condition in Why 1 exist?}
**Why 3:** {Why did the condition in Why 2 exist?}
**Why 4:** {Why did the condition in Why 3 exist?}
**Why 5:** {Root cause — the systemic or process-level reason}

**Root Cause Statement:** {Concise one-sentence root cause}
```

Not every incident requires all five levels. Stop when the answer is actionable and systemic. Some incidents may require fewer; complex incidents may require branching (multiple Why chains for contributing factors).

## Common Cortex Incident Patterns

Reference this table during root cause analysis to identify known failure patterns:

| Pattern | Typical Root Cause | Prevention |
|---------|-------------------|------------|
| ADAPT pipeline failure | Schema change in upstream source system; infrastructure timeout; credential expiry | Schema validation gate before ingestion; retry logic with exponential backoff; credential rotation monitoring |
| Snowflake transform error | Upstream data quality issue (nulls, type mismatches); SQL logic error in transform layer | Data quality checks at raw-to-curated boundary; unit tests for transform SQL; schema evolution tracking |
| Mesh API degradation | Cosmos DB throttling (RU/s exceeded); payload size exceeding limits; connection pool exhaustion | RU auto-scaling; response pagination; connection pool monitoring and alerting |
| Data freshness breach | Upstream source delivery delay; pipeline queue congestion; dependency chain failure | Monitoring alerts on source delivery SLA; pipeline priority queuing; SLA buffer in scheduling |
| Environment issue | Credential expiry; SSL certificate rotation; infrastructure configuration drift | Automated credential renewal; certificate expiry monitoring; infrastructure-as-code drift detection |

## Stakeholder Communication Templates

### Initial Notification

Use when an incident is detected and classified:

```
Subject: [P{X}] {System} — {Brief Description}

We are investigating an issue affecting {system/product}.

**What we know:**
- {Description of observed behaviour}
- {When it was detected and by whom}
- {Systems currently affected}

**What we are doing:**
- {Current investigation and triage actions}

**Next update:** {Time — within response target for the severity level}
```

### Resolution Notification

Use when the incident is resolved:

```
Subject: [RESOLVED] [P{X}] {System} — {Brief Description}

The issue affecting {system/product} has been resolved.

**What happened:**
- {Brief root cause description}

**Impact:**
- {Duration, records affected, downstream impact}

**What we have fixed:**
- {Resolution actions taken}

**Prevention:**
- {Key preventive actions planned}

A full Post-Incident Review shall be circulated within {timeframe}.
```

## Quality Checklist

Before presenting the PIR, verify:

- [ ] Severity classification is applied and justified
- [ ] Timeline is complete from detection to restoration with no gaps exceeding 30 minutes unexplained
- [ ] Root cause analysis uses the 5 Whys technique (not just a symptom description)
- [ ] Root cause is distinguished from contributing factors
- [ ] Impact assessment covers all six dimensions (Duration, Records, Systems, SLA, Customer, Financial)
- [ ] Every prevention action has a named owner and a due date
- [ ] Prevention actions are classified by type (Process, Technical, Monitoring, Training)
- [ ] Lessons Learned includes all three categories (went well, did not go well, should change)
- [ ] All dates use DD-MMM-YYYY format
- [ ] All times use HH:MM AEST format
- [ ] JIRA keys use the DME-XXXX format
- [ ] No startup jargon — professional banking language throughout
- [ ] Executive summary is 3–5 sentences, not a paragraph of filler

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- All times in HH:MM AEST format (e.g., 03:42 AEST).
- Use professional banking language. No "disrupt", "pivot", "hustle", or startup jargon.
- Name people explicitly — never say "the team" when you can name individuals.
- JIRA keys use the `DME-XXXX` format.
- Incident IDs should reference the corresponding JIRA ticket where one exists.
