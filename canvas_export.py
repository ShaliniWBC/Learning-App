"""
Canvas LMS Complete Data Export Script
=======================================
Created for urgent Canvas data export from k12.instructure.com.

Exports ALL student data: courses, modules, files, quizzes (with questions
and submission answers), assignments (with submissions), grades, pages,
announcements, syllabus, and external links.

API token is read from canvas_token.txt (never commit this file).

Usage: python canvas_export.py
"""

import os
import sys
import json
import time
import re
import requests
from datetime import datetime
from urllib.parse import urlparse, unquote

# === Configuration ===
API_BASE = "https://k12.instructure.com/api/v1"
EXPORT_DIR = "canvas-export"
TOKEN_FILE = "canvas_token.txt"
RATE_LIMIT_DELAY = 0.3  # seconds between API calls
MAX_RETRIES = 3
PER_PAGE = 100

# === Globals for summary ===
stats = {
    "courses": 0,
    "modules": 0,
    "files_downloaded": 0,
    "quizzes": 0,
    "assignments": 0,
    "pages": 0,
    "announcements": 0,
    "errors": 0,
}
errors_log = []


def sanitize_name(name):
    """Remove illegal Windows filename characters and trim."""
    if not name:
        return "unnamed"
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    name = name.strip('. ')
    return name[:200] if name else "unnamed"


def load_token():
    """Read API token from canvas_token.txt."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(script_dir, TOKEN_FILE)

    if not os.path.exists(token_path):
        print("=" * 60)
        print("ERROR: canvas_token.txt not found!")
        print("=" * 60)
        print()
        print("To create your API token:")
        print("1. Log in to https://k12.instructure.com")
        print("2. Go to Account > Settings")
        print("3. Scroll to 'Approved Integrations'")
        print("4. Click '+ New Access Token'")
        print("5. Give it a name like 'Data Export'")
        print("6. Copy the token")
        print()
        print(f"Then create a file called '{TOKEN_FILE}' in:")
        print(f"  {script_dir}")
        print("and paste ONLY the token into it (nothing else).")
        print()
        print("IMPORTANT: Never share this token or commit it to GitHub!")
        sys.exit(1)

    with open(token_path, 'r', encoding='utf-8') as f:
        token = f.read().strip()

    if not token:
        print("ERROR: canvas_token.txt is empty. Paste your API token into it.")
        sys.exit(1)

    return token


def api_get(endpoint, token, params=None):
    """Make a GET request to Canvas API with pagination, retries, and rate limiting."""
    url = endpoint if endpoint.startswith("http") else f"{API_BASE}{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}
    if params is None:
        params = {}
    params.setdefault("per_page", PER_PAGE)

    all_results = []

    while url:
        time.sleep(RATE_LIMIT_DELAY)

        for attempt in range(1, MAX_RETRIES + 1):
            try:
                resp = requests.get(url, headers=headers, params=params, timeout=30)

                if resp.status_code == 429:
                    wait = min(2 ** attempt, 30)
                    print(f"    Rate limited. Waiting {wait}s (attempt {attempt}/{MAX_RETRIES})...")
                    time.sleep(wait)
                    continue

                if resp.status_code >= 500:
                    wait = 2 ** attempt
                    print(f"    Server error {resp.status_code}. Retrying in {wait}s...")
                    time.sleep(wait)
                    continue

                if resp.status_code == 401:
                    log_error("Authentication failed", url, "Check your API token")
                    return None

                if resp.status_code == 403:
                    log_error("Access denied", url, "You may not have permission")
                    return None

                if resp.status_code == 404:
                    return None

                resp.raise_for_status()
                break

            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES:
                    log_error(f"Request failed after {MAX_RETRIES} retries", url, str(e))
                    return None
                wait = 2 ** attempt
                print(f"    Request error. Retrying in {wait}s...")
                time.sleep(wait)
        else:
            log_error("Max retries exceeded", url, "")
            return None

        data = resp.json()
        if isinstance(data, list):
            all_results.extend(data)
        else:
            return data

        # Handle pagination via Link header
        url = None
        params = {}  # params already in the next URL
        link_header = resp.headers.get("Link", "")
        for part in link_header.split(","):
            if 'rel="next"' in part:
                url = part.split("<")[1].split(">")[0]
                break

    return all_results


def api_get_single(endpoint, token, params=None):
    """GET a single object (not paginated list)."""
    url = endpoint if endpoint.startswith("http") else f"{API_BASE}{endpoint}"
    headers = {"Authorization": f"Bearer {token}"}
    if params is None:
        params = {}

    time.sleep(RATE_LIMIT_DELAY)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)

            if resp.status_code == 429:
                time.sleep(min(2 ** attempt, 30))
                continue
            if resp.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            if resp.status_code in (401, 403, 404):
                return None

            resp.raise_for_status()
            return resp.json()

        except requests.exceptions.RequestException:
            if attempt == MAX_RETRIES:
                return None
            time.sleep(2 ** attempt)

    return None


def download_file(url, dest_path, token):
    """Download a file, following redirects. Returns True on success."""
    headers = {"Authorization": f"Bearer {token}"}
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    time.sleep(RATE_LIMIT_DELAY)

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = requests.get(url, headers=headers, stream=True, timeout=60, allow_redirects=True)

            if resp.status_code == 429:
                time.sleep(min(2 ** attempt, 30))
                continue
            if resp.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            if resp.status_code in (401, 403, 404):
                log_error("Cannot download file", url, f"HTTP {resp.status_code}")
                return False

            resp.raise_for_status()

            with open(dest_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)

            stats["files_downloaded"] += 1
            return True

        except requests.exceptions.RequestException as e:
            if attempt == MAX_RETRIES:
                log_error("File download failed", url, str(e))
                return False
            time.sleep(2 ** attempt)

    return False


def log_error(context, url, detail):
    """Log an error for the summary."""
    stats["errors"] += 1
    errors_log.append({
        "context": context,
        "url": url,
        "detail": detail,
        "time": datetime.now().isoformat(),
    })
    print(f"    ⚠ ERROR: {context} — {detail}")


def save_json(data, path):
    """Save data as formatted JSON."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False, default=str)


def save_html(content, path):
    """Save HTML content to file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content or "")


def makedirs(path):
    """Create directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)


# === Export Functions ===

def export_course_info(course, course_dir, token):
    """Export basic course information."""
    save_json(course, os.path.join(course_dir, "_course_info.json"))


def export_grades(course_id, course_dir, token):
    """Export student's grades/enrollments for this course."""
    print("  📊 Exporting grades...")
    enrollments = api_get(f"/courses/{course_id}/enrollments", token, {"type[]": "StudentEnrollment"})
    if enrollments:
        save_json(enrollments, os.path.join(course_dir, "_grades.json"))


def export_syllabus(course_id, course_dir, token):
    """Export course syllabus."""
    print("  📋 Exporting syllabus...")
    course_data = api_get_single(f"/courses/{course_id}", token, {"include[]": "syllabus_body"})
    if course_data and course_data.get("syllabus_body"):
        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Syllabus - {course_data.get('name', '')}</title></head>
<body>
<h1>Syllabus: {course_data.get('name', '')}</h1>
{course_data['syllabus_body']}
</body></html>"""
        save_html(html, os.path.join(course_dir, "_syllabus.html"))


def export_modules(course_id, course_dir, token):
    """Export all modules and their items."""
    print("  📦 Exporting modules...")
    modules = api_get(f"/courses/{course_id}/modules", token, {"include[]": "items"})
    if not modules:
        print("    No modules found.")
        return

    modules_dir = os.path.join(course_dir, "modules")
    external_links = []

    for mod in modules:
        stats["modules"] += 1
        position = mod.get("position", 0)
        mod_name = sanitize_name(mod.get("name", "Unnamed Module"))
        mod_folder = os.path.join(modules_dir, f"{position:02d} - {mod_name}")
        makedirs(mod_folder)

        print(f"    Module: {mod_name}")

        save_json(mod, os.path.join(mod_folder, "_module_info.json"))

        # Get module items
        items = api_get(f"/courses/{course_id}/modules/{mod['id']}/items", token)
        if not items:
            continue

        for item in items:
            item_type = item.get("type", "")
            item_title = sanitize_name(item.get("title", "unnamed"))

            if item_type == "File":
                file_dir = os.path.join(mod_folder, "files")
                makedirs(file_dir)
                # Get file info to find the download URL
                if item.get("url"):
                    file_info = api_get_single(item["url"], token)
                    if file_info and file_info.get("url"):
                        filename = sanitize_name(file_info.get("display_name") or file_info.get("filename") or item_title)
                        dest = os.path.join(file_dir, filename)
                        print(f"      📥 File: {filename}")
                        download_file(file_info["url"], dest, token)

            elif item_type == "Page":
                pages_dir = os.path.join(mod_folder, "pages")
                makedirs(pages_dir)
                page_url = item.get("page_url")
                if page_url:
                    page_data = api_get_single(f"/courses/{course_id}/pages/{page_url}", token)
                    if page_data:
                        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{page_data.get('title', '')}</title></head>
<body>
<h1>{page_data.get('title', '')}</h1>
{page_data.get('body', '')}
</body></html>"""
                        save_html(html, os.path.join(pages_dir, f"{item_title}.html"))

            elif item_type == "ExternalUrl":
                external_links.append({
                    "title": item.get("title"),
                    "url": item.get("external_url"),
                    "module": mod.get("name"),
                })

            elif item_type == "ExternalTool":
                external_links.append({
                    "title": item.get("title"),
                    "url": item.get("external_url") or item.get("url"),
                    "module": mod.get("name"),
                    "type": "ExternalTool",
                })

    # Save external links
    if external_links:
        links_dir = os.path.join(course_dir, "external_links")
        makedirs(links_dir)
        save_json(external_links, os.path.join(links_dir, "links.json"))


def export_quizzes(course_id, course_dir, token):
    """Export all quizzes with questions and submissions."""
    print("  📝 Exporting quizzes...")
    quizzes = api_get(f"/courses/{course_id}/quizzes", token)
    if not quizzes:
        print("    No quizzes found.")
        return

    quizzes_dir = os.path.join(course_dir, "quizzes")

    for quiz in quizzes:
        stats["quizzes"] += 1
        quiz_name = sanitize_name(quiz.get("title", "Unnamed Quiz"))
        quiz_folder = os.path.join(quizzes_dir, quiz_name)
        makedirs(quiz_folder)

        print(f"    Quiz: {quiz_name}")

        # Save quiz info
        save_json(quiz, os.path.join(quiz_folder, "quiz_info.json"))

        quiz_id = quiz["id"]

        # Get questions
        questions = api_get(f"/courses/{course_id}/quizzes/{quiz_id}/questions", token)
        if questions:
            save_json(questions, os.path.join(quiz_folder, "questions.json"))

        # Get submissions
        submissions = api_get(f"/courses/{course_id}/quizzes/{quiz_id}/submissions", token)
        submission_data = []

        if submissions:
            # Canvas wraps quiz submissions in a key
            if isinstance(submissions, dict):
                sub_list = submissions.get("quiz_submissions", [])
            else:
                sub_list = submissions

            for sub in sub_list:
                sub_entry = dict(sub)
                sub_id = sub.get("id")

                # Try to get the actual answers for this submission
                if sub_id:
                    answers = api_get(
                        f"/quiz_submissions/{sub_id}/questions",
                        token,
                    )
                    if answers:
                        sub_entry["submission_questions"] = answers

                submission_data.append(sub_entry)

        if submission_data:
            save_json(submission_data, os.path.join(quiz_folder, "my_submissions.json"))


def export_assignments(course_id, course_dir, token):
    """Export all assignments with submissions."""
    print("  📄 Exporting assignments...")
    assignments = api_get(f"/courses/{course_id}/assignments", token)
    if not assignments:
        print("    No assignments found.")
        return

    assignments_dir = os.path.join(course_dir, "assignments")

    for assignment in assignments:
        stats["assignments"] += 1
        asgn_name = sanitize_name(assignment.get("name", "Unnamed Assignment"))
        asgn_folder = os.path.join(assignments_dir, asgn_name)
        makedirs(asgn_folder)

        print(f"    Assignment: {asgn_name}")

        save_json(assignment, os.path.join(asgn_folder, "assignment_info.json"))

        asgn_id = assignment["id"]

        # Get student's own submission
        submission = api_get_single(
            f"/courses/{course_id}/assignments/{asgn_id}/submissions/self",
            token,
        )
        if submission:
            save_json(submission, os.path.join(asgn_folder, "my_submission.json"))

            # Download any submitted files
            attachments = submission.get("attachments", [])
            if attachments:
                files_dir = os.path.join(asgn_folder, "submitted_files")
                makedirs(files_dir)
                for att in attachments:
                    filename = sanitize_name(att.get("display_name") or att.get("filename") or "file")
                    dl_url = att.get("url")
                    if dl_url:
                        print(f"      📥 Submitted file: {filename}")
                        download_file(dl_url, os.path.join(files_dir, filename), token)


def export_files(course_id, course_dir, token):
    """Export all course files."""
    print("  📁 Exporting course files...")
    files = api_get(f"/courses/{course_id}/files", token)
    if not files:
        print("    No files found (or no access).")
        return

    files_dir = os.path.join(course_dir, "files")
    makedirs(files_dir)

    for f in files:
        filename = sanitize_name(f.get("display_name") or f.get("filename") or "file")
        dl_url = f.get("url")
        if dl_url:
            print(f"    📥 File: {filename}")
            download_file(dl_url, os.path.join(files_dir, filename), token)


def export_pages(course_id, course_dir, token):
    """Export all wiki pages."""
    print("  📄 Exporting pages...")
    pages = api_get(f"/courses/{course_id}/pages", token)
    if not pages:
        print("    No pages found.")
        return

    pages_dir = os.path.join(course_dir, "pages")
    makedirs(pages_dir)

    for page in pages:
        stats["pages"] += 1
        page_url = page.get("url")
        page_title = sanitize_name(page.get("title", "unnamed"))

        if page_url:
            full_page = api_get_single(f"/courses/{course_id}/pages/{page_url}", token)
            if full_page:
                html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{full_page.get('title', '')}</title></head>
<body>
<h1>{full_page.get('title', '')}</h1>
{full_page.get('body', '')}
</body></html>"""
                save_html(html, os.path.join(pages_dir, f"{page_title}.html"))


def export_announcements(course_id, course_dir, token):
    """Export course announcements."""
    print("  📢 Exporting announcements...")
    announcements = api_get(
        "/announcements",
        token,
        {"context_codes[]": f"course_{course_id}"},
    )
    if not announcements:
        print("    No announcements found.")
        return

    stats["announcements"] += len(announcements)
    ann_dir = os.path.join(course_dir, "announcements")
    makedirs(ann_dir)
    save_json(announcements, os.path.join(ann_dir, "announcements.json"))


def export_course(course, token):
    """Export everything for a single course."""
    course_id = course["id"]
    course_name = sanitize_name(course.get("name") or course.get("course_code") or str(course_id))

    print()
    print(f"{'=' * 60}")
    print(f"📚 Exporting course: {course_name}")
    print(f"{'=' * 60}")

    course_dir = os.path.join(EXPORT_DIR, course_name)
    makedirs(course_dir)

    export_course_info(course, course_dir, token)
    export_grades(course_id, course_dir, token)
    export_syllabus(course_id, course_dir, token)
    export_modules(course_id, course_dir, token)
    export_quizzes(course_id, course_dir, token)
    export_assignments(course_id, course_dir, token)
    export_files(course_id, course_dir, token)
    export_pages(course_id, course_dir, token)
    export_announcements(course_id, course_dir, token)


def main():
    print()
    print("=" * 60)
    print("  Canvas LMS Complete Data Export")
    print("  k12.instructure.com")
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    # Step 1: Load token
    print()
    print("🔑 Reading API token...")
    token = load_token()
    print("   Token loaded.")

    # Step 2: Test connection
    print()
    print("🔗 Testing API connection...")
    user = api_get_single("/users/self", token)
    if not user:
        print("ERROR: Could not connect to Canvas API.")
        print("Check your API token and internet connection.")
        sys.exit(1)
    print(f"   Connected as: {user.get('name', 'Unknown')} ({user.get('login_id', '')})")

    # Step 3: Get all courses
    print()
    print("📚 Fetching course list...")
    courses = api_get("/courses", token, {
        "enrollment_state": "active",
        "include[]": "term",
        "state[]": "available",
    })

    if not courses:
        # Try without filters
        courses = api_get("/courses", token)

    if not courses:
        print("No courses found. You may not have any active enrollments.")
        sys.exit(0)

    # Filter out invalid entries (sometimes Canvas returns empty dicts)
    courses = [c for c in courses if isinstance(c, dict) and c.get("id")]
    stats["courses"] = len(courses)

    print(f"   Found {len(courses)} courses:")
    for c in courses:
        print(f"     - {c.get('name', 'Unknown')} (ID: {c['id']})")

    # Step 4: Create export directory
    makedirs(EXPORT_DIR)

    # Step 5: Export each course
    for course in courses:
        try:
            export_course(course, token)
        except Exception as e:
            log_error(f"Failed to export course: {course.get('name')}", "", str(e))
            print(f"  ❌ Error exporting course, continuing to next...")

    # Step 6: Save export summary
    summary = {
        "export_date": datetime.now().isoformat(),
        "user": user.get("name", "Unknown"),
        "courses_exported": stats["courses"],
        "modules_exported": stats["modules"],
        "files_downloaded": stats["files_downloaded"],
        "quizzes_exported": stats["quizzes"],
        "assignments_exported": stats["assignments"],
        "pages_exported": stats["pages"],
        "announcements_exported": stats["announcements"],
        "errors": stats["errors"],
        "course_list": [
            {"id": c["id"], "name": c.get("name", "")}
            for c in courses
        ],
    }
    save_json(summary, os.path.join(EXPORT_DIR, "_export_summary.json"))

    # Save errors log
    if errors_log:
        save_json(errors_log, os.path.join(EXPORT_DIR, "_errors.json"))

    # Step 7: Print summary
    print()
    print("=" * 60)
    print("  EXPORT COMPLETE!")
    print("=" * 60)
    print()
    print(f"  📚 Courses:       {stats['courses']}")
    print(f"  📦 Modules:       {stats['modules']}")
    print(f"  📥 Files:         {stats['files_downloaded']}")
    print(f"  📝 Quizzes:       {stats['quizzes']}")
    print(f"  📄 Assignments:   {stats['assignments']}")
    print(f"  📄 Pages:         {stats['pages']}")
    print(f"  📢 Announcements: {stats['announcements']}")
    print(f"  ⚠  Errors:        {stats['errors']}")
    print()
    print(f"  Data saved to: {os.path.abspath(EXPORT_DIR)}")

    if errors_log:
        print(f"  Error details: {os.path.join(os.path.abspath(EXPORT_DIR), '_errors.json')}")

    print()
    end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"  Finished: {end_time}")
    print()


if __name__ == "__main__":
    main()
