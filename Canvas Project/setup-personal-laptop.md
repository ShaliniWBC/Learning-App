# 🖥️ Personal Laptop Setup Guide — Learning App

> **For**: Shalini's personal Windows 11 laptop
> **Purpose**: Get everything set up to build the Learning App with Claude Code
> **Time needed**: ~30 minutes (plus 15-45 min for Canvas export)

---

## Section 1: Check What You Already Have

### ✅ Check VS Code

Open VS Code from your Start menu or taskbar → if it opens, you're good. ✅ Done.

### ✅ Check Claude Code Extension

1. Open VS Code
2. Click the **Extensions** icon on the left sidebar (looks like 4 squares, or press **Ctrl+Shift+X**)
3. In the search box, type **"Claude"**
4. If you see **"Claude" by Anthropic** with a green **"Installed"** label → ✅ already installed
5. If NOT installed → click **"Install"** on the "Claude" extension by Anthropic
6. After installing, you'll see a **Claude icon** in the left sidebar
7. Click it and **sign in with your Claude Max account**

### ✅ Check Git

1. Open **Command Prompt** (press **Win + R** → type `cmd` → press **Enter**)
2. Type:
   ```
   git --version
   ```
3. If you see `git version 2.x.x` → ✅ Git is installed
4. If you see **"not recognized"** → Git is NOT installed, follow the steps below to install it

### 📥 Install Git (only if NOT already installed)

1. Go to https://git-scm.com/download/win
2. Download the **64-bit installer**
3. Run the installer
4. **Accept all defaults** (click Next through everything)
5. **IMPORTANT**: On the "Adjusting your PATH" screen, keep the default: **"Git from the command line and also from 3rd-party software"**
6. Click **Install**, then **Finish**
7. **Close and reopen** Command Prompt
8. Verify by typing:
   ```
   git --version
   ```

### ✅ Check Python

1. In Command Prompt, type:
   ```
   python --version
   ```
2. If you see `Python 3.x.x` → ✅ installed (you already did this)

---

## Section 2: Connect Git to Your GitHub Account

1. Open **Command Prompt**
2. Set your name:
   ```
   git config --global user.name "Claudeagent11"
   ```
3. Set your email (use the email you signed up to GitHub with):
   ```
   git config --global user.email "your-email@example.com"
   ```
4. Verify it worked:
   ```
   git config --list
   ```
   You should see your name and email in the output.

---

## Section 3: Clone Your GitHub Repo

1. Open **Command Prompt**
2. Navigate to your user folder:
   ```
   cd C:\Users\Shali
   ```
3. Clone the repo:
   ```
   git clone https://github.com/Claudeagent11/Learning-App.git
   ```
4. Navigate into the repo:
   ```
   cd Learning-App
   ```
5. Verify the contents:
   ```
   dir
   ```
   You should see the repo files listed.

> 💡 **Note**: If the repo is private, GitHub may ask you to log in. A browser window will open — sign in with your GitHub account.

---

## Section 4: Set Up Your Project Folder Structure

Your Learning App project lives at: **`C:\Users\Shali\Learning-App`** (this is the cloned repo).

Copy these files into the project folder:

1. Copy **`canvas_export.py`** into `C:\Users\Shali\Learning-App\`
2. Copy **`canvas_token.txt`** into `C:\Users\Shali\Learning-App\`

> ⚠️ **NEVER commit `canvas_token.txt` to GitHub!** The `.gitignore` file already excludes it, but be careful.

---

## Section 5: Install Your Claude Skills

The skills are stored in the GitHub repo under `skills-library/`.

1. Create the skills config directory. In **Command Prompt**:
   ```
   mkdir C:\Users\Shali\.config\agents\skills
   ```
2. Copy all skills from the repo into the config directory:
   ```
   xcopy /E /I "C:\Users\Shali\Learning-App\skills-library\*" "C:\Users\Shali\.config\agents\skills\"
   ```
3. Verify they copied:
   ```
   dir C:\Users\Shali\.config\agents\skills
   ```
   You should see all the skill folders listed.

---

## Section 6: Set Up Your Personal AGENTS.md

1. Create the Claude config directory:
   ```
   mkdir C:\Users\Shali\.config\claude
   ```
2. Copy your personal AGENTS.md into it:
   ```
   copy "C:\Users\Shali\Learning-App\personal-AGENTS.md" "C:\Users\Shali\.config\claude\AGENTS.md"
   ```

> 💡 This tells Claude about you and your project every time you start a new conversation.

---

## Section 7: Run the Canvas Export

1. Make sure **`canvas_token.txt`** is in `C:\Users\Shali\Learning-App\`
2. Open **Command Prompt**
3. Navigate to the project:
   ```
   cd C:\Users\Shali\Learning-App
   ```
4. Install the `requests` library:
   ```
   pip install requests
   ```
5. Run the export script:
   ```
   python canvas_export.py
   ```
6. **Wait** for it to finish (this takes **15-45 minutes** depending on how much data there is)
7. When it's done, check the **`canvas-export`** folder for your data:
   ```
   dir canvas-export
   ```

---

## Section 8: Push Your Code to GitHub (but NOT your data or token)

The `.gitignore` file already excludes `canvas_token.txt` and `canvas-export/` — your sensitive data won't be uploaded.

1. In **Command Prompt**, make sure you're in the Learning-App folder:
   ```
   cd C:\Users\Shali\Learning-App
   ```
2. Stage all files:
   ```
   git add .
   ```
3. Commit:
   ```
   git commit -m "Initial setup with export script and skills"
   ```
4. Push to GitHub:
   ```
   git push
   ```
5. Go to https://github.com/Claudeagent11/Learning-App in your browser to verify your files are there

---

## ✅ Final Checklist

Go through this list to make sure everything is set up:

- [ ] VS Code installed
- [ ] Claude Code extension installed and signed in
- [ ] Git installed and configured
- [ ] GitHub repo cloned to `C:\Users\Shali\Learning-App`
- [ ] Python installed
- [ ] `requests` library installed
- [ ] `canvas_token.txt` created with API token
- [ ] Skills copied to `C:\Users\Shali\.config\agents\skills\`
- [ ] Personal AGENTS.md copied to `C:\Users\Shali\.config\claude\AGENTS.md`
- [ ] Canvas export script run successfully
- [ ] Data verified in `canvas-export` folder

---

## ⚡ Reminders

- 🔴 **URGENT**: Run the Canvas export **BEFORE April 6, 2026**
- ⚠️ **NEVER** commit `canvas_token.txt` to GitHub
- ⚠️ The `canvas-export/` data folder is excluded from GitHub (too large)
- 💡 Back up the `canvas-export` folder to a USB drive or cloud storage after export
