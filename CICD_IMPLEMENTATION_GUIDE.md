# Step-by-Step: Setting Up CI/CD with GitHub Actions

## What You're About to Learn

You'll learn how to:
1. ✅ Set up GitHub (free code hosting)
2. ✅ Push your code to GitHub
3. ✅ Automatically run tests on every push
4. ✅ View test results on GitHub
5. ✅ Download test reports
6. ✅ Understand what's happening at each step

**Time Required:** 30-60 minutes (first time)  
**Cost:** FREE  
**Difficulty:** Beginner-friendly ⭐⭐

---

## Phase 1: Preparation (What You Have)

### Files Already Created for You:
```
QAfox/
├── .github/
│   └── workflows/
│       └── pytest.yml              ← GitHub Actions workflow ✅ Created
├── requirements.txt                ← Dependencies list ✅ Created
├── pytest.ini                      ← Pytest config ✅ Created
├── CICD_LEARNING_GUIDE.md         ← Full learning guide ✅ Created
└── Tests/                          ← Your test files ✅ Ready
```

### What Each File Does:
- **pytest.yml** = Instructions for GitHub to run tests
- **requirements.txt** = List of Python packages needed
- **pytest.ini** = How pytest should run
- **Tests/** = Your actual test files

---

## Phase 2: Set Up GitHub Account & Repository

### Step 1: Create GitHub Account (if you don't have one)

1. Go to https://github.com
2. Click "Sign up"
3. Fill in:
   - Email
   - Password
   - Username (something like: your-name-qafox)
4. Verify email
5. You're done! ✅

### Step 2: Create a New Repository

1. Go to https://github.com/new
2. Fill in:
   - Repository name: `QAfox` (or any name)
   - Description: `QA automation tests with Selenium`
   - Visibility: `Public` (for free CI/CD)
3. **IMPORTANT:** Do NOT check:
   - "Add a README file"
   - "Add .gitignore"
   - "Choose a license"
4. Click "Create repository"
5. You'll see instructions - **copy them** (you'll use next)

---

## Phase 3: Push Your Code to GitHub

### Step 1: Initialize Git on Your Computer

Open PowerShell in your QAfox folder:

```powershell
cd C:\Users\2025\PycharmProjects\QAfox
git init
```

**What this does:** Prepares your folder to track changes

### Step 2: Add All Your Files

```powershell
git add .
```

**What this does:** Stages all files for saving

### Step 3: Create First Commit

```powershell
git commit -m "Initial commit: Add QAfox tests with CI/CD setup"
```

**What this does:** Saves a snapshot of your code with a message

### Step 4: Create Main Branch

```powershell
git branch -M main
```

**What this does:** Makes sure your branch is called "main"

### Step 5: Connect to GitHub

Replace `YOUR_USERNAME` with your GitHub username:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/QAfox.git
```

**What this does:** Links your local folder to GitHub

### Step 6: Push to GitHub

```powershell
git push -u origin main
```

**What this does:** Uploads your code to GitHub

**Expected Output:**
```
Enumerating objects: 50, done.
Counting objects: 100% (50/50), done.
...
To https://github.com/YOUR_USERNAME/QAfox.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

✅ **Your code is now on GitHub!**

---

## Phase 4: Watch GitHub Actions Run

### Step 1: Go to Your GitHub Repository

1. Open: https://github.com/YOUR_USERNAME/QAfox
2. You should see your files there ✅

### Step 2: Click the "Actions" Tab

1. At the top of your repo page, click "Actions"
2. You should see your workflow running!

### Step 3: Watch the Workflow

1. Click on "Pytest Tests" (or your first workflow)
2. You'll see it's running through steps:
   - ✅ Checkout code
   - ✅ Set up Python
   - ✅ Install dependencies
   - ✅ Run pytest
   - ✅ Upload reports
   - ✅ Publish results

### Step 4: Wait for Completion

The workflow will take 2-5 minutes first time. You'll see:
- 🟡 **Yellow dot** = Running
- ✅ **Green checkmark** = Success
- ❌ **Red X** = Failed

---

## Phase 5: View Test Results

### Option A: View Results on GitHub (Easiest)

1. In the Actions tab, click your workflow run
2. Click the "test" job
3. See the output in real-time
4. Scroll down to see test results summary

### Option B: Download Test Reports

1. In the Actions tab, click your workflow run
2. Scroll to bottom, find "Artifacts" section
3. Click "test-reports" to download
4. Extract ZIP file
5. Open `report.html` to see beautiful report

### Option C: View in GitHub UI

1. Scroll down on workflow page
2. Find "Annotations" section
3. See test results inline

---

## Phase 6: Understanding the Results

### What You're Looking At:

#### Workflow Overview
```
Pytest Tests
├── test (job)
│   ├── Checkout code ✅
│   ├── Set up Python ✅
│   ├── Install dependencies ✅
│   ├── Run pytest ✅
│   ├── Upload test reports ✅
│   └── Publish test results ✅
```

#### Test Results Summary
```
Tests:
- 11 passed
- 0 failed
- 0 skipped
Duration: ~120 seconds
```

#### Artifacts Section
- **test-reports** folder (click to download)
  - Contains: report.html, junit.xml, coverage/, allure-results/

---

## Phase 7: Test It Out (Make a Change)

Now let's test that CI/CD actually works!

### Step 1: Make a Small Code Change

Open any test file and add a comment:

```python
def test_login_with_valid_credentials(self):
    """
    Test logging in with valid email and password
    # CI/CD Testing!
    """
    # ... rest of code
```

### Step 2: Save and Commit

```powershell
git add .
git commit -m "Add comment to test CI/CD automation"
git push
```

### Step 3: Watch GitHub Actions Run Again

1. Go to your GitHub repo
2. Click "Actions"
3. Click your new workflow
4. Watch it run!

**This proves CI/CD is working!** ✅

---

## Phase 8: Interpreting Workflow Steps

### Let's Look at Each Step

#### Step: Checkout code
```yaml
- uses: actions/checkout@v3
```
**What it does:** Downloads your code from GitHub  
**Why:** GitHub needs your source code to run tests  
**Expected time:** 5 seconds

#### Step: Set up Python
```yaml
- uses: actions/setup-python@v4
  with:
    python-version: '3.10'
```
**What it does:** Installs Python 3.10 on the CI machine  
**Why:** Your tests need Python to run  
**Expected time:** 10 seconds

#### Step: Install dependencies
```yaml
- run: |
  pip install pytest pytest-html pytest-cov
  pip install selenium webdriver-manager
```
**What it does:** Installs required Python packages  
**Why:** Your code depends on these packages  
**Expected time:** 30-60 seconds

#### Step: Run pytest
```yaml
- run: |
  pytest --maxfail=1 -v \
         --junitxml=reports/junit.xml \
         --html=reports/report.html \
         --self-contained-html \
         --cov=. \
         --cov-report=html:reports/coverage
```
**What it does:** Runs your test suite  
**Why:** This is the actual testing  
**Expected time:** 2 minutes (your tests)

#### Step: Upload reports
```yaml
- uses: actions/upload-artifact@v3
  with:
    name: test-reports
    path: reports/
    retention-days: 30
```
**What it does:** Saves test reports for download  
**Why:** You can view reports later  
**Expected time:** 5 seconds

---

## Phase 9: When Tests Fail

If you see a ❌ red X, here's what to do:

### Step 1: Click the Failed Workflow

1. Go to Actions tab
2. Click the failed workflow
3. Click "test" job

### Step 2: Find the Error

Scroll through and look for red text or errors:

```
FAILED Tests/test_login.py::TestLogin::test_login_with_invalid_credentials
AssertionError: Expected 'Dashboard' in page title
```

### Step 3: Understand the Error

The test failed because:
- Expected text: "Dashboard"
- Got something different
- Could be a timing issue, UI change, or real bug

### Step 4: Fix Locally First

1. Run test on your computer:
   ```powershell
   pytest Tests/test_login.py -v
   ```
2. Fix the issue
3. Commit and push
4. CI/CD will run automatically

### Step 5: View Full Logs

In the "Run pytest" step, expand to see:
- Each test status
- Timing information
- Full error messages
- Stack traces

---

## Phase 10: Protecting Your Main Branch

Once you're comfortable, prevent untested code from merging:

### Step 1: Go to Repository Settings

1. Click "Settings" tab
2. Click "Branches" in left menu
3. Click "Add rule"

### Step 2: Create Rule

```
Branch name pattern: main

✅ Require a pull request
✅ Require status checks to pass
   - Select "test"
✅ Dismiss stale pull request approvals
```

### Step 3: What This Does

Now, before merging:
1. Must create a Pull Request
2. Tests must pass
3. Can't merge if tests fail

**This prevents broken code from reaching production!** 🛡️

---

## Phase 11: Quick Reference

### Common Commands

```powershell
# See git status
git status

# Add all changes
git add .

# Add specific file
git add filename.py

# Commit with message
git commit -m "Your message"

# Push to GitHub
git push

# Pull latest changes
git pull

# See commit history
git log --oneline
```

### Common Workflow Files Locations

```
QAfox/
├── .github/workflows/pytest.yml      ← Main workflow file
├── requirements.txt                  ← Dependencies
└── pytest.ini                        ← Pytest config
```

### GitHub Actions URLs

```
View workflows:
https://github.com/YOUR_USERNAME/QAfox/actions

View specific workflow:
https://github.com/YOUR_USERNAME/QAfox/actions/runs/RUN_ID

View repository:
https://github.com/YOUR_USERNAME/QAfox
```

---

## Phase 12: Troubleshooting

### Problem: Workflow shows error "No tests ran"

**Cause:** Tests folder path is wrong  
**Fix:** Check `testpaths` in pytest.ini matches your folder name

```ini
[pytest]
testpaths = Tests    # Make sure this matches your folder
```

### Problem: "ModuleNotFoundError: No module named 'selenium'"

**Cause:** Selenium not in requirements.txt  
**Fix:** Add to requirements.txt:
```
selenium==4.15.2
webdriver-manager==4.0.2
```

### Problem: Tests pass locally but fail in CI

**Causes:**
- Different Python version
- Missing dependencies
- Environment variables
- Selenium/Chrome issues

**Debug:**
Add this to your workflow:
```yaml
- name: Debug info
  run: |
    python --version
    pip list
```

### Problem: "Permission denied" error

**Cause:** Git authentication issue  
**Fix:** Use SSH instead:
```powershell
git remote set-url origin git@github.com:YOUR_USERNAME/QAfox.git
```

---

## Phase 13: Next Steps & Learning Path

### This Week:
- [ ] Create GitHub account
- [ ] Push code using this guide
- [ ] Watch workflow run
- [ ] Download and view reports
- [ ] Make a test change and push

### Next Week:
- [ ] Understand workflow file syntax
- [ ] Modify pytest.yml for your needs
- [ ] Set up branch protection
- [ ] Learn to read error messages

### This Month:
- [ ] Add matrix testing (multiple Python versions)
- [ ] Add notifications (Slack, email)
- [ ] Try Jenkins (more advanced)
- [ ] Help teammates set up CI/CD

---

## Success Checklist

When you've completed this guide, you'll have:

- [ ] GitHub account created
- [ ] Repository created
- [ ] Code pushed to GitHub
- [ ] First workflow run successfully
- [ ] Test reports generated
- [ ] Made a test commit
- [ ] Watched workflow run on your change
- [ ] Downloaded and viewed reports
- [ ] Understood all 6 workflow steps
- [ ] Know how to troubleshoot errors

**If you check all these boxes, you've mastered CI/CD basics!** 🎉

---

## Getting Help

### GitHub Resources
- [GitHub Docs](https://docs.github.com)
- [GitHub Actions Marketplace](https://github.com/marketplace?type=actions)
- GitHub Learning Lab (free courses)

### Pytest Resources
- [Pytest Official Docs](https://docs.pytest.org)
- Stack Overflow: `[pytest]` tag

### General CI/CD
- YouTube: "GitHub Actions tutorial"
- Udemy: "GitHub Actions" courses
- Free courses on Coursera

---

## Key Takeaways

1. **CI/CD automates testing** - Run tests on every push automatically
2. **GitHub Actions is easy** - No server setup, free for public repos
3. **Workflows are YAML files** - Just text configuration
4. **Reports are important** - They tell you what passed/failed
5. **Failures happen** - Use logs to debug and fix

---

## You've Got This! 💪

This is your foundation. Once you understand this:
- Jenkins becomes easy (same concepts)
- GitLab CI makes sense (similar workflow)
- Advanced topics open up (matrix testing, notifications, deployments)

**Keep learning, one step at a time.**

---

**Created:** December 6, 2025  
**Status:** Ready for implementation  
**Estimated Setup Time:** 30-60 minutes  
**Difficulty:** ⭐⭐ Beginner-Friendly

