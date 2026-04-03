---
name: writing-model-cards
description: "Generates ML model cards for Cortex Suite models with performance metrics, fairness assessments, and governance documentation. Use when asked to write a model card, document a model, produce model governance documentation, or create fairness and performance reporting for a machine learning model."
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

# ML Model Cards for Cortex Suite

Generates structured model cards for machine learning models within Westpac's Cortex Suite, covering performance metrics, fairness assessments, explainability, monitoring plans, and governance documentation aligned to APRA model risk management requirements.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite at Westpac Group. Model cards are produced for ML models developed by the Data Science team and are a critical artefact for regulatory compliance, model risk governance, and internal transparency.

**Regulatory environment:**

- Westpac operates under APRA prudential standards including CPS 220 (Risk Management) and CPS 234 (Information Security).
- Credit decisioning models shall comply with responsible lending obligations under the National Consumer Credit Protection Act.
- All models used in customer-facing decisions require explainability documentation and fairness assessment before production deployment.
- The Model Risk Committee governs model approval, monitoring cadence, and retirement decisions.

**Data Science team:**

| Person | Role | Notes |
|--------|------|-------|
| Tom | Lead Data Scientist | DS team lead, model review authority |
| Rupa | Data Scientist | |
| Simran | Data Scientist | |
| Justin | Data Scientist | |
| Vivasha | Data Scientist | |
| Claudia | Data Scientist | |
| Richard | Data Scientist | |
| Vinoth | Data Scientist | Part-time — 0.5 FTE |

**Platform stack:**

| Component | Platform | Purpose |
|-----------|----------|---------|
| ML Training | Databricks | Model development, training, experimentation |
| Feature Store | Snowflake | Feature engineering, feature serving |
| Data Storage | Azure Data Lake Storage Gen2 (ADLS2) | Raw and curated data layers |
| Model Registry | Databricks MLflow | Model versioning, staging, production promotion |
| Monitoring | Databricks / custom | Drift detection, performance tracking |

**Key initiative — Project Hawkeye:** A FICO credit decisioning replacement using ML models. Model cards for Hawkeye models are Tier 1 (Critical) and require quarterly review and Chief Risk Officer (CRO) approval.

## Model Card Standard

Model cards follow the format established by Google's *Model Cards for Model Reporting* (Mitchell et al., 2019), adapted for Westpac's regulated banking environment with additional sections for:

- Regulatory obligations (APRA CPS 220, responsible lending)
- Fairness assessment across protected attributes
- Explainability approach and adverse action reasons
- Champion-challenger framework
- Model risk classification and governance approval chain

## Workflow

### Step 1 — Gather Model Information

Before drafting, establish the following:

1. **What model?** — Model name, version, and identifier in the model registry.
2. **What purpose?** — Business problem the model solves and the decision it supports.
3. **Who built it?** — Model developer(s) from the Data Science team.
4. **What data?** — Training data sources, feature store tables, date range, and volume.
5. **What algorithm?** — Model type, framework, and key hyperparameters.
6. **What status?** — Development, validation, staging, production, or retired.

If a JIRA key is provided, use `mcp__jira__jira_get_issue` to pull the model development epic. Use `mcp__jira__jira_search_issues` to find related stories for training, validation, and deployment.

If a Confluence page is referenced, use `mcp__confluence__search_pages` and `mcp__confluence__get_page` to retrieve existing model documentation, experiment logs, or design decisions.

### Step 2 — Document Model Details

Record the technical specification:

- Model type (e.g., XGBoost, LightGBM, logistic regression, neural network)
- Model version and registry identifier
- Framework and library versions (e.g., scikit-learn 1.4.2, XGBoost 2.0.3)
- Training infrastructure (Databricks cluster configuration, GPU/CPU, runtime)
- Training duration and compute cost
- Hyperparameter configuration (list all non-default values)

### Step 3 — Document Data

Record data provenance and characteristics:

- **Training data**: Source tables, date range, row count, feature count, label distribution
- **Evaluation data**: Source, sampling method, relationship to training data (holdout, temporal split, stratified)
- **Feature descriptions**: List all features with data type, source, and business description
- **Data quality**: Missing value rates, outlier treatment, class imbalance handling
- **Data provenance**: Lineage from source system through to feature store

### Step 4 — Document Performance

Record model performance metrics:

- Metrics computed on each dataset split (training, validation, test, out-of-time)
- Metrics segmented by demographic subgroups where applicable
- Comparison against baseline model or champion model
- Performance on edge cases and boundary conditions
- Use the Performance Metrics table format defined in the Model Card Structure below

### Step 5 — Assess Fairness

Conduct and document fairness analysis:

- Identify protected attributes: Age, Gender, Geography, Income Band
- Compute fairness metrics per subgroup (disparate impact ratio, equalised odds, demographic parity)
- Compare subgroup performance against acceptable ranges
- Document any disparities found and mitigations applied
- Use the Fairness Assessment table format defined in the Model Card Structure below

### Step 6 — Document Limitations

Record known limitations and risks:

- Known failure modes and scenarios where the model performs poorly
- Out-of-scope use cases (what the model should NOT be used for)
- Performance degradation conditions (data drift, population shift, economic cycle changes)
- Boundary conditions and input constraints

### Step 7 — Define Monitoring

Establish the production monitoring plan:

- Metrics to track in production (prediction distribution, feature drift, performance decay)
- Monitoring frequency (real-time, daily, weekly, monthly)
- Drift detection method and thresholds (PSI, KS statistic, KL divergence)
- Performance thresholds that trigger review or retraining
- Alerting rules and escalation path
- Champion-challenger framework (if applicable)

### Step 8 — Governance Sign-off

Document governance requirements:

- Model risk classification tier (see Model Risk Classification below)
- Required approvals based on tier
- Review cadence and next scheduled review date
- Regulatory obligations specific to this model
- Approval chain with named individuals and sign-off dates

## Model Card Structure

The model card is the primary output. All sections below are required. Read `reference/model-card-template.md` for the fillable skeleton.

### 1. Model Overview

| Field | Value |
|-------|-------|
| **Model Name** | [Name] |
| **Version** | [e.g., 2.1.0] |
| **Type** | [e.g., XGBoost classifier] |
| **Purpose** | [Business problem and decision supported] |
| **Owner** | [Model developer name] |
| **Date** | [DD-MMM-YYYY] |
| **Status** | Development / Validation / Staging / Production / Retired |
| **Registry ID** | [MLflow model URI or registry path] |
| **Risk Tier** | [Tier 1 / Tier 2 / Tier 3] |

### 2. Intended Use

- **Primary use case**: [Describe the specific business decision this model supports]
- **Intended users**: [e.g., Credit decisioning engine, risk analysts, automated lending platform]
- **Out-of-scope uses**: [Uses for which this model is not designed or validated]

### 3. Training Data

| Attribute | Detail |
|-----------|--------|
| **Source** | [Snowflake table(s), ADLS2 path(s)] |
| **Date Range** | [DD-MMM-YYYY to DD-MMM-YYYY] |
| **Row Count** | [N records] |
| **Feature Count** | [N features] |
| **Label Distribution** | [e.g., 5.2% positive, 94.8% negative] |
| **Data Quality** | [Missing rate, outlier treatment, imputation method] |
| **Class Balancing** | [Method applied, e.g., SMOTE, undersampling, none] |

### 4. Evaluation Data

| Attribute | Detail |
|-----------|--------|
| **Source** | [Same source / separate source] |
| **Date Range** | [DD-MMM-YYYY to DD-MMM-YYYY] |
| **Row Count** | [N records] |
| **Sampling Method** | [Holdout / temporal split / stratified / k-fold] |
| **Relationship to Training** | [Describe separation method and any overlap controls] |

### 5. Model Architecture

| Attribute | Detail |
|-----------|--------|
| **Algorithm** | [e.g., XGBoost, LightGBM, logistic regression] |
| **Framework** | [e.g., scikit-learn 1.4.2, XGBoost 2.0.3] |
| **Key Hyperparameters** | [List non-default values] |
| **Training Infrastructure** | [Databricks cluster type, GPU/CPU, runtime version] |
| **Training Duration** | [e.g., 2.5 hours] |
| **Model Size** | [e.g., 12 MB serialised] |

### 6. Performance Metrics

| Metric | Overall | Segment A | Segment B | Segment C | Threshold |
|--------|---------|-----------|-----------|-----------|-----------|
| AUC-ROC | | | | | ≥ 0.XX |
| Precision | | | | | ≥ 0.XX |
| Recall | | | | | ≥ 0.XX |
| F1 Score | | | | | ≥ 0.XX |
| Accuracy | | | | | ≥ 0.XX |
| Gini Coefficient | | | | | ≥ 0.XX |
| KS Statistic | | | | | ≥ 0.XX |
| Log Loss | | | | | ≤ X.XX |

**Standard metrics for credit models:** AUC-ROC, Gini coefficient, KS statistic, Precision, Recall, F1, Accuracy, Log Loss.

**Segment columns** should be replaced with meaningful business segments (e.g., by product type, customer segment, or risk band). Include as many segment columns as relevant.

**Performance comparison:**

| Metric | This Model | Champion Model | Baseline | Improvement |
|--------|-----------|----------------|----------|-------------|
| AUC-ROC | | | | |
| Gini | | | | |

### 7. Fairness Assessment

| Protected Attribute | Group | Metric | Value | Acceptable Range | Status |
|---------------------|-------|--------|-------|-------------------|--------|
| Age | 18–25 | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Age | 26–35 | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Age | 36–50 | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Age | 51–65 | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Age | 65+ | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Gender | Male | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Gender | Female | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Geography | Metro | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Geography | Regional | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Geography | Remote | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Income Band | Low | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Income Band | Medium | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |
| Income Band | High | Approval Rate | | [X%–Y%] | Pass / Flag / Fail |

**Fairness metrics applied:**

| Metric | Definition | Threshold |
|--------|-----------|-----------|
| Disparate Impact Ratio | Ratio of favourable outcome rates between groups | 0.80–1.25 |
| Equalised Odds | Difference in true positive and false positive rates | ≤ 0.10 |
| Demographic Parity | Difference in positive prediction rates | ≤ 0.10 |

### 8. Limitations & Risks

**Known limitations:**
1. [Limitation — describe scenario and expected behaviour]
2. [Limitation — describe scenario and expected behaviour]

**Failure modes:**
1. [Scenario where the model produces unreliable outputs]
2. [Scenario where the model produces unreliable outputs]

**Boundary conditions:**
- Minimum input requirements: [e.g., customer must have ≥ 6 months transaction history]
- Input value ranges: [e.g., income must be > $0, age must be 18–120]
- Population constraints: [e.g., model trained on AU residents only]

### 9. Monitoring Plan

| Aspect | Detail |
|--------|--------|
| **Metrics Tracked** | [e.g., PSI, KS statistic, AUC-ROC, prediction distribution] |
| **Monitoring Frequency** | [Real-time / Daily / Weekly / Monthly] |
| **Drift Detection Method** | [e.g., PSI with threshold 0.20, KS statistic with threshold 0.05] |
| **Performance Threshold** | [e.g., AUC-ROC drop > 0.03 triggers review] |
| **Alerting** | [Who is notified, via what channel, escalation path] |
| **Retraining Trigger** | [Conditions that trigger model retraining] |
| **Champion-Challenger** | [Whether a challenger model runs in parallel; comparison cadence] |

### 10. Ethical Considerations

- **Potential harms**: [Describe potential negative impacts on customers or groups]
- **Mitigations applied**: [What controls are in place to prevent or reduce harm]
- **Human oversight**: [Where human review is required in the decision chain]
- **Recourse mechanism**: [How customers can challenge decisions made using this model]

### 11. Governance

| Attribute | Detail |
|-----------|--------|
| **Model Risk Classification** | [Tier 1 / Tier 2 / Tier 3] |
| **Review Cadence** | [Quarterly / Semi-annual / Annual] |
| **Next Scheduled Review** | [DD-MMM-YYYY] |
| **Approval Chain** | [List approvers in order] |
| **Regulatory Obligations** | [APRA CPS 220, responsible lending, other] |
| **Model Risk Committee Review** | [Date of last review, outcome] |

### 12. Version History

| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | [DD-MMM-YYYY] | Initial model card | [Name] |

## Credit Model Specific Sections

For Project Hawkeye and other credit decisioning models, the following additional sections shall be included in the model card.

### Regulatory Requirements

- **APRA CPS 220**: Model shall comply with Westpac's risk management framework under CPS 220, including model validation, independent review, and ongoing monitoring.
- **Responsible Lending**: Model outputs shall support compliance with responsible lending obligations. The model shall not be the sole determinant of a credit decision — human oversight is required for edge cases.
- **Anti-Discrimination**: Model shall not use prohibited attributes (race, religion, marital status, sexual orientation) as direct inputs. Proxy variable analysis shall be documented.

### Explainability Approach

| Method | Purpose | Scope |
|--------|---------|-------|
| SHAP (SHapley Additive exPlanations) | Global and local feature importance | All predictions |
| LIME (Local Interpretable Model-agnostic Explanations) | Local explanations for individual decisions | Sampled predictions, adverse actions |
| Feature Importance (gain-based) | Global feature ranking | Model-level |
| Partial Dependence Plots | Feature-outcome relationships | Key features |

### Adverse Action Reasons

For credit decline decisions, the model shall produce the top N reasons for the adverse action. These reasons shall be:

1. Expressed in plain language understandable by the customer
2. Specific to the individual application (not generic)
3. Ordered by contribution magnitude (most impactful reason first)
4. Compliant with responsible lending disclosure requirements

**Adverse action reason mapping:**

| Feature | Customer-Facing Reason | Priority |
|---------|----------------------|----------|
| [Feature name] | [Plain language reason, e.g., "Insufficient credit history length"] | [1–N] |

### Champion-Challenger Framework

| Attribute | Champion | Challenger |
|-----------|----------|------------|
| Model Name | [Current production model] | [New candidate model] |
| Version | [X.X] | [Y.Y] |
| Algorithm | [Type] | [Type] |
| AUC-ROC | [Value] | [Value] |
| Gini | [Value] | [Value] |
| Traffic Split | [e.g., 90%] | [e.g., 10%] |
| Evaluation Period | [Start – End date] | |
| Promotion Criteria | [Metrics and thresholds for challenger promotion] | |

### Back-Testing Results

| Period | Predicted Default Rate | Actual Default Rate | Ratio | Status |
|--------|----------------------|--------------------:|-------|--------|
| [MMM-YYYY] | [X.X%] | [X.X%] | [X.XX] | Pass / Flag / Fail |

Back-testing shall compare predicted outcomes against actual outcomes over historical periods. A prediction-to-actual ratio between 0.80 and 1.20 is considered acceptable. Ratios outside this range shall trigger a model review.

## Model Risk Classification

All models shall be classified into one of three tiers based on their business criticality and regulatory exposure.

| Tier | Description | Examples | Review Cadence | Approval Level |
|------|-------------|----------|----------------|----------------|
| **Tier 1 — Critical** | Models that directly determine customer outcomes in regulated domains | Credit decisioning, fraud detection, anti-money laundering | Quarterly | Chief Risk Officer (CRO) |
| **Tier 2 — Significant** | Models that influence business decisions or customer experience but do not directly determine regulated outcomes | Customer analytics, segmentation, propensity scoring, churn prediction | Semi-annual | General Manager (GM) |
| **Tier 3 — Standard** | Models used for internal analytics, operational efficiency, or non-customer-facing purposes | Internal reporting, operational forecasting, resource allocation | Annual | Team Lead (Data Science) |

**Classification criteria:**

1. Does the model directly determine a customer outcome (approval, decline, pricing)? → Tier 1
2. Does the model influence customer-facing decisions or operate in a regulated domain? → Tier 2
3. Is the model used for internal purposes with no direct customer impact? → Tier 3

When in doubt, classify upward (e.g., if uncertain between Tier 2 and Tier 3, classify as Tier 2).

## Quality Checklist

Before presenting any model card, verify:

- [ ] Model Overview is complete with name, version, type, purpose, owner, date, status, and risk tier
- [ ] Intended Use clearly states primary use case, intended users, and out-of-scope uses
- [ ] Training Data documents source, date range, volume, feature count, and label distribution
- [ ] Evaluation Data documents source, sampling method, and relationship to training data
- [ ] Model Architecture records algorithm, framework, hyperparameters, and training infrastructure
- [ ] Performance Metrics table includes all standard metrics with per-segment breakdowns
- [ ] Performance comparison against champion model or baseline is included
- [ ] Fairness Assessment covers all four protected attributes (Age, Gender, Geography, Income Band)
- [ ] Fairness metrics include disparate impact ratio with acceptable range
- [ ] Limitations & Risks lists known failure modes, boundary conditions, and out-of-scope scenarios
- [ ] Monitoring Plan specifies metrics, frequency, drift thresholds, and alerting
- [ ] Ethical Considerations documents potential harms, mitigations, and human oversight
- [ ] Governance section includes risk tier, review cadence, approval chain, and regulatory obligations
- [ ] Version History is initialised
- [ ] Credit model sections are included if the model is Tier 1 credit decisioning (Hawkeye)
- [ ] All dates use DD-MMM-YYYY format
- [ ] Professional banking language throughout — no startup jargon
- [ ] "Shall" for mandatory requirements, "should" for recommendations, "may" for optional items

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use professional banking language. No "disrupt", "pivot", "hustle", or startup jargon.
- Name people explicitly — never say "the team" when you can name individuals.
- Version numbers follow semantic convention: Major.Minor.Patch (e.g., 2.1.0).
- Model risk tiers shall always be stated as "Tier 1 — Critical", "Tier 2 — Significant", or "Tier 3 — Standard".

## Output Format

- Output the model card as a single Markdown document.
- Use the header table format shown in the Model Overview section.
- Include a table of contents after the Model Overview.
- Use horizontal rules (`---`) between major sections.
- Tables shall be properly formatted Markdown tables.
- Save the completed model card as `{Model-Name}-Model-Card-v{Version}.md` in the workspace root or a location the PM specifies.
