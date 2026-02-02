# Enterprise Intelligence Platform

A unified enterprise analytics platform built in Tableau integrating sales, customer, HR, financial, supply chain, and risk data into a single multi-dashboard system.

## Project Overview

**Problem Statement:** Organizations struggle to make decisions because data is siloed across Sales, Customers, HR, Finance, Operations, Supply Chain, Risk/Fraud, and Public Impact domains.

**Solution:** A single Tableau platform with 8 interactive dashboard tabs that executives and analysts can use to monitor performance, detect risks, and plan strategy.

## Dashboard Sections

### 1. Executive Overview (Main Home Page)
- **Purpose:** High-level decision dashboard
- **KPIs:** Total Revenue, Profit Margin, Customer Growth, Turnover Rate, Inventory Risk, Fraud Risk Score
- **Visuals:** KPI tiles, Monthly trend line, Global map, Filters (year, region, department)

### 2. Sales & Customer Intelligence
- Sales by region & product
- Customer segmentation (RFM analysis)
- Loyalty trends
- Geographic heatmap
- Top/bottom performers

### 3. HR, Diversity & Retention
- Employee count by department
- Turnover rate
- Diversity breakdown
- Time-to-hire
- Satisfaction index

### 4. Healthcare / Operations Flow
- Throughput / volume
- Wait times
- Bottleneck departments
- Capacity utilization
- Trend analysis

### 5. Supply Chain & Inventory Risk
- Inventory levels
- Supplier delays
- Forecasted shortages
- Demand trends
- Risk heat indicators

### 6. Financial Performance & Forecasting
- Budget vs actual
- Expense categories
- Profit forecast
- What-if scenario slider
- Trend projections

### 7. Fraud & Anomaly Detection
- Outlier transactions
- Risk score
- Unusual activity by region
- Drill-down table
- Conditional alerts

### 8. Public Impact / Story Dashboard
- Housing, climate, or health data
- Interactive maps
- Long-term trends
- Narrative captions
- Policy insights

## Technical Skills Demonstrated

- LOD Expressions
- Parameters & What-if analysis
- Forecasting
- Clustering
- Calculated KPIs
- Maps (Geographic visualization)
- Dashboard actions
- Drill-downs
- Storytelling
- Multi-source data blending
- Executive UX design

## Project Structure

```
enterprise-intelligence-platform/
├── README.md
├── data/
│   ├── sales/
│   │   └── sales_data.csv
│   ├── hr/
│   │   └── hr_data.csv
│   ├── finance/
│   │   └── finance_data.csv
│   ├── healthcare/
│   │   └── operations_data.csv
│   ├── supply_chain/
│   │   └── supply_chain_data.csv
│   ├── fraud/
│   │   └── fraud_data.csv
│   └── public_impact/
│       └── public_impact_data.csv
├── documentation/
│   ├── data_dictionary.md
│   └── tableau_instructions.md
├── tableau/
│   └── (Tableau workbook files)
└── scripts/
    └── data_generation.py
```

## Data Strategy

All datasets share common fields for integration:
- **Date** (standardized format: YYYY-MM-DD)
- **Region** (North, South, East, West, Central)
- **Department** (where applicable)

This enables:
- Joining by common fields
- Multi-source blending in Tableau
- Cross-domain parameter filtering

## Build Phases

### Phase 1: Data Prep
- [x] Collect/generate datasets
- [x] Standardize Date, Region, Department fields
- [ ] Load into Tableau Prep (optional cleaning)

### Phase 2: Core Dashboards
- [ ] Build Executive Overview
- [ ] Build Sales & Customer Intelligence
- [ ] Build Financial Performance
- [ ] Build HR, Diversity & Retention
- [ ] Build Supply Chain & Inventory Risk

### Phase 3: Advanced Analytics
- [ ] Add forecasting models
- [ ] Add clustering analysis
- [ ] Add anomaly detection
- [ ] Add parameters for what-if analysis

### Phase 4: Storytelling
- [ ] Create Public Impact dashboard
- [ ] Add captions and insights
- [ ] Create Tableau Story mode
- [ ] Final UX polish

## Portfolio Description

> Designed and built a unified enterprise analytics platform in Tableau integrating sales, customer, HR, financial, supply chain, and risk data into a single multi-dashboard system. The platform provides executive-level KPIs, predictive forecasts, anomaly detection, and interactive storytelling to support strategic and operational decision-making.

## Resume Bullet

> Built an enterprise-grade Tableau intelligence dashboard combining multi-domain datasets (sales, HR, finance, operations, and risk) with forecasting, anomaly detection, and interactive decision tools for executive reporting.

## Author

Alexander Art

## License

MIT License
