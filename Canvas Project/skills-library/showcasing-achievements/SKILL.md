---
name: showcasing-achievements
description: "Documents and frames career achievements and product impact for performance reviews, career discussions, and leadership visibility. Use when asked to capture an achievement, build a career narrative, prepare for a performance review, or frame accomplishments for skip-level meetings."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__outlook__outlook_get_calendar_events
  - mcp__outlook__outlook_search_emails
  - mcp__outlook__teams_search_messages
  - Read
  - create_file
  - edit_file
  - task_list
---

# Showcasing Achievements — Career Portfolio Skill

Documents and frames career achievements for performance reviews, career discussions, skip-level meetings, and leadership visibility. Produces evidence-backed achievement logs, competency-mapped career narratives, and audience-tailored impact summaries.

## Context

Achievements that are not documented and framed do not exist in organisational memory. This is especially true when leadership changes — new executives start with a blank slate. A decade of exceptional delivery becomes invisible overnight unless it is captured, quantified, and accessible.

This skill helps **Shalini Gangadharan**, Product Manager for Cortex Suite, maintain a living portfolio of achievements framed for different audiences and purposes. It is NOT about self-promotion — it is about ensuring the organisation has accurate information to make talent decisions.

The agent shall approach achievement documentation with the same rigour applied to any enterprise data product: structured, evidence-backed, version-controlled, and fit for purpose.

### Why This Matters Now

- New leadership inherits no institutional memory of prior contributions
- Promotion panels require demonstrated competency evidence, not tenure
- Career discussions without quantified impact default to recency bias
- Internal mobility applications require structured achievement portfolios
- The gap between "what Shalini has delivered" and "what the organisation knows she has delivered" represents a material career risk

## Achievement Types

The agent shall categorise achievements using the following taxonomy:

| Type | Description | Example | Impact Level |
|---|---|---|---|
| **Product Launch** | New capability delivered, new consumer onboarded | New Cortex capability, Digital Banker onboarding | Medium–High |
| **Business Outcome** | Measurable revenue, cost, or risk impact | Revenue uplift, cost reduction, risk mitigation | High |
| **Strategic Initiative** | Enterprise-level programmes or operating model changes | Data products operating model, Hawkeye FICO replacement | Very High |
| **Technical Milestone** | Platform migration, architecture modernisation | DirectShares migration, ADAPT pipeline redesign | Medium |
| **Team Development** | Talent growth, hiring, culture building | Graduate engineer development, squad formation | Medium |
| **Thought Leadership** | Presentations, publications, internal forums | TechX presentation, community of practice facilitation | Medium |
| **Process Innovation** | New ways of working, efficiency improvements | AI-augmented PM workflow (Amp skills), sprint health scoring | Medium |

## Achievement Documentation Framework

For each achievement, the agent shall capture the following fields:

| Field | Content | Guidance |
|---|---|---|
| **Title** | Action-oriented headline | Lead with a verb: "Established", "Delivered", "Led", "Designed" |
| **Date / Period** | When this occurred | DD-MMM-YYYY or date range (e.g., Jan-2025 – Jun-2025) |
| **Type** | Achievement category | From the taxonomy above |
| **Context** | Situation before the achievement | What was the problem, gap, or opportunity? |
| **Action** | What Shalini specifically did | Her individual contribution — not the team's collective effort |
| **Result** | Quantified outcome | Revenue ($), efficiency (%), adoption (#users), risk reduction, time saved |
| **Evidence** | Verifiable proof | JIRA tickets, Confluence pages, stakeholder quotes, metrics dashboards |
| **Strategic Significance** | Why this matters at enterprise level | Connect to enterprise strategy, customer outcomes, or regulatory compliance |
| **Skills Demonstrated** | Leadership competencies showcased | Map to Westpac leadership competency framework |

### Documentation Principles

1. **Quantify everything** — "improved" is not a metric. "Reduced processing time by 60%" is.
2. **Distinguish YOUR contribution from the team's** — promotion panels care about individual impact, not team output.
3. **Never fabricate or inflate** — credibility is non-negotiable in a regulated institution.
4. **Capture context** — without the "before" state, the "after" has no meaning.
5. **Link to evidence** — every claim shall be traceable to a JIRA ticket, Confluence page, or verifiable metric.

## Career Narrative Formats

The agent shall produce achievement summaries tailored to the intended audience and purpose:

| Purpose | Format | Length | Audience | Tone |
|---|---|---|---|---|
| **Performance Review** | Achievement log with evidence and competency mapping | Comprehensive (3–5 pages) | Direct manager | Factual, evidence-rich |
| **Skip-Level / Career Discussion** | Career narrative with trajectory and aspiration | 1 page | Senior leader (GM+) | Strategic, forward-looking |
| **Internal Application** | Achievement portfolio with competency matrix | Detailed (4–6 pages) | Hiring panel | Structured, competency-mapped |
| **LinkedIn / External** | Impact summary with headline metrics | Brief (1 page) | Professional network | Confident, outcome-focused |
| **Elevator Pitch** | 60-second verbal narrative | 3–4 sentences | Networking / ad hoc | Conversational, memorable |

## Workflow

### Step 1 — Capture the Achievement

As soon as a win occurs, the agent shall document it using the Achievement Documentation Framework. Do not wait for review season — capture while context and evidence are fresh.

The agent should search JIRA and Confluence for supporting evidence:
```
mcp__jira__jira_search_issues(jql="project = DME AND status = Done AND assignee = currentUser()", maxResults=50)
mcp__confluence__search_pages(query="cortex launch release", limit=10)
```

### Step 2 — Quantify Impact

Translate every achievement into measurable outcomes. The agent shall apply the following transformations:

| Vague | Quantified |
|---|---|
| "Led migration" | "Led migration of 5M customer records, reducing query latency by 60%" |
| "Improved process" | "Redesigned sprint planning workflow, reducing planning overhead from 3 hours to 30 minutes per cycle" |
| "Built deposit product" | "Designed and launched term deposit product from ground up, contributing $X to portfolio growth" |
| "Managed stakeholders" | "Aligned 14 downstream consumers across 6 business units to Cortex data contract framework" |
| "Presented at conference" | "Selected as 1 of 12 presenters at Westpac TechX (2,000+ attendees) on AI-augmented product management" |

Where exact figures are unavailable, the agent should use defensible estimates with stated assumptions: "Estimated 40% reduction based on before/after pipeline execution times."

### Step 3 — Frame for Audience

Rewrite the same achievement for different contexts. The agent shall produce audience-specific framings:

**Example — Hawkeye FICO Replacement:**

- **Performance Review:** "Leading Hawkeye programme (FICO credit scorecard replacement) across 3 squads, managing $X budget, coordinating with APRA-aligned model governance, and delivering against 12-month roadmap with 85% milestone completion rate."
- **Skip-Level:** "Driving Westpac's strategic independence from a single-vendor credit decisioning model, reducing licensing costs and enabling in-house IP for credit risk assessment."
- **Elevator Pitch:** "I'm leading the replacement of Westpac's FICO credit scorecards with in-house ML models — it's one of the bank's most strategically significant data initiatives this year."

### Step 4 — Map to Competencies

The agent shall map each achievement to Westpac leadership competencies. This is critical for promotion panels, which assess competency breadth — not just delivery volume.

See the Competency Mapping section below.

### Step 5 — Build the Portfolio

The agent shall assemble achievements into a coherent career narrative showing:

1. **Progression** — increasing scope, complexity, and strategic impact over time
2. **Breadth** — competencies across delivery, strategy, people, and commercial dimensions
3. **Trajectory** — a clear direction toward CPO / Head of Product
4. **Distinctiveness** — what Shalini brings that is rare or unique (e.g., MIT Sloan + P&L management + enterprise data products + AI/ML governance)

Read `reference/achievement-portfolio-template.md` for the fillable template.

### Step 6 — Update Regularly

- **Monthly:** Capture new achievements using the framework
- **Quarterly:** Refresh career narrative; update competency mapping; review trajectory
- **Annually:** Comprehensive portfolio review; align to performance review cycle
- **On trigger:** Leadership change, internal application, or career discussion

## Competency Mapping — Westpac Leadership Framework

The agent shall map achievements to the following competency framework, typical for major Australian banks:

| Competency | What It Means | Shalini's Evidence Areas |
|---|---|---|
| **Strategic Thinking** | Sees the big picture; connects work to enterprise strategy; anticipates shifts | Data products operating model design, Cortex roadmap, Hawkeye strategic case |
| **Stakeholder Influence** | Builds relationships; drives alignment without direct authority; manages up and across | Cross-team Cortex adoption (14 consumers), architecture alignment with Mandar/Raja, executive engagement |
| **Delivery Excellence** | Ships on time; manages risks and dependencies; drives quality | Sprint delivery cadence, Hawkeye milestones, sprint health scoring |
| **Innovation** | Introduces new approaches; challenges the status quo; experiments | AI-augmented PM workflow (21 Amp skills), ML-powered credit decisioning, process automation |
| **People Leadership** | Develops talent; builds culture; manages performance across diverse teams | Graduate development (Josh, Jolin, Richard, Claudia, Theresa), 3-squad leadership, hiring |
| **Commercial Acumen** | Understands P&L; builds rigorous business cases; manages budgets | Investment products P&L management, Account Scrutiny $122K, Hawkeye budgetary guidance |
| **Customer Centricity** | Drives customer outcomes; understands end-to-end experience | Customer Cortex 360° view, personalisation enablement, downstream consumer experience |

### Competency Coverage Assessment

The agent should assess competency coverage and identify gaps:

```
✅ Strong evidence (3+ achievements)
⚠️ Moderate evidence (1-2 achievements)
❌ Gap — needs deliberate effort
```

## Career Narrative Template

The agent shall use the following structure for career narrative outputs:

```markdown
## Career Summary
{2–3 sentences: who Shalini is professionally, her trajectory, her distinctive strengths}

## Current Role Impact
{3–5 achievement bullets from current role, quantified, with competency tags}

## Career Highlights
{5–7 most significant achievements across full career, quantified, with competency tags}

## Where I'm Heading
{2–3 sentences: career aspiration, what she's building toward, why she's ready}

## What Others Say
{2–3 recommendation excerpts or stakeholder quotes, attributed}
```

## Achievement Capture Prompts

The agent should use the following reflective questions during monthly capture sessions:

1. What did I deliver this month that would not have happened without me?
2. What decision did I influence? What was the outcome?
3. What problem did I solve that others could not?
4. Who did I develop or support? What was the impact on their growth?
5. What strategic connection did I make that no one else saw?
6. What did I learn that changed how I operate?
7. What feedback did I receive — positive or constructive — that I should document?
8. What risk did I identify or mitigate before it materialised?
9. What process did I improve? What was the before/after?
10. What cross-functional relationship did I build or strengthen?

## Known Achievement Inventory

The following achievements are known from context and shall be used as seeds for the portfolio. Each requires full documentation using the framework.

| Achievement | Type | Period | Impact Level | Competencies |
|---|---|---|---|---|
| MIT Sloan Executive Education | Thought Leadership | Historical | High | Strategic Thinking, Innovation |
| P&L management for investment products | Business Outcome | Historical | Very High | Commercial Acumen, Strategic Thinking |
| Built deposit products from ground up | Product Launch | Historical | High | Delivery Excellence, Commercial Acumen |
| Doubled new accounts via digital origination | Business Outcome | Historical | Very High | Innovation, Customer Centricity |
| Led DirectShares platform migration | Technical Milestone | Historical | High | Delivery Excellence, Stakeholder Influence |
| Developed Westpac data products operating model | Strategic Initiative | Current | Very High | Strategic Thinking, Innovation |
| Presented at TechX conference | Thought Leadership | Current | Medium | Innovation, Stakeholder Influence |
| Leading Hawkeye FICO replacement programme | Strategic Initiative | Current | Very High | Strategic Thinking, Delivery Excellence, People Leadership |
| Built AI-augmented PM workflow (21 Amp skills) | Process Innovation | Current | High | Innovation, Delivery Excellence |
| Customer Cortex 360° enterprise data product | Product Launch | Current | Very High | Strategic Thinking, Customer Centricity |

## Guardrails

1. The agent **shall** quantify every achievement — "improved" is not a metric.
2. The agent **shall** distinguish Shalini's individual contribution from the team's collective output.
3. The agent **shall not** fabricate, inflate, or embellish any achievement or metric.
4. The agent **should** capture achievements continuously, not just at review time — recency bias is real and damaging.
5. The agent **shall** frame achievements in terms of business impact, not personal effort — "worked hard" is irrelevant; "delivered $X outcome" is material.
6. The agent **shall** use evidence (JIRA, Confluence, metrics, stakeholder quotes) to substantiate every claim.
7. The agent **should** identify competency gaps and suggest deliberate actions to address them.
8. The agent **shall not** use self-promotional language — let the evidence speak. "Delivered" not "amazingly delivered."
9. The agent **shall** maintain version history for the portfolio — track what was added and when.
10. The agent **shall** treat the achievement portfolio as a living document, not a point-in-time snapshot.

## Writing Style

- Use clear, professional language appropriate for banking and financial services.
- Avoid jargon from consumer technology or startup culture. No "disrupt", "pivot", "hustle", "crushing it."
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym thereafter.
- Achievement titles shall be action-oriented and begin with a past-tense verb (Delivered, Established, Led, Designed).
- Numbers under ten are written as words in prose; tables use numerals throughout.
- Percentages always use numerals: "60% reduction", not "sixty percent reduction."

## Quality Checklist

Before delivering any achievement documentation or career narrative, the agent shall verify:

- [ ] Every achievement has all 9 framework fields completed (Title through Skills Demonstrated)
- [ ] All results are quantified with specific metrics, not qualitative adjectives
- [ ] Shalini's individual contribution is clearly distinguished from team effort
- [ ] Evidence sources are cited for every claim (JIRA, Confluence, metrics, quotes)
- [ ] Competency mapping covers at least 5 of 7 competencies
- [ ] Career narrative follows the template structure
- [ ] Audience-specific framing matches the stated purpose (review, skip-level, application, etc.)
- [ ] No fabricated or inflated claims — all metrics are defensible
- [ ] All dates use DD-MMM-YYYY format
- [ ] Language is professional — no startup jargon, no self-promotional tone
- [ ] Portfolio version and last-updated date are recorded
- [ ] Artefact has been saved to the specified location
