# GitHub for Beginners — A Plain-English Guide

## 🤔 What IS GitHub?

Think of GitHub as **Google Drive for code** — but with superpowers. It's a website (github.com) where people store, share, and collaborate on code projects. The projects are stored in **repositories** (or "repos" for short), which are basically folders that track every change ever made.

---

## 📦 What is a Repository (Repo)?

A **repository** is like a project folder that remembers everything. Imagine a Word document that keeps every version you've ever saved — that's what a repo does for code files.

- **Public repos** → Anyone on the internet can see them (like a public Google Doc)
- **Private repos** → Only people you invite can see them (like a private Google Doc)

---

## ✅ What You CAN Do on GitHub

### 🟢 Without Any Coding Knowledge

| Action | What It Means | Real-World Analogy |
|--------|--------------|-------------------|
| **Browse repos** | Look at other people's code and projects | Window shopping |
| **Star a repo** ⭐ | Bookmark a project you like | Adding a favourite in your browser |
| **Fork a repo** 🍴 | Make your own copy of someone else's project | Photocopying a recipe to modify at home |
| **Download a repo** | Get all the files onto your computer | Downloading a ZIP file |
| **Read documentation** | Most repos have a README file explaining the project | Reading the instruction manual |
| **Report issues** 🐛 | Tell the project owner about a bug or suggest a feature | Leaving feedback on a product |
| **Discuss** 💬 | Join conversations about projects | Commenting on a forum post |
| **Create a repo** | Start your own project | Creating a new folder on your computer |
| **Upload files** | Add files directly through the website | Uploading to Google Drive |
| **Edit files** ✏️ | Make changes to files right in your browser | Editing a Google Doc |
| **Use GitHub Pages** 🌐 | Host a simple website for FREE | Publishing a blog |

### 🟡 With Basic Git Knowledge (Learnable in a Day)

| Action | What It Means | Real-World Analogy |
|--------|--------------|-------------------|
| **Clone** | Download a repo to your computer with full history | Moving a shared folder to your laptop |
| **Commit** | Save a snapshot of your changes with a description | Saving a version with a sticky note |
| **Push** | Upload your saved changes to GitHub | Syncing your local folder back to the cloud |
| **Pull** | Download the latest changes others made | Refreshing a shared document |
| **Branch** 🌿 | Create a separate workspace to try things without breaking the main project | Making a draft copy before editing the original |
| **Merge** | Combine your branch back into the main project | Accepting tracked changes in Word |
| **Pull Request (PR)** | Ask the project owner to review and accept your changes | Submitting your draft for approval |

### 🔵 Intermediate Features

| Action | What It Means |
|--------|--------------|
| **GitHub Actions** | Automate tasks (e.g., run tests every time code changes) |
| **Projects** | Kanban boards for task management (like Trello) |
| **Releases** | Package and publish versions of your software |
| **Wiki** | Create documentation pages for your project |
| **Codespaces** | Write code directly in your browser (no setup needed!) |

---

## ❌ What You CANNOT Do on GitHub

| Limitation | Explanation |
|-----------|-------------|
| **Store very large files** | Individual files should be under 100 MB. Repos should stay under 1 GB. (There's a workaround called Git LFS for large files.) |
| **Run code directly** | GitHub stores code but doesn't run it (except via GitHub Actions or Codespaces) |
| **Use it as a general file store** | It's designed for code, not for storing videos, datasets, or random documents |
| **Make private repos with unlimited collaborators on Free plan** | Free plan allows private repos but has some limitations on advanced features |
| **Undo a public push easily** | Once you push something public (like a password or secret), assume it's been seen — even if you delete it |
| **Guarantee uptime** | Like any cloud service, it occasionally has outages |
| **Bypass licensing** | Just because code is public doesn't mean you can use it however you want — check the licence |

---

## 🗺️ Key GitHub Concepts — A Visual Map

```
YOUR COMPUTER                          GITHUB.COM (Cloud)
─────────────                          ──────────────────
                                       
  📁 Local Folder    ── push ──►       📦 Repository
       │                                    │
       │              ◄── pull ──           │
       │                                    │
   ✏️ Edit files                        🌿 Branches
       │                                    │
   💾 Commit                            🔀 Pull Requests
   (save snapshot)                      (ask to merge)
                                            │
                                        ✅ Merge
                                        (accept changes)
```

---

## 🚀 Getting Started — Three Paths

### Path 1: Browser Only (Easiest)
1. Go to [github.com](https://github.com) and create a free account
2. Click **"New Repository"**
3. Upload your files or create them in the browser
4. Edit directly on the website
5. **Best for:** Simple projects, documentation, learning

### Path 2: GitHub Desktop App (Easy)
1. Download [GitHub Desktop](https://desktop.github.com)
2. Sign in with your GitHub account
3. Use the visual interface to clone, commit, push, and pull
4. **Best for:** People who prefer clicking over typing commands

### Path 3: Git Command Line (Most Powerful)
1. Install [Git](https://git-scm.com)
2. Use terminal/command prompt commands
3. **Best for:** Developers and power users

---

## 🌐 GitHub Pages — Free Website Hosting!

This is especially relevant for your learning app idea. GitHub Pages lets you host a website **for free** directly from a repository.

### How it works:
1. Create a repo with your HTML/CSS/JavaScript files
2. Go to **Settings → Pages**
3. Choose your branch (usually `main`)
4. Your site is live at `https://yourusername.github.io/repo-name`

### What you can host:
- ✅ Static websites (HTML, CSS, JavaScript)
- ✅ Learning apps and interactive pages
- ✅ Documentation sites
- ✅ Personal portfolios
- ❌ NOT server-side apps (no databases, no backend code)

---

## 💡 For Your Learning App

Since you want to create a learning app/webpage, here's a suggested approach:

1. **Create a GitHub account** (free)
2. **Create a new repository** called something like `learning-app`
3. **Build your app** using HTML + CSS + JavaScript (runs in the browser)
4. **Push your code** to GitHub
5. **Enable GitHub Pages** to make it live on the internet

### Frameworks that work well with GitHub Pages:
- **Plain HTML/CSS/JS** — simplest, no build step needed
- **React** (with Vite) — modern, component-based
- **Vue.js** — beginner-friendly framework
- **Svelte** — lightweight and fast

---

## 📚 Free Learning Resources

| Resource | Link | Best For |
|----------|------|----------|
| GitHub Skills | https://skills.github.com | Interactive GitHub tutorials |
| Git Handbook | https://guides.github.com/introduction/git-handbook | Understanding Git basics |
| GitHub Docs | https://docs.github.com | Official documentation |
| GitHub Desktop Docs | https://docs.github.com/en/desktop | Using the desktop app |

---

## 🔑 Key Terms Glossary

| Term | Plain English |
|------|--------------|
| **Git** | The version-control system (the engine under the hood) |
| **GitHub** | The website that hosts Git repositories (the car body) |
| **Repository (Repo)** | A project folder with version history |
| **Clone** | Download a copy of a repo |
| **Fork** | Copy someone else's repo to your account |
| **Commit** | Save a snapshot of changes |
| **Push** | Upload commits to GitHub |
| **Pull** | Download latest changes from GitHub |
| **Branch** | A parallel version of your project |
| **Merge** | Combine branches together |
| **Pull Request (PR)** | A request to merge your changes |
| **Issue** | A bug report or feature request |
| **README** | The front page / instruction manual of a repo |
| **`.gitignore`** | A file listing things Git should NOT track |
| **Licence** | Rules for how others can use your code |

---

*Created: 3 April 2026 | For: Shalini's Learning App Project*
