# AI/ML Use Case Feasibility Assessment — Cortex Suite

---

## 1. Document Header

| Field | Value |
|-------|-------|
| **Use Case Title** | [Descriptive name for the AI/ML use case] |
| **Version** | 0.1 Draft |
| **Author** | [PM Name] |
| **Date** | [DD-MMM-YYYY] |
| **Status** | Draft / In Review / Assessed |
| **JIRA Reference** | [DME-XXXX — link to epic] |
| **Product** | [Customer Cortex / Customer Interactions / Transcat / Cross-Product] |
| **Use Case Category** | [Operational Efficiency / Customer Analytics / Risk & Credit / Personalisation] |
| **Regulatory Scrutiny** | [Low / Medium / High] |
| **Recommendation** | [Proceed / Pilot / Defer / Reject] |

---

## 2. Use Case Definition

### Problem Statement

[What specific problem is the AI/ML model solving? Be precise — reference the current manual process, decision being augmented, or capability gap.]

### Target Variable / Outcome

[What is the model predicting, classifying, or optimising? State the target variable for supervised learning, or the objective for unsupervised approaches.]

### Decision Being Augmented or Automated

[What decision does a human currently make that this model will support or replace? Describe the current process and the intended future state.]

### Intended Deployment Mode

| Attribute | Detail |
|-----------|--------|
| **Model Type** | [Classification / Regression / NLP / Time-Series / Clustering / Recommender / Other] |
| **Deployment Mode** | [Batch scoring / Near-real-time API / Real-time streaming] |
| **Inference Latency** | [Hours / Seconds / Milliseconds] |
| **Scoring Frequency** | [Daily / Hourly / Per-request / Event-driven] |
| **Consumers** | [List downstream systems or teams that will consume model outputs] |

---

## 3. Feasibility Scorecard

| # | Dimension | Score (1–5) | Weight | Weighted Score | Evidence | Risks |
|---|-----------|-------------|--------|----------------|----------|-------|
| 1 | Data Readiness | [X] | 25% | [X × 0.25] | [Key evidence] | [Key risks] |
| 2 | Technical Feasibility | [X] | 20% | [X × 0.20] | [Key evidence] | [Key risks] |
| 3 | Business Value | [X] | 25% | [X × 0.25] | [Key evidence] | [Key risks] |
| 4 | Ethical & Regulatory Risk | [X] | 20% | [X × 0.20] | [Key evidence] | [Key risks] |
| 5 | Organisational Readiness | [X] | 10% | [X × 0.10] | [Key evidence] | [Key risks] |
| | **Total** | | **100%** | **[Sum]** | | |

**Scoring thresholds:** 4.0–5.0 = Proceed · 3.0–3.9 = Pilot · 2.0–2.9 = Defer · <2.0 = Reject

---

## 4. Data Readiness Assessment

### Data Sources

| Source | Location | Attributes Required | Available | Quality Score | Volume | History Depth |
|--------|----------|---------------------|-----------|---------------|--------|---------------|
| [Source 1] | [Snowflake schema / ADLS2 path] | [Key attributes] | Yes / No / Partial | [X%] | [Row count] | [Months] |
| [Source 2] | [Snowflake schema / ADLS2 path] | [Key attributes] | Yes / No / Partial | [X%] | [Row count] | [Months] |

### Data Readiness Checklist

- [ ] Source data exists in Snowflake or ADLS2
- [ ] Sufficient historical volume available (minimum 12 months)
- [ ] Data quality score >90% on key attributes
- [ ] Labels are available or labelling strategy is defined
- [ ] No PII or data classification blockers
- [ ] Refresh cadence supports deployment mode requirements
- [ ] Feature engineering requirements are understood
- [ ] Data access permissions are in place for the DS team
- [ ] Data lineage is documented for key training attributes
- [ ] Test/holdout data strategy is defined

### Data Gaps & Remediation

| Gap | Impact | Remediation | Effort | Owner |
|-----|--------|-------------|--------|-------|
| [Gap 1] | [Impact on model quality or feasibility] | [Action to close gap] | [Days/sprints] | [Name] |
| [Gap 2] | [Impact on model quality or feasibility] | [Action to close gap] | [Days/sprints] | [Name] |

---

## 5. Technical Feasibility Assessment

### Proposed Approach

| Attribute | Detail |
|-----------|--------|
| **Algorithm / Model Family** | [e.g., XGBoost, logistic regression, transformer, LSTM] |
| **Baseline Approach** | [Simplest viable model for benchmarking] |
| **Advanced Approach** | [More complex model if baseline is insufficient] |
| **Feature Count (estimated)** | [Approximate number of input features] |
| **Training Data Size** | [Rows × features] |
| **Estimated Training Time** | [Hours / days] |
| **Infrastructure Required** | [Databricks cluster spec, GPU requirements] |

### Platform Readiness

| Capability | Current State | Required State | Gap |
|------------|---------------|----------------|-----|
| Databricks ML runtime | [Current version] | [Required version] | [None / Upgrade needed] |
| Experiment tracking (MLflow) | [Available / Not configured] | [Required] | [None / Setup needed] |
| Model serving (Mesh API) | [Available / Not configured] | [Required for deployment mode] | [None / Setup needed] |
| CI/CD for ML | [Available / Not configured] | [Required] | [None / Setup needed] |
| Feature store | [Available / Not configured] | [Required / Not required] | [None / Setup needed] |

### Technical Risks

| Risk | Likelihood (H/M/L) | Impact (H/M/L) | Mitigation |
|------|---------------------|-----------------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Mitigation action] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Mitigation action] |

---

## 6. Business Value Assessment

### Quantified Benefits

| Benefit Category | Description | Annual Value ($) | Methodology | Confidence |
|------------------|-------------|------------------|-------------|------------|
| Efficiency Gains | [Description] | $[X] | [Calculation basis] | High / Med / Low |
| Risk Reduction | [Description] | $[X] | [Calculation basis] | High / Med / Low |
| Revenue Impact | [Description] | $[X] | [Calculation basis — apply 50% realisation factor] | High / Med / Low |
| **Total Quantified** | | **$[X]** | | |

### Strategic Alignment

| Strategy Pillar | Alignment (H/M/L) | Description |
|-----------------|-------------------|-------------|
| Cortex Product Roadmap | [H/M/L] | [How this use case supports it] |
| Enterprise Data Strategy | [H/M/L] | [How this use case supports it] |
| Customer Outcomes | [H/M/L] | [How this use case supports it] |

### Urgency & Drivers

[Describe time-sensitive drivers: regulatory deadlines, competitive pressure, executive mandate, or contractual obligations. State "No urgent driver" if applicable.]

---

## 7. Ethical & Regulatory Risk Assessment

### Responsible AI Checklist

| Consideration | Assessment | Detail |
|---------------|------------|--------|
| **Bias risk** | Low / Medium / High | [Which protected attributes could be affected? Age, gender, ethnicity, geography, disability] |
| **Explainability required** | Yes / No | [Must individual predictions be explainable? What method — SHAP, LIME, other?] |
| **APRA CPS 220 applicable** | Yes / No | [Does this model fall under risk management obligations?] |
| **APRA CPS 234 applicable** | Yes / No | [Does this model process information assets requiring security controls?] |
| **Customer impact** | Direct / Indirect / None | [Does the model directly affect customer outcomes — credit, pricing, eligibility?] |
| **PII in training data** | Yes / No | [Does the model require personally identifiable information?] |
| **Consent constraints** | Yes / No | [Are there consent or privacy limitations on data use?] |
| **Recourse mechanism** | Required / Not required | [Can customers contest model-driven decisions?] |

### Human Oversight Model

| Level | Description | Applicable |
|-------|-------------|------------|
| **Full automation** | Model decision executed without human review | [ ] |
| **Human-on-the-loop** | Model decision executed, flagged for periodic review | [ ] |
| **Human-in-the-loop** | Model produces recommendation, human makes final decision | [ ] |

### Approval Governance

| Governance Body | Required | Status |
|-----------------|----------|--------|
| DS team lead review (Tom) | Yes / No | Pending / Approved |
| Product owner review | Yes / No | Pending / Approved |
| Model risk committee | Yes / No | Pending / Approved / Not required |
| APRA notification | Yes / No | Pending / Submitted / Not required |

---

## 8. Organisational Readiness Assessment

### DS Team Capacity

| Person | Role | Current Allocation | Available for This Use Case | Notes |
|--------|------|--------------------|-----------------------------|-------|
| Tom | Lead DS | [X FTE on current work] | [X FTE available] | DS team lead |
| Rupa | Data Scientist | [X FTE] | [X FTE] | [Leave / availability notes] |
| Simran | Data Scientist | [X FTE] | [X FTE] | |
| Justin | Data Scientist | [X FTE] | [X FTE] | |
| Vivasha | Data Scientist | [X FTE] | [X FTE] | |
| Claudia | Data Scientist | [X FTE] | [X FTE] | |
| Richard | Data Scientist | [X FTE] | [X FTE] | |
| Vinoth | Data Scientist | [0.5 FTE total] | [X FTE] | Part-time allocation |

### Skill & Capability Assessment

| Required Capability | Team Has It | Gap | Mitigation |
|---------------------|-------------|-----|------------|
| [e.g., NLP expertise] | Yes / No / Partial | [Description] | [Training, hiring, external support] |
| [e.g., MLOps deployment] | Yes / No / Partial | [Description] | [Training, hiring, external support] |

### MLOps Maturity

| Capability | Current State | Required for This Use Case |
|------------|---------------|---------------------------|
| Model versioning | [In place / Partial / Not in place] | [Required / Not required] |
| Automated retraining | [In place / Partial / Not in place] | [Required / Not required] |
| Performance monitoring | [In place / Partial / Not in place] | [Required / Not required] |
| Data drift detection | [In place / Partial / Not in place] | [Required / Not required] |
| Champion-challenger | [In place / Partial / Not in place] | [Required / Not required] |
| Model rollback | [In place / Partial / Not in place] | [Required / Not required] |

---

## 9. Recommendation

### Overall Assessment: [Proceed / Pilot / Defer / Reject]

**Rationale:**

[3–5 sentences explaining the recommendation. Link directly to dimension scores and evidence. Be specific about what supports or undermines feasibility.]

### Conditions for Proceeding (if Pilot or Defer)

| # | Condition | Owner | Target Date |
|---|-----------|-------|-------------|
| 1 | [Condition that must be met before proceeding] | [Name] | [DD-MMM-YYYY] |
| 2 | [Condition that must be met before proceeding] | [Name] | [DD-MMM-YYYY] |

### Recommended Next Steps

| # | Action | Owner | Timeline |
|---|--------|-------|----------|
| 1 | [Next step] | [Name] | [Duration or target date] |
| 2 | [Next step] | [Name] | [Duration or target date] |
| 3 | [Next step] | [Name] | [Duration or target date] |

### Estimated Effort (if Proceed or Pilot)

| Phase | Duration | DS Team Allocation | Key Activities |
|-------|----------|--------------------|----------------|
| Exploration / EDA | [X sprints] | [Names, FTE] | [Data profiling, feature exploration, baseline model] |
| Model Development | [X sprints] | [Names, FTE] | [Feature engineering, model training, evaluation] |
| Validation & Testing | [X sprints] | [Names, FTE] | [Bias testing, explainability, performance validation] |
| Deployment & Monitoring | [X sprints] | [Names, FTE] | [API deployment, monitoring setup, documentation] |
| **Total** | **[X sprints]** | | |

---

## 10. Appendix

### A. Glossary

| Acronym / Term | Definition |
|----------------|------------|
| ADAPT | Westpac's data pipeline framework |
| ADLS2 | Azure Data Lake Storage Gen2 |
| APRA | Australian Prudential Regulation Authority |
| CPS 220 | APRA Prudential Standard — Risk Management |
| CPS 234 | APRA Prudential Standard — Information Security |
| Cortex | Westpac's suite of Enterprise Data Products |
| EDP | Enterprise Data Product |
| LIME | Local Interpretable Model-agnostic Explanations |
| Mesh API | Data product consumption API layer |
| MLOps | Machine Learning Operations |
| SHAP | SHapley Additive exPlanations |
| Transcat | Transaction Categorisation |

### B. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DD-MMM-YYYY] | [Name] | Initial assessment |
