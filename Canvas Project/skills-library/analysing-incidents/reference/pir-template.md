# Post-Incident Review: {Incident Title}

**Incident ID:** {JIRA key, e.g., DME-XXXX}
**Severity:** {P1 / P2 / P3 / P4}
**Date of Incident:** {DD-MMM-YYYY}
**Author:** {Name}
**Status:** {Draft / Under Review / Final}
**Review Date:** {DD-MMM-YYYY}

---

## Executive Summary

{3–5 sentences covering: what happened, the impact, how it was resolved, and the key learning or preventive action. This section shall be self-contained — a reader should understand the incident without reading further.}

---

## Timeline

| Time (AEST) | Event | Actor | System |
|-------------|-------|-------|--------|
| DD-MMM-YYYY HH:MM | {Incident onset — first observable symptom} | {System / monitoring} | {Component} |
| DD-MMM-YYYY HH:MM | {Detection — when and how the incident was identified} | {Person / alert} | {Component} |
| DD-MMM-YYYY HH:MM | {Triage — initial assessment and severity classification} | {Person} | — |
| DD-MMM-YYYY HH:MM | {Escalation — who was notified and when} | {Person} | — |
| DD-MMM-YYYY HH:MM | {Investigation milestone — key finding during diagnosis} | {Person} | {Component} |
| DD-MMM-YYYY HH:MM | {Fix applied — description of the corrective action} | {Person} | {Component} |
| DD-MMM-YYYY HH:MM | {Service restored — confirmation of normal operation} | {Person} | {Component} |
| DD-MMM-YYYY HH:MM | {Data recovery — reprocessing completed if applicable} | {Person} | {Component} |

---

## Impact Assessment

| Dimension | Detail |
|-----------|--------|
| **Duration** | {Total time from onset to full restoration, e.g., 2h 45m} |
| **Records Affected** | {Count or percentage, e.g., 12,400 records (~3.2% of daily volume)} |
| **Systems Impacted** | {List: ADAPT pipeline, Snowflake curated layer, Mesh API, Digital Banker, etc.} |
| **SLA Breach** | {Yes / No — if Yes, state which SLA and by how much, e.g., "Data freshness SLA breached by 4 hours"} |
| **Customer Impact** | {Direct / Indirect / None — describe if applicable, e.g., "Digital Banker displayed stale customer data for 2 hours"} |
| **Financial Impact** | {Quantified cost or "Not Assessed" — include reprocessing costs, penalty clauses, etc.} |

---

## Root Cause Analysis

### 5 Whys

**Problem Statement:** {What happened — single sentence, e.g., "The ADAPT pipeline for Customer Cortex (EDP001) failed during the raw-to-curated transform at 03:42 AEST on DD-MMM-YYYY."}

**Why 1:** {Immediate cause — why did the failure occur?}
↳ {Evidence supporting this answer}

**Why 2:** {Why did the condition in Why 1 exist?}
↳ {Evidence supporting this answer}

**Why 3:** {Why did the condition in Why 2 exist?}
↳ {Evidence supporting this answer}

**Why 4:** {Why did the condition in Why 3 exist?}
↳ {Evidence supporting this answer}

**Why 5:** {Root cause — the systemic or process-level reason}
↳ {Evidence supporting this answer}

### Root Cause Statement

{One sentence identifying the fundamental cause, e.g., "The root cause was the absence of a schema validation gate in the ADAPT ingestion pipeline, which allowed an upstream schema change to propagate undetected into the curated layer."}

### Contributing Factors

- {Factor 1 — condition that increased likelihood or severity}
- {Factor 2 — condition that increased likelihood or severity}
- {Factor 3 — condition that increased likelihood or severity}

---

## Resolution

### Actions Taken

1. {Action 1 — what was done to resolve the immediate issue}
2. {Action 2 — subsequent corrective actions}
3. {Action 3 — if applicable}

### Restoration Confirmation

- **Service restored at:** {DD-MMM-YYYY HH:MM AEST}
- **Confirmed by:** {Person name}
- **Verification method:** {How restoration was confirmed, e.g., "End-to-end pipeline execution completed successfully; downstream data refresh confirmed in Digital Banker"}

### Data Recovery

- **Data loss occurred:** {Yes / No}
- **Reprocessing required:** {Yes / No}
- **Reprocessing completed:** {DD-MMM-YYYY HH:MM AEST / Not Applicable}
- **Data integrity confirmed:** {Yes / Pending — describe verification method}

---

## Prevention Actions

| # | Action | Type | Owner | Due Date | JIRA |
|---|--------|------|-------|----------|------|
| 1 | {Description of preventive action} | {Process / Technical / Monitoring / Training} | {Person name} | {DD-MMM-YYYY} | {DME-XXXX} |
| 2 | {Description of preventive action} | {Process / Technical / Monitoring / Training} | {Person name} | {DD-MMM-YYYY} | {DME-XXXX} |
| 3 | {Description of preventive action} | {Process / Technical / Monitoring / Training} | {Person name} | {DD-MMM-YYYY} | {DME-XXXX} |
| 4 | {Description of preventive action} | {Process / Technical / Monitoring / Training} | {Person name} | {DD-MMM-YYYY} | {DME-XXXX} |

---

## Lessons Learned

### What Went Well

- {Positive observation, e.g., "Monitoring alert fired within 5 minutes of onset"}
- {Positive observation, e.g., "On-call engineer responded within 15 minutes"}
- {Positive observation}

### What Did Not Go Well

- {Negative observation, e.g., "Root cause took 90 minutes to identify due to insufficient logging"}
- {Negative observation, e.g., "Downstream teams were not notified until 45 minutes after detection"}
- {Negative observation}

### What Should Change

- {Recommended change, e.g., "Add structured logging to ADAPT pipeline transform stage"}
- {Recommended change, e.g., "Implement automated downstream notification on pipeline failure"}
- {Recommended change}

---

## Appendix

### Monitoring Logs

{Reference to monitoring dashboard, alert ID, or log query used during investigation.}

### Pipeline Execution Logs

{Reference to ADAPT pipeline run ID, Snowflake query history, or Databricks job run.}

### Data Quality Reports

{Reference to data quality check results, record counts, or validation reports.}

### Related JIRA Tickets

| JIRA Key | Title | Relationship |
|----------|-------|-------------|
| DME-XXXX | {Title} | {Incident ticket / Prevention action / Related defect} |
| DME-XXXX | {Title} | {Incident ticket / Prevention action / Related defect} |

### Related Confluence Pages

| Page Title | Link | Relevance |
|------------|------|-----------|
| {Title} | {URL} | {Prior PIR / Runbook / Architecture documentation} |
