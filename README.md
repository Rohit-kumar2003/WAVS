# WAVS
Web Application Vulnerability Scanner
📌 Project Description

This project is a lightweight, automated web application vulnerability scanner that integrates two popular open-source tools—Nikto and OWASP ZAP—to detect and report common web security flaws. Built using Python and Flask, the tool provides a simple web interface for users to enter a URL, initiate scans, and view results with graphical severity breakdowns.

🚀 Features

Scan websites using Nikto (server-level vulnerabilities)

Scan using OWASP ZAP API (application-level vulnerabilities)

Dynamic charts (via Chart.js) to visualize vulnerability severity

Clear output in tabular and graphical formats

Works on Windows OS with Python virtual environment support

🛠️ Technologies Used

Python 3.10+

Flask

HTML5, CSS3

Chart.js (for graphs)

Nikto (requires Strawberry Perl)

OWASP ZAP (requires API access)

🖥️ System Requirements

Software

Python 3.10+

Flask

Strawberry Perl (for Nikto)

OWASP ZAP 2.12+ (run in daemon mode)

Git (for cloning repository)

Hardware

Windows OS (Tested on Windows 10)

Minimum 4 GB RAM (8 GB recommended)

500 MB free disk space

📦 Installation Steps

Clone the repository

   git clone https://github.com/yourusername/web-vuln-scanner.git
   cd web-vuln-scanner

Set up a virtual environment

   python -m venv venv
   venv\Scripts\activate

Install dependencies

   pip install -r requirements.txt

Download and configure OWASP ZAP

Download from: https://www.zaproxy.org/download/

Start in daemon mode:

   zap.bat -daemon

Run the Flask app

   python app.py

Access the application

Open browser and go to http://127.0.0.1:5000

🔍 How It Works

Users input a target URL on the homepage.

Backend calls Nikto (via subprocess) and ZAP (via API).

Scan results are parsed and categorized.

The frontend displays a bar chart (High, Medium, Low vulnerabilities) and a detailed table.
