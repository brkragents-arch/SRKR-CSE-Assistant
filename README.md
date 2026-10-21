# SRKR CSE Assistant

Automated academic and departmental assistant for the Computer Science & Engineering (CSE) Department at S.R.K.R. Engineering College (SRKREC), aligned with JNTUK curriculum standards.

---

## 📌 Overview

**SRKR CSE Assistant** streamlines departmental workflows, including:
- **Automated Lab Evaluation:** Automated grading and verification for student lab submissions (e.g., Python / Full Stack labs).
- **Research & Publications Tracking:** Parsing and compiling Scopus / SCI publication datasets and generating annual research summaries.
- **Departmental Portal:** Local portal for metric dashboards, grading overviews, and publication registries.

---

## 📂 Project Structure

```text
SRKR CSE Asst/
├── srkr_cse_workspace/
│   ├── portal/                  # Departmental portal server and assets
│   ├── raw_publications/       # Raw publication data (CSV/exports)
│   ├── submissions/            # Student lab submissions
│   └── irins_metrics.json      # Faculty IRINS/research metrics
├── srkr_cse_knowledge_base/     # Knowledge base documents and references
├── grader.py                    # Lab evaluation script
├── compile_records.py           # Publication compiler script
├── grades_summary.md            # Lab grading output summary
├── publications_annual_report.md# Annual research & citation report
├── cse_publications_registry.json # Compiled publications data
├── AGENTS.md                    # Agent directives and workspace rules
└── README.md                    # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Node.js (for the portal server)
- Git

### 1. Lab Grading
To execute automated verification for student submissions:
```bash
python grader.py
```
Outputs are recorded in `grades_summary.md`.

### 2. Research Records Compilation
To process raw Scopus publications:
```bash
python compile_records.py
```
Outputs:
- `publications_annual_report.md`
- `cse_publications_registry.json`

### 3. Running the Department Portal Locally
Navigate to the portal directory and launch the server:
```bash
npm start
# or
node srkr_cse_workspace/portal/server.js
```
Open your browser and navigate to `http://localhost:5000`.

---

## 🌐 Production Deployment

### Option 1: GitHub Pages (Automatic CI/CD)
The portal is pre-configured with a GitHub Actions workflow (`.github/workflows/deploy.yml`):
1. In your GitHub repository, navigate to **Settings** > **Pages**.
2. Under **Build and deployment** > **Source**, choose **GitHub Actions**.
3. Any push to `main` will automatically deploy the site to:
   `https://brkragents-arch.github.io/SRKR-CSE-Assistant/`

### Option 2: Cloud / Container Deployment (Render / Railway / AWS / Docker)
A production `Dockerfile` and `Procfile` are included:
```bash
# Build & run Docker container
docker build -t srkr-cse-assistant .
docker run -p 5000:5000 srkr-cse-assistant
```
The server reads `process.env.PORT` automatically when deployed on cloud providers.

---

## 🏛️ Institution Details
- **Department:** Computer Science and Engineering (CSE)
- **Institution:** S.R.K.R. Engineering College (Autonomous), Bhimavaram, AP, India
- **Affiliation:** JNTU Kakinada (JNTUK)
