# 🛡️ PureStack Blue Team Challenge: Digital Forensics & Log Analysis

**PureStack.es - Security Validation Protocol.**
> *"Certifications are paper. Code is proof. We audit Scripting, Parsing, and Incident Response."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Cybersecurity.
We don't ask you to click buttons in a SIEM. We ask you to parse raw evidence and automate threat detection via code.

**The Scenario:** Our legacy web server has been compromised. The SIEM is flooded, so we extracted the raw log file (`data/server_logs.txt`). We suspect a specific type of attack against our database.
**The Mission:** Write a Python script (`incident_response.py`) to parse the logs, detect the attack pattern, and identify the perpetrator.

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by the depth of your analysis and the flexibility of your tool. State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level (Passes the Test)
* **Focus:** String Parsing & Basic Logic.
* **Requirement:** Neutralize the immediate threat.
* **Tasks:**
    1.  **Parse:** Read `data/server_logs.txt`.
    2.  **Detection:** Identify requests containing suspicious keywords (e.g., `UNION`, `SELECT`, `' OR '1'='1`).
    3.  **Output:** The function `analyze_logs()` must return a dictionary with:
        * `attacker_ip`: The IP address responsible for the attacks.
        * `attack_type`: A string classifying the attack (e.g., "sql_injection").
* **Deliverable:** A script that passes the automated tests (turns the Red semaphore to Green).

#### 🥈 Level 2: Pro / Senior
* **Focus:** RegEx & Context.
* **Requirement:** Everything in Level 3 + **Detailed Forensics**.
* **Extra Tasks:**
    1.  **RegEx:** Use Python's `re` module to strictly extract the IP addresses (validate the format `xxx.xxx.xxx.xxx`).
    2.  **Scope:** Calculate how many **unique** paths/files the attacker tried to exploit (e.g., `/login.php`, `/search.php`).
* **Deliverable:** The script works, but the internal logic uses robust Regular Expressions instead of simple string splitting.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Tooling & Reporting.
* **Requirement:** Everything above + **CLI Support**.
* **Extra Tasks:**
    1.  **CLI Transformation:** Use `argparse`. The script should be callable via command line: `python incident_response.py -f data/server_logs.txt`.
    2.  **Reporting:** If run as `__main__`, generate a `forensic_report.json` file on disk with the findings.
* **Deliverable:** A production-grade security tool suitable for CI/CD pipelines.

---

### 🛠️ Tech Stack & Constraints
* **Language:** Python 3.9+.
* **Libraries:** **Standard Library ONLY** (`re`, `collections`, `json`, `argparse`, `os`). No `pandas` allowed (Simulating a restricted server environment).
* **Logic:** Do not hardcode the IP. The script must dynamically find it based on the log patterns.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Analyze `data/server_logs.txt` manually to understand the HTTP log format.
3.  Implement your logic in `incident_response.py`.
4.  Run tests locally:
    ```bash
    pip install pytest
    PYTHONPATH=. pytest tests/
    ```
5.  Submit via **Pull Request**.

> **Note on Build Status:** You will see a ❌ (**Red Cross**) initially. This is expected (TDD). Your goal is to write the code that turns it ✅ (**Green**).

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Accuracy** | 50% | Does it find the correct IP (192.168.1.66) and Attack Type? |
| **Code Structure** | 30% | Modular functions vs Spaghetti script. |
| **Pattern Matching** | 20% | Correct identification of SQL Injection patterns. |

---

### 🚨 Project Structure (Strict)
To ensure our **Automated Auditor** works, keep the core structure:

```text
/
├── .github/
│   └── workflows/
│       └── audit.yml          # Automated Assessment Pipeline
├── data/
│   └── server_logs.txt        # Forensic Evidence (Log file)
├── tests/
│   └── test_ir.py             # Validation Tests (Run via pytest)
├── incident_response.py       # <--- CANDIDATE SOLUTION GOES HERE
└── README.md                  # Challenge Instructions
