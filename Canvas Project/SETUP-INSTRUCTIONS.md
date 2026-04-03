# Canvas Data Export — Setup Instructions

> **Purpose:** Export all your Canvas LMS data (courses, quizzes, assignments, files, grades) before your account is closed.

---

## Step 1: Check if Python is Installed

1. Press **Win + R**, type `cmd`, press Enter to open Command Prompt
2. Type:
   ```
   python --version
   ```
3. If you see something like `Python 3.11.5` → ✅ Python is installed, skip to Step 2

### If Python is NOT installed:

1. Go to **https://www.python.org/downloads/**
2. Click the big yellow **"Download Python 3.x.x"** button
3. Run the installer
4. ⚠️ **IMPORTANT:** Tick the checkbox **"Add Python to PATH"** at the bottom of the first screen
5. Click "Install Now"
6. Close and reopen Command Prompt, then try `python --version` again

---

## Step 2: Install the `requests` Library

In Command Prompt, type:

```
pip install requests
```

You should see `Successfully installed requests-...`. If you get an error about `pip` not being found, try:

```
python -m pip install requests
```

---

## Step 3: Set Up Your Canvas API Token

### Create the token in Canvas:

1. Log in to **https://k12.instructure.com**
2. Click your **profile picture** (top-left) → **Settings**
3. Scroll down to **"Approved Integrations"**
4. Click **"+ New Access Token"**
5. Purpose: type `Data Export`
6. Leave expiry blank (or set it for tomorrow)
7. Click **"Generate Token"**
8. **Copy the token** — you won't be able to see it again!

### Save the token:

1. Open **Notepad**
2. Paste the token (it looks like a long string of numbers and letters)
3. Make sure there are **no extra spaces or blank lines** — just the token
4. Save As → navigate to:
   ```
   c:\Users\F043435\OneDrive - Westpac Group\New Amp experimentation folder\Learning App
   ```
5. Filename: `canvas_token.txt`
6. Save as type: **All Files (\*.\*)**
7. Click Save

> ⚠️ **SECURITY:** Never share `canvas_token.txt` or upload it anywhere. It gives full access to your Canvas account.

---

## Step 4: Run the Export

1. Open **Command Prompt** (Win + R → `cmd` → Enter)
2. Navigate to the folder:
   ```
   cd "c:\Users\F043435\OneDrive - Westpac Group\New Amp experimentation folder\Learning App"
   ```
3. Run the script:
   ```
   python canvas_export.py
   ```

---

## Step 5: What to Expect

- The script will first test your API connection and show your Canvas username
- It then lists all your courses and exports them one by one
- You'll see progress like:
  ```
  📚 Exporting course: Algebra 2
    📊 Exporting grades...
    📋 Exporting syllabus...
    📦 Exporting modules...
      Module: Unit 1 - Linear Functions
        📥 File: worksheet.pdf
    📝 Exporting quizzes...
      Quiz: Chapter 1 Test
    📄 Exporting assignments...
  ```

### How long will it take?

- **5–10 courses:** ~5–15 minutes
- **10+ courses with lots of files:** ~20–45 minutes
- Large file downloads (videos, big PDFs) take the most time

**Don't close the Command Prompt window while it's running!**

---

## Step 6: Troubleshooting

### "python is not recognized..."
- Python isn't in your PATH. Reinstall Python and make sure to tick **"Add Python to PATH"**

### "ModuleNotFoundError: No module named 'requests'"
- Run: `pip install requests`
- If that doesn't work: `python -m pip install requests`

### "ERROR: canvas_token.txt not found!"
- Make sure the file is in the same folder as `canvas_export.py`
- Make sure it's named exactly `canvas_token.txt` (not `canvas_token.txt.txt`)
- Check: in File Explorer, go to View → tick "File name extensions" to see the real extension

### "Authentication failed" or "401" errors
- Your API token may be wrong or expired
- Go back to Canvas Settings and generate a new token
- Replace the contents of `canvas_token.txt` with the new token

### "SSL: CERTIFICATE_VERIFY_FAILED"
- This can happen on corporate networks. Try:
  ```
  pip install pip-system-certs
  ```
  Then run the export again.
- If that doesn't work, you may need to run from a personal device without the corporate proxy.

### "Access denied" or "403" on some items
- This is normal! Some courses or resources may be locked
- The script logs these and keeps going
- Check `canvas-export/_errors.json` to see what was skipped

### "Permission denied" when saving files
- Close any open files in the `canvas-export` folder
- Make sure OneDrive isn't syncing that folder right now

### Script seems stuck
- It pauses briefly between API calls (to avoid being rate-limited)
- If it's been stuck for more than 5 minutes on one item, press **Ctrl+C** to stop, then run it again (it won't overwrite existing files)

---

## Step 7: After the Export

### Verify Your Data

1. Open the `canvas-export` folder — you should see one subfolder per course
2. Open `canvas-export/_export_summary.json` to see totals
3. Spot-check:
   - Open a quiz folder → check `questions.json` has your quiz questions
   - Open a course folder → check `_grades.json` has your grades
   - Open the `files` folder → check PDFs/documents open correctly

### If something is missing

1. Check `canvas-export/_errors.json` for any failed downloads
2. Re-run the script — it will re-fetch everything (overwrites existing files)
3. Some content may be locked by teachers and inaccessible via the API

### Keep your data safe

- Copy the entire `canvas-export` folder to a USB drive or cloud storage as a backup
- The export includes JSON files (data) and original files (PDFs, docs, etc.)

---

## Quick Reference

| Command | What it does |
|---------|-------------|
| `python --version` | Check Python is installed |
| `pip install requests` | Install required library |
| `python canvas_export.py` | Run the export |
| `cd "c:\Users\F043435\OneDrive - Westpac Group\New Amp experimentation folder\Learning App"` | Navigate to the right folder |
