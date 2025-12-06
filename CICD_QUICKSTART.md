# CI/CD Quick Start - Copy & Paste Commands

This file contains all the exact commands you need to run, copy-pasted ready to use.

---

## Phase 1: Initial Setup (Do This Once)

### 1A: Navigate to Your Project
```powershell
cd C:\Users\2025\PycharmProjects\QAfox
```

### 1B: Initialize Git
```powershell
git init
```

### 1C: Add All Files
```powershell
git add .
```

### 1D: Create First Commit
```powershell
git commit -m "Initial commit: Add QAfox tests with CI/CD setup"
```

### 1E: Create Main Branch
```powershell
git branch -M main
```

---

## Phase 2: Connect to GitHub (Do This Once)

### 2A: Create GitHub Account
Go to https://github.com and sign up (free)

### 2B: Create New Repository
1. Go to https://github.com/new
2. Enter name: `QAfox`
3. Description: `QA automation tests with Selenium`
4. Public (for free CI/CD)
5. Click "Create repository"

### 2C: Connect Local Folder to GitHub

**Replace YOUR_USERNAME with your actual GitHub username:**

```powershell
git remote add origin https://github.com/YOUR_USERNAME/QAfox.git
```

### 2D: Push to GitHub (First Time)
```powershell
git push -u origin main
```

### 2E: Verify on GitHub
Open: https://github.com/YOUR_USERNAME/QAfox

---

## Phase 3: Workflow Already Created

✅ Your workflow file is already at: `.github/workflows/pytest.yml`  
✅ Your dependencies are listed in: `requirements.txt`

**The workflow will run automatically when you push!**

---

## Phase 4: Watch Workflow Run

1. Go to: https://github.com/YOUR_USERNAME/QAfox
2. Click the "Actions" tab at the top
3. Click "Pytest Tests" in the list
4. Watch the workflow run (yellow spinning circle)
5. Wait for green checkmark (success) or red X (failure)

---

## Phase 5: Daily Workflow (After Initial Setup)

### Make Changes to Your Tests

Edit any test file:
```
Tests/test_login.py
Tests/test_register.py
etc.
```

### Commit and Push

```powershell
# Check what changed
git status

# Add all changes
git add .

# Create a commit with a message
git commit -m "Fix login test"

# Push to GitHub
git push
```

### Workflow Runs Automatically!

1. Go to Actions tab
2. See your workflow running
3. Check results when done

---

## Phase 6: Download Test Reports

### Option A: From GitHub Web
1. Go to Actions tab
2. Click your workflow run
3. Scroll to "Artifacts"
4. Click "test-reports" to download
5. Extract ZIP file
6. Open `report.html` in browser

### Option B: Command Line
```powershell
# Files are in reports/ folder after local run
Start-Process .\reports\report.html
```

---

## Phase 7: Troubleshooting Commands

### Check Git Status
```powershell
git status
```
Shows what files changed

### See Commit History
```powershell
git log --oneline
```
Shows your commits

### Run Tests Locally (Before Push)
```powershell
pytest -v
```
Same as GitHub will run

### Check Python Version
```powershell
python --version
```

### Check Installed Packages
```powershell
pip list
```

### Install Missing Package
```powershell
pip install package-name
pip freeze > requirements.txt
```

---

## Phase 8: When Tests Fail

### 1. Check the Error
In GitHub Actions:
- Click the failed workflow
- Click "Run pytest" step
- Read the error message

### 2. Run Locally to Reproduce
```powershell
pytest -v
```

### 3. Fix Your Code
Edit the test file

### 4. Test Locally Again
```powershell
pytest -v
```

### 5. Commit and Push
```powershell
git add .
git commit -m "Fix test issue"
git push
```

### 6. Workflow Runs Again Automatically

---

## Phase 9: Common Commands Cheat Sheet

### Git Commands
```powershell
# See what changed
git status

# Add all files
git add .

# Create checkpoint
git commit -m "Your message"

# Send to GitHub
git push

# Get latest from GitHub
git pull

# See history
git log --oneline

# Undo last commit (before push)
git reset --soft HEAD~1

# Switch to different branch
git checkout branch-name

# Create new branch
git checkout -b new-branch-name
```

### Pytest Commands
```powershell
# Run all tests
pytest

# Run specific test
pytest Tests/test_login.py

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Run last failed tests
pytest --lf

# Generate reports
pytest --junitxml=reports/junit.xml --html=reports/report.html
```

### File Management
```powershell
# View file contents
Get-Content filename.txt

# List files
ls
# or
dir

# Open folder
explorer .

# Open in browser
Start-Process .\reports\report.html
```

---

## Phase 10: Important Files & Locations

### Key Files
```
C:\Users\2025\PycharmProjects\QAfox\
├── .github/workflows/pytest.yml         ← CI/CD config
├── requirements.txt                     ← Dependencies
├── pytest.ini                           ← Pytest config
└── Tests/                              ← Your tests
```

### GitHub URLs
```
Your Repository:
https://github.com/YOUR_USERNAME/QAfox

Actions Tab:
https://github.com/YOUR_USERNAME/QAfox/actions

New Repository:
https://github.com/new
```

### Local Commands Folder
```
cd C:\Users\2025\PycharmProjects\QAfox
```

---

## Phase 11: Verification Checklist

After setup, verify everything works:

```powershell
# 1. Check git is initialized
ls .git

# 2. Check requirements.txt exists
ls requirements.txt

# 3. Check workflow file exists
ls .github/workflows/pytest.yml

# 4. Check you're on main branch
git branch

# 5. Check remote is configured
git remote -v

# 6. Run tests locally
pytest

# 7. Check status before push
git status
```

All commands above should work without errors.

---

## Phase 12: Step-by-Step First Push Summary

### Run These Commands in Order:
```powershell
# 1. Navigate to project
cd C:\Users\2025\PycharmProjects\QAfox

# 2. Initialize git
git init

# 3. Add all files
git add .

# 4. First commit
git commit -m "Initial commit: QAfox tests"

# 5. Set main branch
git branch -M main

# 6. Add GitHub connection (REPLACE YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/QAfox.git

# 7. Push to GitHub
git push -u origin main

# 8. Wait a moment, then check:
# Visit: https://github.com/YOUR_USERNAME/QAfox/actions
```

That's it! ✅

---

## Phase 13: After First Push

Every time you change code:

```powershell
# 1. Make your changes to test files

# 2. Check status
git status

# 3. Add changes
git add .

# 4. Commit with message
git commit -m "Describe your changes"

# 5. Push to GitHub
git push

# 6. Workflow runs automatically!
# Check: https://github.com/YOUR_USERNAME/QAfox/actions
```

---

## Phase 14: Quick Troubleshooting

### Issue: "fatal: not a git repository"
**Fix:**
```powershell
cd C:\Users\2025\PycharmProjects\QAfox
git init
```

### Issue: "Permission denied"
**Fix:**
```powershell
# Remove and re-add origin with HTTPS
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/QAfox.git
```

### Issue: "nothing to commit"
**Fix:**
```powershell
# Only run push, nothing changed since last commit
git push
```

### Issue: "Merge conflict"
**Fix:**
```powershell
# Undo last push
git reset --hard HEAD~1
# Then fix code manually
```

### Issue: "No such file or directory"
**Fix:**
```powershell
# Make sure you're in correct folder
cd C:\Users\2025\PycharmProjects\QAfox
ls
```

---

## Phase 15: You Did It! 🎉

When you see:
1. ✅ Code on GitHub (github.com/YOUR_USERNAME/QAfox)
2. ✅ Actions tab shows workflow
3. ✅ Green checkmark on workflow
4. ✅ Test reports generated

**You've successfully set up CI/CD!**

---

## Next Steps

1. **Tomorrow:** Make a small code change, push it, watch workflow run
2. **This Week:** Try failing a test intentionally, see error in GitHub
3. **Next Week:** Add more advanced features (notifications, etc.)
4. **Learning:** Read the detailed guides in this folder

---

## Support Cheat Sheet

**Can't remember a command?**
Look in this file first! All common commands are here.

**Need full explanation?**
Read: `CICD_IMPLEMENTATION_GUIDE.md`

**Need visuals?**
Read: `CICD_VISUAL_GUIDE.md`

**Need advanced concepts?**
Read: `CICD_LEARNING_GUIDE.md`

---

## Files Created for You

✅ `.github/workflows/pytest.yml` - Your CI/CD workflow  
✅ `requirements.txt` - Python dependencies  
✅ `CICD_LEARNING_GUIDE.md` - Full educational guide  
✅ `CICD_IMPLEMENTATION_GUIDE.md` - Step-by-step implementation  
✅ `CICD_VISUAL_GUIDE.md` - Diagrams and visual explanations  
✅ `CICD_QUICKSTART.md` - This file (quick reference)

---

**Created:** December 6, 2025  
**Purpose:** Quick reference for CI/CD setup  
**Status:** Ready to use!  
**Keep this file handy:** Yes!

