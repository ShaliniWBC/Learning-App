---
name: managing-stakeholders
description: "Mapping stakeholder landscapes and generating tailored communication plans for Cortex Suite initiatives. Use when preparing stakeholder briefs, planning engagement strategies, or building communication cadences for EDP001, EDP006, or Transcat."
allowed-tools:
  - mcp__jira__jira_get_issue
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

# Managing Stakeholders — Cortex Suite

Maps stakeholder landscapes and generates tailored communication plans for Cortex Suite products (Customer Cortex EDP001, Customer Interactions EDP006, Transcat) within Westpac Group.

## Context

The agent supports Shalini Gangadharan, Product Manager for Cortex Suite, who manages diverse stakeholders across technology, business, strategy, and architecture functions. The squad comprises approximately 15 people across 3 squads. Communication cadences include fortnightly manager updates, weekly Leadership Team (LT) updates, Hawkeye sponsor updates, and SteerCo presentations.

This skill shall produce stakeholder analyses, communication plans, meeting briefs, and engagement strategies that reflect Westpac's professional standards and enterprise governance expectations.

## Stakeholder Register

The following register captures known stakeholders. The agent shall reference and extend this register when performing stakeholder analysis.

| Name | Role | Influence | Interest | Communication Preference | Key Concerns | Cadence |
|---|---|---|---|---|---|---|
| Carolyn McCann | General Manager | High | High | Executive briefings, SteerCo | Strategic alignment, delivery milestones, risk | As required / SteerCo |
| Damian McRae | General Manager | High | High | Executive briefings, SteerCo | Business outcomes, investment returns, capacity | As required / SteerCo |
| Mandar | Architect | High | Medium | Technical forums, architecture reviews | Solution integrity, platform standards, non-functional requirements | Fortnightly / as required |
| Raja | Architect | High | Medium | Technical forums, design reviews | Data architecture, integration patterns, compliance | Fortnightly / as required |
| Lily Zhao | Strategy | High | Medium | Strategy forums, written briefs | Strategic roadmap alignment, market positioning, portfolio fit | Monthly / as required |
| Jeni | Manager (Direct) | High | High | 1:1 meetings, written updates | Team performance, delivery risk, resource allocation, escalations | Fortnightly |
| Peter | Senior Business Analyst | Low | High | Squad ceremonies, direct collaboration | Requirements clarity, scope definition, business rules | Weekly / as required |
| Kadeeja | Scrum Master | Low | High | Squad ceremonies, direct collaboration | Delivery cadence, impediments, team health | Weekly |
| Sasi | Lead Engineer | Low | High | Technical discussions, squad ceremonies | Technical feasibility, engineering capacity, technical debt | Weekly |
| Tom | Lead Data Scientist | Low | High | Technical discussions, squad ceremonies | Model performance, data quality, analytical rigour | Weekly |
| GK | Solution Designer | Medium | High | Design sessions, written briefs | Solution coherence, user experience, design standards | Weekly / as required |

## Influence/Interest Matrix

The agent shall classify stakeholders using the following 2×2 framework:

```
                        HIGH INTEREST                    LOW INTEREST
                ┌──────────────────────────┬──────────────────────────┐
HIGH            │   MANAGE CLOSELY         │   KEEP SATISFIED         │
INFLUENCE       │                          │                          │
                │   Carolyn McCann (GM)    │   Mandar (Architect)     │
                │   Damian McRae (GM)      │   Raja (Architect)       │
                │   Jeni (Manager)         │   Lily Zhao (Strategy)   │
                │                          │                          │
                │   → Regular engagement   │   → Targeted updates     │
                │   → Tailored messaging   │   → Escalation pathway   │
                │   → Early consultation   │   → Seek endorsement     │
                ├──────────────────────────┼──────────────────────────┤
LOW             │   KEEP INFORMED          │   MONITOR                │
INFLUENCE       │                          │                          │
                │   Peter (Sr BA)          │   (Identify as needed)   │
                │   Kadeeja (SM)           │                          │
                │   Sasi (Lead Eng)        │   → Minimal effort       │
                │   Tom (Lead DS)          │   → Standard comms       │
                │   GK (Solution Designer) │   → Watch for changes    │
                │                          │                          │
                │   → Regular updates      │                          │
                │   → Open channels        │                          │
                └──────────────────────────┴──────────────────────────┘
```

## Workflow

### Step 1: Identify Stakeholder Context

The agent shall gather the following before commencing analysis:

1. **Initiative** — which Cortex Suite product or initiative is involved (EDP001, EDP006, Transcat, cross-cutting)
2. **Decision or Change** — what decision is being sought, what change is being proposed, or what update is being communicated
3. **Impact Scope** — who is impacted by this decision or change (teams, functions, platforms)
4. **Timeframe** — when does this need to land, what are the key dates

The agent should search JIRA for relevant epics/stories and Confluence for related documentation to build context.

### Step 2: Map Stakeholders

For the identified initiative, the agent shall:

1. Plot each relevant stakeholder on the Influence/Interest Matrix
2. Classify each stakeholder as:
   - **Champion** — actively supports the initiative
   - **Blocker** — likely to resist or impede progress
   - **Neutral** — no strong position, may be influenced
3. Identify any stakeholders not in the register who should be added
4. Note any shifts in influence or interest from default positions

### Step 3: Analyse Concerns

For each stakeholder in the "Manage Closely" and "Keep Satisfied" quadrants, the agent shall document:

1. **What they care about** — their primary concerns and success criteria
2. **Likely objections** — what pushback should be anticipated
3. **Persuasion evidence** — what data, precedent, or framing would address their concerns
4. **Relationship history** — any prior commitments, decisions, or sensitivities to be aware of

The agent should search Outlook emails and Teams messages for recent communications with these stakeholders to inform the analysis.

### Step 4: Build Communication Plan

The agent shall produce a communication plan using the format below, tailored to each stakeholder segment:

- **Manage Closely** — personalised messaging, early consultation, regular touchpoints
- **Keep Satisfied** — targeted updates at key milestones, escalation pathway
- **Keep Informed** — regular squad-level updates, open channels for questions
- **Monitor** — standard communications only

### Step 5: Prepare Meeting Briefs

When preparing for a specific stakeholder meeting, the agent shall generate a brief containing:

1. **Meeting Context** — purpose, attendees, date, duration
2. **Attendee Profiles** — for each attendee, their role, what they care about, recent interactions
3. **Key Messages** — maximum 3 messages to land in the meeting
4. **Anticipated Questions** — likely questions with prepared responses
5. **Decision or Action Sought** — what outcome is desired from this meeting
6. **Follow-up Commitments** — what follow-ups should be expected or offered

The agent should check Outlook calendar for the meeting details and search prior emails/Teams messages for context.

### Step 6: Track Commitments

The agent shall maintain a commitment log:

| Date (DD-MMM-YYYY) | Commitment | Made By | Made To | Due Date (DD-MMM-YYYY) | Status | Follow-up Action |
|---|---|---|---|---|---|---|
| | | | | | Open / In Progress / Complete / Overdue | |

The agent should create or update a task list to track outstanding commitments.

## Communication Plan Format

| Stakeholder | Segment | Channel | Frequency | Key Message | Owner | Next Due (DD-MMM-YYYY) |
|---|---|---|---|---|---|---|
| Carolyn McCann | Manage Closely | SteerCo / Executive Brief | As required | [Tailored to initiative] | Shalini | |
| Damian McRae | Manage Closely | SteerCo / Executive Brief | As required | [Tailored to initiative] | Shalini | |
| Jeni | Manage Closely | 1:1 Update | Fortnightly | [Delivery progress, risks, decisions needed] | Shalini | |
| Mandar | Keep Satisfied | Architecture Review | Fortnightly | [Technical alignment, standards compliance] | Shalini | |
| Raja | Keep Satisfied | Design Review | Fortnightly | [Data architecture, integration approach] | Shalini | |
| Lily Zhao | Keep Satisfied | Strategy Brief | Monthly | [Strategic alignment, roadmap fit] | Shalini | |
| Squad Leads | Keep Informed | Weekly LT Update | Weekly | [Sprint progress, impediments, decisions] | Shalini | |

## Meeting Brief Format

```markdown
# Meeting Brief: [Meeting Title]
**Date:** [DD-MMM-YYYY]
**Duration:** [Time]
**Location/Channel:** [Teams / In-person / Hybrid]

## Objective
[Single sentence: what this meeting should achieve]

## Attendees
| Name | Role | What They Care About | Recent Context |
|---|---|---|---|
| | | | |

## Key Messages (Maximum 3)
1. [Primary message — the one thing they should remember]
2. [Supporting message — evidence or context]
3. [Forward-looking message — next steps or ask]

## Anticipated Questions & Prepared Responses
| Question | Prepared Response |
|---|---|
| | |

## Decision or Action Sought
[What specific decision, approval, or action is needed from this meeting]

## Follow-up Commitments
| Commitment | Owner | Due Date (DD-MMM-YYYY) |
|---|---|---|
| | | |
```

## Stakeholder Engagement Patterns

### Seeking Approval

When the initiative requires formal approval (e.g., SteerCo endorsement, architecture sign-off):

1. The agent shall identify the approver and their decision criteria
2. Pre-socialise the proposal with the approver before the formal forum
3. Frame the recommendation in terms the approver values (e.g., risk reduction for GMs, standards compliance for architects)
4. Prepare a clear decision paper with options, recommendation, and rationale
5. Anticipate objections and prepare mitigations

### Managing Resistance

When a stakeholder is likely to resist or block:

1. The agent shall identify the root cause of resistance (concern, misunderstanding, competing priority)
2. Seek to understand before seeking to persuade — document their perspective
3. Find common ground or shared objectives
4. Propose accommodations that address their concerns without compromising the initiative
5. If resistance persists, identify an escalation pathway through a shared authority

### Building Coalition

When broad support is needed across multiple stakeholders:

1. The agent shall identify early champions and secure their visible support
2. Build momentum by engaging neutral stakeholders with evidence of champion support
3. Frame the initiative in terms that resonate with each stakeholder segment
4. Create opportunities for stakeholders to contribute and take ownership
5. Communicate progress and wins to sustain engagement

### Escalating Blockers

When an impediment requires escalation:

1. The agent shall document the blocker factually: what is blocked, by whom, since when, impact
2. Identify the appropriate escalation authority (Jeni for operational, GMs for strategic)
3. Propose a resolution, not just the problem
4. Frame the escalation as seeking guidance, not assigning blame
5. Follow up with all parties after resolution

## Conventions

1. The agent **shall** refer to stakeholders by name where known
2. All dates **shall** use DD-MMM-YYYY format (e.g., 28-Mar-2026)
3. The agent **shall** use professional banking language appropriate for Westpac Group
4. Communication plans **should** align with existing cadences (fortnightly manager, weekly LT, SteerCo)
5. The agent **shall** track commitments with explicit due dates and owners
6. The agent **should** cross-reference JIRA and Confluence for initiative context
7. The agent **shall not** use startup jargon, informal language, or colloquialisms
8. Meeting briefs **should** be concise — no more than 2 pages equivalent
9. The agent **shall** distinguish between "shall" (mandatory) and "should" (recommended)
10. All artefacts **shall** be saved to the appropriate project directory

## Quality Checklist

Before delivering any stakeholder analysis or communication plan, the agent shall verify:

- [ ] All relevant stakeholders have been identified and classified
- [ ] Influence/Interest Matrix positions are justified
- [ ] Communication plan covers all "Manage Closely" and "Keep Satisfied" stakeholders
- [ ] Key messages are specific to the initiative (not generic)
- [ ] Meeting briefs include anticipated questions with prepared responses
- [ ] All dates use DD-MMM-YYYY format
- [ ] Commitments have explicit owners and due dates
- [ ] Language is professional and appropriate for Westpac Group
- [ ] No startup jargon or informal language
- [ ] Artefact has been saved to the specified location
