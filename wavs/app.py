from flask import Flask, render_template, request
import subprocess
import requests
import time

app = Flask(__name__)

# Nikto Scan Function
def run_nikto(url):
    result = subprocess.run(["perl",'nikto\program\nikto.pl', '-h', url], capture_output=True, text=True)
    return result.stdout

# ZAP Scan Start Function
def run_zap(url):
    zap_url = "http://localhost:8080/JSON/ascan/action/scan/"
    params = {'url': url, 'apikey': ''}  # API key nahi lagayi hai (agar disable hai)
    response = requests.get(zap_url, params=params)
    if response.status_code == 200:
        return "ZAP scan initiated successfully!"
    else:
        return "Failed to initiate ZAP scan."

# ZAP Alerts Fetch karne ka Function
def get_zap_alerts():
    zap_alerts_url = "http://localhost:8080/JSON/core/view/alerts/"
    params = {'baseurl': '', 'apikey': ''}
    response = requests.get(zap_alerts_url, params=params)
    if response.status_code == 200:
        return response.json()['alerts']
    else:
        return []

# Flask route for Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Flask route for Scan
@app.route('/scan', methods=['POST'])
def scan():
    url = request.form['url']

    nikto_result = run_nikto(url)   # Nikto Scan Run
    run_zap(url)                    # ZAP Scan Start
    time.sleep(15)                  # ZAP ko time do scan karne ka

    zap_alerts = get_zap_alerts()    # ZAP Scan Result

    # Count severity
    severity_counts = {'high': 0, 'medium': 0, 'low': 0}
    for alert in zap_alerts:
        risk = alert.get('risk')
        if risk == 'High':
            severity_counts['high'] += 1
        elif risk == 'Medium':
            severity_counts['medium'] += 1
        elif risk == 'Low':
            severity_counts['low'] += 1

    return render_template('result.html', url=url, nikto_result=nikto_result, zap_alerts=zap_alerts, severity_counts=severity_counts)

if __name__ == "__main__":
    app.run(debug=True)
