# Antigravity Goal Specification

/agent srkr_cse_agent.yaml --instructions system.md

/goal 
Parse and systematically compile the CSE department's raw publication files located in `./srkr_cse_workspace/raw_publications/`.
1. Use the terminal tool to scan for raw metadata files (CSVs exported from Scopus/Google Scholar or BibTeX citations).
2. Write and execute a Python data processor script to clean up duplicate entries, unify conflicting author naming conventions (e.g., matching "Dr. Bh. V. S. R. K. Raju" with "Bh. V. S. Rama Krishnam Raju"), and filter out records missing DOI tracking codes.
3. Classify all verified records strictly into three target indexes: 'SCI/SCIE Indexed', 'Scopus Indexed', or 'International Conferences (e.g., ICAAAI)'.
4. Export a comprehensive structural breakdown file named `cse_publications_registry.json` and a beautifully readable summary dashboard in markdown format named `publications_annual_report.md`.

Target Metric validation:
- Count total active publications per calendar year.
- Extract the top 5 most prolific faculty contributors for the current cycle.
- Send a desktop completion notification with the final aggregate tally once successfully generated.
