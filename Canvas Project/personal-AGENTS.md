## About Me
- **Name**: Shalini Gangadharan
- **Role**: Parent, Educator & Learning App Developer
- **Goal**: Building a personalised learning platform for primary school education
- **Working Style**: Strategic and structured, automation-focused, iterates fast, learns by doing. Scaling from a single student to multiple students over time.

## Current Project — Learning App
- **Purpose**: Personal learning management system for primary school students
- **Source Data**: Exported from Canvas LMS (k12.instructure.com)
- **Content Types**: Quizzes, assignments, grades, learning materials (PDFs, docs), teacher comments
- **Tech Stack**: Python, HTML/CSS/JavaScript, VS Code, Claude Code, GitHub
- **GitHub Repo**: https://github.com/Claudeagent11/Learning-App

## Vision
- **Phase 1**: Export all Canvas data before account closure
- **Phase 2**: Build a local learning app with personalised content
- **Phase 3**: Add progress tracking and adaptive learning paths
- **Phase 4**: Scale to support multiple students with customised curricula

## Workflow Guidelines

### 1. Plan First
Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
If something goes sideways, STOP and re-plan immediately
Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
Use subagents liberally to keep main context window clean
Offload research, exploration, and parallel analysis to subagents
For complex problems, throw more compute at it via subagents

### 3. Self-Improvement Loop
After ANY correction from the user: update tasks/lessons.md with the pattern
Write rules for yourself that prevent the same mistake
Review lessons at session start for relevant project

### 4. Verification Before Done
Never mark a task complete without proving it works
Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
For non-trivial changes: pause and ask "is there a more elegant way?"
Skip this for simple, obvious fixes - don't over-engineer

### 6. Autonomous Bug Fixing
When given a bug report: just fix it. Don't ask for hand-holding
Point at logs, errors, failing tests - then resolve them

## Task Management
**Plan First**: Write plan to "tasks/todo.md" with checkable items
**Track Progress**: Mark items complete as you go
**Explain Changes**: High-level summary at each step
**Capture Lessons**: Update tasks/lessons.md after corrections

## Core Principles
**Simplicity First**: Make every change as simple as possible
**No Laziness**: Find root causes. No temporary fixes
**Minimal Impact**: Changes should only touch what's necessary
