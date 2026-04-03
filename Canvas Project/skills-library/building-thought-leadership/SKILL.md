---
name: building-thought-leadership
description: "Creates internal thought leadership content and visibility plans to establish Cortex Suite as a recognised enterprise capability and Shalini as a strategic data product leader. Use when asked to build visibility, draft a brown bag abstract, write an internal article, plan thought leadership, or create a content calendar."
allowed-tools:
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__confluence__create_page
  - mcp__jira__jira_search_issues
  - mcp__outlook__outlook_get_calendar_events
  - mcp__outlook__outlook_search_emails
  - Read
  - create_file
  - edit_file
  - task_list
---

# Building Thought Leadership for Cortex Suite

Creates internal thought leadership content and visibility plans to establish Cortex Suite as a recognised enterprise capability and position Shalini Gangadharan as a strategic voice in data products, AI, and customer analytics within Westpac Group.

## Context

Visibility at CPO / Head of Product level comes from being recognised as a strategic thinker, not just an executor. This skill helps build a "Cortex brand" inside Westpac through consistent, useful insight shared in trusted channels.

Shalini has the credentials — MIT Sloan educated, TechX presenter ("Customer Obsession through Data & ML"), P&L experience, built enterprise data products ground-up, 2K+ LinkedIn followers — but these are largely invisible to new leadership. Thought leadership makes expertise visible.

**The principle is simple:** share genuinely useful insight, consistently, in the places leadership reads. This is not personal marketing. It is making Cortex's value — and the thinking behind it — visible to the people who fund, sponsor, and consume enterprise data products.

You are assisting **Shalini Gangadharan**, Product Manager for the Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat) within Westpac Group's DDAI Division.

### Key Audiences for Thought Leadership

| Audience | Where They Are | What They Value |
|---|---|---|
| Executive sponsors (GMs, VPs) | Leadership meetings, intranet, newsletters | Strategic framing, enterprise impact, ROI |
| Architecture & engineering leaders | Architecture forums, TechX, Confluence | Technical depth, design decisions, trade-offs |
| Peer product managers | Product community channels, brown bags | Practical PM approaches, data product patterns |
| Data community | Data/analytics channels, Confluence | Data strategy, governance, quality, ML |
| Downstream consumers | Teams channels, release comms | What Cortex does, what is coming, how to use it |

## Content Pillars

These are the topics Shalini should own — areas where she has genuine authority built from hands-on experience:

| Pillar | Why She Owns It | Example Topics |
|---|---|---|
| **Enterprise Data Products** | Built the data products operating model at Westpac | Data product strategy; data-as-a-product; data mesh in banking; consumer-centric data platforms; building an enterprise data product catalogue |
| **AI/ML in Banking** | Runs Project Hawkeye (FICO replacement), propensity models | Responsible AI in financial services; credit decisioning with ML; ML governance and model risk; building vs buying models |
| **Customer 360 & Personalisation** | Cortex IS the enterprise customer 360 | Customer data strategy; cross-channel interaction insights; personalisation at scale; single customer view architecture |
| **Product Management for Data** | Her core discipline across multiple data products | PM for internal platforms; measuring data product value; adoption-driven product strategy; building PM rigour in data teams |
| **Scaling with AI & Automation** | Actively doing this — using Amp, Copilot, automation | AI-augmented product management; scaling a small team with AI tools; practical automation for PMs; productivity without headcount |

## Content Formats

| Format | Channel | Audience | Effort | Frequency | Impact |
|---|---|---|---|---|---|
| Brown Bag / Lunch & Learn | In-person or Teams | Immediate org | Medium | Quarterly | High — face-to-face visibility, Q&A builds reputation |
| Internal Article / Intranet Post | Confluence or intranet | Broad organisation | Medium | Monthly | Medium — searchable, persistent, shareable |
| Forum Presentation | TechX, architecture forums | Cross-organisation | High | Annually | Very high — established credibility with senior audience |
| Newsletter Snippet | Team or division newsletter | Manager's peers, leadership | Low | Monthly | Medium — reaches leadership inbox directly |
| Teams Channel Post | Cortex / data community channels | Data community | Low | Bi-weekly | Low-medium — consistent presence, low barrier |
| Confluence Knowledge Article | Confluence | Technical audience | Medium | As needed | Medium — referenced over time, builds a body of work |

## Workflow

### Step 1 — Build Content Calendar

Align topics with Westpac strategic priorities and upcoming events. Check:

- **Calendar**: Use `mcp__outlook__outlook_get_calendar_events` to identify upcoming forums, TechX, architecture reviews, or brown bag slots.
- **JIRA**: Use `mcp__jira__jira_search_issues` to find recently completed work that yields a good story (shipped features, solved problems, interesting trade-offs).
- **Confluence**: Use `mcp__confluence__search_pages` to review existing Cortex content and identify gaps — topics with no clear articulation.

Create a 90-day content calendar using the format in the Content Calendar Format section below.

### Step 2 — Select Topic & Format

Choose from the content pillars. Match the format to the audience and effort budget:

1. **High-effort, high-impact** (quarterly): Brown bags, forum presentations — reserve for pillar topics with the strongest evidence.
2. **Medium-effort, persistent** (monthly): Internal articles, Confluence knowledge articles — build a searchable body of work.
3. **Low-effort, consistent** (bi-weekly/monthly): Teams posts, newsletter snippets — maintain visibility between bigger pieces.

Every topic shall connect to at least one content pillar and one current Cortex initiative.

### Step 3 — Draft Content

Read the appropriate template from `reference/thought-leadership-templates.md`.

Every piece of content must teach something useful. The reader should finish with at least one insight they can apply to their own work. No fluff, no corporate boilerplate, no self-promotion.

### Step 4 — Add Cortex Evidence

Ground every insight in real Cortex examples and data:

- Reference specific initiatives (Hawkeye, Customer Cortex migration, Transcat enrichment).
- Include quantified outcomes where available (records processed, latency improved, consumers onboarded).
- Use the Cortex value ledger, sprint metrics, and JIRA data to support claims.
- Where proprietary data cannot be shared, describe the pattern without the specific numbers.

### Step 5 — Plan Distribution

For each piece of content, determine:

1. **Primary channel** — where the content shall be published.
2. **Amplification** — who should be tagged, thanked, or asked to share (e.g., "cc Jeni", "tag in Data Community channel").
3. **Cross-posting** — should a summary go to the newsletter, a Teams post link to the article?
4. **Timing** — align publication with relevant events (before a steering committee, after a milestone, during a strategic planning cycle).

### Step 6 — Track Engagement

After publication, note:

- Reactions, likes, or views (where visible).
- Questions or comments received.
- Follow-up conversations initiated.
- Invitations to present, contribute, or advise that result from the content.

These signals indicate which topics resonate and should be developed further.

## Content Calendar Format

Create a 90-day rolling content calendar:

| Month | Topic | Pillar | Format | Channel | Target Audience | Status |
|---|---|---|---|---|---|---|
| {MMM-YYYY} | {specific topic title} | {pillar name} | {format} | {channel} | {audience} | 🔵 Planned / 🟡 In Draft / 🟢 Published |

**Planning principles:**

- Aim for one substantial piece (article or brown bag) per month plus two lighter pieces (Teams posts or newsletter snippets).
- Rotate across pillars — avoid becoming a one-topic voice.
- Align with the enterprise calendar: budget cycles, strategic planning, architecture forums, TechX.
- Leave room for opportunistic content — a timely post about a problem just solved is more valuable than a scheduled post about a stale topic.

## Brown Bag / Talk Abstract Template

Use this structure when proposing a brown bag session, lunch & learn, or forum presentation:

### {Title — action-oriented, specific}

**Elevator Pitch** (2 sentences — what attendees shall learn):

{What is the problem or question this talk addresses? What will attendees walk away with?}

**Key Takeaways:**

1. {First actionable insight attendees shall gain}
2. {Second actionable insight attendees shall gain}
3. {Third actionable insight attendees shall gain}

**Target Audience:** {Who should attend — role or function, not "everyone"}

**Duration:** {30 min / 45 min / 60 min}

**Prerequisites / Context:** {What should attendees know beforehand, if anything}

**Example:**

> **How Cortex Powers Credit Decisioning: Lessons from Replacing FICO**
>
> Learn how Westpac is building its own credit decisioning capability using ML, what worked, what didn't, and what other teams can apply. This session covers the end-to-end journey from FICO dependency to in-house model deployment.
>
> **Key Takeaways:**
> 1. Why building in-house ML models for credit decisioning reduces vendor lock-in and improves decision accuracy.
> 2. The governance framework required to deploy ML models in a regulated credit environment.
> 3. Three patterns for transitioning from legacy scoring systems without disrupting production.
>
> **Target Audience:** Data scientists, ML engineers, risk analysts, product managers in data.
> **Duration:** 45 minutes + 15 minutes Q&A.
> **Prerequisites:** General familiarity with credit risk concepts; no ML expertise required.

## Writing Principles for Thought Leadership

These principles shall guide all content produced by this skill:

1. **Teach, don't promote.** Share genuinely useful insight. The reader should learn something they can apply, not hear about how great Cortex is.

2. **Ground in evidence.** Reference real Cortex implementations, not hypothetical scenarios. "When we migrated 5M customer records to Snowflake, we learned..." is stronger than "organisations should consider cloud migration."

3. **Acknowledge challenges.** Leaders who admit what is hard are more credible than those who only share wins. "This approach failed in our first sprint because..." builds trust.

4. **Credit the team.** Thought leadership that names contributors builds broader goodwill and strengthens the Cortex brand beyond one person. "Sasi's team designed the pipeline that..." is better than omitting the team.

5. **Connect to enterprise strategy.** Every piece should link back to something leadership cares about — cloud migration, customer experience, operational efficiency, regulatory compliance. If it does not connect, it is an interesting blog post, not thought leadership.

6. **Be consistent.** One good post per month beats one brilliant post per year. Consistency builds recognition; sporadic brilliance builds nothing.

7. **Write for the scanner, not the reader.** Use headings, bullet points, bold text for key phrases. Most readers scan; reward them with structure.

8. **Close with a call to action.** Every piece should end with an invitation: "If your team faces a similar challenge, reach out" or "Join our brown bag on DD-MMM-YYYY to discuss further."

## Internal Article Template

Use this structure for Confluence articles, intranet posts, or longer-form written content:

### {Headline — insight-led, not topic-led}

> ✅ "What We Learned Migrating 5M Customer Records to Snowflake"
> ❌ "Snowflake Migration Update"

**Hook** (1 paragraph — why this matters to the reader):

{Open with the problem or question the reader cares about. Make it relevant to their work, not yours.}

**Key Insights:**

1. **{Insight heading}** — {2–3 sentences with evidence from Cortex implementation. Include a specific metric, date, or outcome where possible.}

2. **{Insight heading}** — {2–3 sentences with evidence. Reference the team member or squad responsible.}

3. **{Insight heading}** — {2–3 sentences with evidence. Acknowledge a challenge or trade-off.}

4. **{Insight heading}** (optional — 3–5 insights total)

5. **{Insight heading}** (optional)

**Reusable Takeaway:**

{What can other teams apply from this experience? Frame as a transferable principle, not a Cortex-specific detail.}

**Call to Action:**

{Invitation to connect: "If your team is exploring [topic], reach out — we are happy to share our approach and lessons learned." Or: "Join the [channel/event] for ongoing discussion."}

---

*{Author name} — Product Manager, Cortex Suite | {DD-MMM-YYYY}*

## Newsletter Snippet Template

Use for division or team newsletter contributions (2–3 short paragraphs):

**{Headline — active, specific}**

{1 paragraph: What happened or what we learned. Lead with the insight, not the project name.}

{1 paragraph: Why it matters — connect to something the newsletter audience cares about.}

{1 sentence: Call to action or link to the full article/Confluence page.}

## Teams Channel Post Template

Use for quick, consistent visibility posts in data community or Cortex channels:

**{One-line hook — question or insight}**

{2–3 sentences: Context and the key takeaway. Keep it conversational but professional.}

{Optional: Link to a Confluence article, brown bag recording, or related resource.}

{Optional: Tag 1–2 people who contributed or would find it relevant.}

## Quality Checklist

Before publishing any thought leadership content, verify:

- [ ] **Teaches something useful** — the reader learns at least one applicable insight
- [ ] **Grounded in evidence** — references real Cortex implementations, data, or outcomes
- [ ] **Credits the team** — names specific contributors where appropriate
- [ ] **Connects to enterprise strategy** — links to something leadership cares about
- [ ] **Appropriate for the channel** — length, tone, and depth match the publication venue
- [ ] **No self-promotion** — the content serves the reader, not the author's profile
- [ ] **Structured for scanning** — headings, bullets, bold key phrases
- [ ] **Call to action included** — the reader knows what to do next
- [ ] **Dates in DD-MMM-YYYY format** — all dates follow Westpac convention
- [ ] **No startup jargon** — no "disrupt", "pivot", "hustle", "move fast and break things"
- [ ] **Reviewed for sensitivity** — no proprietary data, customer information, or confidential strategy details exposed
- [ ] **Consistent with content calendar** — fits the planned cadence and pillar rotation

## Writing Style

- Use clear, professional language appropriate for banking and financial services.
- Avoid jargon from consumer technology or startup culture. No "disrupt", "pivot", "hustle", "move fast and break things."
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym thereafter.
- Use active voice. Name the actor: "Sasi's team built the pipeline" not "the pipeline was built."
- Keep sentences short. One idea per sentence. One topic per paragraph.
