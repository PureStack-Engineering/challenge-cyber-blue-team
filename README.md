# 🛡️ PureStack Blue Team Challenge: Digital Forensics & Log Analysis

**PureStack.es - Security Validation Protocol.**
> *"Certifications are paper. Code is proof. We audit Scripting, Regex, and Incident Response."*

---

### 📋 Context & Mission
Welcome to the PureStack Technical Validation Protocol for Cybersecurity.
We don't ask you to configure a firewall via GUI. We ask you to parse raw evidence and automate threat detection.

**The Scenario:** Our honeypot has been hit. We have a raw log file (`data/server_logs.txt`) containing mixed traffic (SSH, HTTP).
**The Mission:** Write a Python script (`incident_response.py`) to parse the file and extract actionable intelligence.

### 🚦 Certification Levels (Choose your Difficulty)
Your seniority is defined by the depth of your analysis and the flexibility of your tool. State your target level in your Pull Request.

#### 🥉 Level 3: Essential / Mid-Level
* **Focus:** Regex & Basic Parsing.
* **Requirement:** Identify the attacker.
* **Tasks:**
    1.  **Parse:** Read `data/server_logs.txt`.
    2.  **Detection:** Identify the **IP Address** with the highest frequency of failed login attempts (SSH "Failed password").
    3.  **Output:** The function `analyze_logs()` must return a dictionary/JSON with the suspect IP and the count of attacks.
* **Deliverable:** A script that passes the basic test (turns the Red semaphore to Green).

#### 🥈 Level 2: Pro / Senior
* **Focus:** Structured Reporting & Metadata Extraction.
* **Requirement:** Everything in Level 3 + **Detailed Forensics**.
* **Extra Tasks:**
    1.  **User Extraction:** Extract the list of unique **Usernames** the attacker tried to guess.
    2.  **Timeline:** Determine the **Start Time** and **End Time** of the attack sequence.
    3.  **Report:** Instead of just printing, generate a `forensic_report.json` file containing the IP, attack type, timestamps, and target users.
* **Deliverable:** A comprehensive forensic script that provides context, not just an IP.

#### 🥇 Level 1: Elite / Architect
* **Focus:** Tooling, CLI & Advanced Patterns.
* **Requirement:** Everything above + **CLI Support & Multi-Vector Detection**.
* **Extra Tasks:**
    1.  **CLI Transformation:** Use `argparse`. The script should be callable via command line: `python incident_response.py -f data/server_logs.txt --threshold 50`.
    2.  **Advanced Pattern:** Detect a second attack vector in the logs: **SQL Injection** attempts (look for common SQLi patterns in HTTP requests).
    3.  **Efficiency:** Process the file using Generators (`yield`) to handle potential multi-gigabyte logs without loading everything into RAM.
* **Deliverable:** A production-grade security tool suitable for CI/CD pipelines.

---

### 🛠️ Tech Stack & Constraints
* **Language:** Python 3.10+.
* **Libraries:** **Standard Library ONLY** (`re`, `collections`, `json`, `argparse`, `sys`). No `pandas` or external deps allowed (Simulating a restricted production environment).
* **Logic:** Do not hardcode the IP. The script must dynamically find it based on frequency.

---

### 🚀 Execution Instructions

1.  **Fork** this repository.
2.  Analyze `data/server_logs.txt` manually to understand the format.
3.  Implement your logic in `incident_response.py`.
4.  Run tests: `pytest`.
5.  Submit via **Pull Request** stating your target Level.

> **Note on Build Status:** You will see a ❌ (**Red Cross**) initially. This is expected (TDD). Your goal is to write the code that turns it ✅ (**Green**).

### 🧪 Evaluation Criteria (PureStack Audit)

| Criteria | Weight | Audit Focus |
| :--- | :--- | :--- |
| **Accuracy** | 40% | Does it find the correct IP? Does it count correctly? |
| **Regex Mastery** | 30% | Are the regex patterns efficient and precise? |
| **Code Structure** | 20% | Modular functions vs Spaghetti script. |
| **Tooling** | 10% | CLI implementation and Report generation (Level 1/2). |

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
