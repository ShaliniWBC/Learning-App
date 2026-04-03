---
name: writing-success-stories
description: "Transforms Cortex consumer implementations into structured internal case studies and reusable success narratives. Use when asked to write a case study, success story, quick win post, consumer win write-up, reusable pattern, or visibility artifact for leadership."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - mcp__outlook__outlook_search_emails
  - Read
  - create_file
  - edit_file
  - task_list
---

# Writing Success Stories — Cortex Suite

Transforms Cortex Suite consumer implementations into structured internal case studies and reusable success narratives for Westpac's Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat).

## Context

Every successful consumer onboarding is an untapped visibility asset. Case studies circulate naturally through leadership packs, internal forums, architecture reviews, and communities of practice. They shift the Product Manager from "operational PM" to "strategic product leader who creates repeatable growth playbooks."

Current Cortex consumers include Digital Banker, Unity, WLive, AEP (Adobe Experience Platform), and Salesforce (being decommissioned). Each implementation represents a distinct integration pattern, business outcome, and reusable lesson. Documenting these systematically creates a compounding library of proof that demonstrates platform value to leadership — particularly when new leaders have limited visibility of prior achievements.

Success stories are not self-promotion. They are teaching tools that help other teams replicate what worked, avoid what did not, and build confidence in the Cortex platform.

## Success Story Types

| Type | Length | Audience | Use |
|------|--------|----------|-----|
| 1-Page Case Study | 1 page (~500 words) | Leadership Team, GMs, architecture reviewers | LT packs, Confluence knowledge base, architecture reviews |
| 3-Slide Story | 3 slides (title + 2 content) | Broad audience, internal forums | Presentations, TechX-style events, community of practice |
| Quick Win Post | 3–5 paragraphs | Immediate network, teams | Teams channels, intranet posts, newsletters |
| Reusable Pattern | 1–2 pages, technical focus | Architects, other product teams | Architecture forums, integration playbooks, onboarding guides |

Select the format based on audience and distribution channel. A single consumer win may produce multiple formats — a 1-page case study for Confluence and a quick win post for Teams from the same source material.

## Workflow

### Step 1 — Select the Win

Identify which consumer implementation to document. Prioritise wins that score highly on these criteria:

| Criterion | Weight | Example |
|-----------|--------|---------|
| Recency | High | Completed within the last 1–2 sprints |
| Measurable Outcome | High | Quantifiable time savings, adoption numbers, error reduction |
| Strategic Relevance | Medium | Aligns with current LT priorities or roadmap themes |
| Leadership Connectivity | Medium | Involves a stakeholder connected to new leadership |
| Reusability | Medium | Pattern could be applied by other teams or consumers |

If multiple wins are available, prioritise the one with the strongest measurable outcome and broadest reusability.

### Step 2 — Gather Evidence

Pull supporting data from available sources:

- **JIRA**: Use `mcp__jira__jira_search_issues` to find delivery tickets for the consumer implementation. Filter by epic, label, or sprint. Use `mcp__jira__jira_get_issue` for individual ticket details (timeline, assignee, resolution).
- **Confluence**: Use `mcp__confluence__search_pages` to find design decisions, architecture records, or prior communications related to the implementation.
- **Consumer Feedback**: Search emails using `mcp__outlook__outlook_search_emails` for consumer feedback, thank-you messages, or outcome reports.
- **Outcome Metrics**: Identify quantifiable results — API call volumes, onboarding duration, error rates, time-to-market.
- **Timeline**: Establish key dates — when engagement started, key milestones, go-live date.

Compile evidence into a structured brief before drafting.

### Step 3 — Structure the Narrative

Every success story shall follow this narrative arc:

1. **Problem** — What challenge did the consumer face? What was the cost of inaction?
2. **Why Cortex** — Why was Cortex the right solution? What alternatives existed?
3. **Implementation** — How was it delivered? Key decisions, architecture, timeline.
4. **Outcome** — What was achieved? Quantified business impact.
5. **Reusable Pattern** — What can other teams learn from this?
6. **Where Else** — Which other teams or use cases could benefit from the same pattern?

This arc ensures every story is both a visibility artifact and a teaching tool.

### Step 4 — Quantify Impact

Outcomes shall be quantified wherever possible. Use specific numbers, not qualitative statements.

| Weak | Strong |
|------|--------|
| "Faster onboarding" | "Reduced onboarding time from 6 weeks to 2 weeks" |
| "Improved data quality" | "Increased match rate from 82% to 96%" |
| "Better customer insights" | "Enabled 14 new propensity models across 3 business lines" |
| "Saved time" | "Eliminated 40 hours/month of manual data reconciliation" |

Categories of impact to measure:

- **Time saved** — hours/days/weeks reduced in a process
- **Time-to-market** — how much faster a consumer went live vs previous integrations
- **Data quality** — match rates, accuracy, freshness improvements
- **Decisions enabled** — new models, campaigns, or products made possible
- **Cost avoided** — manual effort eliminated, infrastructure consolidated

If the `measuring-product-value` skill is available, use its attribution framework for rigorous impact quantification.

### Step 5 — Draft in Selected Format

Read the appropriate template from `reference/success-story-templates.md` and populate every section. Apply the Writing Principles below. Ensure no placeholder text remains in the final output.

### Step 6 — Identify Distribution

Determine who should see this story and through which channels. Use the Distribution Strategy table below to match format to channel and audience.

For each story, identify:

1. **Primary channel** — where it shall be published first
2. **Secondary channels** — where it should be cross-posted or adapted
3. **Named recipients** — specific people who should receive it (e.g., "include in Jeni's next 1:1 pack")
4. **Timing** — when to publish for maximum impact (e.g., before a leadership review, after a quarterly milestone)

## 1-Page Case Study Structure

The 1-page case study is the core format. All other formats derive from it.

### Header
- Title (action-oriented: "How Digital Banker Reduced Onboarding Time by 67% with Cortex")
- Consumer name
- Cortex product(s) used
- Date (DD-MMM-YYYY)
- Author

### The Challenge (2–3 sentences)
What problem the consumer faced. Frame in business terms, not technical terms. Include the cost of inaction — what happened if this problem was not solved.

### Why Cortex (2–3 sentences)
Why Cortex was the right solution. What alternatives existed and why they were insufficient. This section establishes Cortex's strategic positioning.

### The Implementation (1 paragraph)
Brief description of: timeline (start to go-live), key architectural decisions, team members involved, integration pattern used. Keep this concise — the audience cares about outcomes, not implementation minutiae.

### The Outcome (quantified)
Metrics, business impact, and consumer feedback. Use specific numbers. Include direct quotes from the consumer where available — their words carry more weight than the product team's.

### The Reusable Pattern (1 paragraph)
The key insight that makes this a teaching tool, not just a celebration. What did this implementation prove? What pattern emerged that other teams can adopt? This is the section that transforms a brag into a contribution.

### Where Else This Works (2–3 bullets)
Name 2–3 other teams, consumers, or use cases that could benefit from the same pattern. This signals growth thinking to leadership and opens doors for future engagement.

## Distribution Strategy

Where success stories create visibility:

| Channel | Audience | Format | Frequency | Notes |
|---------|----------|--------|-----------|-------|
| LT / GM Updates | Leadership Team, GMs | Embedded in status report | When available | Attach as appendix or inline key metrics |
| Confluence Knowledge Base | All teams | Full 1-page case study | After each win | Tag with `cortex-success-story` label |
| Architecture Forums | Architects, tech leads | Reusable pattern | Quarterly | Focus on integration pattern and architecture decisions |
| TechX / Internal Conferences | Broad audience | 3-slide story | Annually | Submit to call for presentations |
| Teams Channels | Immediate network | Quick win post | Within 1 week of win | Post in relevant product and team channels |
| Manager 1:1 Pack | Jeni (manager) | Case study + "where else" section | Fortnightly | Include in regular manager update materials |
| Stakeholder Comms | Named stakeholders | Tailored excerpt | As relevant | Reference in stakeholder update emails |

## Writing Principles for Success Stories

1. **Lead with the consumer's problem, not Cortex's capabilities.** The reader shall understand the pain before the solution. "Digital Banker needed real-time customer risk scores but was waiting 48 hours for batch updates" — not "Cortex provides real-time API access to customer data."

2. **Quantify outcomes.** "Reduced onboarding time from 6 weeks to 2 weeks" — not "faster onboarding." Every outcome statement shall include at least one number.

3. **Name people.** Credit the team members who delivered. "Sasi designed the integration architecture; Cooper built the API connector" — not "the team delivered the integration." This builds individual visibility and team morale.

4. **Include the reusable pattern.** This is what makes the story a teaching tool, not self-promotion. "This proved that Cortex Mesh APIs can serve real-time use cases with sub-200ms latency — a pattern any consumer with real-time requirements can adopt."

5. **End with "where else."** This signals growth thinking to leadership. "The same pattern could serve the National Proactive Engagement team, who face a similar real-time scoring requirement."

6. **Keep the consumer's voice central.** Direct quotes from the consumer carry more weight than internal claims. "As Ben Choy noted: 'Cortex cut our integration timeline in half.'"

7. **Use professional banking language.** No startup jargon. No "disrupt", "pivot", "hustle." Use "shall" for mandatory, "should" for recommended, "may" for optional. All dates in DD-MMM-YYYY format.

8. **Write for the sceptical reader.** Assume the reader has not heard of Cortex. Provide enough context that the story is self-contained.

## Quality Checklist

Before presenting any success story, verify:

- [ ] Story follows the Problem → Why Cortex → Implementation → Outcome → Reusable Pattern → Where Else arc
- [ ] Outcomes are quantified with specific numbers (not qualitative statements)
- [ ] Consumer's problem is stated before Cortex's solution
- [ ] Team members are named and credited
- [ ] Reusable pattern section is present and substantive
- [ ] "Where else" section names specific teams or use cases
- [ ] Consumer's voice is included (direct quotes where available)
- [ ] All dates are in DD-MMM-YYYY format
- [ ] JIRA references use `DME-XXXX` format where applicable
- [ ] No placeholder text remains in the output
- [ ] Tone is professional banking language — no startup jargon
- [ ] "Shall" / "should" / "may" used correctly for requirement levels
- [ ] Story is self-contained — a reader unfamiliar with Cortex can follow it
- [ ] Distribution channels are identified for the completed story
- [ ] Format matches the intended audience and channel
