---
name: presenting-to-executives
description: "Drafts executive communications including SteerCo narratives, LT updates, manager updates, and decision briefs for Cortex Suite stakeholders. Use when asked to prepare a presentation, executive update, SteerCo paper, sponsor update, or board summary."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__jira__jira_get_sprints
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__outlook__outlook_get_calendar_events
  - Read
  - create_file
  - edit_file
  - task_list
---

# Executive Communication Skill

Produces structured executive communications for Cortex Suite — from fortnightly manager updates to Steering Committee narratives — using the SCQA framework and professional banking language.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite of Enterprise Data Products within Westpac Group's Enterprise Data & Analytics function. The Cortex Suite comprises:

- **Customer Cortex (EDP001)** — enterprise customer data product
- **Customer Interactions (EDP006)** — interaction and engagement data product
- **Transcat** — transaction categorisation capability

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

### Stakeholder Landscape

| Stakeholder | Role | Relationship |
|---|---|---|
| **Carolyn McCann** | General Manager | Executive sponsor / SteerCo member |
| **Damian McRae** | General Manager | Executive sponsor / SteerCo member |
| **Jeni** | Shalini's Manager | Direct line manager — fortnightly updates |
| **Mandar** | Architect | Architecture governance, design reviews |
| **Raja** | Architect | Architecture governance, technical direction |
| **Lily Zhao** | Strategy Team | Strategic alignment, investment cases |
| **Leadership Team (LT)** | Functional leadership | Weekly operational updates |

### Communication Cadences

| Cadence | Audience | Frequency | Purpose |
|---|---|---|---|
| Manager Update | Jeni | Fortnightly | Progress, risks, decisions needed, capacity |
| LT Weekly Update | Leadership Team | Weekly | Operational status, RAG, blockers, wins |
| Hawkeye Sponsor Update | Executive sponsors | As scheduled | Programme health, milestone tracking, decisions |
| SteerCo Narrative | Steering Committee | Quarterly / as convened | Strategic decisions, investment, programme direction |

## Communication Types

| Type | Audience | Cadence | Format | Typical Length |
|---|---|---|---|---|
| SteerCo Narrative | Steering Committee (GMs, sponsors) | Quarterly / as convened | Formal narrative document | 4–8 pages |
| LT Weekly Update | Leadership Team | Weekly | Structured status update | 1–2 pages |
| Manager Fortnightly Update | Jeni (direct manager) | Fortnightly | Conversational but structured | 1 page |
| Hawkeye Sponsor Update | Executive sponsors | As scheduled | Programme status narrative | 2–4 pages |
| Board/Exec Summary | Board or Exec Committee | Ad hoc | Highly compressed summary | 1 page |
| Decision Brief | Named decision-maker(s) | Ad hoc | Options analysis with recommendation | 1–2 pages |

## Workflow

### Step 1 — Determine Communication Type

Ask the following before drafting:

1. **What type of communication?** (SteerCo narrative, LT update, manager update, sponsor update, decision brief, or other)
2. **Who is the audience?** (Name specific stakeholders)
3. **What decision or action is needed?** (Approval, endorsement, noting, or information only)
4. **Is there a deadline?** (Meeting date, submission date)
5. **What is the key message?** (The single most important thing the audience should take away)

### Step 2 — Gather Context

Pull data from available sources in parallel:

- **JIRA**: Active sprint status, blockers, velocity, epic progress for relevant initiatives
  ```
  mcp__jira__jira_search_issues(jql="project = DME AND sprint in openSprints()", maxResults=50)
  mcp__jira__jira_get_board_issues(boardId=106106, maxResults=50)
  mcp__jira__jira_get_board_issues(boardId=106133, maxResults=50)
  ```
- **Confluence**: Prior updates, decision logs, architecture decision records, programme pages
  ```
  mcp__confluence__search_pages(query="cortex status update", limit=10)
  ```
- **Calendar**: Upcoming meetings with stakeholders to identify timing and context
  ```
  mcp__outlook__outlook_get_calendar_events(startDate="<today>", endDate="<today+7d>")
  ```
- **Sprint health**: Calculate progress percentages, burn-down trajectory, carry-over count

### Step 3 — Frame the Narrative

Use the **SCQA framework** for all executive communications:

| Element | Purpose | Example |
|---|---|---|
| **Situation** | Establish shared context the audience already accepts | "Customer Cortex serves 14 downstream systems and processes 22M customer records daily." |
| **Complication** | Introduce the tension, change, or problem | "The current refresh cadence cannot support the real-time personalisation requirements from Digital Banker." |
| **Question** | The question the audience should be asking | "How do we bridge the gap between batch processing and near-real-time consumption?" |
| **Answer** | Your recommendation or update | "We propose a streaming ingestion layer using Databricks Structured Streaming, with a 3-sprint delivery window." |

**Critical principle:** Lead with the "so what", not the "what". Executives read the first paragraph and the recommendations. Everything else is supporting evidence.

### Step 4 — Draft the Document

1. Read the appropriate reference template from `reference/`.
2. Fill all sections with concrete data — no placeholder text in the final output.
3. Ensure every claim is supported by evidence from JIRA, Confluence, or provided context.
4. Apply the formatting standards from the Communication Type table (length, format).

### Step 5 — Review & Sharpen

Before presenting the draft:

1. **Remove filler** — delete every sentence that does not inform a decision or convey status.
2. **Verify data accuracy** — cross-check JIRA numbers, dates, and stakeholder names.
3. **Test the "so what"** — cover the executive summary; does the reader know what to do?
4. **Check RAG consistency** — a Green status with three open risks is a contradiction.
5. **Validate decisions framing** — every "Decision Required" item must specify what the committee is asked to do (approve, endorse, note).

## Executive Communication Principles

1. **Lead with the decision or ask, not the background.** If the committee needs to approve funding, say so in the first paragraph.

2. **One page = one message.** If a document tries to convey more than one core message, it needs splitting into separate papers.

3. **Tables over paragraphs for data.** Executives scan tables; they skip dense paragraphs. Use prose only for narrative context and recommendations.

4. **RAG status for everything trackable.** Every initiative, risk, milestone, and budget line shall carry a Red/Amber/Green indicator with defined thresholds.

5. **Name owners, not teams.** "Mandar to complete architecture review by 15-Apr-2026" — not "the architecture team will review."

6. **Quantify impact.** Never write "significant improvement" or "notable progress." Write "12% reduction in processing time" or "3 of 5 milestones delivered on schedule."

7. **Risk = Impact × Likelihood, with mitigation and owner.** Every risk shall have a named mitigation action, an owner, and a due date. Orphaned risks are unacceptable.

8. **Decisions are binary.** Frame as "approve/reject", "endorse/defer", or "note." Avoid "discuss" as a decision verb — if discussion is needed, say what question the discussion should resolve.

## SteerCo Narrative Structure

This is the primary output format for formal executive communications. Read `reference/steerco-narrative-template.md` for the fillable skeleton.

### 1. Header

| Field | Value |
|---|---|
| **Title** | {Programme/Initiative Name} — Steering Committee Update |
| **Date** | {DD-MMM-YYYY} |
| **Author** | Shalini Gangadharan, Product Manager — Cortex Suite |
| **Classification** | {Westpac Internal / Confidential} |
| **Version** | {X.Y} |

### 2. Executive Summary

3–5 sentences that compress the entire narrative. A time-poor executive who reads only this section shall understand:
- What is the current state (RAG)?
- What has changed since the last update?
- What decisions are required?

### 3. Strategic Context

Why this programme matters now. Link to enterprise strategy (data mesh, customer 360, cloud migration). Reference any recent strategic shifts, regulatory changes, or market events that affect priority.

### 4. Current State — Programme Status

| Initiative | Status | Progress | Key Metric | Owner |
|---|---|---|---|---|
| Customer Cortex (EDP001) | 🟢 Green | {summary} | {metric} | {name} |
| Customer Interactions (EDP006) | 🟡 Amber | {summary} | {metric} | {name} |
| Transcat | 🟢 Green | {summary} | {metric} | {name} |
| {Additional initiative} | {RAG} | {summary} | {metric} | {name} |

### 5. Options Analysis (Decision Items Only)

Include this section only when the committee is asked to choose between alternatives.

| Option | Description | Cost | Timeline | Risk | Recommendation |
|---|---|---|---|---|---|
| A | {description} | {$X} | {sprints/months} | {L/M/H} | |
| B | {description} | {$X} | {sprints/months} | {L/M/H} | ✅ Recommended |
| C | {description} | {$X} | {sprints/months} | {L/M/H} | |

### 6. Financial Summary

| Category | Budget | Actual to Date | Forecast | Variance | Commentary |
|---|---|---|---|---|---|
| People (FTE) | {$X} | {$X} | {$X} | {+/-$X} | {explanation} |
| Infrastructure | {$X} | {$X} | {$X} | {+/-$X} | {explanation} |
| Licensing | {$X} | {$X} | {$X} | {+/-$X} | {explanation} |
| **Total** | **{$X}** | **{$X}** | **{$X}** | **{+/-$X}** | |

### 7. Risk Register

| ID | Risk | Likelihood | Impact | RAG | Mitigation | Owner | Due Date |
|---|---|---|---|---|---|---|---|
| R1 | {risk description} | {L/M/H} | {L/M/H} | {🔴/🟡/🟢} | {mitigation action} | {name} | {DD-MMM-YYYY} |
| R2 | {risk description} | {L/M/H} | {L/M/H} | {🔴/🟡/🟢} | {mitigation action} | {name} | {DD-MMM-YYYY} |

### 8. Decisions Required

Number each decision and frame explicitly:

1. **The Steering Committee is asked to approve** {specific decision, e.g., "additional $150K investment for Databricks capacity to support streaming ingestion for EDP001."}.
2. **The Steering Committee is asked to endorse** {specific direction, e.g., "the recommended Option B for Transcat re-architecture."}.
3. **The Steering Committee is asked to note** {information item, e.g., "the revised delivery timeline for EDP006 Phase 2, now targeting 30-Jun-2026."}.

### 9. Next Steps

| # | Action | Owner | Due Date |
|---|---|---|---|
| 1 | {action description} | {name} | {DD-MMM-YYYY} |
| 2 | {action description} | {name} | {DD-MMM-YYYY} |
| 3 | {action description} | {name} | {DD-MMM-YYYY} |

### 10. Appendix

Supporting detail tables, data extracts, architecture diagrams, or supplementary analysis. Reference from the main body as "See Appendix A" rather than embedding detail inline.

## RAG Status Definitions

Use these definitions consistently across all communications:

| Dimension | 🟢 Green | 🟡 Amber | 🔴 Red |
|---|---|---|---|
| **Schedule** | On track to meet committed dates | 1–2 week delay likely; recovery plan in place | >2 week delay; committed date at risk without intervention |
| **Scope** | Delivering agreed scope | Minor scope adjustments under discussion; no impact to outcomes | Material scope change required; impacts business outcomes |
| **Budget** | Within approved budget (±5%) | 5–15% variance; requires reforecast | >15% variance; requires additional funding approval |
| **Risk** | No critical risks; all mitigations on track | 1–2 risks with incomplete mitigations | Critical risk materialised or mitigation failed |
| **Quality** | Meets all acceptance criteria; no critical defects | Minor defects in non-critical areas; workarounds available | Critical defects affecting core functionality or data integrity |

## Stakeholder Register

Reference this when tailoring communication tone and content:

| Stakeholder | Role | Communication Preference | Key Concerns |
|---|---|---|---|
| **Carolyn McCann** | General Manager | Executive summary first; data tables for detail | Strategic alignment, ROI, risk exposure |
| **Damian McRae** | General Manager | Concise updates; escalation-focused | Delivery confidence, resource utilisation, blockers |
| **Jeni** | Shalini's Manager | Conversational but structured; fortnightly rhythm | Team health, career development, delivery risks |
| **Mandar** | Architect | Technical depth welcome; decision-oriented | Architecture compliance, technical debt, scalability |
| **Raja** | Architect | Technical depth welcome; standards-focused | Platform standards, integration patterns, security |
| **Lily Zhao** | Strategy Team | Strategic framing; investment language | Business case alignment, market positioning, portfolio fit |
| **Leadership Team (LT)** | Functional leadership | Scannable format; RAG-driven | Operational health, velocity, cross-team dependencies |

## Writing Style

- Use clear, professional language appropriate for banking and financial services.
- Avoid jargon from consumer technology or startup culture. No "disrupt", "pivot", "hustle", "move fast and break things."
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym thereafter.
- Version numbers follow semantic convention: Major.Minor (e.g., 1.0, 1.1, 2.0).
- Numbers under ten are written as words in prose; tables use numerals throughout.
- Percentages always use numerals: "5% improvement", not "five percent improvement."

## Quality Checklist

Before presenting any executive communication, verify:

- [ ] Every claim has supporting evidence (JIRA data, metrics, or stated source)
- [ ] RAG statuses are justified — Green with open risks is a contradiction
- [ ] Decisions are clearly framed with specific ask verbs (approve, endorse, note)
- [ ] No orphaned risks — every risk has a mitigation, owner, and due date
- [ ] Financial figures reconcile — actuals + forecast = budget ± stated variance
- [ ] Stakeholder names are current and correctly spelled
- [ ] All dates use DD-MMM-YYYY format
- [ ] The executive summary stands alone — a reader of only that section knows what to do
- [ ] Document length matches the communication type (see Communication Types table)
- [ ] No filler sentences — every sentence informs a decision or conveys status
