from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = "cyber_matrix_secret_key"

# قائمة لتخزين السجلات الأمنية في الذاكرة
security_logs = []

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('index.html', logs=security_logs)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "Shahad Alqarni" and password == "cyber2026":
            session['logged_in'] = True
            return redirect(url_for('index'))
        return "Invalid Credentials", 401
    return '''
        <h2>Security SIEM Login</h2>
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

# --- نقطة الاستقبال (API Endpoint) ---
@app.route('/api/report', methods=['POST'])
def report_event():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400

    # هنا يتم استقبال بيانات الهجوم الأساسية + استهلاك المعالج كإضافة ثانوية
    log_entry = {
        "id": len(security_logs) + 1,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "attack_type": data.get("attack_type", "Unknown Threat"),
        "source_ip": data.get("source_ip", "127.0.0.1"),
        "details": data.get("details", "No details"),
        "risk_score": data.get("risk_score", 50),
        "cpu_usage": data.get("cpu_usage", 0.0)  # <-- استقبال نسبة استهلاك المعالج هنا وتخزينها
    }
    
    # إضافة السجل الجديد في أعلى القائمة ليعرض أحدث التنبيهات أولاً
    security_logs.insert(0, log_entry)
    return jsonify({"status": "success", "message": "Security event logged"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)