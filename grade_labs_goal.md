# Antigravity Goal Specification

/agent srkr_cse_agent.yaml --instructions system.md

/goal 
Automate the assessment of B.Tech. CSE Lab Assignment 1 (Python Fundamentals) located in `./srkr_cse_workspace/submissions/`.
1. Use the terminal tool to dynamically check for Python files (`.py`) inside each student's subdirectory.
2. For every student file found, execute it inside the sandbox environment using `python`.
3. Feed the program three specific test inputs (defined below) and capture the stdout/stderr.
4. Compare output against the expected master test keys using a grading script.
5. Generate a formatted Markdown grading summary report (`grades_summary.md`) inside the workspace root containing student name, status (PASS/FAIL), execution logs, and an assigned score out of 100.

Test Specifications:
- Target Assignment: Read an integer array and find the maximum product of two distinct elements.
- Test case 1: Input "5 3 1 4 2" -> Expected Output "20"
- Test case 2: Input "-1 -5 2 4 0" -> Expected Output "8"
- Test case 3: Input "10 10 2" -> Expected Output "100"
