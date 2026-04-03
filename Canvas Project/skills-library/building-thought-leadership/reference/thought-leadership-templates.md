# Thought Leadership Templates — Cortex Suite

Reference templates for internal thought leadership content. Read the appropriate template when drafting content using the building-thought-leadership skill.

---

## 1. 90-Day Content Calendar Template

Use this template to plan a rolling 90-day content calendar. Review and refresh at the start of each quarter.

### Content Calendar — {Quarter, e.g., Q2 FY2026}

**Planning Date:** {DD-MMM-YYYY}
**Next Review Date:** {DD-MMM-YYYY — 90 days from planning date}

| Month | Week | Topic | Pillar | Format | Channel | Target Audience | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| {MMM} | W1 | {topic title} | {pillar} | {format} | {channel} | {audience} | Shalini | 🔵 Planned |
| {MMM} | W2 | {topic title} | {pillar} | Teams Post | {channel} | {audience} | Shalini | 🔵 Planned |
| {MMM} | W3 | {topic title} | {pillar} | Newsletter Snippet | Newsletter | {audience} | Shalini | 🔵 Planned |
| {MMM} | W4 | — | — | — | — | — | — | — |
| {MMM+1} | W1 | {topic title} | {pillar} | {format} | {channel} | {audience} | Shalini | 🔵 Planned |
| {MMM+1} | W2 | {topic title} | {pillar} | Teams Post | {channel} | {audience} | Shalini | 🔵 Planned |
| {MMM+1} | W3 | {topic title} | {pillar} | Newsletter Snippet | Newsletter | {audience} | Shalini | 🔵 Planned |
| {MMM+1} | W4 | — | — | — | — | — | — | — |
| {MMM+2} | W1 | {topic title} | {pillar} | {format} | {channel} | {audience} | Shalini | 🔵 Planned |
| {MMM+2} | W2 | {topic title} | {pillar} | Teams Post | {channel} | {audience} | Shalini | 🔵 Planned |
| {MMM+2} | W3 | {topic title} | {pillar} | Newsletter Snippet | Newsletter | {audience} | Shalini | 🔵 Planned |
| {MMM+2} | W4 | — | — | — | — | — | — | — |

**Status Legend:**
- 🔵 Planned — topic selected, not yet drafted
- 🟡 In Draft — content being written
- 🟠 In Review — draft complete, awaiting review
- 🟢 Published — live and distributed
- ⚪ Deferred — moved to next cycle

**Cadence Target:**
- 1× substantial piece per month (article or brown bag)
- 2× lighter pieces per month (Teams posts or newsletter snippets)
- Rotate across all five content pillars over 90 days

**Alignment Checkpoints:**
- [ ] Topics align with current Westpac strategic priorities
- [ ] At least one piece timed with an upcoming event (architecture forum, TechX, steering committee)
- [ ] No single pillar dominates — aim for 3+ pillars covered per quarter
- [ ] Effort budget is realistic given current sprint load

---

## 2. Brown Bag / Talk Abstract Template

Use when proposing a brown bag session, lunch & learn, or forum presentation.

```markdown
# {Title — Action-Oriented, Specific}

## Elevator Pitch

{2 sentences: What is the problem or question this talk addresses? What will attendees walk away with?}

## Key Takeaways

1. {First actionable insight attendees shall gain}
2. {Second actionable insight attendees shall gain}
3. {Third actionable insight attendees shall gain}

## Details

| Field | Value |
|---|---|
| **Target Audience** | {Who should attend — role or function, not "everyone"} |
| **Duration** | {30 / 45 / 60 minutes, including Q&A} |
| **Format** | {Presentation / Demo / Workshop / Panel} |
| **Prerequisites** | {What attendees should know beforehand, or "None"} |
| **Presenter** | Shalini Gangadharan, Product Manager — Cortex Suite |
| **Proposed Date** | {DD-MMM-YYYY or "Flexible — next available slot"} |

## Session Outline

| Time | Section | Description |
|---|---|---|
| 0–5 min | Context Setting | {Brief background on the problem or opportunity} |
| 5–20 min | Core Content | {Main insights, evidence, and examples} |
| 20–30 min | Lessons & Patterns | {What worked, what didn't, what is transferable} |
| 30–40 min | Live Demo (optional) | {If applicable — demonstrate a tool, dashboard, or workflow} |
| 40–45 min | Q&A | {Open questions from the audience} |

## Supporting Materials

- {Link to Confluence page, if available}
- {Link to related JIRA epic, if relevant}
- {Slides shall be shared post-session via {channel}}
```

### Example — Completed Abstract

```markdown
# How Cortex Powers Credit Decisioning: Lessons from Replacing FICO

## Elevator Pitch

Learn how Westpac is building its own credit decisioning capability using ML, what worked, what didn't, and what other teams can apply. This session covers the end-to-end journey from FICO dependency to in-house model deployment.

## Key Takeaways

1. Why building in-house ML models for credit decisioning reduces vendor lock-in and improves decision accuracy.
2. The governance framework required to deploy ML models in a regulated credit environment.
3. Three patterns for transitioning from legacy scoring systems without disrupting production.

## Details

| Field | Value |
|---|---|
| **Target Audience** | Data scientists, ML engineers, risk analysts, product managers in data |
| **Duration** | 45 minutes + 15 minutes Q&A |
| **Format** | Presentation with architecture walkthrough |
| **Prerequisites** | General familiarity with credit risk concepts; no ML expertise required |
| **Presenter** | Shalini Gangadharan, Product Manager — Cortex Suite |
| **Proposed Date** | Flexible — next available TechX or architecture forum slot |

## Session Outline

| Time | Section | Description |
|---|---|---|
| 0–5 min | Context Setting | FICO dependency, cost, and limitations in Westpac's credit decisioning |
| 5–25 min | Core Content | Hawkeye architecture, model selection, data pipeline design |
| 25–35 min | Lessons & Patterns | Governance hurdles, model risk management, stakeholder alignment |
| 35–45 min | Q&A | Open discussion |
```

---

## 3. Internal Article Template

Use for Confluence articles, intranet posts, or longer-form written content.

```markdown
# {Headline — Insight-Led, Not Topic-Led}

> ✅ "What We Learned Migrating 5M Customer Records to Snowflake"
> ❌ "Snowflake Migration Update"

*By Shalini Gangadharan, Product Manager — Cortex Suite | {DD-MMM-YYYY}*

---

## Why This Matters

{1 paragraph: Open with the problem or question the reader cares about. Make it relevant to their work, not yours. What will they gain from reading this?}

## Key Insights

### 1. {Insight Heading — Active, Specific}

{2–3 sentences with evidence from Cortex implementation. Include a specific metric, date, or outcome where possible.}

### 2. {Insight Heading — Active, Specific}

{2–3 sentences with evidence. Reference the team member or squad responsible.}

### 3. {Insight Heading — Active, Specific}

{2–3 sentences with evidence. Acknowledge a challenge or trade-off.}

### 4. {Insight Heading} (optional — aim for 3–5 insights total)

{Evidence and context.}

### 5. {Insight Heading} (optional)

{Evidence and context.}

## What Other Teams Can Apply

{1–2 paragraphs: Frame the lessons as transferable principles. What patterns or approaches from this experience are relevant beyond Cortex?}

## Get in Touch

{If your team is exploring {topic}, reach out — we are happy to share our approach and lessons learned. You can find us in the {Teams channel} or contact Shalini Gangadharan directly.}

{Optional: Link to related brown bag, Confluence documentation, or upcoming session.}

---

*Tags: {content pillar}, {product name}, {technology}, {business domain}*
```

### Headline Writing Guide

Strong headlines teach or provoke curiosity. Weak headlines describe.

| ✅ Strong | ❌ Weak |
|---|---|
| "What We Learned Migrating 5M Customer Records to Snowflake" | "Snowflake Migration Update" |
| "Why Our First ML Model in Production Failed — and What We Changed" | "ML Model Deployment" |
| "Three Patterns for Building Data Products That People Actually Use" | "Data Product Strategy" |
| "How a 5-Person Team Delivers Like a 15-Person Team Using AI" | "AI Productivity Tools" |
| "The Hidden Cost of Not Having a Customer 360" | "Customer Cortex Overview" |

---

## 4. Newsletter Snippet Template

Use for division or team newsletter contributions. Aim for 80–120 words.

```markdown
### {Headline — Active, Specific}

{1 paragraph (2–3 sentences): What happened or what we learned. Lead with the insight, not the project name. Be specific — include a number, date, or outcome.}

{1 paragraph (2–3 sentences): Why it matters — connect to something the newsletter audience cares about. Frame it as "what this means for you" not "what we did."}

**Read more:** {Link to full Confluence article or recording}
**Questions?** Reach out to {name} in {channel}.
```

### Example — Completed Snippet

```markdown
### How Cortex Cut Customer Data Refresh Time by 60%

Last month, the Cortex engineering team redesigned the Customer Cortex refresh pipeline, reducing end-to-end processing time from 8 hours to 3.2 hours. The change means downstream consumers — including Digital Banker and the personalisation engine — now access updated customer data before the start of the business day.

If your team consumes customer data from Cortex APIs, you may notice improved data freshness with no changes required on your end. Teams exploring similar pipeline optimisations on Databricks can review our approach.

**Read more:** [Confluence — Cortex Pipeline Optimisation](link)
**Questions?** Reach out to Sasi in the Cortex Engineering channel.
```

---

## 5. Teams Channel Post Template

Use for quick, consistent visibility posts in data community or Cortex channels. Aim for 40–80 words.

```markdown
**{One-Line Hook — Question or Insight}**

{2–3 sentences: Context and the key takeaway. Keep it conversational but professional. One concrete detail — a number, a lesson, a pattern.}

{Optional: 📎 Link to Confluence article, brown bag recording, or related resource.}

{Optional: cc @{person} who contributed or would find it relevant.}
```

### Example — Completed Post

```markdown
**Did you know Cortex processes 22M customer records daily across 14 downstream systems?**

We recently published a breakdown of how Customer Cortex data flows from source systems through ADAPT pipelines to Snowflake and out via Mesh APIs. If your team consumes customer data — or is thinking about onboarding — this is a useful reference.

📎 [How Customer Cortex Works — Confluence](link)

cc @Sasi @GK — thanks for pulling the architecture diagrams together.
```

### Variations for Different Contexts

**After a milestone:**
> **Hawkeye just deployed its third ML model to production.** {What it does, why it matters, who made it happen.}

**Sharing a lesson:**
> **One thing we got wrong in our Snowflake migration (and how we fixed it).** {Brief lesson, link to full write-up.}

**Before a brown bag:**
> **Join us on {DD-MMM-YYYY}: {Talk Title}.** {1 sentence on what attendees shall learn. Link to calendar invite or sign-up.}

**Asking a question:**
> **How does your team measure data product adoption?** {Brief context on why you are asking. Invite responses.}

---

## Template Selection Guide

| Situation | Template | Effort |
|---|---|---|
| Proposing a talk or session | Brown Bag / Talk Abstract | Medium |
| Sharing a detailed lesson or case study | Internal Article | Medium-High |
| Contributing to a newsletter | Newsletter Snippet | Low |
| Quick visibility post in a channel | Teams Channel Post | Low |
| Planning the next 90 days of content | Content Calendar | Medium |
