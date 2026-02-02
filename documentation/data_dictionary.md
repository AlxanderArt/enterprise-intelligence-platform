# Data Dictionary

## Enterprise Intelligence Platform

This document describes all fields across the 7 datasets used in the Enterprise Intelligence Platform.

---

## Common Fields (Used for Joining/Blending)

| Field | Type | Description | Values |
|-------|------|-------------|--------|
| date | Date | Transaction/record date | 2022-01-01 to 2024-12-31 |
| region | String | Geographic region | North, South, East, West, Central |
| department | String | Business department | Sales, Marketing, Engineering, HR, Finance, Operations, Customer Support, R&D |

---

## 1. Sales Data (`sales/sales_data.csv`)

**Records:** 5,000 | **Purpose:** Sales & Customer Intelligence Dashboard

| Field | Type | Description |
|-------|------|-------------|
| transaction_id | String | Unique transaction identifier (TXN-XXXXXX) |
| date | Date | Transaction date |
| region | String | Sales region |
| country | String | Customer country |
| customer_id | String | Customer identifier (CUST-XXXX) |
| customer_segment | String | Enterprise, SMB, Startup, Individual, Government |
| product | String | Product name |
| sales_channel | String | Direct, Partner, Online, Retail |
| quantity | Integer | Units sold |
| unit_price | Float | Price per unit |
| discount_percent | Integer | Discount applied (0-25%) |
| customer_lifetime_value | Float | CLV estimate |
| recency_days | Integer | Days since last purchase (RFM) |
| frequency | Integer | Purchase frequency (RFM) |
| monetary_value | Float | Monetary value (RFM) |
| satisfaction_score | Float | Customer satisfaction (1-5) |
| nps_score | Integer | Net Promoter Score (-100 to 100) |
| revenue | Float | Calculated: quantity * unit_price * (1 - discount) |
| cost | Float | Cost of goods sold |
| profit | Float | Revenue minus cost |
| profit_margin | Float | Profit margin percentage |

---

## 2. HR Data (`hr/hr_data.csv`)

**Records:** 1,500 | **Purpose:** HR, Diversity & Retention Dashboard

| Field | Type | Description |
|-------|------|-------------|
| employee_id | String | Unique employee identifier (EMP-XXXXX) |
| department | String | Employee department |
| region | String | Office region |
| job_title | String | Job title/role |
| hire_date | Date | Date of hire |
| gender | String | Male, Female, Non-Binary |
| ethnicity | String | White, Black, Hispanic, Asian, Mixed, Other |
| age | Integer | Employee age |
| education | String | High School, Associate, Bachelor, Master, PhD |
| salary | Float | Annual salary |
| performance_rating | Float | Performance rating (1-5) |
| satisfaction_score | Float | Job satisfaction (1-5) |
| engagement_score | Float | Engagement level (1-100) |
| training_hours | Integer | Training hours completed |
| promotion_last_3_years | Integer | Promoted in last 3 years (0/1) |
| employment_status | String | Active, Terminated, On Leave |
| time_to_hire_days | Integer | Days to fill position |
| turnover_risk | Float | Predicted turnover risk (0-1) |
| tenure_years | Float | Years with company |

---

## 3. Finance Data (`finance/finance_data.csv`)

**Records:** 2,000 | **Purpose:** Financial Performance & Forecasting Dashboard

| Field | Type | Description |
|-------|------|-------------|
| transaction_id | String | Unique identifier (FIN-XXXXXX) |
| date | Date | Transaction date |
| region | String | Budget region |
| department | String | Department |
| category | String | Revenue, COGS, Operating Expenses, etc. |
| sub_category | String | Salaries, Materials, Utilities, etc. |
| cost_center | String | Cost center code (CC-XXX) |
| budget_amount | Float | Budgeted amount |
| actual_amount | Float | Actual spent/received |
| forecast_amount | Float | Forecasted amount |
| quarter | String | Q1, Q2, Q3, Q4 |
| fiscal_year | Integer | 2022, 2023, 2024 |
| variance | Float | Actual minus budget |
| variance_percent | Float | Variance as percentage |
| forecast_accuracy | Float | Forecast accuracy percentage |

---

## 4. Operations Data (`healthcare/operations_data.csv`)

**Records:** 3,000 | **Purpose:** Healthcare/Operations Flow Dashboard

| Field | Type | Description |
|-------|------|-------------|
| case_id | String | Unique case identifier (CASE-XXXXXX) |
| date | Date | Service date |
| region | String | Facility region |
| department | String | Emergency, Radiology, Surgery, etc. |
| service_type | String | Outpatient, Inpatient, Emergency, etc. |
| priority | String | Low, Medium, High, Critical |
| wait_time_minutes | Integer | Wait time in minutes |
| service_time_minutes | Integer | Service duration |
| throughput | Integer | Cases processed |
| capacity_utilization | Float | Capacity used (0.4-1.0) |
| staff_count | Integer | Staff assigned |
| patient_volume | Integer | Daily patient volume |
| satisfaction_score | Float | Patient satisfaction (1-5) |
| cost_per_case | Float | Cost per case |
| readmission_rate | Float | 30-day readmission rate |
| bottleneck_flag | Integer | Bottleneck indicator (0/1) |
| total_time_minutes | Integer | Wait + service time |
| efficiency_score | Float | Service efficiency percentage |

---

## 5. Supply Chain Data (`supply_chain/supply_chain_data.csv`)

**Records:** 2,500 | **Purpose:** Supply Chain & Inventory Risk Dashboard

| Field | Type | Description |
|-------|------|-------------|
| inventory_id | String | Unique identifier (INV-XXXXXX) |
| date | Date | Record date |
| region | String | Warehouse region |
| product | String | Product/material name |
| supplier | String | Supplier identifier |
| warehouse | String | Warehouse location |
| inventory_level | Integer | Current stock units |
| reorder_point | Integer | Reorder threshold |
| demand_forecast | Integer | Forecasted demand |
| lead_time_days | Integer | Supplier lead time |
| supplier_delay_days | Integer | Recent delay days |
| order_quantity | Integer | Standard order quantity |
| unit_cost | Float | Cost per unit |
| holding_cost | Float | Holding cost per unit |
| stockout_count | Integer | Stockout incidents |
| supplier_rating | Float | Supplier rating (1-5) |
| risk_level | String | Low, Medium, High, Critical |
| on_time_delivery_rate | Float | OTD rate (0.7-1.0) |
| inventory_value | Float | Total inventory value |
| days_of_supply | Float | Days of inventory remaining |
| shortage_risk | Integer | Below reorder point (0/1) |

---

## 6. Fraud Data (`fraud/fraud_data.csv`)

**Records:** 4,000 | **Purpose:** Fraud & Anomaly Detection Dashboard

| Field | Type | Description |
|-------|------|-------------|
| transaction_id | String | Unique identifier (FRD-XXXXXX) |
| date | Date | Transaction date |
| region | String | Transaction region |
| country | String | Transaction country |
| customer_id | String | Customer identifier |
| transaction_type | String | Purchase, Refund, Transfer, etc. |
| merchant_category | String | Retail, Online, Travel, etc. |
| amount | Float | Transaction amount |
| device_type | String | Desktop, Mobile, Tablet, POS, ATM |
| ip_risk_score | Float | IP address risk (0-100) |
| velocity_24h | Integer | Transactions in 24 hours |
| distance_from_home | Integer | Miles from home location |
| time_since_last_txn_minutes | Integer | Minutes since last transaction |
| failed_attempts | Integer | Failed auth attempts |
| is_weekend | Integer | Weekend transaction (0/1) |
| is_night | Integer | Night transaction (0/1) |
| is_international | Integer | International transaction (0/1) |
| fraud_risk_score | Float | Calculated risk score (0-100) |
| is_fraud | Integer | Confirmed fraud (0/1) |
| is_anomaly | Integer | Flagged as anomaly (0/1) |

---

## 7. Public Impact Data (`public_impact/public_impact_data.csv`)

**Records:** 1,500 | **Purpose:** Public Impact Story Dashboard

| Field | Type | Description |
|-------|------|-------------|
| record_id | String | Unique identifier (PUB-XXXXX) |
| date | Date | Record date |
| region | String | Geographic region |
| country | String | Country |
| category | String | Housing, Climate, Health, etc. |
| indicator | String | Specific metric name |
| value | Float | Current indicator value |
| target_value | Float | Target value |
| previous_year_value | Float | Prior year value |
| population_affected | Integer | Population impacted |
| budget_allocated | Float | Budget allocated |
| budget_spent | Float | Budget utilized |
| projects_completed | Integer | Completed projects |
| projects_in_progress | Integer | Ongoing projects |
| satisfaction_rating | Float | Public satisfaction (1-5) |
| trend_direction | String | Improving, Stable, Declining |
| priority_level | String | Low, Medium, High, Critical |
| year_over_year_change | Float | YoY change percentage |
| target_achievement | Float | Progress toward target (%) |
| budget_utilization | Float | Budget utilization (%) |

---

## Key Calculated Fields for Tableau

### Executive KPIs
- **Total Revenue:** SUM([revenue]) from Sales
- **Profit Margin:** SUM([profit]) / SUM([revenue])
- **Customer Growth:** COUNT(DISTINCT [customer_id]) with YoY comparison
- **Turnover Rate:** COUNT([employment_status] = 'Terminated') / COUNT([employee_id])
- **Inventory Risk:** COUNT([shortage_risk] = 1) / COUNT([inventory_id])
- **Fraud Risk Score:** AVG([fraud_risk_score])

### LOD Expressions Examples
```
// Customer-level revenue
{ FIXED [customer_id] : SUM([revenue]) }

// Department turnover rate
{ FIXED [department] : COUNTD(IF [employment_status] = 'Terminated' THEN [employee_id] END) / COUNTD([employee_id]) }

// Regional fraud rate
{ FIXED [region] : SUM([is_fraud]) / COUNT([transaction_id]) }
```

### RFM Segmentation
- **Recency:** Lower is better (days since last purchase)
- **Frequency:** Higher is better (purchase count)
- **Monetary:** Higher is better (total spend)
