# {Product/Suite Name} Roadmap

| Field | Value |
|---|---|
| **Product** | {Cortex Suite / Customer Cortex (EDP001) / Customer Interactions (EDP006) / Transcat} |
| **Period** | {Q1 FY26 / H1 FY26 / FY26} |
| **View** | {Strategic / Tactical / Delivery / Stakeholder} |
| **Author** | Shalini Gangadharan, Product Manager — Cortex Suite |
| **Version** | {X.Y} |
| **Date** | {DD-MMM-YYYY} |
| **Status** | {Draft / In Review / Approved} |

---

## Strategic Themes

| # | Theme | Description | Strategic Alignment |
|---|---|---|---|
| T1 | {Theme Name} | {One-line description of what this theme delivers} | {Enterprise strategy pillar or objective} |
| T2 | {Theme Name} | {One-line description} | {Enterprise strategy pillar} |
| T3 | {Theme Name} | {One-line description} | {Enterprise strategy pillar} |
| T4 | {Theme Name} | {One-line description} | {Enterprise strategy pillar} |
| T5 | {Theme Name} | {One-line description} | {Enterprise strategy pillar} |

---

## Initiative Prioritisation

### Scoring Summary

**Framework used:** {RICE / WSJF}

#### RICE Scoring (if applicable)

| # | Initiative | Product | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|---|---|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {R} | {I} | {C%} | {E} | {R×I×C÷E} | {rank} |
| 2 | | | | | | | | |
| 3 | | | | | | | | |
| 4 | | | | | | | | |
| 5 | | | | | | | | |

#### WSJF Scoring (if applicable)

| # | Initiative | Product | Business Value | Time Criticality | Risk Reduction | CoD | Job Duration | WSJF | Rank |
|---|---|---|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {BV} | {TC} | {RR} | {CoD} | {JD} | {CoD÷JD} | {rank} |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |

**Non-discretionary items (regulatory/contractual):**

| # | Initiative | Product | Mandate | Deadline | JIRA Epic |
|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {Regulatory / Contractual / Compliance} | {DD-MMM-YYYY} | DME-XXXX |

---

## Initiative Table

| # | Initiative | Product | Priority Score | Framework | Quarter | Squad | Owner | Dependencies | Status | JIRA Epic |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {score} | {RICE/WSJF} | {Quarter} | {Squad} | {Person} | {Dependency list} | {🟢/🟡/🔴} | DME-XXXX |
| 2 | | | | | | | | | | |
| 3 | | | | | | | | | | |
| 4 | | | | | | | | | | |
| 5 | | | | | | | | | | |
| 6 | | | | | | | | | | |
| 7 | | | | | | | | | | |
| 8 | | | | | | | | | | |
| 9 | | | | | | | | | | |
| 10 | | | | | | | | | | |

---

## Now / Next / Later View

### Now — {Current Quarter}

Committed work. Resourced, dependencies resolved or managed, JIRA epics with stories.

| # | Initiative | Product | Owner | Squad | Dependencies | Status | JIRA Epic |
|---|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {Person} | {Squad} | {Dependencies} | {🟢/🟡/🔴} | DME-XXXX |
| 2 | | | | | | | |
| 3 | | | | | | | |
| 4 | | | | | | | |
| 5 | | | | | | | |

### Next — {Next Quarter}

Scoped at epic level. Prioritised and sequenced, not yet resourced.

| # | Initiative | Product | Owner | Squad | Dependencies | Target Quarter | JIRA Epic |
|---|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {Person} | {Squad} | {Dependencies} | {Quarter} | DME-XXXX |
| 2 | | | | | | | |
| 3 | | | | | | | |

### Later — {Future Quarters}

Directionally agreed. Strategic intent, not yet scoped in detail.

| # | Initiative | Product | Owner | Strategic Theme | Tentative Quarter | Notes |
|---|---|---|---|---|---|---|
| 1 | {Initiative name} | {Product} | {Person} | {Theme from above} | {Quarter} | {High-level context} |
| 2 | | | | | | |
| 3 | | | | | | |

---

## Dependency Map

```
{Initiative A} → blocks → {Initiative B} : {Reason — e.g., EDP001 entity resolution must complete before EDP006 enrichment can consume resolved IDs}
{Initiative C} → blocks → {Initiative D} : {Reason}
{External: Platform Upgrade} → blocks → {Initiative E} : {Reason}
{Data Source: Core Banking Migration} → blocks → {Initiative F} : {Reason}
```

**Cross-team dependencies:**

| # | From (Initiative / Team) | To (Initiative / Team) | Dependency Description | Status | Resolution Date |
|---|---|---|---|---|---|
| 1 | {Source initiative or team} | {Dependent initiative or team} | {What is needed} | {Open / Confirmed / Resolved} | {DD-MMM-YYYY} |
| 2 | | | | | |
| 3 | | | | | |

---

## Capacity Summary

| Squad | Available Sprints | Team Size (FTE) | Velocity (avg pts/sprint) | Total Capacity (pts) | Committed (pts) | Utilisation | Buffer (pts) |
|---|---|---|---|---|---|---|---|
| Cortex Engineering | {N} | {FTE} | {V} | {N×V} | {committed} | {%} | {remaining} |
| Customer Insights DS | {N} | {FTE} | {V} | {N×V} | {committed} | {%} | {remaining} |
| Project Hawkeye | {N} | {FTE} | {V} | {N×V} | {committed} | {%} | {remaining} |
| **Total** | | | | **{total}** | **{total}** | **{%}** | **{total}** |

> **Target utilisation:** 70–80%. Remaining buffer accommodates unplanned work, technical debt, and production support.

**Capacity notes:**

- {Person} on leave {DD-MMM-YYYY} to {DD-MMM-YYYY}
- {Person} ramping down / transitioning
- {Person} joining squad from {DD-MMM-YYYY}
- Public holidays: {list any in the period}

---

## Risks & Trade-offs

| # | Risk / Trade-off | Impact | Likelihood | RAG | Mitigation | Owner | Due Date |
|---|---|---|---|---|---|---|---|
| R1 | {Risk description} | {L/M/H} | {L/M/H} | {🟢/🟡/🔴} | {Specific mitigation action} | {Person} | {DD-MMM-YYYY} |
| R2 | {Risk description} | {L/M/H} | {L/M/H} | {🟢/🟡/🔴} | {Specific mitigation action} | {Person} | {DD-MMM-YYYY} |
| R3 | {Risk description} | {L/M/H} | {L/M/H} | {🟢/🟡/🔴} | {Specific mitigation action} | {Person} | {DD-MMM-YYYY} |

**Trade-off decisions:**

| # | Trade-off | Option Chosen | Rationale |
|---|---|---|---|
| 1 | {What was traded off — e.g., "Deferred Transcat re-architecture to prioritise EDP006 streaming"} | {What was chosen} | {Why — cost, capacity, strategic priority} |
| 2 | | | |

---

## Change Log

| Version | Date | Author | Changes |
|---|---|---|---|
| {X.Y} | {DD-MMM-YYYY} | {Name} | {Initial draft / What moved in, out, or changed — with reason} |
| | | | |
| | | | |

---

## Approvals

| Role | Name | Date | Decision |
|---|---|---|---|
| Product Manager | Shalini Gangadharan | {DD-MMM-YYYY} | {Draft / Approved} |
| {Architect} | {Mandar / Raja} | {DD-MMM-YYYY} | {Reviewed / Approved} |
| {Manager} | {Jeni} | {DD-MMM-YYYY} | {Reviewed / Approved} |
| {GM / Sponsor} | {Carolyn McCann / Damian McRae} | {DD-MMM-YYYY} | {Endorsed / Approved} |
