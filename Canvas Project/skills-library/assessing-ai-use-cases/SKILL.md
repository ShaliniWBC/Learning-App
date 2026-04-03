---
name: assessing-ai-use-cases
description: "Evaluates AI and ML use case feasibility for Cortex Suite data products across data readiness, technical feasibility, business value, ethical risk, and organisational readiness dimensions. Use when asked to assess an AI use case, evaluate ML feasibility, score a machine learning proposal, or determine whether an AI initiative should proceed."
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

# Assessing AI & ML Use Case Feasibility for Cortex Suite

Evaluates AI and ML use case feasibility for Westpac's Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat), producing structured feasibility scorecards with evidence-based recommendations.

## Context

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite within Westpac Group's Enterprise Data & Analytics function. AI/ML use cases in enterprise banking carry elevated scrutiny compared to general software initiatives:

- **Regulatory environment** — APRA CPS 220 (Risk Management), CPS 234 (Information Security), and emerging AI-specific guidance require explainability, bias testing, and governance for models that influence customer outcomes or credit decisions.
- **Responsible AI obligations** — Westpac's responsible AI framework mandates human-in-the-loop oversight, bias monitoring, and model risk committee approval for production ML models.
- **Credit decisioning context** — Project Hawkeye (FICO credit decisioning replacement using ML models) is the highest-profile AI initiative. Any credit-adjacent use case carries High regulatory scrutiny by default.
- **ML platform** — Databricks serves as the ML workload platform (model training, feature engineering, experiment tracking). Production models are served via Mesh APIs with monitoring pipelines.

**Architecture stack:** ADAPT pipelines, Snowflake, Databricks, Azure Data Lake (ADLS2), Cosmos DB, Mesh APIs.

**Data Science team:**

| Person | Role | Notes |
|--------|------|-------|
| Tom | Lead Data Scientist | DS team lead; architecture and model decisions |
| Rupa | Data Scientist | Check leave cover |
| Simran | Data Scientist | |
| Justin | Data Scientist | |
| Vivasha | Data Scientist | |
| Claudia | Data Scientist | |
| Richard | Data Scientist | |
| Vinoth | Data Scientist | Part-time — apply 0.5 FTE |

**JIRA project key:** DME.

## Feasibility Dimensions

Every AI/ML use case shall be assessed across five dimensions:

| # | Dimension | What It Measures | Weight |
|---|-----------|------------------|--------|
| 1 | **Data Readiness** | Availability, quality, volume, labelling, and access of training and inference data | 25% |
| 2 | **Technical Feasibility** | Model complexity, infrastructure requirements, latency constraints, platform capability | 20% |
| 3 | **Business Value** | ROI potential, strategic alignment, urgency, and benefit quantification | 25% |
| 4 | **Ethical & Regulatory Risk** | Bias risk, explainability requirements, APRA obligations, customer impact | 20% |
| 5 | **Organisational Readiness** | DS team capacity, MLOps maturity, monitoring capability, operational readiness | 10% |

Weights may be adjusted if the PM specifies different priorities. Any adjustment shall be documented with rationale.

## Workflow

### Step 1 — Define the Use Case

Before assessing anything, establish the fundamentals. Do NOT jump straight to scoring.

**Always ask:**
1. What problem is the AI/ML model solving? Be specific — not "improve customer experience" but "predict which customers are likely to churn within 90 days".
2. What data would the model use? Name specific datasets, tables, or attributes.
3. What decision is being augmented or automated? Is a human currently making this decision?
4. Which Cortex product does this relate to? (Customer Cortex, Customer Interactions, Transcat, or cross-product)
5. Is there an existing JIRA epic or Confluence page? If yes, get the reference.
6. What is the intended deployment mode? (Batch scoring, near-real-time API, real-time streaming)

**If a JIRA key is provided:**
- Use `mcp__jira__jira_get_issue` to pull the epic summary, description, status, and linked issues.
- Use `mcp__jira__jira_search_issues` with JQL `parent = <EPIC-KEY> AND project = DME` to find child stories/tasks and gauge scope.

**If a Confluence page is referenced:**
- Use `mcp__confluence__search_pages` to find existing documentation, design decisions, or prior assessments.
- Read relevant pages for context before assessing.

### Step 2 — Assess Data Readiness

Evaluate the data foundation required for the use case:

1. **Source data availability** — Does the required data exist in Snowflake or ADLS2? Search Confluence for data catalogues or data product documentation.
2. **Data quality** — What are the completeness, accuracy, and timeliness metrics for key attributes? Target >90% quality score on critical fields.
3. **Historical volume** — Is there sufficient history for model training? Most ML use cases require a minimum of 12 months of historical data; time-series models may require 24+ months.
4. **Labels** — For supervised learning: are labels available, or does a labelling strategy need to be defined? Quantify the labelling effort if required.
5. **Feature availability** — Can candidate features be computed from existing data, or do new pipelines need to be built?
6. **Data access** — Are there data classification, RBAC, or privacy constraints that limit access to training data?
7. **Refresh cadence** — Does the data refresh frequency support the intended deployment mode? (e.g., real-time inference requires near-real-time data)

Score: 1 (Critical gaps, data does not exist) to 5 (Data is available, high quality, labelled, and accessible).

### Step 3 — Evaluate Technical Feasibility

Assess the technical complexity and platform readiness:

1. **Model type** — Classification, regression, NLP, time-series forecasting, clustering, recommender, or other. State the likely approach.
2. **Model complexity** — Is this a well-understood problem with established approaches (e.g., logistic regression for propensity), or does it require novel methods (e.g., graph neural networks for fraud detection)?
3. **Infrastructure requirements** — What Databricks cluster configuration is required? GPU requirements? Estimated training time?
4. **Latency constraints** — Batch scoring (hours acceptable), near-real-time (seconds), or real-time (milliseconds). Real-time inference carries significantly higher infrastructure complexity.
5. **Integration complexity** — How many downstream systems need to consume model outputs? What API contract changes are required?
6. **Platform capability** — Does the current Databricks and Mesh API setup support the deployment mode, or are platform enhancements required?
7. **Experiment infrastructure** — Can experiments be run within existing MLflow/Databricks experiment tracking, or is additional tooling required?

Score: 1 (Requires significant platform investment and novel techniques) to 5 (Well-understood problem, existing infrastructure supports it fully).

### Step 4 — Quantify Business Value

Assess the potential return and strategic importance:

1. **Efficiency gains** — FTE savings, time reduction, process automation. Quantify in annual dollar terms where possible.
2. **Risk reduction** — Avoided losses, improved detection rates, compliance improvements. Quantify probability × impact where possible.
3. **Revenue impact** — New capability, customer retention, cross-sell uplift. Apply a 50% realisation factor to be conservative.
4. **Strategic alignment** — How does this use case align with the Cortex product roadmap, enterprise data strategy, and customer outcomes?
5. **Urgency** — Is there a time-sensitive driver (regulatory deadline, competitive pressure, executive mandate)?
6. **Opportunity cost** — What else could the DS team work on instead? Does this use case justify the allocation?

For detailed financial modelling, reference the `modeling-business-cases` skill.

Score: 1 (Low value, weak strategic fit) to 5 (High quantified value, strong strategic alignment, urgent).

### Step 5 — Assess Ethical & Regulatory Risk

Evaluate responsible AI and regulatory considerations:

1. **Bias risk** — Could the model produce systematically different outcomes across protected attributes (age, gender, ethnicity, geography, disability)? Credit and risk models carry the highest bias risk.
2. **Explainability requirements** — Must the model provide individual prediction explanations? Credit decisions require model-agnostic explanations (e.g., SHAP values). Black-box models are not acceptable for credit decisioning.
3. **Regulatory obligations** — Does the use case fall under APRA CPS 220 (Risk Management) or CPS 234 (Information Security)? Credit scoring models require formal model validation and ongoing monitoring.
4. **Customer impact** — Does the model directly affect customer outcomes (credit limits, pricing, eligibility)? Higher customer impact requires stricter governance.
5. **Data privacy** — Does the model require PII or sensitive attributes for training or inference? Are there consent or privacy constraints?
6. **Recourse and contestability** — If the model denies a customer something (credit, service), is there a clear mechanism for the customer to understand and contest the decision?
7. **Approval governance** — Which governance body must approve this model? (DS team review, model risk committee, APRA notification)

Score: 1 (High risk across multiple ethical/regulatory dimensions) to 5 (Low risk, well-understood regulatory position, standard governance applies).

**Note:** A score of 1–2 on this dimension does NOT necessarily mean reject. It means the use case requires additional governance investment, which should be factored into cost and timeline.

### Step 6 — Check Organisational Readiness

Assess whether the team and operating environment can support the use case:

1. **DS team capacity** — Does the team have bandwidth? Map against current sprint commitments. Name specific individuals who would work on this.
2. **Skill match** — Does the team have the required expertise (e.g., NLP specialists for text models, time-series expertise for forecasting)?
3. **MLOps maturity** — Can the team deploy, monitor, and retrain models in production? Is there an established CI/CD pipeline for ML?
4. **Monitoring capability** — Are model performance monitoring, data drift detection, and alerting pipelines in place?
5. **Champion-challenger framework** — Can a new model be deployed alongside the incumbent (or baseline) for controlled comparison?
6. **Operational support** — Who monitors the model in production? Is there a defined escalation path for model degradation?

Score: 1 (Team lacks capacity and capability, no MLOps foundation) to 5 (Team has capacity, expertise, and mature MLOps practices).

### Step 7 — Score & Recommend

1. Score each dimension from 1 to 5 using the evidence gathered in Steps 2–6.
2. Apply dimension weights to calculate the weighted total.
3. Map the total score to a recommendation:

| Weighted Score | Recommendation | Action |
|----------------|----------------|--------|
| 4.0–5.0 | **Proceed** | Use case is feasible and well-supported. Initiate delivery planning. |
| 3.0–3.9 | **Pilot** | Use case has merit but gaps exist. Run a time-boxed pilot (2–4 sprints) to validate assumptions before committing to full delivery. |
| 2.0–2.9 | **Defer** | Significant gaps in one or more dimensions. Address identified gaps (data quality, team capacity, regulatory clarity) before re-assessing. |
| <2.0 | **Reject** | Use case is not feasible given current constraints. Document reasons and conditions for future reconsideration. |

4. Document the recommendation with:
   - Clear rationale linking scores to evidence.
   - Specific conditions or prerequisites for proceeding (if Pilot or Defer).
   - Risks and mitigations for the recommended path.
   - Estimated timeline and DS team allocation for the recommended path.

Read `reference/ai-use-case-assessment-template.md` for the fillable output template.

## Feasibility Scorecard

The primary output of every assessment:

| # | Dimension | Score (1–5) | Weight | Weighted Score | Evidence | Risks |
|---|-----------|-------------|--------|----------------|----------|-------|
| 1 | Data Readiness | [X] | 25% | [X × 0.25] | [Key evidence supporting score] | [Key risks] |
| 2 | Technical Feasibility | [X] | 20% | [X × 0.20] | [Key evidence supporting score] | [Key risks] |
| 3 | Business Value | [X] | 25% | [X × 0.25] | [Key evidence supporting score] | [Key risks] |
| 4 | Ethical & Regulatory Risk | [X] | 20% | [X × 0.20] | [Key evidence supporting score] | [Key risks] |
| 5 | Organisational Readiness | [X] | 10% | [X × 0.10] | [Key evidence supporting score] | [Key risks] |
| | **Total** | | **100%** | **[Sum]** | | |

**Scoring thresholds:** 4.0–5.0 = Proceed · 3.0–3.9 = Pilot · 2.0–2.9 = Defer · <2.0 = Reject

## Data Readiness Checklist

Use this checklist during Step 2 to ensure comprehensive data assessment:

- [ ] Source data exists in Snowflake or ADLS2
- [ ] Sufficient historical volume available (minimum 12 months for most ML use cases)
- [ ] Data quality score >90% on key attributes (completeness, accuracy, timeliness)
- [ ] Labels are available or a labelling strategy has been defined with effort estimate
- [ ] No PII or data classification blockers that prevent model training
- [ ] Refresh cadence supports the intended deployment mode (batch, near-real-time, real-time)
- [ ] Feature engineering requirements are understood and achievable within existing pipelines
- [ ] Data access permissions are in place for the DS team
- [ ] Data lineage is documented for key training attributes
- [ ] Test/holdout data strategy is defined (temporal split, stratified sampling)

## Responsible AI Framework

Westpac-specific responsible AI considerations that shall be assessed for every AI/ML use case:

### Explainability

- All models that influence customer outcomes shall provide model-agnostic explanations (e.g., SHAP, LIME).
- Credit decisioning models shall provide individual prediction explanations that can be communicated to customers.
- Feature importance rankings shall be documented and reviewed for face validity by domain experts.
- Black-box models (deep neural networks without explanation layers) are not acceptable for credit or risk decisions without explicit model risk committee approval.

### Bias Testing

- Models shall be tested for systematic performance differences across protected attributes: age, gender, ethnicity, geography, and disability status.
- Bias testing shall use appropriate fairness metrics for the use case (e.g., equalised odds for credit scoring, demographic parity for marketing).
- Bias test results shall be documented in the model card (reference the `writing-model-cards` skill for documentation).
- Where bias is detected, mitigation strategies shall be documented and approved before production deployment.

### Human-in-the-Loop

- All use cases shall define the level of human oversight required:
  - **Full automation** — model decision is executed without human review (lowest scrutiny use cases only).
  - **Human-on-the-loop** — model decision is executed but flagged for periodic human review.
  - **Human-in-the-loop** — model produces a recommendation; a human makes the final decision.
- Credit decisions shall require human-in-the-loop or human-on-the-loop as a minimum.

### Model Monitoring & Drift Detection

- Production models shall have automated monitoring for:
  - Prediction distribution shifts (output drift).
  - Input feature distribution shifts (data drift).
  - Model performance degradation (accuracy, precision, recall against labelled samples).
- Alert thresholds and escalation paths shall be defined before production deployment.
- Retraining triggers shall be documented (scheduled cadence, drift threshold, performance threshold).

### Approval Governance

- **Low-scrutiny models** (operational efficiency, internal analytics) — DS team lead approval (Tom).
- **Medium-scrutiny models** (customer analytics, personalisation) — DS team lead + product owner approval.
- **High-scrutiny models** (credit scoring, fraud detection, risk models) — model risk committee approval required. APRA notification may be required.

### Documentation Requirements

- Every production model shall have a model card documenting purpose, training data, performance metrics, bias test results, limitations, and monitoring plan.
- Reference the `writing-model-cards` skill for model card creation.

## Use Case Classification

Use this classification to set initial expectations for complexity and regulatory scrutiny:

| Category | Examples | Typical Complexity | Regulatory Scrutiny | Governance Level |
|----------|----------|-------------------|---------------------|------------------|
| **Operational Efficiency** | Pipeline anomaly detection, data quality prediction, automated testing | Low–Medium | Low | DS team lead approval |
| **Customer Analytics** | Customer segmentation, propensity modelling, churn prediction | Medium | Medium | DS lead + product owner |
| **Risk & Credit** | Credit scoring (Hawkeye), fraud detection, collections optimisation | High | High | Model risk committee |
| **Personalisation** | Next best action, product recommendations, content personalisation | Medium–High | Medium–High | DS lead + product owner + privacy review |

Credit and risk use cases (Hawkeye context) shall always be classified as High scrutiny regardless of model complexity.

## Writing Conventions

- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use professional banking language. No "disrupt", "pivot", "hustle", "move fast and break things", or startup jargon.
- Name DS team members explicitly when discussing capacity or skill allocation.
- JIRA keys use the `DME-XXXX` format.

## Quality Checklist

Before presenting any assessment, verify:

- [ ] Use case is clearly defined — problem statement, target variable, and decision being augmented are explicit
- [ ] All five feasibility dimensions are scored with evidence and risk commentary
- [ ] Data readiness checklist has been completed
- [ ] Responsible AI considerations are addressed (explainability, bias, human oversight, monitoring)
- [ ] Use case classification and regulatory scrutiny level are stated
- [ ] Recommendation is one of: Proceed, Pilot, Defer, or Reject — with clear rationale
- [ ] DS team capacity is assessed with named individuals
- [ ] Conditions for proceeding are documented (if Pilot or Defer)
- [ ] Cross-references to related skills are included where relevant (modeling-business-cases, writing-model-cards)
- [ ] All dates use DD-MMM-YYYY format
- [ ] JIRA keys use the DME-XXXX format
- [ ] No startup jargon — professional banking language throughout

## Output Format

- Output the assessment as a single Markdown document.
- Use the header table format shown in the reference template.
- Use horizontal rules (`---`) between major sections.
- Tables shall be properly formatted Markdown tables.
- Save the completed assessment as `AI-Use-Case-Assessment-[Use-Case-Name].md` in the workspace root or a location the PM specifies.
