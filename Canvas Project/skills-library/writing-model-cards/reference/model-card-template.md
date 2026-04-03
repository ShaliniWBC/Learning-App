# Model Card Template — Cortex Suite ML Models

---

## 1. Model Overview

| Field | Value |
|-------|-------|
| **Model Name** | [Model name] |
| **Version** | [e.g., 2.1.0] |
| **Type** | [e.g., XGBoost classifier, LightGBM regressor] |
| **Purpose** | [Business problem and decision supported] |
| **Owner** | [Model developer name from DS team] |
| **Date** | [DD-MMM-YYYY] |
| **Status** | [Development / Validation / Staging / Production / Retired] |
| **Registry ID** | [MLflow model URI or registry path] |
| **Risk Tier** | [Tier 1 — Critical / Tier 2 — Significant / Tier 3 — Standard] |
| **JIRA Reference** | [DME-XXXX or relevant epic key] |

---

## Table of Contents

1. [Intended Use](#2-intended-use)
2. [Training Data](#3-training-data)
3. [Evaluation Data](#4-evaluation-data)
4. [Model Architecture](#5-model-architecture)
5. [Performance Metrics](#6-performance-metrics)
6. [Fairness Assessment](#7-fairness-assessment)
7. [Limitations & Risks](#8-limitations--risks)
8. [Monitoring Plan](#9-monitoring-plan)
9. [Ethical Considerations](#10-ethical-considerations)
10. [Governance](#11-governance)
11. [Credit Model Sections](#12-credit-model-sections) *(Tier 1 credit models only)*
12. [Version History](#13-version-history)

---

## 2. Intended Use

### Primary Use Case

[Describe the specific business decision this model supports. Be precise — reference the product, process, or system that consumes the model output.]

### Intended Users

[List the systems, teams, or roles that consume model outputs.]

- [e.g., Automated credit decisioning engine (Project Hawkeye)]
- [e.g., Risk analysts reviewing model outputs]
- [e.g., Collections strategy team]

### Out-of-Scope Uses

[Uses for which this model is NOT designed or validated. Be explicit.]

1. [e.g., This model shall not be used for pricing decisions]
2. [e.g., This model shall not be applied to commercial lending]
3. [e.g., This model shall not be used outside the Australian market]

---

## 3. Training Data

| Attribute | Detail |
|-----------|--------|
| **Source** | [Snowflake table(s), ADLS2 path(s)] |
| **Date Range** | [DD-MMM-YYYY to DD-MMM-YYYY] |
| **Row Count** | [N records] |
| **Feature Count** | [N features] |
| **Label Distribution** | [e.g., 5.2% positive (default), 94.8% negative (non-default)] |
| **Data Quality** | [Missing rate %, outlier treatment method, imputation approach] |
| **Class Balancing** | [Method applied: SMOTE / undersampling / oversampling / class weights / none] |
| **Data Classification** | [Restricted / Confidential / Internal] |

### Feature Summary

| # | Feature Name | Data Type | Source | Description | Missing Rate |
|---|-------------|-----------|--------|-------------|-------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

<!-- List all features used in the model. For models with > 50 features, list the top 20 by importance and note the total count. -->

### Data Provenance

[Describe the data lineage from source system through ingestion, transformation, and feature engineering to the final training dataset.]

- **Source system(s)**: [e.g., Core Banking, CRM, Bureau data]
- **Ingestion pipeline**: [e.g., ADAPT pipeline, batch/streaming]
- **Feature engineering**: [e.g., Snowflake feature store tables, Databricks notebooks]
- **Snapshot method**: [e.g., Point-in-time correct features to prevent data leakage]

---

## 4. Evaluation Data

| Attribute | Detail |
|-----------|--------|
| **Source** | [Same source as training / separate source — describe] |
| **Date Range** | [DD-MMM-YYYY to DD-MMM-YYYY] |
| **Row Count** | [N records] |
| **Sampling Method** | [Holdout / temporal split / stratified / k-fold cross-validation] |
| **Relationship to Training** | [Describe separation method and overlap controls] |
| **Label Distribution** | [e.g., 5.0% positive, 95.0% negative] |

### Out-of-Time Validation

| Attribute | Detail |
|-----------|--------|
| **Date Range** | [DD-MMM-YYYY to DD-MMM-YYYY] |
| **Row Count** | [N records] |
| **Purpose** | [Validate model stability on data from a period not seen during training] |

---

## 5. Model Architecture

| Attribute | Detail |
|-----------|--------|
| **Algorithm** | [e.g., XGBoost, LightGBM, logistic regression, random forest, neural network] |
| **Framework** | [e.g., scikit-learn 1.4.2, XGBoost 2.0.3, LightGBM 4.1.0] |
| **Training Infrastructure** | [Databricks cluster type, node count, GPU/CPU, runtime version] |
| **Training Duration** | [e.g., 2.5 hours] |
| **Model Size** | [e.g., 12 MB serialised] |
| **Serialisation Format** | [e.g., pickle, ONNX, MLflow pyfunc] |

### Hyperparameters

| Parameter | Value | Default | Rationale |
|-----------|-------|---------|-----------|
| [e.g., max_depth] | [e.g., 6] | [e.g., 6] | [Why this value was selected] |
| [e.g., learning_rate] | [e.g., 0.05] | [e.g., 0.3] | [Why this value was selected] |
| [e.g., n_estimators] | [e.g., 500] | [e.g., 100] | [Why this value was selected] |
| [e.g., min_child_weight] | [e.g., 10] | [e.g., 1] | [Why this value was selected] |
| [e.g., subsample] | [e.g., 0.8] | [e.g., 1.0] | [Why this value was selected] |
| [e.g., colsample_bytree] | [e.g., 0.8] | [e.g., 1.0] | [Why this value was selected] |
| [e.g., reg_alpha] | [e.g., 0.1] | [e.g., 0] | [Why this value was selected] |
| [e.g., reg_lambda] | [e.g., 1.0] | [e.g., 1] | [Why this value was selected] |

### Hyperparameter Tuning

| Attribute | Detail |
|-----------|--------|
| **Method** | [Grid search / random search / Bayesian optimisation / manual] |
| **Search Space** | [Describe ranges explored] |
| **Optimisation Metric** | [e.g., AUC-ROC on validation set] |
| **Cross-Validation** | [e.g., 5-fold stratified] |

---

## 6. Performance Metrics

### Overall Performance

| Metric | Training | Validation | Test | Out-of-Time | Threshold |
|--------|----------|------------|------|-------------|-----------|
| AUC-ROC | | | | | ≥ 0.XX |
| Gini Coefficient | | | | | ≥ 0.XX |
| KS Statistic | | | | | ≥ 0.XX |
| Precision | | | | | ≥ 0.XX |
| Recall | | | | | ≥ 0.XX |
| F1 Score | | | | | ≥ 0.XX |
| Accuracy | | | | | ≥ 0.XX |
| Log Loss | | | | | ≤ X.XX |

### Performance by Segment

| Metric | Overall | [Segment A] | [Segment B] | [Segment C] | [Segment D] | Threshold |
|--------|---------|-------------|-------------|-------------|-------------|-----------|
| AUC-ROC | | | | | | ≥ 0.XX |
| Gini Coefficient | | | | | | ≥ 0.XX |
| KS Statistic | | | | | | ≥ 0.XX |
| Precision | | | | | | ≥ 0.XX |
| Recall | | | | | | ≥ 0.XX |

<!-- Replace [Segment A/B/C/D] with meaningful business segments: product type, customer segment, risk band, geography, etc. -->

### Confusion Matrix (at operating threshold)

| | Predicted Positive | Predicted Negative |
|---|-------------------|-------------------|
| **Actual Positive** | [TP] | [FN] |
| **Actual Negative** | [FP] | [TN] |

**Operating threshold**: [e.g., 0.50 — describe how threshold was selected]

### Performance Comparison

| Metric | This Model (vX.X) | Champion Model (vY.Y) | Baseline | Improvement |
|--------|-------------------|----------------------|----------|-------------|
| AUC-ROC | | | | |
| Gini Coefficient | | | | |
| KS Statistic | | | | |
| Precision | | | | |
| Recall | | | | |

---

## 7. Fairness Assessment

### Subgroup Performance

| Protected Attribute | Group | Sample Size | Approval Rate | FPR | FNR | Disparate Impact | Status |
|---------------------|-------|-------------|---------------|-----|-----|------------------|--------|
| Age | 18–25 | | | | | | Pass / Flag / Fail |
| Age | 26–35 | | | | | | Pass / Flag / Fail |
| Age | 36–50 | | | | | | Pass / Flag / Fail |
| Age | 51–65 | | | | | | Pass / Flag / Fail |
| Age | 65+ | | | | | | Pass / Flag / Fail |
| Gender | Male | | | | | | Pass / Flag / Fail |
| Gender | Female | | | | | | Pass / Flag / Fail |
| Geography | Metro | | | | | | Pass / Flag / Fail |
| Geography | Regional | | | | | | Pass / Flag / Fail |
| Geography | Remote | | | | | | Pass / Flag / Fail |
| Income Band | Low | | | | | | Pass / Flag / Fail |
| Income Band | Medium | | | | | | Pass / Flag / Fail |
| Income Band | High | | | | | | Pass / Flag / Fail |

### Fairness Metrics Summary

| Metric | Definition | Threshold | Result | Status |
|--------|-----------|-----------|--------|--------|
| Disparate Impact Ratio | Ratio of favourable outcome rates between groups | 0.80–1.25 | [Value] | Pass / Flag / Fail |
| Equalised Odds | Max difference in TPR and FPR across groups | ≤ 0.10 | [Value] | Pass / Flag / Fail |
| Demographic Parity | Max difference in positive prediction rates | ≤ 0.10 | [Value] | Pass / Flag / Fail |
| Predictive Parity | Max difference in PPV across groups | ≤ 0.10 | [Value] | Pass / Flag / Fail |

### Proxy Variable Analysis

[Document analysis of whether any features serve as proxies for protected attributes.]

| Feature | Correlation with Protected Attribute | Action Taken |
|---------|-------------------------------------|-------------|
| [e.g., Postcode] | [e.g., 0.45 correlation with Geography] | [e.g., Retained — business justification documented] |

### Fairness Remediation

[If fairness issues were identified, document the mitigations applied.]

1. [e.g., Threshold adjustment for underperforming subgroup]
2. [e.g., Feature removal to reduce proxy effect]
3. [e.g., Resampling to balance subgroup representation]

---

## 8. Limitations & Risks

### Known Limitations

1. [Limitation — describe the scenario and expected model behaviour]
2. [Limitation — describe the scenario and expected model behaviour]
3. [Limitation — describe the scenario and expected model behaviour]

### Failure Modes

1. [Scenario where the model produces unreliable or misleading outputs]
2. [Scenario where the model produces unreliable or misleading outputs]

### Boundary Conditions

| Condition | Requirement | Behaviour if Violated |
|-----------|-------------|----------------------|
| Minimum history | [e.g., Customer shall have ≥ 6 months transaction history] | [e.g., Model returns "insufficient data" flag] |
| Input value range | [e.g., Income > $0, Age 18–120] | [e.g., Input validation rejects record] |
| Population scope | [e.g., Australian residents only] | [e.g., Model not validated for non-AU applicants] |
| Feature availability | [e.g., All required features must be non-null] | [e.g., Fallback to rules-based decision] |

### Risk Assessment

| # | Risk | Likelihood | Impact | Mitigation | Owner |
|---|------|------------|--------|------------|-------|
| 1 | | L / M / H | L / M / H | | |
| 2 | | L / M / H | L / M / H | | |

---

## 9. Monitoring Plan

### Production Monitoring

| Aspect | Detail |
|--------|--------|
| **Metrics Tracked** | [e.g., PSI, KS statistic, AUC-ROC, prediction distribution, feature drift] |
| **Monitoring Frequency** | [Real-time / Daily / Weekly / Monthly] |
| **Monitoring Platform** | [e.g., Databricks monitoring dashboard, custom alerting] |
| **Dashboard Location** | [URL or path to monitoring dashboard] |

### Drift Detection

| Metric | Method | Threshold | Action if Breached |
|--------|--------|-----------|-------------------|
| Feature drift | PSI (Population Stability Index) | PSI > 0.20 | Trigger model review |
| Prediction drift | PSI on score distribution | PSI > 0.20 | Trigger model review |
| Concept drift | KS statistic on target variable | KS > 0.05 | Trigger retraining evaluation |
| Performance decay | AUC-ROC on labelled production data | Drop > 0.03 from baseline | Escalate to Model Risk Committee |

### Alerting & Escalation

| Severity | Condition | Notification | Escalation |
|----------|-----------|-------------|------------|
| Warning | PSI 0.10–0.20 on any feature | [Model owner — e.g., Tom] | Review within 5 business days |
| Critical | PSI > 0.20 or AUC-ROC drop > 0.03 | [Model owner + DS Lead] | Model Risk Committee within 48 hours |
| Emergency | Model producing decisions outside acceptable range | [DS Lead + CRO office] | Immediate model suspension, fallback to rules |

### Retraining Schedule

| Attribute | Detail |
|-----------|--------|
| **Scheduled Retraining** | [e.g., Quarterly, or triggered by drift] |
| **Retraining Data Window** | [e.g., Rolling 24 months] |
| **Validation Requirements** | [e.g., Must meet all performance thresholds before promotion] |
| **Approval for Redeployment** | [e.g., DS Lead sign-off for Tier 3; Model Risk Committee for Tier 1] |

### Champion-Challenger Setup

| Attribute | Champion | Challenger |
|-----------|----------|------------|
| Model Name | [Current production model] | [New candidate model] |
| Version | [X.X.X] | [Y.Y.Y] |
| Algorithm | [Type] | [Type] |
| AUC-ROC | [Value] | [Value] |
| Gini | [Value] | [Value] |
| Traffic Split | [e.g., 90%] | [e.g., 10%] |
| Evaluation Period | [DD-MMM-YYYY to DD-MMM-YYYY] | |
| Promotion Criteria | [Metrics and thresholds required for challenger to replace champion] | |

---

## 10. Ethical Considerations

### Potential Harms

[Describe potential negative impacts on customers or specific groups.]

1. [e.g., Model may disproportionately decline applications from customers in regional areas due to limited bureau data availability]
2. [e.g., Model may perpetuate historical lending patterns that disadvantaged certain demographics]

### Mitigations Applied

1. [e.g., Fairness-aware threshold calibration across geographic subgroups]
2. [e.g., Regular fairness monitoring with automated alerting on disparate impact]
3. [e.g., Human review mandatory for borderline decisions within X points of threshold]

### Human Oversight Requirements

| Decision Type | Oversight Level | Description |
|--------------|-----------------|-------------|
| Clear approve | Automated | Model score above upper threshold — no human review required |
| Borderline | Human review | Model score within [X] points of threshold — referred to assessor |
| Clear decline | Automated + notification | Model score below lower threshold — automated with adverse action notice |
| Override | Senior assessor | Customer dispute or exceptional circumstances — manual override with documentation |

### Recourse Mechanism

[Describe how customers can challenge decisions made using this model.]

- [e.g., Customer may request a manual reassessment through branch or contact centre]
- [e.g., Internal dispute resolution process with independent review]
- [e.g., External dispute resolution via Australian Financial Complaints Authority (AFCA)]

---

## 11. Governance

| Attribute | Detail |
|-----------|--------|
| **Model Risk Classification** | [Tier 1 — Critical / Tier 2 — Significant / Tier 3 — Standard] |
| **Review Cadence** | [Quarterly / Semi-annual / Annual] |
| **Next Scheduled Review** | [DD-MMM-YYYY] |
| **Regulatory Obligations** | [APRA CPS 220, responsible lending, other] |
| **Model Risk Committee Review** | [Date of last review: DD-MMM-YYYY, outcome: Approved / Conditional / Rejected] |

### Approval Chain

| # | Role | Name | Sign-off Date | Status |
|---|------|------|---------------|--------|
| 1 | Model Developer | [Name] | [DD-MMM-YYYY] | Pending / Approved |
| 2 | DS Lead (Peer Review) | Tom | [DD-MMM-YYYY] | Pending / Approved |
| 3 | Model Validation (Independent) | [Name] | [DD-MMM-YYYY] | Pending / Approved |
| 4 | Model Risk Committee | [Committee] | [DD-MMM-YYYY] | Pending / Approved |
| 5 | Business Owner | [Name] | [DD-MMM-YYYY] | Pending / Approved |
| 6 | CRO / GM (per tier) | [Name] | [DD-MMM-YYYY] | Pending / Approved |

### Regulatory Mapping

| Obligation | Requirement | How Addressed |
|-----------|-------------|---------------|
| APRA CPS 220 | Model risk management framework | [Describe compliance approach] |
| Responsible Lending | Explainability and adverse action reasons | [Describe compliance approach] |
| Privacy Act | Personal information handling in model inputs | [Describe compliance approach] |
| Anti-Discrimination | No prohibited attributes as direct inputs | [Describe compliance approach] |

---

## 12. Credit Model Sections

*Include this section for Tier 1 credit decisioning models (e.g., Project Hawkeye). Remove for non-credit models.*

### Explainability

| Method | Scope | Output |
|--------|-------|--------|
| SHAP | Global + local | Feature importance values per prediction |
| LIME | Sampled predictions | Local explanations for adverse actions |
| Feature Importance (gain) | Model-level | Ranked feature list |
| Partial Dependence Plots | Key features | Feature-outcome relationship curves |

### Top Feature Importance

| Rank | Feature | Importance Score | Description |
|------|---------|-----------------|-------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

### Adverse Action Reason Mapping

| # | Feature | Customer-Facing Reason | Priority |
|---|---------|----------------------|----------|
| 1 | [Feature name] | [e.g., "Insufficient credit history length"] | 1 |
| 2 | [Feature name] | [e.g., "High proportion of credit limit utilised"] | 2 |
| 3 | [Feature name] | [e.g., "Recent credit enquiries"] | 3 |
| 4 | [Feature name] | [e.g., "Limited savings history"] | 4 |
| 5 | [Feature name] | [e.g., "Inconsistent income pattern"] | 5 |

### Back-Testing Results

| Period | Predicted Default Rate | Actual Default Rate | Ratio (P/A) | Status |
|--------|----------------------|---------------------|-------------|--------|
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |

**Acceptable range**: Prediction-to-actual ratio between 0.80 and 1.20. Ratios outside this range shall trigger a model review.

---

## 13. Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | [DD-MMM-YYYY] | Initial model card | [Name] |
| | | | |

---

## Appendix

### A. Glossary

| Acronym / Term | Definition |
|----------------|------------|
| ADLS2 | Azure Data Lake Storage Gen2 |
| APRA | Australian Prudential Regulation Authority |
| AUC-ROC | Area Under the Receiver Operating Characteristic Curve |
| CPS 220 | APRA Cross-industry Prudential Standard 220 — Risk Management |
| CRO | Chief Risk Officer |
| FNR | False Negative Rate |
| FPR | False Positive Rate |
| Gini | Gini coefficient — measure of model discriminatory power (2 × AUC − 1) |
| KS | Kolmogorov–Smirnov statistic |
| LIME | Local Interpretable Model-agnostic Explanations |
| MLflow | Databricks model registry and experiment tracking platform |
| PPV | Positive Predictive Value (Precision) |
| PSI | Population Stability Index |
| SHAP | SHapley Additive exPlanations |
| SMOTE | Synthetic Minority Over-sampling Technique |

### B. Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [DD-MMM-YYYY] | [Name] | Initial draft |
