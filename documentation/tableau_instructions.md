# Tableau Build Instructions

## Enterprise Intelligence Platform

Step-by-step guide to building the 8-dashboard Tableau workbook.

---

## Phase 1: Data Connection Setup

### Step 1.1: Connect Data Sources

1. Open Tableau Desktop
2. Click **Connect** > **Text file** (CSV)
3. Navigate to the `data/` folder
4. Connect each CSV file as a separate data source:
   - `sales/sales_data.csv`
   - `hr/hr_data.csv`
   - `finance/finance_data.csv`
   - `healthcare/operations_data.csv`
   - `supply_chain/supply_chain_data.csv`
   - `fraud/fraud_data.csv`
   - `public_impact/public_impact_data.csv`

### Step 1.2: Data Relationships (Optional)

For cross-source analysis, create relationships using:
- **Date** (convert to Date type)
- **Region** (North, South, East, West, Central)

Or use **Data Blending** with Region as the linking field.

---

## Phase 2: Create Calculated Fields

### Global Parameters

Create these parameters for interactivity:

```
// Year Filter Parameter
Name: [Select Year]
Data type: Integer
Allowable values: List (2022, 2023, 2024)
Current value: 2024

// Region Filter Parameter
Name: [Select Region]
Data type: String
Allowable values: List (All, North, South, East, West, Central)
Current value: All

// Forecast Months Parameter
Name: [Forecast Months]
Data type: Integer
Range: 1 to 24
Current value: 12
```

### Sales Calculated Fields

```
// Total Revenue
SUM([revenue])

// Profit Margin %
SUM([profit]) / SUM([revenue])

// Customer Count
COUNTD([customer_id])

// Average Order Value
SUM([revenue]) / COUNT([transaction_id])

// YoY Revenue Growth
(SUM([revenue]) - LOOKUP(SUM([revenue]), -12)) / LOOKUP(SUM([revenue]), -12)

// RFM Segment (LOD)
IF { FIXED [customer_id] : AVG([recency_days]) } <= 30
   AND { FIXED [customer_id] : SUM([frequency]) } >= 10
   AND { FIXED [customer_id] : SUM([monetary_value]) } >= 5000
THEN "Champions"
ELSEIF { FIXED [customer_id] : AVG([recency_days]) } <= 90
THEN "Loyal"
ELSE "At Risk"
END
```

### HR Calculated Fields

```
// Turnover Rate
COUNTD(IF [employment_status] = "Terminated" THEN [employee_id] END)
/ COUNTD([employee_id])

// Average Tenure
AVG([tenure_years])

// Diversity Index
COUNTD([ethnicity]) / 6  // 6 categories

// High Performer Count
COUNTD(IF [performance_rating] >= 4 THEN [employee_id] END)

// Turnover Risk (Department Level)
{ FIXED [department] : AVG([turnover_risk]) }
```

### Finance Calculated Fields

```
// Budget Variance
SUM([actual_amount]) - SUM([budget_amount])

// Variance %
([Budget Variance] / SUM([budget_amount])) * 100

// Forecast Accuracy
AVG([forecast_accuracy])

// What-If Scenario (Parameter-driven)
SUM([actual_amount]) * (1 + [Growth Rate Parameter])
```

### Operations Calculated Fields

```
// Average Wait Time
AVG([wait_time_minutes])

// Capacity Utilization %
AVG([capacity_utilization]) * 100

// Bottleneck Count
SUM([bottleneck_flag])

// Efficiency Score
AVG([efficiency_score])
```

### Supply Chain Calculated Fields

```
// Inventory Risk %
SUM([shortage_risk]) / COUNT([inventory_id])

// Days of Supply (Avg)
AVG([days_of_supply])

// Supplier Performance
AVG([on_time_delivery_rate]) * 100

// At-Risk Inventory Value
SUM(IF [risk_level] IN ("High", "Critical") THEN [inventory_value] END)
```

### Fraud Calculated Fields

```
// Fraud Rate
SUM([is_fraud]) / COUNT([transaction_id])

// Average Risk Score
AVG([fraud_risk_score])

// High Risk Transaction Count
COUNTD(IF [fraud_risk_score] > 70 THEN [transaction_id] END)

// Anomaly Detection (Z-Score)
([amount] - WINDOW_AVG([amount])) / WINDOW_STDEV([amount])
```

---

## Phase 3: Build Dashboards

### Dashboard 1: Executive Overview

**Layout:** Fixed size 1920x1080

**Components:**
1. **KPI Tiles (6 total)** - BANs at top
   - Total Revenue (Sales data)
   - Profit Margin (Sales data)
   - Customer Growth (Sales data)
   - Turnover Rate (HR data)
   - Inventory Risk (Supply Chain data)
   - Fraud Risk Score (Fraud data)

2. **Monthly Trend Line** - Line chart
   - X: Date (Month)
   - Y: Revenue, Profit
   - Color: Year

3. **Global Map** - Symbol map
   - Geography: Country
   - Size: Revenue
   - Color: Profit Margin

4. **Filter Panel** (Right side)
   - Year parameter
   - Region parameter
   - Department dropdown

**Dashboard Actions:**
- Filter: Map click filters all sheets
- Highlight: Hover highlights related data

---

### Dashboard 2: Sales & Customer Intelligence

**Components:**
1. **Sales by Region** - Bar chart
2. **Product Performance** - Treemap
3. **RFM Segmentation** - Scatter plot
   - X: Recency
   - Y: Monetary Value
   - Size: Frequency
   - Color: RFM Segment
4. **Geographic Heatmap** - Filled map
5. **Top 10 / Bottom 10 Toggle** - Parameter-driven table

**Advanced Features:**
- Add clustering on RFM scatter
- Set actions for drill-through

---

### Dashboard 3: HR, Diversity & Retention

**Components:**
1. **Employee Count by Department** - Bar chart
2. **Turnover Rate Trend** - Line chart
3. **Diversity Breakdown** - Donut/Pie charts
   - Gender
   - Ethnicity
   - Education
4. **Time-to-Hire** - Bullet chart
5. **Satisfaction Index** - Gauge or BAN

**Advanced Features:**
- Add turnover risk heatmap by department
- Parameter for diversity dimension toggle

---

### Dashboard 4: Healthcare / Operations Flow

**Components:**
1. **Throughput by Department** - Bar chart
2. **Wait Time Distribution** - Histogram
3. **Bottleneck Heatmap** - Matrix
   - Rows: Department
   - Columns: Priority
   - Color: Wait Time
4. **Capacity Utilization** - Bullet chart
5. **Trend Analysis** - Line chart with reference bands

**Advanced Features:**
- Add conditional formatting for bottlenecks
- Forecasting on throughput

---

### Dashboard 5: Supply Chain & Inventory Risk

**Components:**
1. **Inventory Levels** - Area chart by product
2. **Supplier Performance** - Scatter plot
   - X: On-time delivery rate
   - Y: Supplier rating
   - Size: Order volume
3. **Risk Heat Map** - Matrix
   - Color by risk level
4. **Demand vs Supply** - Dual-axis line chart
5. **Shortage Alerts** - Table with conditional formatting

**Advanced Features:**
- Forecasting on demand trends
- Reference lines for reorder points

---

### Dashboard 6: Financial Performance & Forecasting

**Components:**
1. **Budget vs Actual** - Bullet chart by category
2. **Expense Breakdown** - Waterfall chart
3. **Profit Forecast** - Line chart with forecast
   - Enable Tableau's built-in forecasting
4. **What-If Slider** - Parameter control
   - Links to calculated field
5. **Variance Analysis** - Diverging bar chart

**Advanced Features:**
- What-if parameter (growth rate slider)
- Trend projections with confidence bands

---

### Dashboard 7: Fraud & Anomaly Detection

**Components:**
1. **Fraud Rate Over Time** - Line chart
2. **Risk Score Distribution** - Histogram with reference line
3. **Geographic Risk Map** - Filled map
   - Color: Average fraud risk score
4. **Anomaly Table** - Detail table
   - Highlight rows where is_fraud = 1
5. **Alert Indicators** - BANs with conditional coloring

**Advanced Features:**
- Clustering for anomaly detection
- Drill-down from map to transaction detail
- Conditional alerts (color coding)

---

### Dashboard 8: Public Impact / Story Dashboard

**Components:**
1. **Interactive Map** - Symbol/filled map
   - Size/Color by indicator value
2. **Long-term Trends** - Line chart
   - Multiple indicators
3. **Target Progress** - Bullet chart
4. **Narrative Captions** - Text boxes with insights
5. **Category Filter** - Quick filter or parameter

**Story Mode:**
- Create Tableau Story with 4-5 story points
- Add annotations and captions
- Include policy insights

---

## Phase 4: Advanced Analytics

### Forecasting Setup

1. Select a time-series measure (Revenue, Demand, etc.)
2. Right-click > **Forecast** > **Show Forecast**
3. Configure:
   - Forecast length: Use parameter
   - Model: Automatic
   - Confidence: 95%

### Clustering Setup

1. Drag measures to Rows/Columns
2. Analytics Pane > **Cluster** > Drag to view
3. Configure number of clusters (3-5 recommended)
4. Color marks by cluster

### Parameter What-If Analysis

1. Create parameter (e.g., Growth Rate: 0% to 50%)
2. Create calculated field using parameter
3. Add parameter control to dashboard
4. Users can slide to see projections

---

## Phase 5: Final Polish

### Visual Design Guidelines

- **Color Palette:** Use consistent corporate colors
  - Primary: #1A365D (Navy)
  - Accent: #3182CE (Blue)
  - Success: #38A169 (Green)
  - Warning: #D69E2E (Gold)
  - Danger: #E53E3E (Red)

- **Typography:**
  - Titles: 14pt Bold
  - Labels: 10pt Regular
  - KPIs: 24pt Bold

- **Layout:**
  - Consistent padding (8-16px)
  - Clear visual hierarchy
  - White space for breathing room

### Performance Optimization

1. Extract data (don't use live connection for large files)
2. Use context filters for heavy dashboards
3. Limit marks on complex visualizations
4. Hide unused worksheets

### Publishing

1. Publish to Tableau Public or Tableau Server
2. Enable mobile layout (optional)
3. Test all interactions
4. Add workbook description

---

## Keyboard Shortcuts

| Action | Shortcut |
|--------|----------|
| New Worksheet | Ctrl/Cmd + M |
| New Dashboard | - |
| Duplicate Sheet | Ctrl/Cmd + D |
| Undo | Ctrl/Cmd + Z |
| Format Painter | Ctrl/Cmd + Shift + C |
| Show/Hide Cards | - |

---

## Resources

- [Tableau Documentation](https://help.tableau.com)
- [Tableau Public Gallery](https://public.tableau.com/gallery)
- [LOD Expressions Guide](https://help.tableau.com/current/pro/desktop/en-us/calculations_calculatedfields_lod.htm)
- [Forecasting in Tableau](https://help.tableau.com/current/pro/desktop/en-us/forecast_create.htm)
