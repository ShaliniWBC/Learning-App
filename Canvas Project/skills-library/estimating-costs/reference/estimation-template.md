# Cost & Effort Estimation — [Initiative Name]

---

## 1. Document Header

| Field | Value |
|-------|-------|
| **Title** | [Initiative / Feature Name] |
| **Version** | 0.1 Draft |
| **Author** | Shalini Gangadharan |
| **Date** | [DD-MMM-YYYY] |
| **Status** | Draft / In Review / Approved |
| **JIRA Reference** | [DME-XXXX — link to epic or initiative] |
| **Product** | [Customer Cortex / Customer Interactions / Transcat / Cross-Product] |

---

## 2. Executive Summary

[2–3 paragraphs summarising: what is being estimated, the delivery context (new build / enhancement / integration), the total estimated effort range, overall confidence level, and the key caveat or constraint that stakeholders should be aware of.]

**Bottom Line:**
- **Effort:** [X – Y] person-days across [N] streams
- **Cost:** $[X] – $[Y] (including contingency)
- **Duration:** [N] sprints ([start date] – [end date])
- **Confidence:** [High / Medium / Low]

---

## 3. Scope & Boundaries

### In Scope of This Estimate

1. [Specific deliverable or work item]
2. [Specific deliverable or work item]
3. [Specific deliverable or work item]
4. [Specific deliverable or work item]

### Out of Scope (shall be estimated separately)

1. [Item] — [Reason for exclusion]
2. [Item] — [Reason for exclusion]
3. [Item] — [Reason for exclusion]

### Assumptions

1. [Assumption that underpins the estimate]
2. [Assumption that underpins the estimate]
3. Team capacity remains stable for the duration of the delivery (no unplanned attrition)
4. Existing ADAPT pipeline framework version shall not change during delivery
5. [Additional assumption]

### Caveats

1. Estimate is valid for 30 calendar days from the date of issue — re-estimation shall be required if delivery does not commence within this period
2. [Caveat about technology or platform dependency]
3. [Caveat about external dependency or third-party timeline]
4. [Caveat about data availability or quality]

---

## 4. Effort Estimation by Stream

### Analogous Work Referenced

| Analogue | JIRA Key | Scope Summary | Actual Effort | Duration | Relevance |
|----------|----------|---------------|---------------|----------|-----------|
| [Prior initiative name] | DME-XXXX | [Brief scope description] | [X person-days] | [N sprints] | [Why this analogue applies] |
| [Prior initiative name] | DME-XXXX | [Brief scope description] | [X person-days] | [N sprints] | [Why this analogue applies] |

### Stream Estimates

| Stream | Optimistic (days) | Likely (days) | Pessimistic (days) | Confidence | Key Assumptions |
|--------|--------------------|---------------|---------------------|------------|-----------------|
| Engineering | | | | High / Med / Low | [Assumption] |
| Data Science | | | | High / Med / Low | [Assumption] |
| Testing / QA | | | | High / Med / Low | [Assumption] |
| Release Management | | | | High / Med / Low | [Assumption] |
| Overhead (20%) | | | | — | Ceremonies, admin, context switching |
| **Total** | **X** | **Y** | **Z** | **Overall** | |

### Confidence Level Definitions

| Level | Definition | Expected Variance |
|-------|-----------|-------------------|
| **High** | Well-understood scope. Team has completed analogous work. Estimate calibrated against actuals. | ±15% |
| **Medium** | Scope mostly understood, some unknowns. Estimate based on similar (not identical) work. | ±30% |
| **Low** | Significant unknowns. New technology or patterns. Rough order of magnitude. | ±50% or more |

---

## 5. Resource Matrix

| Person | Role | Sprint N | Sprint N+1 | Sprint N+2 | Sprint N+3 | Sprint N+4 | Notes |
|--------|------|----------|------------|------------|------------|------------|-------|
| Sasi | Lead Engineer | | | | | | Architecture lead |
| Cooper | Engineer | | | — | — | — | Exits after Sprint 6 |
| Josh | Grad Engineer | | | | | | Ramping up — 0.6 FTE |
| Jolin | Grad Engineer | | | | | | Ramping up — 0.6 FTE |
| Jack | Analyst | | | | | | |
| GK | SME / Solution Designer | | | | | | Shared allocation — confirm FTE |
| Tom | Lead DS | | | | | | DS team lead |
| Rupa | Data Scientist | | | | | | Check leave cover |
| Simran | Data Scientist | | | | | | |
| Justin | Data Scientist | | | | | | Sole EDB contributor — SPOF |
| Vivasha | Data Scientist | | | | | | |
| Claudia | Data Scientist | | | | | | |
| Richard | Data Scientist | | | | | | |
| Vinoth | Data Scientist | | | | | | Part-time — 0.5 FTE |
| Peter | Senior BA | | | | | | Hawkeye focus |
| Kadeeja | Scrum Master | | | | | | Facilitation |
| **Total FTE** | | **X.X** | **X.X** | **X.X** | **X.X** | **X.X** | |

**Capacity Notes:**
- 1 sprint = 10 business days
- Available person-days per sprint = FTE × 10
- Total available person-days for initiative = sum of all sprint allocations

---

## 6. Cost Summary

### Labour Costs

| Stream | Person-Days (Likely) | Day Rate ($) | Stream Cost ($) | Notes |
|--------|----------------------|--------------|-----------------|-------|
| Engineering | | | | |
| Data Science | | | | |
| Testing / QA | | | | |
| Release Management | | | | |
| **Subtotal (Labour)** | **X** | | **$X** | |

### Cost Range View

| Scenario | Person-Days | Labour ($) | Infra ($) | Contingency ($) | Total ($) |
|----------|-------------|-----------|-----------|-----------------|-----------|
| Optimistic | | | | | |
| Likely | | | | | |
| Pessimistic | | | | | |

---

## 7. Architecture & Infrastructure Costs

| Cost Driver | Description | Estimated Cost ($) | Frequency | Notes |
|-------------|-------------|--------------------|-----------| ------|
| ADAPT pipeline development | [New / modified pipelines] | | One-off | |
| Snowflake compute credits | [Warehouse sizing, query volume] | | Monthly | |
| Databricks cluster costs | [Notebook dev, ML training] | | Monthly | |
| Azure Data Lake (ADLS2) | [Storage volume] | | Monthly | |
| Cosmos DB throughput | [RU/s, document size] | | Monthly | |
| Mesh API hosting | [Compute, scaling] | | Monthly | |
| Environment provisioning | [Dev, Test, Staging, Prod] | | One-off | |
| **Infrastructure Subtotal** | | **$X** | | |

---

## 8. Contingency

| Confidence Level | Contingency % | Applied To | Contingency Amount ($) |
|-----------------|---------------|-----------|----------------------|
| [Overall confidence] | [15% / 25% / 40%] | [Labour + Infra subtotal] | |

**Grand Total (Likely + Contingency):** $[X]

**Grand Total Range:** $[Optimistic] – $[Pessimistic] (including contingency)

---

## 9. Risks to Estimate

| # | Risk | Likelihood | Impact on Estimate | Mitigation | Owner |
|---|------|------------|-------------------|------------|-------|
| 1 | [Risk that could increase effort or cost] | L / M / H | [+X days or +$X] | [Action to reduce risk] | [Name] |
| 2 | [Risk that could increase effort or cost] | L / M / H | [+X days or +$X] | [Action to reduce risk] | [Name] |
| 3 | [Risk that could increase effort or cost] | L / M / H | [+X days or +$X] | [Action to reduce risk] | [Name] |
| 4 | Key person unavailability (SPOF) | M | [+X days] | Cross-train second person | [Name] |
| 5 | Scope change after estimate approval | M | [Variable] | Re-estimate if scope changes >10% | Shalini |

---

## 10. Appendix

### A. Detailed Task Breakdown

| # | Task | Stream | Estimated Days (Likely) | Assignee | Dependencies | Notes |
|---|------|--------|------------------------|----------|-------------|-------|
| 1 | | Engineering | | | | |
| 2 | | Engineering | | | | |
| 3 | | Data Science | | | | |
| 4 | | Testing / QA | | | | |
| 5 | | Release Mgmt | | | | |

### B. Analogous Work References

| Initiative | JIRA Key | Completion Date | Actual Effort | Actual Cost | Lessons for This Estimate |
|-----------|----------|-----------------|---------------|-------------|--------------------------|
| Hawkeye Budgetary Guidance | DME-9222 | [DD-MMM-YYYY] | [X person-days] | [If known] | [What applies] |
| Account Scrutiny | [DME-XXXX] | [DD-MMM-YYYY] | [X person-days] | $122,000 | [What applies] |
| [Additional analogue] | [DME-XXXX] | [DD-MMM-YYYY] | [X person-days] | [If known] | [What applies] |

### C. Glossary

| Term | Definition |
|------|-----------|
| ADAPT | Westpac's enterprise data pipeline framework |
| ADLS2 | Azure Data Lake Storage Gen2 |
| Cortex | Westpac's suite of Enterprise Data Products |
| EDP | Enterprise Data Product |
| FTE | Full-Time Equivalent |
| Mesh API | Data product consumption API layer |
| RU/s | Request Units per second (Cosmos DB throughput measure) |
| SPOF | Single Point of Failure |
| Transcat | Transaction Categorisation |

### D. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DD-MMM-YYYY] | Shalini Gangadharan | Initial estimate |
