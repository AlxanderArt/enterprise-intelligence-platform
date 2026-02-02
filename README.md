# Tableau Enterprise Intelligence Automation Platform

A script-driven enterprise analytics platform that generates, publishes, and refreshes multi-domain datasets for Tableau dashboards.

## Features
- Automated dataset generation (Sales, HR, Finance, Supply Chain, Fraud, Public Impact)
- Tableau publishing via API
- Extract refresh automation
- Executive analytics dashboards
- Forecasting & anomaly detection ready

## Tech Stack
- Python (pandas, numpy)
- Tableau Server Client API
- tabcmd
- Tableau Desktop

## How to Run
1. Install dependencies:
   pip install -r requirements.txt
2. Generate data:
   python scripts/generate_data.py
3. Publish to Tableau:
   python scripts/publish_to_tableau.py
4. Open Tableau Desktop and connect to data folder
5. Build dashboards using enterprise_dashboard_template.twbx

## Author
Alexander Art
