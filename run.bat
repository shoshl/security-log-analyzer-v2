@echo off
echo [*] Starting Cyber Matrix Server & Agent...
start cmd /k "python app.py"
timeout /t 3 >nul
start cmd /k "python agent.py"