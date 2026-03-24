# Canvas Learning Hub — Project Plan

> **Document Purpose**: This document serves as the single source of truth for the Canvas Learning Hub project. It is written for two audiences: (1) a **Product Manager** who needs to understand scope, phases, and decisions, and (2) a **Full-Stack Developer** who needs detailed technical instructions to build the app.
>
> **Last Updated**: 2026-03-21

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [User Personas & Requirements](#2-user-personas--requirements)
3. [Architecture & Tech Stack](#3-architecture--tech-stack)
4. [Phase 1 — Canvas Content Extraction](#4-phase-1--canvas-content-extraction)
5. [Phase 2 — App Build (Learning Hub)](#5-phase-2--app-build-learning-hub)
6. [Phase 3 — Assessment Engine](#6-phase-3--assessment-engine)
7. [Phase 4 — Polish & Production Readiness](#7-phase-4--polish--production-readiness)
8. [Document & File Handling Strategy](#8-document--file-handling-strategy)
9. [Canvas Quiz Assessment Strategy](#9-canvas-quiz-assessment-strategy)
10. [Authentication & Student Safety](#10-authentication--student-safety)
11. [Deployment & Infrastructure](#11-deployment--infrastructure)
12. [Content Versioning & Sync Strategy](#12-content-versioning--sync-strategy)
13. [Monitoring, Backups & Reliability](#13-monitoring-backups--reliability)
14. [Accessibility & iPad UX Considerations](#14-accessibility--ipad-ux-considerations)
15. [Backlog & Future Enhancements](#15-backlog--future-enhancements)
16. [Task Checklist](#16-task-checklist)
17. [Decision Log](#17-decision-log)
18. [Glossary](#18-glossary)

---

## 1. Project Overview

### What Are We Building?

A web-based educational app ("Canvas Learning Hub") that:

- **Extracts** all educational content from an existing Canvas LMS instance across 4 courses
- **Presents** that content in a clean, student-friendly learning interface optimized for iPad
- **Delivers assessments** (quizzes/tests) imported from Canvas, with scoring and feedback

### The Four Courses

| # | Course Name | Content Types Expected |
|---|-------------|----------------------|
| 1 | Reading Comprehension | YouTube videos, HTML pages, Word docs, PDFs, quizzes |
| 2 | Thinking Skills | YouTube videos, HTML pages, Word docs, PDFs, quizzes |
| 3 | Writing | YouTube videos, HTML pages, Word docs, PDFs, quizzes |
| 4 | Maths | YouTube videos, HTML pages, Word docs, PDFs, quizzes |

### Key Constraints

- **1 student** (age 10–15) to start with
- **1 instructor** (the app owner)
- **iPad-primary** usage via browser (Safari)
- **No offline access** required (revisit later)
- **Budget**: Free tier (Vercel + Supabase) — sufficient for 1 student
- **Domain**: `*.vercel.app` (free subdomain, no custom domain needed now)

---

## 2. User Personas & Requirements

### Persona 1: Student (Age 10–15)

- **Device**: iPad (Safari browser)
- **Login**: Email + password
- **Needs**:
  - Browse courses and modules in a clear, intuitive structure
  - Watch YouTube educational videos inline
  - Read text content (HTML pages) with good readability
  - View PDFs and documents without leaving the app
  - Take quizzes/tests and see scores immediately
  - Track progress across courses (which modules completed, quiz scores)
- **UX Considerations**:
  - Large touch targets (minimum 44x44px per Apple HIG)
  - Clear navigation — a 10-year-old should not get lost
  - Readable fonts (minimum 16px body text)
  - No distracting ads or unnecessary complexity

### Persona 2: Instructor

- **Device**: Desktop or iPad
- **Login**: Email + password (same auth system, elevated role)
- **Needs**:
  - Trigger content sync from Canvas (import/refresh content)
  - View student progress and quiz results
  - (Future) Author custom quizzes
  - Manage student account(s)

### Functional Requirements

| ID | Requirement | Priority | Phase |
|----|------------|----------|-------|
| FR-01 | Student can log in with email + password | Must | 2 |
| FR-02 | Student can browse courses → modules → content | Must | 2 |
| FR-03 | Student can watch embedded YouTube videos | Must | 2 |
| FR-04 | Student can read HTML text content | Must | 2 |
| FR-05 | Student can view PDFs in-browser | Must | 2 |
| FR-06 | Student can take quizzes and see scores | Must | 3 |
| FR-07 | Student can see progress (completed items, scores) | Should | 3 |
| FR-08 | Instructor can trigger Canvas content sync | Must | 1 |
| FR-09 | Instructor can view student results | Should | 3 |
| FR-10 | Instructor can author custom quizzes | Want | Backlog |
| FR-11 | Word docs converted to PDF during import | Must | 1 |

---

## 3. Architecture & Tech Stack

### Why This Stack?

| Component | Choice | Rationale |
|-----------|--------|-----------|
| **Frontend + Backend** | Next.js 14+ (App Router) | Single project for UI + API routes. React-based with huge ecosystem. Server-side rendering for fast iPad load times. |
| **Database** | Supabase (PostgreSQL) | Relational DB ideal for courses → modules → content → quizzes → attempts. Built-in auth. Free tier covers 1 student easily. |
| **Authentication** | Supabase Auth | Email + password out of the box. Row Level Security (RLS) ensures student can only see their own data. |
| **File Storage** | Supabase Storage | PDFs and converted Word docs stored here. Served via CDN. Free tier: 1GB storage, 2GB bandwidth/month — more than enough. |
| **Hosting** | Vercel (free tier) | One-click deploy from GitHub. Automatic HTTPS. Free tier: 100GB bandwidth/month. |
| **Styling** | Tailwind CSS | Utility-first CSS. Fast to build responsive, iPad-friendly layouts. |

### Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                    STUDENT (iPad)                    │
│              Opens: yourapp.vercel.app               │
└─────────────────┬───────────────────────────────────┘
                  │ HTTPS
                  ▼
┌─────────────────────────────────────────────────────┐
│              VERCEL (Free Tier)                      │
│  ┌────────────────────────────────────────────────┐  │
│  │           Next.js Application                  │  │
│  │                                                │  │
│  │  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │  │
│  │  │  Pages/  │  │  API     │  │  Server      │  │  │
│  │  │  UI      │  │  Routes  │  │  Components  │  │  │
│  │  └──────────┘  └────┬─────┘  └─────────────┘  │  │
│  └──────────────────────┼─────────────────────────┘  │
└─────────────────────────┼───────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────┐
│              SUPABASE (Free Tier)                    │
│                                                     │
│  ┌──────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Auth   │  │  PostgreSQL  │  │   Storage    │  │
│  │          │  │  Database    │  │  (PDFs, etc) │  │
│  │ Email +  │  │              │  │              │  │
│  │ Password │  │  - courses   │  │  - PDFs      │  │
│  │          │  │  - modules   │  │  - converted │  │
│  │          │  │  - content   │  │    docs      │  │
│  │          │  │  - quizzes   │  │              │  │
│  │          │  │  - attempts  │  │              │  │
│  │          │  │  - progress  │  │              │  │
│  └──────────┘  └──────────────┘  └──────────────┘  │
└─────────────────────────────────────────────────────┘
```

### Database Schema (Conceptual)

```
users
  ├── id (UUID, from Supabase Auth)
  ├── email
  ├── role (student | instructor)
  ├── display_name
  └── created_at

courses
  ├── id
  ├── title (e.g., "Reading Comprehension")
  ├── description
  ├── canvas_course_id (for sync reference)
  ├── sort_order
  └── created_at

modules
  ├── id
  ├── course_id (FK → courses)
  ├── title
  ├── description
  ├── canvas_module_id
  ├── sort_order
  └── created_at

content_items
  ├── id
  ├── module_id (FK → modules)
  ├── title
  ├── content_type (html | youtube | pdf | external_url)
  ├── body (HTML text content, nullable)
  ├── youtube_url (nullable)
  ├── file_url (Supabase Storage URL for PDFs, nullable)
  ├── external_url (nullable)
  ├── canvas_item_id
  ├── sort_order
  └── created_at

quizzes
  ├── id
  ├── module_id (FK → modules)
  ├── title
  ├── description
  ├── time_limit_minutes (nullable)
  ├── canvas_quiz_id
  └── created_at

quiz_questions
  ├── id
  ├── quiz_id (FK → quizzes)
  ├── question_type (multiple_choice | true_false | short_answer | essay)
  ├── question_text (HTML)
  ├── points
  ├── sort_order
  └── created_at

quiz_answers
  ├── id
  ├── question_id (FK → quiz_questions)
  ├── answer_text
  ├── is_correct (boolean)
  └── sort_order

quiz_attempts
  ├── id
  ├── quiz_id (FK → quizzes)
  ├── user_id (FK → users)
  ├── started_at
  ├── submitted_at
  ├── score
  ├── max_score
  └── status (in_progress | submitted | graded)

quiz_responses
  ├── id
  ├── attempt_id (FK → quiz_attempts)
  ├── question_id (FK → quiz_questions)
  ├── selected_answer_id (FK → quiz_answers, nullable)
  ├── text_response (for short answer/essay, nullable)
  ├── is_correct (boolean, nullable)
  └── points_awarded

student_progress
  ├── id
  ├── user_id (FK → users)
  ├── content_item_id (FK → content_items, nullable)
  ├── quiz_id (FK → quizzes, nullable)
  ├── status (not_started | in_progress | completed)
  ├── completed_at (nullable)
  └── created_at
```

---

## 4. Phase 1 — Canvas Content Extraction

> **Goal**: Get all content out of Canvas and into our database/storage.

### Step 1: Determine Canvas API Access

**Instructions for the instructor**:

1. Log into Canvas at your institution's URL
2. Click your **profile picture** (top-left corner) → **Settings**
3. Scroll down to the section called **"Approved Integrations"**
4. Look for a button labeled **"+ New Access Token"**

**If the button exists**:
- Click it, give it a name like "Learning Hub Import", set expiry to 90 days
- Copy the token immediately (it's shown only once)
- Store it securely (never commit it to code — use environment variables)
- We will use the **Canvas REST API** for extraction (preferred path)

**If the button does NOT exist**:
- Your institution has disabled API tokens
- Fallback plan: Use Canvas's built-in **Export Course Content** feature
  - Go to each course → Settings → Export Course Content → select "Course" → Export
  - This generates a ZIP file in **IMSCC format** (a standard e-learning package format)
  - Download all 4 ZIP files
  - We will parse these ZIP files to extract content

### Step 2A: API-Based Extraction (Preferred)

If you have an API token, the extraction script will:

1. **List all courses** → `GET /api/v1/courses`
2. **For each course, list modules** → `GET /api/v1/courses/:id/modules`
3. **For each module, list items** → `GET /api/v1/courses/:id/modules/:id/items`
4. **For each item, fetch content**:
   - Pages → `GET /api/v1/courses/:id/pages/:url`
   - Files → `GET /api/v1/courses/:id/files/:id` (download URL)
   - Quizzes → `GET /api/v1/courses/:id/quizzes` + questions
5. **Download all files** (PDFs, Word docs) to local storage
6. **Store everything** in structured JSON files as an intermediate format

**Rate Limiting**: Canvas API allows ~10 requests/second. The script must respect `X-Rate-Limit-Remaining` headers and implement exponential backoff.

**Pagination**: All Canvas API list endpoints are paginated. Follow `Link` header `rel="next"` URLs until exhausted.

```
# Environment variables needed
CANVAS_BASE_URL=https://your-institution.instructure.com
CANVAS_API_TOKEN=your_token_here
```

### Step 2B: Manual Export Extraction (Fallback)

If no API token is available:

1. Export each of the 4 courses from Canvas (Settings → Export Course Content)
2. Each export produces a `.imscc` ZIP file containing:
   - `imsmanifest.xml` — the course structure (modules, items, ordering)
   - `wiki_content/` — HTML pages
   - `web_resources/` — files (PDFs, Word docs, images)
   - `assessment_meta.xml` + QTI files — quiz definitions
3. Write a parser script to:
   - Parse `imsmanifest.xml` for structure
   - Extract HTML content from wiki pages
   - Copy files to our storage
   - Parse QTI XML for quiz questions and answers

### Step 3: Content Audit

Before importing, run an audit script that produces a report:

```
CONTENT AUDIT REPORT
====================
Course: Reading Comprehension
  Modules: 8
  HTML Pages: 23
  YouTube Links: 12
  PDF Files: 5
  Word Docs: 3        ← THESE NEED CONVERSION
  Quizzes: 4
  Quiz Type: Classic   ← OR "New Quizzes" (CRITICAL — see Section 9)
  Other/Unknown: 0

Course: Thinking Skills
  ...

TOTAL Word Docs requiring conversion: X
TOTAL file storage needed: X MB
```

**Why this matters**: This audit tells us exactly what we're dealing with before we write import code. It surfaces surprises early (unexpected file types, broken links, etc.).

### Step 4: Import Into Database

After extraction and audit:

1. Run the import script to populate the Supabase database
2. Upload PDFs and converted docs to Supabase Storage
3. Verify: Every module, content item, and quiz question has been imported
4. Generate a verification report comparing Canvas source counts vs imported counts

---

## 5. Phase 2 — App Build (Learning Hub)

> **Goal**: Student can log in, browse courses, and consume content.

### Page Structure

```
/                        → Landing page (redirect to /courses if logged in)
/login                   → Email + password login
/courses                 → Course listing (4 cards)
/courses/[id]            → Single course — list of modules
/courses/[id]/modules/[id] → Single module — list of content items
/content/[id]            → Single content item (HTML, video, or PDF viewer)
/quizzes/[id]            → Quiz taking interface (Phase 3)
/quizzes/[id]/results    → Quiz results (Phase 3)
/progress                → Student progress dashboard (Phase 3)
/admin                   → Instructor dashboard (Phase 3)
/admin/sync              → Trigger Canvas re-sync (Phase 1 integration)
```

### UI/UX Specifications

**Navigation**:
- Top navigation bar with: App logo/name, Course dropdown, Progress link, Logout
- Breadcrumb trail: Courses → [Course Name] → [Module Name] → [Content Title]
- "Next" and "Previous" buttons at the bottom of every content page (sequential navigation through a module)

**Course Listing Page** (`/courses`):
- 4 cards in a 2×2 grid (on iPad landscape) or stacked (portrait)
- Each card shows: Course icon/color, title, progress bar, module count
- Tap a card → navigate to that course's modules

**Module Listing Page** (`/courses/[id]`):
- Vertical list of modules in order
- Each module shows: title, item count, completion status (checkmark if all items done)
- Expand/collapse to see individual content items within each module

**Content Viewer** (`/content/[id]`):
- **For HTML content**: Rendered in a clean reading layout. Body text at 18px minimum. Max width 720px for readability. Good line spacing (1.6).
- **For YouTube videos**: Embedded using `<iframe>` with `youtube-nocookie.com` domain (privacy-enhanced mode — important for a minor). 16:9 aspect ratio, responsive width.
- **For PDFs**: Embedded using `<iframe>` or `<object>` tag pointing to Supabase Storage URL. Fallback "Download PDF" button if rendering fails. Consider PDF.js for consistent cross-browser rendering if native embed is unreliable.
- **Mark as complete**: Button at the bottom. Once clicked, records progress.

### Developer Implementation Notes

**Project Initialization**:
```bash
npx create-next-app@latest canvas-learning-hub --typescript --tailwind --app --src-dir
cd canvas-learning-hub
npm install @supabase/supabase-js @supabase/ssr
```

**Environment Variables** (`.env.local`):
```
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key  # Server-side only, never exposed
```

**Supabase Client Setup**:
- Create a browser client (`createBrowserClient`) for client components
- Create a server client (`createServerClient`) for server components and API routes
- Follow Supabase SSR documentation for Next.js App Router integration

**Row Level Security (RLS)** — CRITICAL for student safety:
```sql
-- Students can only read courses, modules, content (public read)
CREATE POLICY "Anyone can read courses" ON courses FOR SELECT USING (true);
CREATE POLICY "Anyone can read modules" ON modules FOR SELECT USING (true);
CREATE POLICY "Anyone can read content" ON content_items FOR SELECT USING (true);

-- Students can only see their OWN progress and quiz attempts
CREATE POLICY "Users see own progress" ON student_progress
  FOR ALL USING (auth.uid() = user_id);

CREATE POLICY "Users see own attempts" ON quiz_attempts
  FOR ALL USING (auth.uid() = user_id);

-- Only instructor can modify content
CREATE POLICY "Instructor manages courses" ON courses
  FOR ALL USING (
    EXISTS (SELECT 1 FROM users WHERE id = auth.uid() AND role = 'instructor')
  );
```

---

## 6. Phase 3 — Assessment Engine

> **Goal**: Student can take quizzes imported from Canvas and see results.

### Quiz Taking Flow

```
Student clicks "Start Quiz"
  → Create a quiz_attempt record (status: in_progress, started_at: now)
  → Display questions one-per-page or all-at-once (configurable per quiz)
  → Student selects/types answers
  → Each answer auto-saves to quiz_responses (prevent data loss)
  → Student clicks "Submit Quiz"
  → Auto-grade: compare responses to correct answers
  → Update quiz_attempt (status: submitted, score calculated)
  → Redirect to results page
```

### Quiz Interface Specifications

**Question Display**:
- One question at a time with "Next" / "Previous" navigation (better for iPad)
- Progress indicator: "Question 3 of 10"
- Question text rendered as HTML (Canvas stores questions as HTML)
- For multiple choice: Large radio buttons / tap targets (entire row is tappable)
- For true/false: Two large buttons
- For short answer: Text input with on-screen keyboard consideration

**Timer** (if time_limit_minutes is set):
- Countdown displayed in top-right corner
- Warning at 5 minutes remaining (visual highlight)
- Warning at 1 minute remaining (more urgent visual)
- Auto-submit when timer expires
- Timer persists across page refreshes (calculated from started_at)

**Auto-Save**:
- Save the student's response every time they select/change an answer
- Rationale: If the iPad loses connection or Safari crashes, no work is lost
- Implementation: Debounced Supabase upsert on quiz_responses table
- Visual indicator: "Saved ✓" near the submit button

**Results Page**:
- Total score: "You scored 8 out of 10 (80%)"
- Per-question breakdown: ✅ or ❌ with correct answer shown
- For incorrect answers: Show the correct answer (learning opportunity)
- "Retake Quiz" button (creates a new attempt)

### Student Progress Dashboard (`/progress`)

- Course-by-course breakdown
- For each course: modules completed / total modules
- For each quiz: best score, most recent score, number of attempts
- Visual progress bars with percentage

### Instructor Dashboard (`/admin`)

- View the student's progress across all courses
- View all quiz attempts and scores
- (Future) Manually grade essay questions
- (Future) Export results as CSV

---

## 7. Phase 4 — Polish & Production Readiness

> **Goal**: Make the app reliable, safe, and pleasant to use.

### Performance

- **Target**: First Contentful Paint < 2 seconds on iPad over WiFi
- Use Next.js server components for data-heavy pages (courses, modules lists)
- Lazy-load YouTube iframes (don't load until scrolled into view)
- Optimize images with Next.js `<Image>` component
- Cache course/module structure aggressively (content changes rarely)

### Error Handling

- Friendly error pages (not raw stack traces)
- If content fails to load: Show "This content couldn't be loaded. Try refreshing." with a retry button
- If quiz submission fails: Keep data in local state + retry automatically
- Network error detection: "You appear to be offline. Please check your connection."

### Student Safety & Privacy

- **YouTube Privacy Mode**: Always use `youtube-nocookie.com` for embeds
- **No tracking**: No analytics, ad trackers, or third-party scripts
- **Data minimization**: Only collect what's needed (email, name, quiz responses)
- **Secure cookies**: HttpOnly, Secure, SameSite=Strict
- **HTTPS only**: Enforced by Vercel by default

---

## 8. Document & File Handling Strategy

### The Problem

Canvas courses may contain Word documents (.doc, .docx). iPad Safari **cannot reliably render Word documents in-browser**. Students would be forced to download the file and open it in a separate app, breaking the learning flow.

### The Solution

**Convert all Word documents to PDF during the import process** (Phase 1). Students will only ever see PDFs, which iPad Safari handles natively.

### Task: Audit Word Documents

Before building the converter, manually audit each course:

1. **Log into Canvas**
2. For each of the 4 courses, go to **Files** section
3. Note every `.doc` and `.docx` file
4. Record in a table:

```
| Course | File Name | File Size | Location (which module) |
|--------|-----------|-----------|------------------------|
| Reading | worksheet1.docx | 245KB | Module 3 |
| ...    | ...       | ...       | ...                    |
```

### Task: Convert Word Docs to PDF

**Option A — Manual Conversion** (if only a few docs):
- Open each .docx in Microsoft Word or Google Docs
- Export/Save As PDF
- Upload the PDF to the project's import folder
- Quick and reliable for < 20 documents

**Option B — Automated Conversion** (if many docs):
- Use LibreOffice headless mode in the import script:
  ```bash
  libreoffice --headless --convert-to pdf document.docx
  ```
- Or use a Node.js library like `docx-pdf` or call the CloudConvert API
- Rationale: If there are 50+ documents, manual conversion is tedious and error-prone

**Recommendation**: Start with a manual audit (count the docs). If < 20, convert manually. If > 20, automate.

### PDF Storage & Serving

- Upload converted PDFs to **Supabase Storage** bucket named `course-files`
- Set bucket to **public read** (content is educational, not sensitive)
- Store the Supabase Storage URL in the `content_items.file_url` column
- In the app, render PDFs using:
  ```jsx
  <iframe
    src={fileUrl}
    className="w-full h-[80vh] rounded-lg border"
    title={contentTitle}
  />
  ```
- Include a "Download PDF" fallback link below the iframe

---

## 9. Canvas Quiz Assessment Strategy

### Critical Decision: Classic Quizzes vs New Quizzes

Canvas has **two completely different quiz systems**. The extraction approach is fundamentally different for each.

#### How to Check Which Quiz System Your Courses Use

1. Log into Canvas
2. Go to one of your 4 courses
3. Click **"Quizzes"** in the left sidebar
4. Look at the quiz list:

**Classic Quizzes indicators**:
- Quiz page URL contains `/courses/XXX/quizzes/YYY`
- Edit page shows a straightforward form with question tabs
- Quiz settings page has "Quiz Type" dropdown (Practice, Graded, Survey)

**New Quizzes indicators**:
- When you click a quiz, it may say "This is a New Quizzes quiz" or redirect to a different-looking interface
- URL may contain `/courses/XXX/assignments/YYY` (quizzes appear as assignments)
- The editing interface looks modern with drag-and-drop question building
- You may see an "ItemPool" or "Item Bank" concept

**Record your finding**: For each of the 4 courses, note which quiz system is used.

#### Path A: Classic Quizzes (Simpler)

Classic Quizzes are fully accessible via the Canvas REST API:

```
GET /api/v1/courses/:course_id/quizzes
GET /api/v1/courses/:course_id/quizzes/:quiz_id/questions
```

The API returns:
- Question text (HTML)
- Question type (multiple_choice, true_false, short_answer, essay, etc.)
- Answer options with correct answer flagged
- Points per question

**Extraction is straightforward**. Map directly to our `quizzes`, `quiz_questions`, and `quiz_answers` tables.

If using manual export (IMSCC ZIP), quizzes are in **QTI format** (XML files). QTI 1.2 is verbose but parseable.

#### Path B: New Quizzes (Complex)

New Quizzes uses a separate LTI-based engine. The standard Canvas API **does not expose New Quiz questions**.

**Options if courses use New Quizzes**:

1. **QTI Export** (Recommended):
   - In Canvas, go to Settings → Export Course Content
   - Select "Quizzes" and export
   - New Quizzes can be exported as QTI 2.1 packages
   - Parse the QTI XML to extract questions and answers

2. **Manual Recreation**:
   - If export fails or is incomplete, manually copy quiz questions from Canvas
   - Enter them into a JSON/YAML file in our project
   - Import that file into the database
   - Labor-intensive but guaranteed to work

3. **Link-Out to Canvas** (Quickest Phase 1 option):
   - Instead of recreating quizzes in our app, link the student back to Canvas to take the quiz there
   - Pros: Zero quiz extraction work
   - Cons: Student leaves the app, needs a Canvas login, breaks the unified experience
   - Acceptable as a temporary measure while we build proper quiz import

**Recommendation**: Try QTI Export first. If it works cleanly, parse it. If not, manually recreate quizzes (there are likely only a few per course). Reserve link-out as a last resort.

#### Question Type Support Matrix

| Canvas Question Type | Our App Support | Phase |
|---------------------|----------------|-------|
| Multiple Choice | ✅ Full support | 3 |
| True/False | ✅ Full support | 3 |
| Short Answer / Fill in the Blank | ✅ Full support | 3 |
| Essay | ⚠️ Display only, manual grading by instructor | 3 |
| Matching | ✅ Drag-and-drop interface | 3 |
| Multiple Answers (checkboxes) | ✅ Full support | 3 |
| Numerical Answer | ✅ With tolerance range | 3 |
| File Upload | ❌ Not supported initially | Backlog |
| Formula (calculated) | ❌ Not supported initially | Backlog |

---

## 10. Authentication & Student Safety

### Auth System

**Provider**: Supabase Auth with email + password

**User Creation Flow** (Instructor creates accounts):
1. Instructor logs into admin panel
2. Creates a student account with email + password
3. Supabase sends a confirmation email to the student
4. Student clicks confirmation link → account is active
5. Student logs in at the app URL

**Alternative** (if student doesn't have email): Instructor can create the account and provide credentials directly. Disable email confirmation for this flow.

### Role-Based Access

| Role | Can Browse Content | Can Take Quizzes | Can View Own Progress | Can View All Progress | Can Sync Content | Can Manage Users |
|------|-------------------|------------------|----------------------|----------------------|-----------------|-----------------|
| Student | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Instructor | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

### Security Measures

- **Row Level Security (RLS)**: Enforced at database level (see Section 5)
- **Password Requirements**: Minimum 8 characters (Supabase default)
- **Session Management**: Supabase handles JWT tokens with automatic refresh
- **CSRF Protection**: Built into Next.js
- **Input Sanitization**: All user text input sanitized before storage (prevent XSS)
- **Content Sanitization**: Canvas HTML content sanitized with DOMPurify before rendering (Canvas HTML can contain scripts or weird embeds)

### Privacy Considerations (Student Age 10–15)

- No third-party analytics or tracking
- YouTube embeds use `youtube-nocookie.com` (privacy-enhanced mode)
- Student data stored only in Supabase (one jurisdiction)
- No data shared with third parties
- Instructor has ability to delete all student data

---

## 11. Deployment & Infrastructure

### Initial Setup

1. **Create a GitHub Repository**
   ```bash
   git init
   git remote add origin https://github.com/your-username/canvas-learning-hub.git
   ```

2. **Create Supabase Project**
   - Go to [supabase.com](https://supabase.com) → New Project
   - Choose a region close to the student (e.g., Sydney if in Australia)
   - Save the Project URL and API keys

3. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com) → Import GitHub repo
   - Set environment variables (Supabase URL, keys)
   - Deploy → get your `*.vercel.app` URL

### Free Tier Limits (Sufficient for 1 Student)

| Service | Free Tier Limit | Our Expected Usage |
|---------|----------------|-------------------|
| **Vercel** | 100GB bandwidth/month | < 1GB |
| **Vercel** | 100 hours serverless/month | < 5 hours |
| **Supabase** | 500MB database | < 50MB |
| **Supabase** | 1GB file storage | < 200MB (PDFs) |
| **Supabase** | 2GB bandwidth/month | < 500MB |
| **Supabase** | 50,000 monthly active users | 2 users |

**Verdict**: Free tier is massively sufficient. No cost unless the app scales significantly.

### When to Upgrade (Future Reference)

Upgrade to paid tiers if:
- More than 10 students
- File storage exceeds 1GB
- You need daily automated backups (Supabase free tier: weekly backups only)
- You need custom domain with SSL

---

## 12. Content Versioning & Sync Strategy

### Problem

The instructor may update content in Canvas. How does the app stay in sync?

### Strategy: Manual Re-Sync (Phase 1)

1. Instructor clicks "Sync from Canvas" in the admin panel
2. The sync script:
   - Fetches the latest content from Canvas (API or fresh export)
   - Compares with existing database content (by `canvas_item_id`)
   - **New items**: Insert into database
   - **Changed items**: Update content body / file
   - **Deleted items**: Mark as archived (don't hard-delete — preserve quiz attempt history)
3. Generates a sync report: "Added 2 items, Updated 5, Archived 1"

### What We Don't Do (For Now)

- No automatic scheduled sync (over-engineering for 1 student)
- No real-time sync (unnecessary complexity)
- No conflict resolution (instructor is the only content editor)

### Content Integrity Rules

- Never delete a quiz that has student attempts (archive it instead)
- Never delete a content item that has progress records (archive it instead)
- Keep a `sync_log` table recording every sync operation with timestamp and summary

---

## 13. Monitoring, Backups & Reliability

### Backups

| What | How | Frequency |
|------|-----|-----------|
| Database | Supabase automatic backups | Weekly (free tier), Daily (paid) |
| File storage | Supabase Storage (replicated by Supabase) | Continuous |
| Source code | GitHub repository | Every commit |
| Canvas export | Keep a local copy of IMSCC ZIP files | Once per sync |

**Recommendation**: After the initial import, download a Supabase database dump and store it locally as an extra backup. This is a 5-minute task.

### Monitoring (Lightweight)

For 1 student, heavy monitoring is unnecessary. Implement:

- **Vercel Analytics** (free, built-in): Page load times, errors
- **Console error logging**: Next.js logs server errors to Vercel logs automatically
- **Manual check**: Instructor should open the app weekly and verify content loads

### Uptime

- Vercel: 99.99% uptime SLA (even on free tier)
- Supabase: 99.9% uptime
- Practical impact: If either goes down, it's rare and temporary. Not a concern for 1 student.

---

## 14. Accessibility & iPad UX Considerations

### iPad-Specific Design Rules

1. **Touch Targets**: Minimum 44×44 points (Apple Human Interface Guidelines)
2. **Font Size**: Body text minimum 18px, headings proportionally larger
3. **Orientation**: Support both landscape and portrait. Test both.
4. **Safe Areas**: Respect iPad safe areas (notch, home indicator on newer iPads)
5. **Keyboard**: When text inputs are focused, ensure the content scrolls up so the input isn't hidden behind the on-screen keyboard
6. **Scrolling**: Use native scrolling (`-webkit-overflow-scrolling: touch` / `overflow-y: auto`). No custom scroll libraries.
7. **No Hover States**: iPad has no hover. Don't rely on hover for information or navigation. Everything must be accessible via tap.

### YouTube Embed Considerations

- Use `youtube-nocookie.com` domain
- Set `playsinline=1` attribute (prevents forced full-screen on iPhone, helpful on iPad too)
- Set `rel=0` to avoid showing unrelated videos after playback
- Responsive container: 16:9 aspect ratio that fills the content width
- Example embed:
  ```html
  <iframe
    src="https://www.youtube-nocookie.com/embed/VIDEO_ID?playsinline=1&rel=0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
    class="w-full aspect-video rounded-lg"
  />
  ```

### Accessibility (WCAG 2.1 Level A)

- Semantic HTML (`<main>`, `<nav>`, `<article>`, `<button>`)
- Alt text on all images
- Sufficient color contrast (4.5:1 for text)
- Focus indicators visible for keyboard/VoiceOver navigation
- VoiceOver testing: Navigate the app using VoiceOver on iPad to verify

---

## 15. Backlog & Future Enhancements

These items are **explicitly deferred** and should NOT be built in the initial release.

| ID | Enhancement | Rationale for Deferral |
|----|------------|----------------------|
| BL-01 | Custom quiz authoring (instructor creates quizzes in-app) | Phase 2 of assessment. Build after validating imported quizzes work. |
| BL-02 | Offline access (PWA with service worker caching) | Not needed for 1 student on WiFi. Revisit if usage patterns change. |
| BL-03 | Native iPad app (App Store) | Browser-based is sufficient. Consider only if PWA limitations become painful. |
| BL-04 | Multiple students | Requires roster management, bulk account creation, per-student analytics. |
| BL-05 | Multiple instructors | Requires instructor permissions, content ownership model. |
| BL-06 | File Upload question type | Complex to implement (storage, virus scanning, display). |
| BL-07 | Formula/Calculated question type | Requires math expression parser. |
| BL-08 | Automated Canvas sync (scheduled) | Manual sync is fine for 1 instructor. |
| BL-09 | Gamification (badges, streaks, points) | Nice-to-have for student motivation. Not MVP. |
| BL-10 | AI-powered study recommendations | Requires usage analytics and ML. Far future. |
| BL-11 | Custom domain | *.vercel.app is fine for now. Upgrade when needed. |
| BL-12 | Dark mode | Nice UX touch, not essential. |

---

## 16. Task Checklist

### Pre-Build Tasks

- [ ] **Check Canvas API token access** (Section 4, Step 1)
- [ ] **Identify quiz type** per course: Classic vs New Quizzes (Section 9)
- [ ] **Audit Word documents** across all 4 courses — count and list them (Section 8)
- [ ] **Convert Word docs to PDF** — manually or automated based on count (Section 8)
- [ ] **Create GitHub repository**
- [ ] **Create Supabase project** and note credentials
- [ ] **Create Vercel account** and link to GitHub

### Phase 1: Content Extraction

- [ ] Write Canvas content extraction script (API or IMSCC parser)
- [ ] Run content audit (generate report)
- [ ] Extract all HTML page content
- [ ] Extract all YouTube URLs
- [ ] Download all PDF files
- [ ] Download and convert all Word docs to PDF
- [ ] Extract all quiz questions and answers
- [ ] Store extracted content as intermediate JSON files
- [ ] Create Supabase database tables (run migration)
- [ ] Import content into Supabase database
- [ ] Upload files to Supabase Storage
- [ ] Run verification: compare Canvas source vs database counts

### Phase 2: Learning Hub App

- [ ] Initialize Next.js project with TypeScript + Tailwind
- [ ] Set up Supabase client (browser + server)
- [ ] Implement authentication (login page, session management)
- [ ] Create instructor + student accounts
- [ ] Set up Row Level Security policies
- [ ] Build course listing page
- [ ] Build module listing page
- [ ] Build content viewer — HTML content
- [ ] Build content viewer — YouTube embed
- [ ] Build content viewer — PDF viewer
- [ ] Build navigation (breadcrumbs, next/previous)
- [ ] Build "mark as complete" functionality
- [ ] Test on iPad Safari — all content types
- [ ] Deploy to Vercel

### Phase 3: Assessment Engine

- [ ] Build quiz listing (within modules)
- [ ] Build quiz start flow (create attempt)
- [ ] Build question display — multiple choice
- [ ] Build question display — true/false
- [ ] Build question display — short answer
- [ ] Build auto-save for responses
- [ ] Build quiz timer (if time-limited)
- [ ] Build quiz submission + auto-grading
- [ ] Build results page with per-question breakdown
- [ ] Build student progress dashboard
- [ ] Build instructor dashboard (view student results)
- [ ] Test quiz flow end-to-end on iPad

### Phase 4: Polish

- [ ] Error handling and friendly error pages
- [ ] Loading states and skeletons
- [ ] Content sanitization (DOMPurify for HTML)
- [ ] iPad UX testing (touch targets, orientation, keyboard)
- [ ] VoiceOver / accessibility check
- [ ] Performance check (page load times)
- [ ] Manual backup of database

---

## 17. Decision Log

| Date | Decision | Rationale | Alternatives Considered |
|------|----------|-----------|------------------------|
| 2026-03-21 | Use Next.js + Supabase + Vercel | Single-project fullstack, free tier sufficient for 1 student, built-in auth and storage | SvelteKit, Remix, Django + React, Firebase |
| 2026-03-21 | Browser-based, not native iPad app | Zero install friction, instant updates, no App Store review process | React Native, Flutter, PWA |
| 2026-03-21 | Email + password auth | Simple, no dependencies on third-party OAuth | Magic links, class codes, Canvas SSO |
| 2026-03-21 | Convert Word docs to PDF at import time | iPad Safari cannot render .docx in-browser. PDF is universally supported. | Google Docs Viewer embed, Office Online embed, runtime conversion |
| 2026-03-21 | YouTube privacy-enhanced mode | Student is a minor (10-15). Minimize tracking. | Standard YouTube embeds |
| 2026-03-21 | Skip offline access | 1 student on WiFi, unnecessary complexity | PWA with service worker, native app with local DB |
| 2026-03-21 | Free subdomain (*.vercel.app) | No cost, sufficient for 1 student | Custom domain ($10-15/year) |
| 2026-03-21 | Manual content sync (not automated) | 1 instructor, infrequent updates. Automated sync is over-engineering. | Cron job, webhook-based sync |

---

## 18. Glossary

| Term | Definition |
|------|-----------|
| **Canvas LMS** | Learning Management System used by educational institutions. The source of our content. |
| **Supabase** | An open-source Firebase alternative providing database, auth, and file storage. |
| **Vercel** | A cloud platform for deploying web applications (especially Next.js). |
| **Next.js** | A React-based framework for building web applications with server-side rendering. |
| **RLS (Row Level Security)** | Database security feature that restricts which rows a user can read/write based on their identity. |
| **API Token** | A secret key that allows programmatic access to Canvas data. |
| **IMSCC** | IMS Common Cartridge — a standard format for exporting e-learning course content. |
| **QTI** | Question and Test Interoperability — an XML standard for representing quiz questions. |
| **PWA** | Progressive Web App — a website that can behave like a native app (home screen icon, offline access). |
| **LTI** | Learning Tools Interoperability — a standard for integrating external tools with an LMS. |
| **JWT** | JSON Web Token — used for session management in authentication. |
| **DOMPurify** | A JavaScript library that sanitizes HTML to prevent XSS (cross-site scripting) attacks. |
| **WCAG** | Web Content Accessibility Guidelines — standards for making web content accessible. |
| **HIG** | Human Interface Guidelines — Apple's design guidelines for iOS/iPad apps. |

---

> **Next Step**: Complete the three pre-build investigation tasks (API token check, quiz type identification, Word doc audit), then proceed to Phase 1.
