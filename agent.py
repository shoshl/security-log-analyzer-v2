import time
import requests
import random
import psutil  # مكتبة مراقبة الجهاز

SERVER_URL = "http://127.0.0.1:5000/api/report"

# الهجمات الأمنية الأساسية
threat_scenarios = [
    {
        "attack_type": "Brute Force Attack",
        "source_ip": "192.168.1.105",
        "details": "Multiple failed SSH/RDP login attempts on Administrator account",
        "risk_score": 88
    },
    {
        "attack_type": "SQL Injection",
        "source_ip": "45.33.22.11",
        "details": "Payload detected in query parameter: ' OR '1'='1",
        "risk_score": 95
    },
    {
        "attack_type": "Port Scanning",
        "source_ip": "10.0.0.45",
        "details": "Nmap stealth SYN scan detected across ports 20-1024",
        "risk_score": 75
    },
    {
        "attack_type": "Unauthorized Access Attempt",
        "source_ip": "172.16.0.88",
        "details": "Attempt to access restricted system configuration files",
        "risk_score": 82
    }
]

print("[*] Cyber Security Agent with CPU Telemetry is active...")

while True:
    try:
        # اختيار هجوم أمني عشوائي
        threat = random.choice(threat_scenarios)
        
        # قراءة استهلاك المعالج الحقيقي لجهازك كإضافة ثانوية
        cpu_val = psutil.cpu_percent(interval=1)
        
        payload = {
            "attack_type": threat["attack_type"],
            "source_ip": threat["source_ip"],
            "details": f"{threat['details']} | CPU Load: {cpu_val}%",
            "risk_score": threat['risk_score'],
            "cpu_usage": cpu_val
        }
        
        response = requests.post(SERVER_URL, json=payload)
        print(f"[+] Reported -> [{threat['attack_type']}] | CPU: {cpu_val}% | Risk: {threat['risk_score']}%")
        
    except Exception as e:
        print(f"[-] Error: {e}")
        
    time.sleep(8)