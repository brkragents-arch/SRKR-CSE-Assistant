# Google Antigravity Agent Configuration - SRKR CSE Dept
agent:
  name: "SRKR-CSE-Assistant"
  version: "2.0.0"
  description: "AI Assistant for SRKREC CSE lab automation, student project grading, and departmental data analytics."
  model: "gemini-2.5-pro"

capabilities:
  sandbox:
    enabled: true
    type: "linux-isolated"
    workspace_root: "./srkr_cse_workspace"
  
  tools:
    - name: "terminal"
      # Restricted command ecosystem tailored to SRKR CSE's key curriculum tracks:
      allowed_commands:
        # --- Core Data Science, AI/ML & Research Track ---
        - "python"      # Executing ML workflows, Scopus analytics scripts, data parsing
        - "pip"         # Managing scientific and ML libraries (NumPy, Scikit-learn, Pandas)
        - "jupyter"     # Generating or processing JNTUK lab assignment notebooks

        # --- Full Stack Development Track ---
        - "node"        # Runtime for backend JavaScript execution
        - "npm"         # Managing dependencies for web projects (React, Express)
        - "sqlite3"     # Lightweight localized database engine for full-stack student apps

        # --- Cyber Security, Cloud & System Operations Track ---
        - "ssh"         # Allowed selectively if connecting to specialized departmental lab servers
        - "curl"        # Interfacing with internal portals, JNTUK syllabus APIs, or research tools
        - "git"         # Managing lab repositories and student project submissions

        # --- File & Base System Utilities ---
        - "mkdir"       # Creating directory structures for academic years (e.g., BTech_4_Year)
        - "touch"       # Creating configuration or code source files
        - "cat"         # Reading logs, configuration readouts, or text datasets
        - "grep"        # Searching through large text payloads or dataset logs
        
      timeout_ms: 45000 # Extended slightly to account for heavy AI/ML calculations

    - name: "chrome_browser"
      headless: true
      # Restrict browser targets to prevent unwanted external scraping loops
      allowed_domains: ["srkrec.ac.in", "jntuk.edu.in", "ai.google.dev"]

memory:
  type: "persistent-local"
  vault_path: "./srkr_cse_knowledge_base"
  auto_summarize: true

runtime:
  max_steps_per_goal: 75
  parallel_sub_agents: true
