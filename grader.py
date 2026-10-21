import os
import subprocess

# Paths setup
SUBMISSIONS_DIR = "./submissions"
REPORT_FILE = "../grades_summary.md"

# Test Cases: (Input string, Expected Output string)
TEST_CASES = [
    ("5 3 1 4 2\n", "20"),
    ("-1 -5 2 4 0\n", "8"),
    ("10 10 2\n", "100")
]

report_content = "# SRKR Engineering College - CSE Department\n"
report_content += "## Lab Assignment 1 Autonomous Grading Report\n\n"
report_content += "| Student ID | Test 1 | Test 2 | Test 3 | Total Score | Status |\n"
report_content += "|------------|--------|--------|--------|-------------|--------|\n"

if not os.path.exists(SUBMISSIONS_DIR):
    print(f"Error: Submissions directory '{SUBMISSIONS_DIR}' not found.")
    exit(1)

for student_folder in sorted(os.listdir(SUBMISSIONS_DIR)):
    folder_path = os.path.join(SUBMISSIONS_DIR, student_folder)
    if os.path.isdir(folder_path):
        student_id = student_folder
        py_files = [f for f in os.listdir(folder_path) if f.endswith('.py')]
        
        if not py_files:
            report_content += f"| {student_id} | FAIL | FAIL | FAIL | 0/100 | No .py file found |\n"
            continue
            
        student_file = os.path.join(folder_path, py_files[0])
        passed_tests = 0
        test_results = []
        
        for input_data, expected in TEST_CASES:
            try:
                # Run the student script in a sandboxed shell process
                proc = subprocess.run(
                    ['python', student_file],
                    input=input_data,
                    text=True,
                    capture_output=True,
                    timeout=5 # Prevent infinite student loops
                )
                
                output = proc.stdout.strip()
                if output == expected:
                    test_results.append("PASS")
                    passed_tests += 1
                else:
                    test_results.append(f"FAIL (Got: {output})")
            except subprocess.TimeoutExpired:
                test_results.append("TIMEOUT")
            except Exception as e:
                test_results.append("RUNTIME ERROR")
                
        # Calculate final score
        score = int((passed_tests / len(TEST_CASES)) * 100)
        status = "COMPLETED" if score == 100 else "NEEDS REVIEW"
        
        report_content += f"| {student_id} | {test_results[0]} | {test_results[1]} | {test_results[2]} | {score}/100 | {status} |\n"

# Write the final summary report out to the workspace root
with open(REPORT_FILE, "w") as f:
    f.write(report_content)

print("Grading completed successfully. Summary generated.")
