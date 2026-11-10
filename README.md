# 🛡️ Security Log Analyzer & SIEM Simulation Tool

A lightweight Client-Server Security Information and Event Management (SIEM) prototype designed for educational purposes and defensive security monitoring. 

This tool simulates real-time cybersecurity threat detection (such as **Brute Force**, **SQL Injection**, and **Port Scanning**) while simultaneously collecting system telemetry (CPU usage) to correlate security incidents with system performance.

---

## 🚀 Key Features

* **Real-time Threat Detection Simulation:** Monitors and logs simulated cyber-attacks like Brute Force, SQL Injection, and Unauthorized Access.
* **Client-Server Architecture:** Uses a Python-based Agent (`agent.py`) to report events and a Flask Server (`app.py`) to process and display them.
* **System Telemetry Integration:** Captures live CPU load metrics alongside security alerts using `psutil`.
* **Web Dashboard:** Secure login interface displaying an organized, live-updating table of security logs and risk scores.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Libraries:** `requests`, `psutil`
* **Frontend:** HTML, CSS (Responsive security dashboard layout)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/shoshl/security_log_analyzer.git](https://github.com/shoshl/security_log_analyzer.git)
cd security_log_analyzer