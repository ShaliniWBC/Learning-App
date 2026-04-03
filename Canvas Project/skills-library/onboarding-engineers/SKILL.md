---
name: onboarding-engineers
description: "Generates onboarding plans for new Cortex Suite squad members with architecture walkthroughs, access checklists, and milestone tracking. Use when onboarding a new engineer, data scientist, analyst, or contractor into Cortex Engineering, Customer Insights DS, or Project Hawkeye."
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

# Onboarding Engineers — Cortex Suite

Generates structured onboarding plans for new team members joining the Cortex Suite squads within Westpac Group's Enterprise Data & Analytics function.

## Context

Onboarding into an enterprise data product team requires understanding multiple systems, governance frameworks, and team processes. The Cortex Suite spans three products (Customer Cortex EDP001, Customer Interactions EDP006, and Transaction Categorisation/Transcat) across a layered architecture of ADAPT pipelines, Snowflake, Databricks, ADLS2, Cosmos DB, and Mesh APIs.

Effective onboarding reduces time-to-productivity, supports retention, and ensures new joiners meet Westpac's compliance and security obligations from Day 1. A poorly structured onboarding leads to prolonged ramp-up, disengagement, and avoidable knowledge gaps.

## Team Context

| Person | Role | Squad |
|--------|------|-------|
| Sasi | Lead Engineer | Cortex Engineering |
| Cooper | Engineer | Cortex Engineering |
| Josh | Graduate Engineer | Cortex Engineering |
| Jolin | Graduate Engineer | Cortex Engineering |
| Jack | Analyst | Cortex Engineering |
| GK | SME / Solution Designer | Cross-squad |
| Tom | Lead Data Scientist | Customer Insights DS |
| Rupa | Data Scientist | Customer Insights DS |
| Simran | Data Scientist | Customer Insights DS |
| Justin | Data Scientist | Customer Insights DS |
| Vivasha | Data Scientist | Customer Insights DS |
| Claudia | Analyst | Customer Insights DS |
| Richard | Engineer | Project Hawkeye |
| Peter | Senior Business Analyst | Cross-squad |
| Kadeeja | Scrum Master | Cross-squad |
| Vinoth | Engineer (part-time) | Cortex Engineering |

**JIRA:** DME project, boards 106106 (Cortex Engineering / Customer Insights DS) and 106133 (Project Hawkeye).

## Onboarding Tracks

| Track | Target Role | Duration | Buddy | Key Focus |
|-------|-------------|----------|-------|-----------|
| Data Engineer | New/graduate engineers joining Cortex Engineering | 8–12 weeks | Sasi (Lead Engineer) | ADAPT pipelines, Snowflake, Azure infrastructure, CI/CD |
| Data Scientist | Data scientists joining Customer Insights DS | 8–12 weeks | Tom (Lead DS) | Databricks, ML frameworks, feature engineering |
| Business Analyst | BAs joining Hawkeye or cross-squad | 6–8 weeks | GK or Peter | Requirements gathering, stakeholder mapping, JIRA workflow |
| Contractor / Vendor | Short-term resources on scoped engagements | 4 weeks | Varies by deliverable | Scoped to specific deliverable, security clearance |

## Workflow

### Step 1 — Identify Onboarding Context

Gather the following before generating any plan:

1. **Who is joining?** — Full name, employment type (permanent, graduate, contractor, vendor).
2. **What role?** — Data Engineer, Data Scientist, Business Analyst, or other.
3. **Which squad?** — Cortex Engineering, Customer Insights DS, or Project Hawkeye.
4. **Start date** — Confirmed or expected, in DD-MMM-YYYY format.
5. **Buddy assignment** — Confirm with the squad lead. Default buddies per track are listed above.
6. **Prior experience** — Relevant technology background to calibrate the learning path depth.

If a JIRA ticket exists for the onboarding (e.g., DME-XXXX), use `mcp__jira__jira_get_issue` to pull context.

### Step 2 — Generate Access Checklist

Using the role-based access matrix below, generate a personalised checklist for the new joiner. Mark each item with:
- **Required** — shall be provisioned before Day 1 or within the first week.
- **Week 2** — should be provisioned by end of Week 2.
- **As Needed** — may be requested when the joiner reaches the relevant stage.

Escalate any access request that takes longer than five business days.

### Step 3 — Build 30/60/90 Day Plan

Using the 30/60/90 day structure below, generate a plan tailored to the joiner's role and squad. Adjust milestones based on:
- Prior experience level (graduate vs. experienced hire)
- Squad-specific priorities (check active sprint for current work themes)
- Any known deadlines or deliverables the joiner should ramp into

Use `mcp__jira__jira_search_issues` with JQL `project = DME AND sprint in openSprints()` to identify current sprint context.

### Step 4 — Create Architecture Walkthrough Guide

Generate a sequenced learning path through the Cortex architecture using the template below. Adjust based on track:
- **Data Engineer track**: Full depth on all layers, emphasis on pipeline development.
- **Data Scientist track**: Focus on Databricks, feature stores, model deployment. Lighter on infrastructure.
- **Business Analyst track**: Focus on product understanding, data lineage concepts, stakeholder landscape. No deep infrastructure.

Search Confluence for existing architecture documentation:
- Use `mcp__confluence__search_pages` with queries such as "Cortex architecture", "ADAPT pipeline", "Snowflake data model".
- Link relevant pages in the walkthrough guide.

### Step 5 — Schedule Key Meetings

Generate a list of recommended meetings for the first four weeks:

| Week | Meeting | Attendees | Purpose |
|------|---------|-----------|---------|
| 1 | Welcome / squad introduction | Squad members, SM | Meet the team, understand ways of working |
| 1 | 1:1 with buddy | Buddy | Set expectations, answer questions |
| 1 | Product overview | PM (Shalini) | Cortex product landscape and strategy |
| 2 | Architecture walkthrough — data flow | GK or Sasi | End-to-end data flow through Cortex |
| 2 | JIRA & ways of working | Kadeeja (SM) | Sprint ceremonies, board usage, Definition of Done |
| 3 | Deep-dive: primary technology area | Buddy or Lead | ADAPT/Snowflake (Eng), Databricks (DS), Requirements (BA) |
| 3 | Stakeholder introductions | PM + relevant stakeholders | Meet key consumers and business partners |
| 4 | 30-day check-in | Buddy + Lead | Review progress against milestones |

### Step 6 — Set Success Criteria

Define measurable outcomes for each milestone checkpoint:

| Checkpoint | Criteria | How to Measure |
|------------|----------|----------------|
| Day 30 | Can explain what each Cortex product does and who consumes it | Verbal walkthrough with buddy |
| Day 30 | All required access provisioned and verified | Checklist sign-off |
| Day 60 | Has independently completed at least one JIRA story | JIRA ticket in Done status |
| Day 60 | Actively participating in sprint ceremonies | Observation by SM |
| Day 90 | Delivering sprint commitments at expected velocity | Sprint metrics review |
| Day 90 | Contributing to technical discussions and reviews | Peer feedback |

## Access Checklist

| System / Tool | Purpose | Data Engineer | Data Scientist | BA | Request Process |
|---------------|---------|:---:|:---:|:---:|-----------------|
| JIRA (DME project) | Work tracking and sprint management | ✓ | ✓ | ✓ | ServiceNow |
| Confluence | Documentation and knowledge base | ✓ | ✓ | ✓ | ServiceNow |
| Snowflake | Data warehouse — query and develop | ✓ | ✓ (read) | ✗ | Data Access Request |
| Databricks | ML/analytics workspace | ✓ | ✓ | ✗ | Cloud Access Request |
| ADLS2 | Azure Data Lake storage | ✓ | ✓ | ✗ | Cloud Access Request |
| Azure DevOps | CI/CD pipelines | ✓ | ✗ | ✗ | DevOps team |
| Cosmos DB | API data store | ✓ | ✗ | ✗ | Data Access Request |
| AEP (Adobe Experience Platform) | Downstream consumer platform | As needed | ✗ | ✗ | Vendor access request |
| Teams channels | Team communication | ✓ | ✓ | ✓ | Team owner adds member |

**Notes:**
- All access requests shall include the new joiner's Westpac employee ID and line manager approval.
- Snowflake "read" access for Data Scientists covers curated and consumption layers only.
- Contractor/vendor access shall be scoped to the minimum required for their deliverable and time-limited.

## 30/60/90 Day Plan Structure

### Week 1–2 (Orientation)

- Complete access provisioning for all required systems
- Meet squad members and key stakeholders (see meeting schedule above)
- Read product documentation on Confluence — start with Cortex product overview pages
- Attend sprint ceremonies as an observer (stand-up, refinement, review, retro)
- Complete mandatory Westpac training (compliance, information security, code of conduct)
- Set up local development environment (engineering tracks)
- Review team working agreements and Definition of Done

### Day 30 (Foundation)

- Understand Cortex product architecture end-to-end
- Complete first paired task with buddy (e.g., paired code review, paired analysis)
- Attend architecture walkthrough sessions (minimum two from the learning path)
- Review and understand team working agreements
- **Milestone:** Can explain what each Cortex product does and who consumes it

### Day 60 (Contributing)

- Complete first independent task or JIRA story
- Participate actively in sprint ceremonies (contributing to discussions, not just observing)
- Understand ADAPT pipeline patterns and data flow
- Begin contributing to code reviews (engineering) or model reviews (data science)
- **Milestone:** Can independently pick up and deliver a standard story

### Day 90 (Independent)

- Independently delivering sprint commitments at expected velocity for role level
- Contributing to technical discussions and design decisions
- Understanding cross-product dependencies (how Customer Cortex, Interactions, and Transcat relate)
- Mentoring newer joiners if applicable
- **Milestone:** Operating at expected velocity for role level

## Architecture Learning Path

| Week | Topic | Key Concepts | Who Delivers | Outcome |
|------|-------|-------------|--------------|---------|
| 1 | Cortex product overview | EDP001, EDP006, Transcat; data product concepts; consumers and use cases | PM (Shalini) | Can describe what Cortex does and why it exists |
| 2 | ADAPT pipeline architecture | Ingestion patterns, orchestration, data flow from source to consumption | GK or Sasi | Can trace data from source system to API endpoint |
| 3 | Snowflake data model | Key entities, schema design, SCD handling, query patterns | Sasi or Cooper | Can query curated layer and explain the data model |
| 4 (DS) | Databricks ML environment | Notebook setup, feature engineering, model training workflow | Tom | Can run an existing notebook and explain the ML pipeline |
| 4 (Eng) | Azure infrastructure | ADLS2 storage layout, Azure DevOps pipelines, Cosmos DB | Sasi | Can navigate Azure resources and understand deployment |
| 5 | Mesh APIs and downstream consumers | API contracts, consumer applications (Digital Banker, Unity, WLive, AEP) | GK | Can explain how downstream systems consume Cortex data |
| 6 | Monitoring, alerting, and incident response | Pipeline monitoring, data quality checks, incident process | Sasi or Cooper | Can identify a pipeline failure and follow the incident process |

**Notes:**
- The learning path should be adjusted based on the joiner's prior experience. Experienced hires may compress Weeks 1–3 into one to two sessions.
- Search Confluence for existing walkthrough materials before creating new content.
- Each session should be 60–90 minutes with follow-up reading assigned.

## Onboarding Anti-Patterns

Avoid these common failure modes:

1. **Throwing new joiners into sprint work on Day 1 without context** — They shall have at least one week of orientation before picking up stories.
2. **No buddy assignment or inactive buddy** — Every new joiner shall have a named buddy who commits to regular check-ins (minimum twice per week in the first month).
3. **Access provisioning taking longer than one week** — Escalate immediately if access requests are not fulfilled within five business days. A new joiner without system access cannot learn or contribute.
4. **No architecture walkthrough** — Learning by osmosis is slow and inconsistent. The structured learning path shall be followed.
5. **No milestone check-ins** — Without 30/60/90 day reviews, onboarding drift goes undetected. The buddy and lead shall conduct formal check-ins at each milestone.
6. **Overloading with meetings in Week 1** — Balance introductions with self-directed learning time. No more than three to four scheduled meetings per day in the first week.
7. **Skipping compliance training** — Westpac mandatory training shall be completed within the first two weeks. This is non-negotiable.

## Quality Checklist

Before presenting the onboarding plan, verify:

- [ ] New joiner's name, role, squad, and start date are confirmed
- [ ] Buddy is assigned and has confirmed availability
- [ ] Access checklist is complete and role-appropriate
- [ ] 30/60/90 day plan has specific, measurable milestones
- [ ] Architecture learning path is sequenced and has named presenters
- [ ] Key meetings are scheduled or identified with proposed attendees
- [ ] Success criteria are defined for each milestone checkpoint
- [ ] No sections contain placeholder text
- [ ] Anti-patterns have been reviewed and mitigations are in place
- [ ] Plan has been saved as a markdown file in the workspace

## Output Format

- Output the onboarding plan as a single Markdown document.
- Use the reference template at `reference/onboarding-plan-template.md` as the skeleton.
- Name the file `Onboarding-Plan-{Name}-{Squad}.md` in the workspace root or a location specified by the PM.
- All dates shall use DD-MMM-YYYY format (e.g., 28-Mar-2026).
- Use "shall" for mandatory requirements, "should" for recommendations, "may" for optional items.
- Maintain professional banking language throughout. No startup jargon.

## Conventions

- **JIRA keys** use the `DME-XXXX` format.
- **Name people explicitly** — never say "the team" when you can say "Sasi and Cooper".
- **Dates** in DD-MMM-YYYY format.
- **Access requests** shall reference the specific provisioning channel (ServiceNow, Cloud Access Request, etc.).
- **Milestones** shall be specific and verifiable, not vague aspirations.
- Maintain a professional, direct tone. Every sentence earns its place.
