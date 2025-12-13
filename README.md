# 🛡️ PureStack Blue Team Challenge: The Breach

### Context
Welcome to the **PureStack Technical Validation Protocol** for Cybersecurity.
We don't care about certifications if you can't read a log file. We audit for **Scripting**, **Pattern Recognition**, and **Incident Response**.

**⚠️ The Scenario:** Our honeypot has been hit. We need to identify the attacker immediately.

---

### 🎯 The Objective
You are provided with a log file in `data/server_logs.txt`.
Your mission is to write a Python script in `incident_response.py` that parses the file and automatically detects:

1.  **The Attacker's IP:** Identify the IP address with high-frequency failed login attempts (SSH).
2.  **The Attack Vector:** Determine if it's a "brute_force" attack (Rapid failures).

### 🛠️ Requirements
* **Language:** Python 3.
* **No External Libraries:** Use standard libraries (`re`, `collections`, `os`).
* **Logic:** Your code must dynamically parse the file. Do not hardcode the IP.

### 🚀 Getting Started
1.  **Use this template**.
2.  Analyze `data/server_logs.txt` with your eyes first.
3.  Implement the logic in `incident_response.py`.
4.  Run it locally: `python incident_response.py`.
5.  Submit via Pull Request.

---

### 🚨 CRITICAL: Project Structure
To ensure our **Automated Auditor** works correctly, please keep this structure intact:

```text
/
├── .github/workflows/   # PureStack Audit System (DO NOT TOUCH)
├── data/
│   └── server_logs.txt  # <--- EVIDENCE FILE (Do not move)
├── incident_response.py # <--- YOUR SOLUTION GOES HERE
└── README.md
