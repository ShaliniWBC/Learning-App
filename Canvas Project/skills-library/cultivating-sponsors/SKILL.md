---
name: cultivating-sponsors
description: "Maps influence networks and produces sponsor-enablement packs to expand Cortex visibility and career sponsorship. Use when building relationships with new leadership, preparing sponsor briefs for Jeni, or planning stakeholder cultivation across DDAI."
allowed-tools:
  - mcp__jira__jira_search_issues
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

# Cultivating Sponsors — Cortex Suite

Maps influence networks and produces sponsor-enablement packs to expand Cortex visibility and career sponsorship within Westpac Group DDAI.

## Context

Promotions into senior product leadership happen when someone is actively sponsored in rooms they are not in. This skill addresses two complementary objectives:

1. **Stakeholder Cultivation** — deliberately expanding Shalini Gangadharan's stakeholder network through value-led engagement with new leadership (Andrew McMullen, Vicki Wood, Rohith E) and strategic influencers across DDAI.
2. **Sponsor Enablement** — making it effortless for Jeni (direct manager) to advocate for Shalini by providing ready-made talking points, highlight packs, and "where Shalini should be in the room" recommendations.

Every interaction shall be framed around helping a stakeholder solve a problem — never around self-promotion. The value exchange is genuine: Cortex data, insights, and capabilities in return for sponsorship, visibility, and strategic context.

## Stakeholder Cultivation Map

The agent shall maintain and extend this map when performing cultivation analysis. Current Relationship tracks the present state; Target Relationship captures the 90-day aspiration.

| Name | Role | Current Relationship | Target Relationship | Value Exchange | Entry Path |
|---|---|---|---|---|---|
| Andrew McMullen | Group Exec DDAI | None | Engaged | Offer: Cortex impact metrics, enterprise data strategy input. Receive: strategic sponsorship, visibility at Group Exec level | Warm intro via Jeni or Lu Luc; Cortex quarterly review |
| Vicki Wood | GM DDAI | None | Engaged | Offer: Cortex roadmap alignment to GM priorities, consumer adoption data. Receive: endorsement in GM forums, initiative visibility | Warm intro via Jeni; shared initiative alignment |
| Rohith E | Head of Data DDAI | None | Engaged | Offer: Cortex data quality improvements, platform consumption insights. Receive: data strategy context, cross-team visibility | Shared data governance forum; intro via Jeni or Reza |
| Reza S | Chief AI Engineer | Aware | Champion | Offer: Cortex API consumption patterns, Hawkeye FICO capability. Receive: architectural advocacy, engineering credibility | Architecture forum; technical walkthrough invitation |
| Lu Luc | Head of AI Services | Engaged | Champion | Offer: Cortex delivery outcomes, team capability growth. Receive: active sponsorship in AI Services leadership | Existing reporting line; deepen with strategic briefings |
| Phil Hood | Exec Manager Data Science | Engaged | Champion | Offer: Hawkeye delivery progress, model operationalisation insights. Receive: advocacy in data science leadership | Existing Hawkeye collaboration; sponsor briefings |
| Carolyn McCann | Group Exec | Aware | Engaged | Offer: Cortex enterprise impact narrative, cross-BU adoption data. Receive: SteerCo-level visibility | SteerCo presentations; briefing paper via Jeni |
| Damian McRae | GM | Aware | Engaged | Offer: business outcome metrics, consumer adoption success stories. Receive: GM-forum endorsement | SteerCo alignment; initiative-specific briefing |
| Mandar Bhale | Architect | Engaged | Champion | Offer: Cortex architecture evolution, integration pattern insights. Receive: architectural endorsement, design authority credibility | Architecture review forums; technical deep-dives |
| Raja C | Architect | Engaged | Champion | Offer: data architecture patterns, platform standards alignment. Receive: design review advocacy | Architecture forums; shared design sessions |
| Lily Zhao | Strategy | Aware | Engaged | Offer: Cortex strategic positioning data, market alignment evidence. Receive: strategy forum visibility, portfolio context | Strategy forums; written brief via shared initiative |
| Jeni Jose Mannanal | Manager (Direct) | Engaged | Sponsor | Offer: sponsor enablement packs, ready-made talking points, reduced reporting effort. Receive: active advocacy in leadership forums | Existing 1:1; sponsor pack delivery |

### Relationship Categories

The agent shall classify each stakeholder into one of the following categories and track movement between them.

| Category | Definition | Current Names |
|---|---|---|
| Sponsors | Actively advocate in leadership forums where Shalini is not present | *Target: Jeni, Lu Luc* |
| Champions | Enthusiastic about Cortex, will recommend to peers and leadership | Reza S, Phil Hood, Mandar, Raja |
| Allies | Supportive when asked, provide operational assistance | Squad leads (Sasi, Tom, Peter, Kadeeja, GK) |
| Neutral | Aware of Cortex but not actively engaged | Lily Zhao, Carolyn McCann, Damian McRae |
| Unknown | No current relationship — require deliberate outreach | Andrew McMullen, Vicki Wood, Rohith E |
| Blockers | Resistant or creating impediments — identify and address | *None identified — monitor* |

## Cultivation Strategies

The agent shall recommend actions to move stakeholders up the relationship ladder. Each transition requires a specific approach.

### None → Aware

- Deliver a value-led introduction via a shared connection or relevant insight
- Send a brief written summary of Cortex capability relevant to their domain
- Secure a warm introduction through an existing Champion or Ally
- **Example:** "Jeni, could you introduce me to Rohith? Cortex has data quality metrics that align with his Data Strategy priorities."

### Aware → Engaged

- Solve a specific problem for them or their team using Cortex data or capabilities
- Invite them to a targeted Cortex demo aligned to their interests
- Provide an unsolicited insight that demonstrates platform value
- **Example:** "Rohith, we noticed [X pattern] in our data quality dashboard. This might be relevant to the Data Strategy review — happy to walk through the detail."

### Engaged → Champion

- Deliver measurable value they can reference in their own forums
- Share success stories from other Cortex consumers they respect
- Include them in roadmap discussions where their input shapes direction
- **Example:** "Reza, your input on the API design shaped the approach we shipped. The adoption numbers are [X]. Would you be open to referencing this in the architecture forum?"

### Champion → Sponsor

- Provide ready-made talking points about Cortex and Shalini's leadership
- Make their advocacy effortless through the Sponsor Enablement Pack
- Identify specific forums where they can advocate and brief them beforehand
- **Example:** Deliver a Sponsor Enablement Pack to Jeni before the DDAI Leadership Forum.

## Sponsor Enablement Pack

This is the primary output for enabling Jeni (and eventually other sponsors) to advocate effectively. The agent shall generate this pack monthly or before key leadership forums.

```markdown
# Cortex Sponsor Brief — {Month YYYY}
**Prepared for:** {Jeni Jose Mannanal / skip-level sponsor}
**Prepared by:** Shalini Gangadharan
**Date:** {DD-MMM-YYYY}

## Cortex Highlights This Period
- {Win 1: quantified impact — e.g., "Onboarded 3 new consumers, bringing total to X"}
- {Win 2: delivery milestone — e.g., "Delivered Hawkeye FICO replacement Phase 1 on schedule"}
- {Win 3: operational improvement — e.g., "Reduced API onboarding time from 6 weeks to 2 weeks"}
- {Win 4: strategic progress — e.g., "Completed AEP integration, enabling real-time personalisation"}

## Why This Matters for the Group
{2-3 sentences connecting Cortex progress to enterprise strategy. Reference DDAI objectives, Group Exec priorities, or regulatory requirements. Frame around business outcomes, not technical achievements.}

## Upcoming Opportunities
{Forums, reviews, or decisions where Cortex or Shalini should be represented}
- {Opportunity 1: "DDAI Quarterly Review — Cortex impact metrics would strengthen the data platform narrative"}
- {Opportunity 2: "Architecture Review Board — Cortex Mesh API evolution aligns with platform standardisation"}
- {Opportunity 3: "Customer Experience Forum — Cortex propensity scores driving personalisation outcomes"}

## Talking Points
{Ready-to-use statements Jeni can deploy in leadership discussions — no preparation required}
- "Cortex now serves X consumers across Y business units, up from Z last quarter..."
- "The team has reduced consumer onboarding time from X weeks to Y, which means..."
- "Shalini is driving the Hawkeye FICO replacement which will save the Group $X in licensing and..."
- "The Cortex roadmap directly supports the DDAI strategy around [enterprise objective]..."

## Where Shalini Should Be in the Room
{Specific forums framed as business need, not career need}
- "{Forum name}: Shalini can provide context on {topic} which is relevant because {business reason}"
- "{Forum name}: Cortex data is a key input to this decision — Shalini's presence would ensure accurate representation"
- "{Forum name}: The {initiative} discussion requires product ownership perspective on data platform implications"
```

## 90-Day Cultivation Plan

The agent shall generate a rolling 90-day plan focusing on 3-5 stakeholders per quarter. Depth over breadth — do not attempt to cultivate everyone simultaneously.

| Stakeholder | Current State | Target State | Action | By When (DD-MMM-YYYY) | Value Offered |
|---|---|---|---|---|---|
| {Name} | {None / Aware / Engaged / Champion} | {Target category} | {Specific action — e.g., "Secure warm intro via Jeni"} | {Date} | {What Cortex capability or insight is offered} |
| {Name} | | | | | |
| {Name} | | | | | |

### Quarterly Focus (Example)

**Q2 2026 — Priority Stakeholders:**

1. **Rohith E** (None → Engaged): Secure intro via Jeni, deliver data quality insight relevant to Data Strategy
2. **Andrew McMullen** (None → Aware): Brief Jeni with sponsor pack ahead of DDAI Quarterly Review
3. **Vicki Wood** (None → Aware): Provide Cortex consumer adoption summary aligned to GM priorities
4. **Reza S** (Aware → Champion): Invite to Cortex Mesh API architecture walkthrough
5. **Lu Luc** (Engaged → Champion): Deliver monthly sponsor pack, seek specific advocacy opportunities

## Conversation Starters

The agent shall recommend value-led conversation approaches tailored to each stakeholder category. Every approach opens with their needs, not Shalini's.

### For New Leadership (Andrew McMullen, Vicki Wood, Rohith E)

> "I lead the Cortex data platform that powers [specific capability — e.g., customer propensity scoring across Digital Banker and Unity]. I'd welcome 15 minutes to understand your priorities so we can align our roadmap to support them."

### For Architects (Mandar, Raja, Reza)

> "We're planning the next phase of [specific initiative — e.g., Cortex Mesh API evolution]. Your architectural perspective would be valuable — could we schedule a walkthrough so I can incorporate your guidance?"

### For Business Stakeholders (Lily Zhao, Damian McRae)

> "I noticed your team is working on [specific initiative]. Cortex has [specific capability — e.g., transaction categorisation data] that might accelerate that work — happy to share what worked for [similar team or use case]."

### For Data Science Leadership (Phil Hood)

> "The Hawkeye team has delivered [specific milestone]. I wanted to share the impact metrics and discuss how we can replicate this approach for [next initiative]."

### For Sponsor Enablement (Jeni)

> "I've prepared a brief for the upcoming [forum]. It includes talking points and the latest Cortex metrics — should save you preparation time. Happy to adjust if you'd like different emphasis."

### Approaches to Avoid

The agent **shall not** recommend any of the following:

- "I'd like to introduce myself and tell you about what I do" — this centres on Shalini, not the stakeholder
- "Can I get 30 minutes to pick your brain?" — vague, no value offered
- "I'd love your mentorship" — premature and presumptuous for new relationships
- Any framing that positions outreach as career advancement rather than business value

## Workflow

### Step 1: Assess Current State

The agent shall gather context before generating cultivation plans:

1. Review the Stakeholder Cultivation Map for current relationship states
2. Search Outlook calendar for upcoming meetings with target stakeholders
3. Search Outlook emails and Teams messages for recent interactions
4. Identify upcoming leadership forums, reviews, or decisions from calendar

### Step 2: Identify Cultivation Opportunities

For each priority stakeholder, the agent shall:

1. Identify a specific value exchange — what Cortex insight or capability is relevant to their current priorities
2. Determine the appropriate entry path — warm intro, shared initiative, forum, or direct outreach
3. Draft a value-led conversation starter tailored to the individual
4. Set a target date for initial engagement

### Step 3: Generate Sponsor Enablement Pack

When preparing a Sponsor Pack, the agent shall:

1. Search JIRA for recent Cortex delivery milestones and wins
2. Search Confluence for strategy documents to align Cortex narrative
3. Check calendar for upcoming forums where representation is relevant
4. Produce the pack using the template in the Sponsor Enablement Pack section
5. Save the pack to the specified output location

### Step 4: Update Cultivation Plan

After each engagement or monthly review, the agent shall:

1. Update relationship states in the Stakeholder Cultivation Map
2. Record commitments made to stakeholders in a commitment log
3. Refresh the 90-Day Cultivation Plan with revised actions and dates
4. Note any new stakeholders identified through the cultivation process

### Step 5: Track and Report

The agent shall maintain:

| Date (DD-MMM-YYYY) | Stakeholder | Interaction | Outcome | Next Action | Due (DD-MMM-YYYY) |
|---|---|---|---|---|---|
| | | | | | |

## Guardrails

The agent shall observe the following constraints:

1. **Value-first framing** — all outreach shall be framed around business value, never career advancement
2. **Sponsor pack is for Jeni** — it reduces her effort, it does not bypass her authority or reporting line
3. **Commitment tracking** — broken promises destroy credibility faster than anything. Track every commitment made to a stakeholder with an explicit due date and owner
4. **Depth over breadth** — do not cultivate more than 5 stakeholders actively at once. Deep relationships outperform wide networks
5. **Respect the hierarchy** — if Jeni is not advocating, the sponsor pack makes it easier. If she still does not, the expanded network provides alternative visibility paths — but never undermine the reporting relationship
6. **No self-promotion language** — every artefact shall be reviewed for language that centres on Shalini rather than on business value
7. **Patience** — relationship building takes quarters, not weeks. The agent should set realistic timelines

## How This Creates Visibility

The agent shall understand the underlying logic connecting cultivation activities to career visibility:

1. **Sponsor pack gives Jeni ready-made talking points** — she can advocate for Cortex and Shalini without preparing her own material
2. **"Where Shalini Should Be in the Room" plants the seed** — framed as business need, it creates natural inclusion in leadership forums
3. **Value-led stakeholder expansion creates touchpoints** — each new relationship with leadership is anchored to a genuine Cortex capability, not networking
4. **Champion network amplifies reach** — Champions (Reza, Phil, Mandar, Raja) naturally reference Cortex and Shalini in their own forums
5. **Accumulated evidence builds the case** — each sponsor pack builds a longitudinal record of impact that supports promotion discussions

## Conventions

1. The agent **shall** refer to stakeholders by name where known
2. All dates **shall** use DD-MMM-YYYY format (e.g., 28-Mar-2026)
3. The agent **shall** use professional banking language appropriate for Westpac Group
4. Sponsor packs **should** be generated monthly or before key leadership forums
5. The agent **shall** track commitments with explicit due dates and owners
6. The agent **should** cross-reference JIRA and Confluence for Cortex delivery context
7. The agent **shall not** use startup jargon, informal language, or colloquialisms
8. The agent **shall** distinguish between "shall" (mandatory) and "should" (recommended)
9. All artefacts **shall** be saved to the appropriate project directory
10. Conversation starters **shall** be tailored to the individual stakeholder — no generic templates

## Quality Checklist

Before delivering any cultivation plan, sponsor pack, or stakeholder analysis, the agent shall verify:

- [ ] All priority stakeholders have been identified and classified by relationship category
- [ ] Cultivation Map relationship states are current and justified
- [ ] 90-Day Plan focuses on 3-5 stakeholders maximum
- [ ] Sponsor Enablement Pack includes quantified highlights, not vague claims
- [ ] Talking points are ready-to-use — Jeni should not need to rewrite them
- [ ] "Where Shalini Should Be in the Room" entries are framed as business need
- [ ] Conversation starters open with the stakeholder's needs, not Shalini's
- [ ] No self-promotion language — every framing is value-led
- [ ] All dates use DD-MMM-YYYY format
- [ ] Commitments have explicit owners and due dates
- [ ] Language is professional and appropriate for Westpac Group
- [ ] No startup jargon or informal language
- [ ] Artefact has been saved to the specified location
