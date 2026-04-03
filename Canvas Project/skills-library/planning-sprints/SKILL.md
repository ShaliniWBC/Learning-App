---
name: planning-sprints
description: "Generates sprint plans for Cortex Engineering, Customer Insights DS, and Project Hawkeye squads. Use when asked to plan a sprint, create sprint goals, or prepare sprint planning artefacts."
allowed-tools:
  - mcp__jira__jira_get_board
  - mcp__jira__jira_get_board_issues
  - mcp__jira__jira_get_sprints
  - mcp__jira__jira_get_issue
  - mcp__jira__jira_search_issues
  - mcp__jira__jira_get_transitions
  - Read
  - create_file
  - edit_file
  - task_list
---

# Sprint Planning Skill

Produces sprint plans in the PO's established format for three squads: **Cortex Engineering**, **Customer Insights DS**, and **Project Hawkeye**.

## Squads & JIRA Boards

| Squad | Board ID | Project Key |
|---|---|---|
| Cortex Engineering | 106106 | DME |
| Customer Insights DS | 106106 | DME |
| Project Hawkeye | 106133 | DME |

## Workflow

### Step 1 — Gather Sprint Context

1. Fetch active and future sprints from both boards:
   - Board 106106 (Cortex Engineering + Customer Insights DS)
   - Board 106133 (Project Hawkeye)
2. Identify the upcoming sprint number and date range.
3. Pull all issues in the active sprint to find carry-over candidates (anything not Done).

### Step 2 — Assess Carry-Over

1. List every issue from the current/previous sprint that is NOT in "Done" status.
2. For each, note: JIRA key, title, assignee, current status, and reason it didn't complete.
3. These populate the **Carry-Over Watch** section and inform the **Context Block**.

### Step 3 — Review Capacity

Ask the PO (or check provided info) for:
- Who is on leave during the sprint?
- Who is exiting the team or ramping down?
- Any new joiners or part-time allocations?
- Public holidays or blocked days?

Use this to build the **Resource Grid** per squad.

### Step 4 — Draft the Sprint Plan

Read the reference template at `reference/sprint-template.md` and fill in every section. The output MUST follow the exact structure below.

### Step 5 — Flag Risks & Exclusions

- Proactively identify cross-squad dependencies, external blockers, and capacity risks.
- Explicitly list items that were considered but NOT included, with reasons.

### Step 6 — Write the Plan

Save the completed plan as a markdown file named `Sprint-{N}-Plan.md` in the workspace root (or a location the PO specifies).

## Required Output Format

The sprint plan MUST contain these sections in this exact order:

### 1. Header
```
# Sprint {N} Plan
**Date Range:** {start} – {end}
**Squads:** Cortex Engineering · Customer Insights DS · Project Hawkeye
**Product Owner:** {PO name}
**Duration:** {X} weeks
**Theme:** "{theme in quotes}"
```

### 2. Context Block
A blockquote (`>`) explaining:
- What carried over from the previous sprint and why
- Strategic shifts, deadline changes, or timeline updates
- Why this sprint's theme was chosen
- Any external factors (stakeholder reviews, regulatory dates, etc.)

Example tone:
> Sprint 5 carries forward several items from Sprint 4 due to environment delays and scope clarification on the onboarding pipeline. The May 15 stakeholder demo is now confirmed, making UI polish non-negotiable this sprint. Theme reflects the need to close open threads, unblock downstream work, and prepare demo-ready artefacts.

### 3. Sprint Goals Table

| # | Goal | Squad | JIRA Tickets | What Needs to Be Completed | Why |
|---|------|-------|-------------|---------------------------|-----|
| G1 | **Bold initiative name** | Squad name | DME-XXXX, DME-YYYY | Detailed per-ticket breakdown with named assignees. E.g., "DME-1234: {Person A} completes API integration; DME-1235: {Person B} writes unit tests and updates Confluence." | Business justification |
| G2 | ... | ... | ... | ... | ... |

- Number goals G1 through G10 (adjust count as needed).
- Each goal's "What Needs to Be Completed" must name specific people and specific deliverables per JIRA ticket.
- Use **bold** for initiative/feature names in the Goal column.

### 4. Per-Squad Backlog Tables

Create one table per squad. Heading: `## {Squad Name} — Sprint Backlog`

| # | JIRA | Title | Assignee | Status at Sprint Start | Sprint Target | Why Included |
|---|------|-------|----------|----------------------|--------------|-------------|
| 1 | DME-XXXX | Title text | Person Name | In Progress / To Do / etc. | Done / In Review / etc. | Brief reason |

### 5. Per-Squad Resource Grids

One table per squad. Heading: `## {Squad Name} — Resource Allocation`

| Person | Primary Focus | Secondary Focus | Notes |
|--------|--------------|----------------|-------|
| Name | Initiative or ticket area | Secondary area | Leave dates, ramp-down, etc. |

### 6. Dependencies & Risks Table

| # | Dependency / Risk | Impact | Mitigation |
|---|------------------|--------|-----------|
| 1 | Description | What happens if unresolved | Action to reduce risk |

### 7. Sprint Success Criteria

| # | Criteria | Squad | Measure |
|---|---------|-------|---------|
| ✅ 1 | Specific outcome statement | Squad name | DME-XXXX = Done |
| ✅ 2 | ... | ... | ... |

### 8. Items NOT Included

| Item | Reason for Exclusion |
|------|---------------------|
| Feature or ticket description | Why it was deprioritised (capacity, dependency, lower priority, etc.) |

### 9. Carry-Over Watch

| JIRA | Title | Squad | Risk Level | Notes |
|------|-------|-------|-----------|-------|
| DME-XXXX | Title | Squad | High/Medium/Low | What might cause it to slip again |

## Conventions

- **JIRA keys** use the `DME-XXXX` format.
- **Bold** initiative/feature names in goal descriptions.
- **Name people explicitly** — never say "the team" when you can say "Alice and Bob".
- **Sprint theme** is always in quotes and appears in the header.
- **Context block** must reference concrete timeline updates, not generic statements.
- Maintain a professional, direct tone. No filler. Every sentence earns its place.
- When pulling JIRA data, fetch fields: `summary, status, assignee, priority, labels, sprint`.
- If JIRA data is incomplete (missing assignees, vague titles), flag it in the Dependencies & Risks table.

## JIRA Queries

Use these JQL patterns to gather data:

```
# Active sprint issues for board 106106
sprint in openSprints() AND project = DME AND board = 106106

# Carry-over candidates (not done in current sprint)
sprint in closedSprints() AND status != Done AND project = DME

# All issues for a specific sprint
sprint = {sprintId} AND project = DME
```

When using the `jira_get_board_issues` tool, pass `fields: ["summary", "status", "assignee", "priority", "labels", "sprint"]` to minimise payload.

## Quality Checklist

Before presenting the plan, verify:
- [ ] Every goal has named assignees and per-ticket deliverables
- [ ] Resource grids account for all known team members
- [ ] Carry-over items from previous sprint are addressed
- [ ] Dependencies & risks are specific, not generic
- [ ] "Not Included" section has at least 2-3 items (forces prioritisation thinking)
- [ ] Success criteria map to specific JIRA tickets
- [ ] No section is empty or contains placeholder text
