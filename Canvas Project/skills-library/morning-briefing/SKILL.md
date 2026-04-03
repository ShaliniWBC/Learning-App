---
name: morning-briefing
description: "Generates a structured morning briefing for the Cortex Suite PM by pulling live data from JIRA, Outlook, Teams, and Confluence. Use when asked for morning briefing, daily standup prep, or sprint health check."
---

# Morning Briefing

Generates a personalised morning briefing for the Cortex Suite Product Manager across 3 squads: Engineering, Data Science, and Project Hawkeye.

## Data Sources & Tools

Pull data from all four sources **in parallel** before assembling the briefing:

### 1. JIRA — Sprint & Backlog Health
- **Cortex board (Engineering + Data Science):** Board ID `106106`
- **Hawkeye board:** Board ID `106133`

Calls to make:
```
mcp__jira__jira_get_board_issues(boardId=106106, maxResults=50)
mcp__jira__jira_get_board_issues(boardId=106133, maxResults=50)
mcp__jira__jira_search_issues(jql="board in (106106,106133) AND status changed TO Blocked AFTER -1d", maxResults=20)
```

If the board-level JQL fails, fall back to project-level queries:
```
mcp__jira__jira_search_issues(jql="project in (CORTEX, HAWKEYE) AND sprint in openSprints() AND status = Blocked", maxResults=20)
```

Extract from results:
- Total stories in sprint, completed, in progress, blocked, to do
- Any items with no assignee
- Items that haven't moved status in ≥3 business days ("stalled")
- Items added after sprint start ("scope creep")
- Blockers with details (assignee, blocker reason if in comments)

### 2. Outlook Calendar — Today's Meetings
```
mcp__outlook__outlook_get_calendar_events(startDate="<today>", endDate="<today>")
```

Extract:
- Meeting subject, time, organizer, attendees
- Flag meetings that need prep (contains "review", "demo", "showcase", "steering", "stakeholder", "exec")
- Flag back-to-back meetings (gap < 15 min)
- Flag meetings with external attendees

### 3. Teams Messages — Overnight Comms
```
mcp__outlook__teams_search_messages(query="cortex", maxResults=20)
mcp__outlook__teams_search_messages(query="hawkeye", maxResults=20)
```

Extract:
- Messages from the last 18 hours
- Anything flagged as urgent or containing "blocker", "blocked", "escalat", "risk", "decision needed"
- Direct mentions or requests requiring response

### 4. Outlook Email — Key Threads
```
mcp__outlook__outlook_search_emails(query="cortex OR hawkeye", maxResults=15)
```

Extract:
- Emails from last 18 hours
- Emails from stakeholders, leadership, or containing "urgent", "action required", "deadline"

### 5. Confluence — Recent Updates (Optional)
Only run if today is Monday or if a reporting deadline is this week:
```
mcp__confluence__search_pages(query="cortex sprint review OR hawkeye status", limit=5)
```

## Sprint Health Score

Calculate a score for each board separately using this formula:

```
Base Score: 100

Deductions:
  -10  per active blocker
  -5   per scope creep story (added after sprint start)
  -3   per unassigned story in the sprint
  -5   per stalled story (no status change in ≥3 business days)

Sprint Health = max(0, 100 - total_deductions)

Rating:
  85-100  → 🟢 Healthy
  70-84   → 🟡 At Risk
  0-69    → 🔴 Unhealthy
```

Show the breakdown: `Score: 75 🟡 (100 - 10 blocker - 5 scope - 5 stalled - 5 scope)`

## People Watch List

When any of these people appear in JIRA items, meetings, or messages, add context:

| Person    | Watch Reason | What to Look For |
|-----------|-------------|-------------------|
| **Peter** | Coaching — redirect from governance to outputs | Is he stuck in process? Flag if his items are governance-heavy with no delivery output |
| **Cooper** | Shared allocation — may slip | Check if his items are progressing. Flag if stalled or reassigned |
| **Justin** | Sole EDB contributor — SPOF risk | Flag any blocker on his items immediately. If he's on leave, escalate |
| **Rupa** | Leave cover | Check if her items have a cover assignee. Flag orphaned work |
| **Sasi** | Engineering decisions | Flag any architectural or tech decision pending his input |
| **Jack** | AEP progress | Check AEP-related stories for movement. Flag if stuck |
| **GK** | Architecture inputs | Flag items waiting on his review or architecture sign-off |
| **Kadeeja** | Sprint ceremonies | Check if retro/planning/review are scheduled this week |

When a watched person appears in the briefing, append their watch context in parentheses.

## Output Format

### Emoji Key
- 🔴 **Action Required** — you must act today
- 🟡 **Watch** — monitor, may need action soon
- 🟢 **FYI** — awareness only, no action needed

### Output Modes

The user will request one of two modes. Default to **Checklist Mode** unless told otherwise.

---

#### MODE 1: Checklist Mode (default)

Concise, data-driven, scannable. Every line is actionable or informational. No prose.

```markdown
# ☀️ Morning Briefing — {Day, DD MMM YYYY}

## 📅 Calendar ({count} meetings)
{For each meeting, one line:}
- {emoji} **{time}** {subject} — {organizer} {prep_note_if_flagged}
{If back-to-back detected:}
- ⚠️ Back-to-back: {time1} → {time2}, no buffer

## 💬 Comms ({count} items needing attention)
{For each actionable message/email:}
- {emoji} **{source: Teams/Email}** {sender}: {summary} {action_needed}

## 🏃 Sprint Health
### Cortex (Board 106106) — Sprint "{sprint_name}"
- Score: {score} {emoji} ({breakdown})
- Progress: {done}/{total} stories | {in_progress} in flight | {blocked} blocked
- {emoji} Blockers: {list each with assignee and reason}
- {emoji} Scope creep: {count} stories added ({list titles})
- {emoji} Stalled: {count} stories no movement ≥3 days ({list with assignee})
- {emoji} Unassigned: {count} stories ({list titles})

### Hawkeye (Board 106133) — Sprint "{sprint_name}"
{Same structure as above}

### 👀 People Watch
{Only include people who surfaced in today's data:}
- {emoji} **{Name}**: {what was observed} ({watch context})

## 🎯 Today's Focus Areas
1. {Highest priority action}
2. {Second priority action}
3. {Third priority action}
```

---

#### MODE 2: Coaching Mode

Reflective, connects tactical to strategic. Helps the PM think about *why* things matter, not just *what* to do. Written in second person ("you").

```markdown
# ☀️ Morning Briefing — {Day, DD MMM YYYY}

## The Shape of Your Day
{2-3 sentences on what today looks like: meeting load, sprint position, any deadlines.}

## 📅 Calendar
{Same data as Checklist Mode, but add a reflection:}
**Prep thought:** {Which meeting has the highest stakes today? What outcome do you want from it?}

## 💬 What Came In Overnight
{Summarise comms thematically, not as a list. Group by theme: blockers, requests, FYIs.}
**Decision check:** {Are there any decisions only you can make? Who's waiting on you?}

## 🏃 Sprint Health
{Same scores and data as Checklist Mode, but add interpretation:}
**Pattern check:** {Is the score trending down? Is this a recurring issue or a one-off? What's the root cause?}

## 👀 People & Team
{For each watched person who surfaced:}
- **{Name}**: {observation}. *Coaching angle: {what to do about it — nudge, check in, escalate, delegate}*

## 🎯 Three Things That Matter Today
{Each focus area gets 2 lines: what to do + why it matters strategically}
1. **{Action}** — {strategic connection}
2. **{Action}** — {strategic connection}
3. **{Action}** — {strategic connection}

**Closing question:** {One reflective question for the day, e.g., "What's the one thing that, if you got it done today, would make the biggest difference to the squad's momentum?"}
```

## Focus Area Prioritisation

Always end with exactly **3 focus areas**. Rank by this priority stack (highest first):

1. **Active blockers** — anything blocking a squad member right now
2. **Sprint boundary urgency** — sprint ends within 3 days, stories at risk of not completing
3. **Reporting deadlines** — status reports, steering committee prep, exec updates due this week
4. **Pending decisions** — decisions only the PM can make that are holding up work
5. **Strategic work** — OKR progress, roadmap updates, stakeholder alignment

Each focus area must be specific and actionable (not "check on sprint" but "Unblock CORTEX-1234: Justin needs access to EDB staging — escalate to Sasi").

## Execution Steps

When the user triggers the briefing:

1. Determine today's date and day of week
2. Ask: "Checklist or Coaching mode?" — or use default (Checklist) if user says "morning briefing"
3. Make all data-fetching calls **in parallel** (JIRA, Calendar, Teams, Email)
4. If any source fails, note it as `⚠️ {Source} unavailable — skipped` and continue with remaining data
5. Calculate sprint health scores
6. Cross-reference results against People Watch List
7. Rank and select 3 focus areas
8. Render in the requested output format
9. If Coaching Mode, add reflective prompts and strategic connections

## Edge Cases

- **No active sprint:** Report "No active sprint found for {board}. Check if sprint needs to be started."
- **Weekend/holiday:** Adjust "overnight" window to cover since last business day
- **All green:** Still produce the briefing. Note "Clean slate today — use the space for strategic work" in focus areas
- **Too many blockers (>5):** Group by theme and highlight the top 3 to action first
