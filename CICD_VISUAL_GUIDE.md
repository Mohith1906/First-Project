# CI/CD Visual Guides & Diagrams

## How CI/CD Works - Visual Flow

### The Complete Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                          YOUR COMPUTER                              │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  You make code changes                                       │  │
│  │  ├── Edit test file                                         │  │
│  │  ├── Fix a bug                                              │  │
│  │  └── Add new feature                                        │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
│                     │                                               │
│  ┌──────────────────▼───────────────────────────────────────────┐  │
│  │  You run git commands                                        │  │
│  │  $ git add .                                                │  │
│  │  $ git commit -m "Fix test"                                │  │
│  │  $ git push                                                │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
└─────────────────────┼───────────────────────────────────────────────┘
                      │
                      │ (Code goes to GitHub)
                      │
┌─────────────────────▼───────────────────────────────────────────────┐
│                        GITHUB (Cloud)                               │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  GitHub receives your code                                  │  │
│  │  ✓ Your files are stored safely                            │  │
│  │  ✓ Your changes are tracked                                │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
│                     │                                               │
│  ┌──────────────────▼───────────────────────────────────────────┐  │
│  │  GitHub Actions sees the push                              │  │
│  │  "Hey, someone pushed code to main branch!"               │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
└─────────────────────┼───────────────────────────────────────────────┘
                      │
                      │ (Workflow triggers)
                      │
┌─────────────────────▼───────────────────────────────────────────────┐
│                  GITHUB ACTIONS RUNNER (VM)                         │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Step 1: Checkout Code                                      │  │
│  │  ✓ Download your code from GitHub                          │  │
│  │  ✓ Ready to test                                           │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
│                     │                                               │
│  ┌──────────────────▼───────────────────────────────────────────┐  │
│  │  Step 2: Set up Python                                      │  │
│  │  ✓ Install Python 3.10                                     │  │
│  │  ✓ Ready to run code                                       │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
│                     │                                               │
│  ┌──────────────────▼───────────────────────────────────────────┐  │
│  │  Step 3: Install Dependencies                               │  │
│  │  ✓ Install pytest, selenium, etc.                          │  │
│  │  ✓ All packages ready                                      │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
│                     │                                               │
│  ┌──────────────────▼───────────────────────────────────────────┐  │
│  │  Step 4: Run Tests                                          │  │
│  │  $ pytest --junitxml=reports/junit.xml ...                │  │
│  │  ✓ Running 11 tests...                                     │  │
│  │  ✓ Generating reports...                                   │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
│                     │                                               │
│  ┌──────────────────▼───────────────────────────────────────────┐  │
│  │  Step 5: Upload Reports                                     │  │
│  │  ✓ Save report.html                                        │  │
│  │  ✓ Save junit.xml                                          │  │
│  │  ✓ Save coverage reports                                   │  │
│  └──────────────────┬───────────────────────────────────────────┘  │
└─────────────────────┼───────────────────────────────────────────────┘
                      │
                      │ (Results ready)
                      │
┌─────────────────────▼───────────────────────────────────────────────┐
│                      GITHUB (Results Page)                          │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  ✅ ALL TESTS PASSED                                        │  │
│  │                                                              │  │
│  │  11 passed in 124 seconds                                  │  │
│  │                                                              │  │
│  │  📥 Download Artifacts (reports)                           │  │
│  │  └── test-reports/                                         │  │
│  │      ├── report.html                                       │  │
│  │      ├── junit.xml                                         │  │
│  │      ├── coverage/                                         │  │
│  │      └── allure-results/                                   │  │
│  └──────────────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────────────┘
                      │
                      │ (You can see results)
                      │
┌─────────────────────▼───────────────────────────────────────────────┐
│                        YOUR COMPUTER                                │
│  You download reports and view results                             │
│  ✓ Open report.html - see all test results                        │
│  ✓ Share results with team                                        │
│  ✓ Celebrate passing tests!                                       │
└────────────────────────────────────────────────────────────────────┘
```

---

## Workflow File Structure

### Your pytest.yml File Explained

```yaml
name: Pytest Tests                    # ← Display name in GitHub
                                      
on:                                   # ← WHEN to run
  push:                              # Run on code push
    branches: [ main, develop ]      # On these branches
  pull_request:                      # Run on pull request
    branches: [ main ]               # To this branch
  workflow_dispatch:                 # Allow manual trigger

jobs:                                # ← Groups of work
  test:                             # Job name
    runs-on: ubuntu-latest          # Which machine to use
    
    steps:                          # ← Individual tasks
    - name: Checkout code           # Step 1 name
      uses: actions/checkout@v3     # Use pre-built action
    
    - name: Set up Python           # Step 2 name
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'      # Python version to install
    
    - name: Install dependencies    # Step 3 name
      run: |                        # Run commands
        python -m pip install --upgrade pip
        pip install pytest pytest-html
    
    - name: Run pytest              # Step 4 name
      run: pytest --junitxml=reports/junit.xml
    
    - name: Upload reports          # Step 5 name
      if: always()                  # Run even if tests fail
      uses: actions/upload-artifact@v3
      with:
        name: test-reports
        path: reports/
```

---

## When Things Go Wrong - Error Diagnosis

### Scenario 1: Tests Fail

```
FAILED Tests/test_login.py::TestLogin::test_login_with_valid_credentials

❌ WORKFLOW STATUS: RED X (FAILED)

┌─────────────────────────────────────────────────┐
│  What happened:                                 │
│  └─ Test assertion failed                       │
│                                                 │
│  Where to look:                                 │
│  └─ "Run pytest" step → See error message      │
│                                                 │
│  What to do:                                    │
│  1. Read error message carefully                │
│  2. Run test locally: pytest test_login.py -v  │
│  3. Fix the code                                │
│  4. Commit and push                             │
│  5. Workflow runs again automatically           │
└─────────────────────────────────────────────────┘
```

### Scenario 2: Dependency Not Found

```
ModuleNotFoundError: No module named 'selenium'

❌ WORKFLOW STATUS: RED X (ERROR)

┌─────────────────────────────────────────────────┐
│  What happened:                                 │
│  └─ Missing package in requirements.txt         │
│                                                 │
│  Where to look:                                 │
│  └─ "Install dependencies" step                │
│                                                 │
│  What to do:                                    │
│  1. Add package to requirements.txt             │
│     selenium==4.15.2                            │
│  2. Commit and push                             │
│  3. Workflow runs again                         │
└─────────────────────────────────────────────────┘
```

### Scenario 3: Tests Timeout

```
TimeoutException: Unable to locate element

❌ WORKFLOW STATUS: RED X (TIMEOUT)

┌─────────────────────────────────────────────────┐
│  What happened:                                 │
│  └─ Test waited too long for page load          │
│                                                 │
│  Possible causes:                               │
│  ├─ Website is slow                             │
│  ├─ Network issue in CI environment             │
│  ├─ Element selector is wrong                   │
│  └─ Browser didn't start                        │
│                                                 │
│  What to do:                                    │
│  1. Increase wait time in your code             │
│  2. Use WebDriverWait instead of sleep()        │
│  3. Check element selectors                     │
│  4. Use headless mode                           │
└─────────────────────────────────────────────────┘
```

---

## Branching Strategy

### Simple Git Workflow for Beginners

```
GitHub Repository (main branch)
          ▲
          │
          │ (push)
          │
Your Computer
    │
    ├─ main branch
    │  └─ Production code
    │
    └─ feature branch (optional)
       └─ Working on new feature
```

### Basic Commands

```
Create new branch (optional):
$ git checkout -b feature/new-test

Make changes:
$ Edit your files...

Add changes:
$ git add .

Commit:
$ git commit -m "Add new test"

Push to GitHub:
$ git push origin main
(or: git push origin feature/new-test)
```

---

## Repository Structure

### What GitHub Sees

```
Your Repository
│
├── .github/
│   └── workflows/
│       └── pytest.yml           ← CI/CD Configuration
│
├── Tests/                       ← Your test files
│   ├── test_login.py
│   ├── test_register.py
│   └── test_search.py
│
├── PageObjects/                 ← Page Object Model
│   ├── LoginPage.py
│   ├── RegisterPage.py
│   └── HomePage.py
│
├── Utilities/                   ← Helper functions
│   └── Read_Configurations.py
│
├── Configurations/              ← Config files
│   └── config.properties
│
├── pytest.ini                   ← Pytest configuration
├── requirements.txt             ← Dependencies
├── README.md                    ← Documentation (optional)
└── .gitignore                   ← Files to ignore (optional)
```

---

## GitHub Actions Status Indicators

### Understanding the Badges

```
✅ GREEN CHECKMARK
   └─ All tests passed
   └─ Code is good
   └─ Can merge safely

❌ RED X
   └─ At least one test failed
   └─ Code has issues
   └─ Don't merge yet

⏳ YELLOW CIRCLE
   └─ Workflow is running
   └─ Wait for results

❓ GREY CIRCLE
   └─ Workflow hasn't started yet
   └─ Could be queued
```

---

## Timeline Example

### From Push to Results

```
13:45:00  - You run: git push
           └─ Code goes to GitHub

13:45:05  - GitHub detects push
           └─ Triggers workflow

13:45:10  - Runner starts
           └─ Creates new machine

13:45:20  - Checkout code (5 sec)
           └─ ✅ Complete

13:45:30  - Set up Python (10 sec)
           └─ ✅ Complete

13:46:00  - Install deps (30 sec)
           └─ ✅ Complete

13:48:00  - Run tests (120 sec)
           └─ Tests running...
           └─ Generating reports...

13:50:00  - Upload reports (5 sec)
           └─ ✅ Complete

13:50:05  - Workflow done!
           └─ Results on GitHub

13:50:10  - You view results
           └─ See ✅ all passed
           └─ Download reports
```

---

## Git Concepts Explained

### What is Git?

```
Git = Version Control System
  ├─ Tracks changes to code
  ├─ Stores history
  ├─ Allows collaboration
  └─ Lets you undo changes
```

### Key Git Concepts

```
Repository (Repo)
├─ Your project folder
└─ Stores all files and history

Commit
├─ A snapshot of your code
├─ Has a message describing changes
└─ Creates a point you can go back to

Branch
├─ A separate line of development
├─ main = production code
└─ feature branches = work in progress

Push
├─ Send your commits to GitHub
└─ Makes code available to others

Pull
├─ Get latest code from GitHub
└─ Update your local copy
```

### Common Workflow

```
1. Make changes
   └─ Edit files locally

2. Stage changes
   └─ $ git add .

3. Commit changes
   └─ $ git commit -m "message"

4. Push to GitHub
   └─ $ git push

5. GitHub Actions runs automatically
   └─ Tests run
   └─ Reports generated
   └─ Results available

6. View results
   └─ Check GitHub Actions tab
   └─ See if tests passed
```

---

## Decision Tree: What To Do

### My workflow failed. What do I do?

```
                        Workflow Failed
                              │
                ┌─────────────┼─────────────┐
                │             │             │
                ▼             ▼             ▼
            Red X         Yellow           Grey
            (Error)       (Running)        (Queued)
               │             │              │
               │             │              ├─ Wait
               │             │              └─ Refresh
               │             │
               │             ├─ In progress
               │             └─ Check back soon
               │
               ├─ Check error message
               │
               ├─ Is it a test failure?
               │  ├─ YES → Read test error
               │  │        Fix code locally
               │  │        Push again
               │  │
               │  └─ NO → Check for other errors:
               │           ├─ Missing dependency
               │           ├─ Wrong Python version
               │           ├─ File not found
               │           ├─ Syntax error
               │           └─ Config issue
               │
               └─ Still confused?
                  └─ Run locally with same setup
                     $ pytest -v
                     (Debug locally first)
```

---

## Files Checklist

### What Should Be In Your Repository

```
[ ] .github/workflows/pytest.yml
    └─ Your CI/CD configuration

[ ] Tests/
    └─ Your test files (test_*.py)

[ ] PageObjects/
    └─ Page Object classes

[ ] Utilities/
    └─ Helper functions

[ ] Configurations/
    └─ Config files

[ ] requirements.txt
    └─ List of Python packages

[ ] pytest.ini
    └─ Pytest configuration

[ ] README.md (optional)
    └─ Project documentation

[ ] .gitignore (optional)
    └─ Files Git should ignore
```

### What Should NOT Be In Your Repository

```
[ ] .venv/ or venv/
    └─ Virtual environment (excluded via .gitignore)

[ ] __pycache__/
    └─ Python cache files (excluded)

[ ] .coverage
    └─ Coverage data (excluded)

[ ] reports/
    └─ Generated reports (excluded)

[ ] *.log
    └─ Log files (should be ignored)

[ ] config.properties with passwords
    └─ NEVER push secrets!
```

---

## Performance Metrics

### Understanding Workflow Times

```
Fast Workflow (< 5 minutes)
├─ Checkout: 5 sec
├─ Setup Python: 10 sec
├─ Install deps: 30 sec
├─ Run tests: 2 min
└─ Upload: 5 sec
Total: ~3 minutes ✅

Slow Workflow (> 10 minutes)
├─ Checkout: 5 sec
├─ Setup Python: 10 sec
├─ Install deps: 5 min (⚠️ Slow!)
├─ Run tests: 5 min
└─ Upload: 5 sec
Total: ~15 minutes ❌

Optimization Tips:
├─ Cache dependencies
├─ Use lighter test runner
├─ Parallel test execution
└─ Only test changed code
```

---

## Summary Diagram

### Your CI/CD Journey

```
                Start Here
                    │
        ┌───────────┴───────────┐
        │                       │
    GitHub Account         Git Setup
        │                       │
        └───────────┬───────────┘
                    │
            Create Repository
                    │
            Push Your Code
                    │
        GitHub Actions Triggered
                    │
        ┌───────────┴───────────────┐
        │                           │
    Tests Pass            Tests Fail
        │                     │
        ├─ View Results      ├─ Read Error
        ├─ Download Reports  ├─ Fix Locally
        ├─ Share with Team   ├─ Push Again
        └─ Celebrate! 🎉     └─ Workflow Retries
```

---

## Quick Reference Card

```
┌──────────────────────────────────────────────────┐
│           CI/CD QUICK REFERENCE                  │
├──────────────────────────────────────────────────┤
│                                                  │
│ Create account:     github.com                  │
│ Create repo:        github.com/new              │
│ View actions:       repo → Actions tab          │
│ Git init:           git init                    │
│ Add files:          git add .                   │
│ Commit:             git commit -m "msg"         │
│ Push:               git push                    │
│ Status:             git status                  │
│                                                  │
│ Workflow file:      .github/workflows/*.yml    │
│ Configuration:      pytest.ini                  │
│ Dependencies:       requirements.txt             │
│                                                  │
│ When to push:       After commit                │
│ When tests run:     After push to GitHub        │
│ Where results:      GitHub Actions tab          │
│ How to fix:         Fix locally → Push again    │
│                                                  │
└──────────────────────────────────────────────────┘
```

---

**Created:** December 6, 2025  
**Purpose:** Visual learning guide  
**Difficulty:** Beginner-friendly  
**Reference material:** Yes, save this for later!

