# Communication Templates — Cortex Suite

Fillable templates for standard Cortex Suite communications. Replace all `[bracketed]` placeholders before sending.

---

## 1. Release Notes

```
# [Product Name] — Release Notes v[X.Y]

| Field | Value |
|-------|-------|
| **Product** | [Customer Cortex / Customer Interactions / Transcat] |
| **Version** | [X.Y] |
| **Release Date** | [DD-MMM-YYYY] |
| **Author** | [Name] |
| **Distribution** | [Downstream teams / specific recipients] |

## Summary of Changes

- [One-line summary of each change in this release]

## ⚠️ Breaking Changes

- **[Change title]**: [Description of what changed, what breaks, and what consumers must do]. Consumers shall [specific action] by [DD-MMM-YYYY].
- [If none: "No breaking changes in this release."]

## New Features / Enhancements

- **[Feature name]**: [Description and benefit to consumers].
- **[Feature name]**: [Description and benefit to consumers].

## Bug Fixes

- **[DME-XXXX]**: [Description of the fix].
- **[DME-XXXX]**: [Description of the fix].

## Known Issues

- **[Issue description]**: [Workaround if available]. Tracking under [DME-XXXX].
- [If none: "No known issues."]

## Migration / Action Required by Consumers

1. [Step-by-step action with deadline]
2. [Step-by-step action with deadline]
- [If none: "No consumer action required."]

## JIRA References

| JIRA Key | Summary | Type |
|----------|---------|------|
| DME-XXXX | [Title] | Enhancement |
| DME-XXXX | [Title] | Bug Fix |

## Questions?

Contact [Name] via [email/Teams channel].
```

---

## 2. Change Notification

```
Subject: [ACTION REQUIRED] [Product Name] — [Brief Change Description] — Effective [DD-MMM-YYYY]

Hi [Team / Recipients],

**What is changing:**
[Product Name] will [description of the change] effective [DD-MMM-YYYY].

**When:**
- Change effective: [DD-MMM-YYYY]
- Consumer action deadline: [DD-MMM-YYYY]

**Impact on you:**
- [Specific impact — what breaks, what degrades, what changes in behaviour]
- [Which API endpoints / data feeds / schemas are affected]

**What you need to do:**
1. [Specific action with clear instruction]
2. [Specific action with clear instruction]
- Deadline: [DD-MMM-YYYY]

**Rollback plan:**
[Description of rollback approach if the change causes issues, or "N/A — this change is not reversible."]

**JIRA Reference:** [DME-XXXX]

**Questions?**
Contact [Name] at [email] or via [Teams channel].

Regards,
[Your Name]
Product Manager — Cortex Suite
```

---

## 3. Escalation Email

```
Subject: [ESCALATION] [Brief Issue Description] — [Product Name]

Hi [Recipient — e.g., Jeni / Carolyn / Damian],

**The issue:**
[One-sentence factual description of the blocker or risk.]

**Impact if unresolved:**
- [Quantified impact — days of delay, downstream systems affected, cost]
- [Which milestones or commitments are at risk]
- [Timeline: when does this become critical?]

**What I need from you:**
[Specific ask — a decision, a resource allocation, an unblock, a conversation with another party.]
- Needed by: [DD-MMM-YYYY]

**Proposed resolution:**
[Your recommended path forward. Include trade-offs if multiple options exist.]

| Option | Pros | Cons | Recommendation |
|--------|------|------|----------------|
| [Option A] | [Pros] | [Cons] | [Recommended / Not recommended] |
| [Option B] | [Pros] | [Cons] | [Recommended / Not recommended] |

**Supporting detail:**
- JIRA: [DME-XXXX]
- Confluence: [Link to relevant page]

I am available to discuss at your convenience. Please let me know how you would like to proceed.

Regards,
[Your Name]
Product Manager — Cortex Suite
```

---

## 4. Stakeholder Update

```
Subject: Cortex Suite — [Sprint/Period] Update — [DD-MMM-YYYY]

Hi [Recipient — e.g., Carolyn, Damian],

Summary of progress for Cortex Suite for the period [DD-MMM-YYYY] to [DD-MMM-YYYY].

**Outcomes & Wins:**
• [Outcome 1 — what was delivered, quantified impact if available]
• [Outcome 2 — what milestone was reached]
• [Outcome 3 — what was unblocked]

**Risks & Blockers:**
• [Risk 1 — description, impact, mitigation status]
• [Risk 2 — description, owner, expected resolution date]
• [If none: "No active blockers."]

**Upcoming Milestones:**
• [DD-MMM-YYYY] — [Milestone description]
• [DD-MMM-YYYY] — [Milestone description]

**Key Metrics:**
| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| [Metric name] | [Value] | [Value] | ↑ / ↓ / → |

Full sprint details: [Confluence link]

No action required — for awareness only.
[OR: **Action Required**: [specific ask].]

Regards,
[Your Name]
Product Manager — Cortex Suite
```

---

## 5. Team Announcement

```
Subject: [Team Update] [Brief Description — e.g., "Welcome Alex to Cortex Engineering"]

Hi team,

[Opening — state the news clearly.]
[E.g., "I am pleased to share that Alex Chen will be joining the Cortex Engineering squad as a Senior Data Engineer, effective 14-Apr-2026."]

[Context — why this is happening, background.]
[E.g., "Alex comes to us from the Payments Platform team where he led the migration to event-driven architecture. He will be focusing on the ADAPT pipeline modernisation workstream."]

[What happens next — transition plan, key dates, actions.]
[E.g., "Alex's first day with the squad is 14-Apr-2026. Mandar will be his onboarding buddy for the first two weeks. Please make him feel welcome and help him get up to speed on our ways of working."]

[Closing — warm, forward-looking.]
[E.g., "Looking forward to having Alex on the team. If you have any questions about the team structure, please reach out to me or Jeni."]

Regards,
[Your Name]
Product Manager — Cortex Suite
```

---

## 6. Celebration / Recognition

```
Subject: 🎉 [Achievement — e.g., "Customer Cortex v2.3 Shipped!"]

Hi team,

[What happened — name the achievement and the people.]
[E.g., "I want to recognise the outstanding work by Priya, Marcus, and the entire Cortex Engineering squad in delivering Customer Cortex v2.3 ahead of schedule."]

[Quantify the impact — be specific.]
[E.g., "This release reduced the Customer Segments API response time by 35% and resolved 12 outstanding defects that had been affecting downstream consumers. Digital Banker and Unity teams have both confirmed improved performance on their end."]

[Connect to the bigger picture.]
[E.g., "This is a significant step toward our Q2 objective of achieving sub-200ms API response times across all Cortex consumption endpoints. Thank you for your dedication and craftsmanship."]

Well done, team. 👏

[Your Name]
```

---

## Usage Notes

- Replace all `[bracketed]` placeholders before sending.
- All dates shall use DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Adjust section depth to match the significance of the communication.
- For release notes and change notifications, always include JIRA references.
- For escalation emails, always include a proposed resolution — never escalate without a recommendation.
- For stakeholder updates, keep to bullet points and attach detail rather than inlining it.
