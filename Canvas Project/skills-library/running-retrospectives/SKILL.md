---
name: running-retrospectives
description: "Produces retrospective facilitation guides and synthesises improvement trends across Cortex squads. Use when preparing for, facilitating, or analysing sprint retrospectives."
allowed-tools:
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_board_issues
  - mcp__jira__jira_get_sprints
  - mcp__confluence__search_pages
  - mcp__confluence__get_page
  - Read
  - create_file
  - edit_file
  - task_list
---

# Running Retrospectives

Produces retrospective facilitation guides and synthesises improvement trends across Cortex Suite squads.

## Context

The Cortex Suite programme comprises three squads with distinct dynamics:

| Squad | Focus | Lead | Key Considerations |
|-------|-------|------|--------------------|
| Cortex Engineering | Platform build and delivery | Sasi (Lead Engineer) | Grad developers (Josh, Jolin) require structured feedback; Cooper exits after Sprint 6 |
| Customer Insights DS | Data science and analytics | Tom (Lead DS) | Part-time capacity (Vinoth); cross-functional with analysts (Jack, GK) |
| Project Hawkeye | Strategic initiative | — | Stakeholder-heavy; BA-driven (Peter Sr BA) |

**Programme context:**
- Product Manager: Shalini Gangadharan
- Scrum Master: Kadeeja (primary facilitator)
- JIRA project: DME, boards 106106 and 106133
- Sprint-based cadence with continuous improvement focus
- Squad members: Sasi, Cooper, Josh, Jolin, Jack, GK, Tom, Rupa, Simran, Justin, Vivasha, Claudia, Richard, Peter, Vinoth

## Retrospective Formats

The agent shall select a format based on sprint events, team energy, and available time.

| Format | Best For | Duration | Description |
|--------|----------|----------|-------------|
| Start/Stop/Continue | Standard sprint retro; general reflection | 45 min | Three columns: what to begin doing, what to cease, what to maintain. Simple and familiar. |
| 4Ls (Liked/Learned/Lacked/Longed For) | Deeper reflection; after significant change | 60 min | Four quadrants encouraging both positive reflection and gap identification. |
| Sailboat (Wind/Anchor/Rocks/Island) | Visual metaphor; identifying forces for and against progress | 60 min | Wind = what propels us, Anchor = what holds us back, Rocks = risks ahead, Island = our goal. |
| Timeline | After major incidents or long sprints | 75 min | Chronological walkthrough of sprint events, capturing emotions and decisions at each point. |
| Confidence Vote | Quick pulse check; mid-sprint health check | 15 min | Anonymous 1–5 vote on team confidence, followed by brief discussion of outliers. |

### Format Selection Guide

The agent shall recommend a format using these criteria:

- **Standard sprint, no major events** → Start/Stop/Continue
- **Team has new members or significant change** → 4Ls
- **Progress feels blocked or slow** → Sailboat
- **Production incident or complex sprint** → Timeline
- **Time-constrained or between sprints** → Confidence Vote
- **Same format used 3+ consecutive sprints** → Rotate to a different format

## Workflow

### Step 1: Gather Sprint Data

The agent shall pull the following from JIRA (DME project, boards 106106 and 106133):

1. Current sprint details via `jira_get_sprints` (boardId 106106 or 106133, state: active)
2. Sprint issues via `jira_get_board_issues` with JQL filter for the sprint
3. Calculate:
   - Planned story points vs completed story points
   - Carry-over count (issues not completed)
   - Blocker count (issues with blocker priority or flagged)
   - Scope changes (issues added after sprint start)

### Step 2: Review Prior Actions

The agent shall search Confluence for the previous retrospective record:

1. Search via `confluence_search_pages` with query: "Cortex retro" or "retrospective Sprint [N-1]"
2. Retrieve the page via `confluence_get_page`
3. Extract action items and their current status
4. Flag any overdue or incomplete actions for discussion

### Step 3: Select Format

The agent shall recommend a format based on:

- Sprint events identified in Step 1 (incidents, scope changes, blockers)
- Prior retro format (avoid repeating the same format more than twice consecutively)
- Available time slot
- Team energy indicators (high carry-over or blocker count may suggest lower energy)

The agent should present the recommendation with rationale and allow the facilitator to override.

### Step 4: Prepare Facilitation Guide

The agent shall produce a structured facilitation guide following the format defined in the Facilitation Guide Format section below. The guide shall include:

- Pre-populated sprint data from Step 1
- Prior action items with status from Step 2
- Time-boxed agenda for the selected retro format
- Facilitator prompts tailored to the squad context
- Data points to share during the session

### Step 5: Synthesise Outcomes

After the retrospective, the agent shall capture:

1. **Themes** — recurring topics grouped by category
2. **Action Items** — each with owner, due date, and category
3. **Sentiment** — overall team sentiment (positive / mixed / concerning)
4. **Patterns** — connections to prior retro themes

The agent shall produce the output using the Action Items table format defined below.

### Step 6: Track Trends

The agent shall compare themes across the last 3–5 retrospectives:

1. Retrieve prior retro pages from Confluence
2. Build a Trend Analysis table (format defined below)
3. Flag recurring issues (same theme appearing 3+ sprints)
4. Highlight improvement trajectories (issues that have been resolved)
5. Recommend focus areas for the next sprint

## Facilitation Guide Format

The facilitation guide is the primary output. The agent shall structure it as follows:

### Header

```
## Sprint [N] Retrospective — [Squad Name]
**Date:** DD-MMM-YYYY
**Facilitator:** [Name]
**Attendees:** [Names]
**Format:** [Selected format]
**Duration:** [XX] minutes
```

### Sprint Snapshot

| Metric | Value |
|--------|-------|
| Planned Story Points | [X] |
| Completed Story Points | [X] |
| Completion Rate | [X%] |
| Carry-over Items | [X] |
| Blockers Resolved | [X] |
| Scope Changes | [X] |

### Prior Actions Review

| # | Action | Owner | Status | Notes |
|---|--------|-------|--------|-------|
| 1 | [Action from prior retro] | [Name] | Done / In Progress / Not Started | [Context] |

### Retro Activity

The agent shall provide a time-boxed agenda for the selected format. Example for Start/Stop/Continue (45 min):

| Time | Activity | Facilitator Prompt |
|------|----------|--------------------|
| 0–5 min | Welcome and ground rules | "This is a safe space. We focus on process, not people." |
| 5–10 min | Share sprint snapshot | Present the Sprint Snapshot data above |
| 10–15 min | Review prior actions | Walk through the Prior Actions Review table |
| 15–30 min | Individual reflection and grouping | "Write items on sticky notes for Start, Stop, and Continue. One idea per note." |
| 30–40 min | Discussion and dot voting | "Let us discuss the top-voted items. What patterns do we see?" |
| 40–45 min | Agree action items | "For each theme, who shall own the action and by when?" |

### Action Items

| # | Action | Owner | Due Date | Category |
|---|--------|-------|----------|----------|
| 1 | [Specific, measurable action] | [Name] | DD-MMM-YYYY | [Category] |

### Parking Lot

Items raised but deferred for later discussion:

| # | Item | Raised By | Follow-up Forum |
|---|------|-----------|-----------------|
| 1 | [Item] | [Name] | [Where to discuss] |

## Sprint Health Metrics

The agent shall gather and present the following data points:

### Velocity and Completion

- **Planned vs completed story points** — indicates estimation accuracy
- **Completion rate percentage** — target should be above 80%
- **Velocity trend** — comparison with previous 3 sprints

### Carry-over Analysis

- **Carry-over count** — number of items not completed
- **Carry-over reasons** — categorised as: scope creep, blocked, underestimated, capacity, dependency
- **Repeat carry-overs** — items carried over 2+ sprints (shall be flagged)

### Blocker Analysis

- **Blocker count** — total blockers raised during sprint
- **Average resolution time** — mean time from blocker raised to resolved
- **Blocker categories** — technical, dependency, access, decision, capacity

### Sprint Integrity

- **Scope changes** — items added or removed after sprint start
- **Scope change ratio** — percentage of final scope that was not in the original plan
- **Team member utilisation** — planned vs actual availability (relevant for Vinoth part-time, Cooper exit)

## Action Item Categories

The agent shall categorise each action item using one of the following:

| Category | Description | Examples |
|----------|-------------|---------|
| Process | Sprint ceremonies, ways of working, workflow | Refine estimation approach, adjust standup format |
| Technical | Code quality, architecture, tech debt | Address test coverage gap, resolve CI pipeline issue |
| Communication | Information flow, stakeholder updates, documentation | Improve handoff notes, establish decision log |
| Tooling | JIRA configuration, CI/CD, development environment | Update board filters, automate deployment step |
| Capacity | Team availability, workload balance, onboarding | Cross-train on module X, adjust sprint load for part-time members |
| Culture | Team dynamics, psychological safety, recognition | Celebrate sprint achievements, establish pair programming schedule |

## Trend Analysis Format

The agent shall produce a trend analysis table comparing across retrospectives:

| Sprint | Date | Format Used | Top Theme | Action Count | Actions Completed | Completion Rate | Recurring Issues |
|--------|------|-------------|-----------|--------------|-------------------|-----------------|------------------|
| Sprint N | DD-MMM-YYYY | Start/Stop/Continue | [Theme] | [X] | [Y] | [Y/X %] | [Issues seen before] |
| Sprint N-1 | DD-MMM-YYYY | 4Ls | [Theme] | [X] | [Y] | [Y/X %] | [Issues seen before] |

### Trend Indicators

The agent shall flag the following patterns:

- **Improving** — action completion rate trending upward over 3+ sprints
- **Stagnant** — same theme appearing with no measurable improvement
- **Deteriorating** — metric worsening over 2+ sprints
- **Resolved** — previously recurring issue no longer appearing

## Anti-patterns to Flag

The agent shall identify and raise the following anti-patterns:

1. **Retros without action items** — every retrospective should produce at least one concrete action
2. **Recurring issues (3+ sprints)** — if the same theme appears three or more sprints in a row, the agent shall recommend escalation or a dedicated improvement spike
3. **No data backing observations** — the agent should encourage data-driven discussion by presenting sprint metrics
4. **Blame-focused language** — the agent shall frame all prompts around process and systems, not individuals
5. **Action items without owners** — every action shall have a named owner and due date
6. **Action items without follow-up** — prior actions should be reviewed at the start of each retro
7. **Skipped retrospectives** — the agent shall flag if no retro record exists for a sprint
8. **Same format fatigue** — using the same retro format more than three consecutive times

## Quality Checklist

Before delivering a facilitation guide, the agent shall verify:

- [ ] Sprint data has been retrieved from JIRA and is current
- [ ] Prior retro actions have been reviewed and status updated
- [ ] Selected format is appropriate for the sprint context
- [ ] All time boxes in the agenda sum to the total duration
- [ ] Facilitator prompts are neutral, process-focused, and inclusive
- [ ] Sprint snapshot contains all six metrics
- [ ] Prior actions table is populated (or noted as first retro)
- [ ] Action items template includes owner and due date columns
- [ ] Parking lot section is included
- [ ] Date format uses DD-MMM-YYYY throughout
- [ ] Language is professional and appropriate for banking context
- [ ] No startup jargon or informal terminology
- [ ] Output file is saved with naming convention: `retro-sprint-[N]-[squad]-DD-MMM-YYYY.md`
