# SRKR Engineering College - CSE Department
## Lab Assignment 1 Autonomous Grading Report

**Course:** B.Tech. CSE (Autonomous) — JNTUK Curriculum  
**Lab Assignment:** 1 (Python Fundamentals & Array Optimization)  
**Evaluator Engine:** SRKR-CSE-Assistant Verification Suite  
**Evaluation Date:** October 21, 2026  

---

### Test Suite Specification
- **Target Logic:** Find the maximum product of two distinct elements in an integer array.
- **Test Case 1:** Input `"5 3 1 4 2"` $\rightarrow$ Expected `"20"`
- **Test Case 2:** Input `"-1 -5 2 4 0"` $\rightarrow$ Expected `"8"`
- **Test Case 3:** Input `"10 10 2"` $\rightarrow$ Expected `"100"`

---

### Results Summary Table

| Student ID | Test 1 | Test 2 | Test 3 | Total Score | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **22B91A0501** | PASS | PASS | PASS | **100/100** | COMPLETED |
| **22B91A0502** | FAIL (Got: 15) | FAIL (Got: 5) | PASS | **33/100** | NEEDS REVIEW |
| **22B91A0503** | PASS | PASS | PASS | **100/100** | COMPLETED |
| **22B91A0504** | FAIL | FAIL | FAIL | **0/100** | No .py file found |

---

### Detailed Submission Logs

#### 1. Student ID: `22B91A0501`
- **File:** `srkr_cse_workspace/submissions/22B91A0501/solution.py`
- **Algorithm:** Sorted array boundary multiplication: `max(nums[0]*nums[1], nums[-1]*nums[-2])`
- **Test Results:** 3/3 passed (100%)
- **Status:** **PASS / COMPLETED**

#### 2. Student ID: `22B91A0502`
- **File:** `srkr_cse_workspace/submissions/22B91A0502/solution.py`
- **Algorithm:** Multiplies first two elements without sorting or searching: `nums[0]*nums[1]`
- **Test Results:**
  - Test 1 (`5 3 1 4 2`): Expected `20`, received `15` [FAIL]
  - Test 2 (`-1 -5 2 4 0`): Expected `8`, received `5` [FAIL]
  - Test 3 (`10 10 2`): Expected `100`, received `100` [PASS]
- **Status:** **NEEDS REVIEW (Score: 33/100)**

#### 3. Student ID: `22B91A0503`
- **File:** `srkr_cse_workspace/submissions/22B91A0503/solution.py`
- **Algorithm:** Double loop brute-force across all distinct index pairs $\mathcal{O}(n^2)$
- **Test Results:** 3/3 passed (100%)
- **Status:** **PASS / COMPLETED**

#### 4. Student ID: `22B91A0504`
- **File:** None
- **Issue:** No Python source file found in student folder.
- **Status:** **0/100 (Missing Submission)**
