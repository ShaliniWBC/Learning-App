---
name: drafting-comms
description: "Drafts internal communications for Cortex Suite including announcements, release notes, change notifications, stakeholder updates, and escalation emails. Use when asked to write a communication, draft an email, prepare release notes, or compose a team announcement."
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

# Drafting Communications for Cortex Suite

Drafts internal communications for Westpac's Cortex Suite of Enterprise Data Products (Customer Cortex EDP001, Customer Interactions EDP006, Transaction Categorisation/Transcat).

## Context

Enterprise banking communications must be clear, professional, and appropriately targeted. Different audiences require different levels of detail and framing. A release note for downstream API consumers demands technical precision; a stakeholder update for a General Manager demands brevity and outcome focus.

You are assisting a Product Manager who leads the Cortex Suite within Westpac Group's Enterprise Data & Analytics function. Key stakeholders include:

- **General Managers**: Carolyn McCann, Damian McRae
- **Architects**: Mandar, Raja
- **Strategy**: Lily Zhao
- **Manager**: Jeni
- **Downstream consumers**: Digital Banker, Unity, WLive, AEP (Adobe Experience Platform)

Communications are distributed via email, Microsoft Teams, Confluence, and formal documents.

## Communication Types

| Type | Purpose | Audience | Channel | Tone | Length |
|------|---------|----------|---------|------|--------|
| Release Notes | Inform consumers of data product changes | Downstream teams | Confluence / email | Factual, technical | 1–2 pages |
| Change Notification | Advance notice of breaking or significant changes | Downstream teams, architects | Email | Formal, clear action required | 1 page |
| Team Announcement | Internal squad updates (new joiners, exits, structure changes) | Squads, manager | Teams / email | Warm, professional | 3–5 paragraphs |
| Stakeholder Update | Progress or status for specific stakeholders | GMs, sponsors | Email | Concise, outcome-focused | 5–10 bullet points |
| Escalation Email | Raising a blocker or risk to leadership | Manager, GM | Email | Factual, urgent, solution-oriented | 1 page |
| Celebration / Recognition | Acknowledging team achievements | Squads, leadership | Teams | Positive, specific | 2–3 paragraphs |

## Workflow

### Step 1 — Determine Communication Type

Before drafting, establish:

1. **What** needs to be communicated?
2. **To whom** is it directed? (Name specific people or groups.)
3. **By when** must it be sent?
4. **Via what channel** — email, Teams, Confluence, formal document?
5. **What tone** is appropriate for this audience and purpose?

If the user has not specified these, ask before proceeding.

### Step 2 — Gather Content

Pull supporting information as needed:

- **JIRA**: Use `mcp__jira__jira_get_issue` to pull ticket details (summary, status, assignee, resolution). Use `mcp__jira__jira_search_issues` to find related tickets by epic, sprint, or label.
- **Confluence**: Use `mcp__confluence__search_pages` to find existing documentation, architecture decisions, or prior communications. Use `mcp__confluence__get_page` to read page content.
- **Workspace files**: Use `Read` to review any local documents, data dictionaries, or previous drafts.

### Step 3 — Draft

Use the appropriate template from `reference/comms-templates.md` and apply the tone guidance from the Tone Guide section below. Adapt length and depth to the communication type.

### Step 4 — Review

Before presenting the draft, verify:

1. **Tone** — Is it calibrated for this audience? (See Tone Guide.)
2. **Facts** — Are JIRA references, dates, and version numbers accurate?
3. **Action items** — Are they explicit? Does the reader know what to do and by when?
4. **Audience appropriateness** — Does the level of detail match the recipient?
5. **BLUF** — Does the first sentence convey the key message?

## Writing Principles by Communication Type

### Release Notes

- Lead with **what changed**, then **what you need to do**, then **technical details**.
- Include product name, version number, date (DD-MMM-YYYY format), and JIRA references.
- Highlight breaking changes with ⚠️ and place them before enhancements.
- Use bullet points, not paragraphs. Consumers scan release notes; they do not read them end-to-end.

### Change Notifications

- Lead with **what is changing** and **when**.
- Then **impact on you** — what breaks, what degrades, what requires migration.
- Then **what you need to do by when** — specific actions with deadlines.
- Include rollback plan if applicable.
- State a contact for questions.

### Escalation Emails

- Lead with **the issue** — one sentence, factual.
- Then **impact if unresolved** — quantify where possible (days of delay, cost, downstream systems affected).
- Then **what I need from you** — specific ask, specific person.
- Then **proposed resolution** — never escalate a problem without proposing a solution.
- Keep to one page. Attach supporting detail; do not inline it.

### Stakeholder Updates

- Lead with **outcomes and wins** — what shipped, what was delivered, what moved forward.
- Then **risks and blockers** — only those requiring awareness or action.
- Then **upcoming milestones** — next 1–2 sprint horizons.
- Keep to bullet points. Five to ten, no more.
- Attach detailed sprint reports or Confluence links; do not inline the detail.

### Team Announcements

- Lead with the **news** — who is joining, who is leaving, what is changing.
- Provide context — why this change is happening, what it means for the team.
- Close with **what happens next** — transition timelines, handover plans, welcome actions.
- Use a warm but professional tone. Name people. Be specific about dates.

### Celebration / Recognition

- Name the **people** and the **specific achievement**.
- Quantify the impact where possible (e.g., "reduced pipeline runtime by 40%").
- Connect the achievement to a broader goal or milestone.
- Keep it genuine — no corporate boilerplate.

## Email Structure Patterns

### BLUF (Bottom Line Up Front)

State the key message in the **first sentence**. The reader should know the purpose of the email before scrolling.

> **Example**: "Customer Cortex v2.4 will introduce a breaking change to the Customer Segments API on 15-Apr-2026. All consumers must migrate by 01-May-2026."

### Action Required

Clearly state **who** needs to do **what** by **when**. Use bold or a callout block for the action.

> **Action Required**: [Team/Person] — [specific action] by [DD-MMM-YYYY].

### FYI / No Action

Explicitly state when no action is required to prevent unnecessary follow-up.

> "No action required — for awareness only."

## Release Notes Format

Every release note shall follow this structure:

```
# [Product Name] — Release Notes v[X.Y]

| Field | Value |
|-------|-------|
| **Product** | [Customer Cortex / Customer Interactions / Transcat] |
| **Version** | [X.Y] |
| **Release Date** | [DD-MMM-YYYY] |
| **Author** | [Name] |

## Summary of Changes
- Bullet point summary of all changes in this release.

## ⚠️ Breaking Changes
- Description of breaking change, impact, and required consumer action.
- [If none: "No breaking changes in this release."]

## New Features / Enhancements
- Feature description and benefit.

## Bug Fixes
- Description of fix and JIRA reference.

## Known Issues
- Description and workaround if available.
- [If none: "No known issues."]

## Migration / Action Required by Consumers
- Step-by-step actions consumers must take, with deadlines.
- [If none: "No consumer action required."]

## JIRA References
| JIRA Key | Summary | Type |
|----------|---------|------|
| DME-XXXX | Title | Enhancement / Bug Fix / etc. |
```

## Tone Guide

| Audience | Tone | Do | Don't |
|----------|------|-----|-------|
| GM / Leadership Team | Concise, outcome-focused, quantified | Lead with impact and business outcomes | Include technical implementation details |
| Architects (Mandar, Raja) | Precise, technical, specific | Reference architecture decisions and system names | Omit technical rationale or glossary context |
| Squad members | Direct, collaborative, action-oriented | Name people and specific deliverables | Use passive voice or vague ownership |
| Downstream consumers | Clear, actionable, empathetic | Give clear timelines, actions, and contact points | Assume they know Cortex internals or acronyms |

## Writing Style Conventions

- Use clear, professional language appropriate for banking and financial services.
- No startup jargon. No "disrupt", "pivot", "hustle", "move fast and break things".
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Reference systems by their full name on first use with acronym in parentheses, then use the acronym.
- All dates in DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use active voice. Name the actor: "Mandar shall review the schema" not "the schema will be reviewed".
- Keep sentences short. One idea per sentence. One topic per paragraph.

## Quality Checklist

Before presenting any drafted communication, verify:

- [ ] First sentence conveys the key message (BLUF)
- [ ] Tone matches the target audience (see Tone Guide)
- [ ] All dates are in DD-MMM-YYYY format
- [ ] JIRA references are accurate and formatted as `DME-XXXX`
- [ ] Action items specify who, what, and by when
- [ ] No startup jargon or informal language
- [ ] Breaking changes (if any) are highlighted with ⚠️
- [ ] Communication length matches the type guidance
- [ ] Contact point is provided for questions (where applicable)
- [ ] "Shall" / "should" / "may" used correctly for requirement levels
- [ ] No placeholder text remains in the output
