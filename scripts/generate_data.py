#!/usr/bin/env python3
"""
Enterprise Intelligence Platform - Data Generation Script
Generates synthetic datasets for all dashboard domains
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random
import os

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Common dimensions
REGIONS = ['North', 'South', 'East', 'West', 'Central']
DEPARTMENTS = ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance', 'Operations', 'Customer Support', 'R&D']
COUNTRIES = ['USA', 'Canada', 'UK', 'Germany', 'France', 'Australia', 'Japan', 'Brazil', 'India', 'Mexico']

# Date range: 3 years of data
START_DATE = datetime(2022, 1, 1)
END_DATE = datetime(2024, 12, 31)

def generate_date_range(start, end, n_records):
    """Generate random dates within range"""
    delta = end - start
    return [start + timedelta(days=random.randint(0, delta.days)) for _ in range(n_records)]

def get_base_path():
    """Get the base path for data files"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, '..', 'data')

# =============================================================================
# 1. SALES DATA
# =============================================================================
def generate_sales_data(n_records=5000):
    """Generate sales and customer data"""
    products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Enterprise Suite', 'Basic Plan', 'Premium Plan']
    customer_segments = ['Enterprise', 'SMB', 'Startup', 'Individual', 'Government']
    sales_channels = ['Direct', 'Partner', 'Online', 'Retail']

    data = {
        'transaction_id': [f'TXN-{i:06d}' for i in range(1, n_records + 1)],
        'date': generate_date_range(START_DATE, END_DATE, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'country': np.random.choice(COUNTRIES, n_records),
        'customer_id': [f'CUST-{random.randint(1, 1000):04d}' for _ in range(n_records)],
        'customer_segment': np.random.choice(customer_segments, n_records, p=[0.15, 0.35, 0.25, 0.2, 0.05]),
        'product': np.random.choice(products, n_records),
        'sales_channel': np.random.choice(sales_channels, n_records),
        'quantity': np.random.randint(1, 50, n_records),
        'unit_price': np.round(np.random.uniform(50, 5000, n_records), 2),
        'discount_percent': np.random.choice([0, 5, 10, 15, 20, 25], n_records, p=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05]),
        'customer_lifetime_value': np.round(np.random.uniform(500, 50000, n_records), 2),
        'recency_days': np.random.randint(1, 365, n_records),
        'frequency': np.random.randint(1, 50, n_records),
        'monetary_value': np.round(np.random.uniform(100, 25000, n_records), 2),
        'satisfaction_score': np.round(np.random.uniform(1, 5, n_records), 1),
        'nps_score': np.random.randint(-100, 101, n_records),
    }

    df = pd.DataFrame(data)
    df['revenue'] = np.round(df['quantity'] * df['unit_price'] * (1 - df['discount_percent']/100), 2)
    df['cost'] = np.round(df['revenue'] * np.random.uniform(0.4, 0.7, n_records), 2)
    df['profit'] = df['revenue'] - df['cost']
    df['profit_margin'] = np.round((df['profit'] / df['revenue']) * 100, 2)

    return df

# =============================================================================
# 2. HR DATA
# =============================================================================
def generate_hr_data(n_records=1500):
    """Generate HR and employee data"""
    job_titles = ['Analyst', 'Senior Analyst', 'Manager', 'Senior Manager', 'Director', 'VP', 'Engineer', 'Senior Engineer', 'Specialist', 'Coordinator']
    genders = ['Male', 'Female', 'Non-Binary']
    ethnicities = ['White', 'Black', 'Hispanic', 'Asian', 'Mixed', 'Other']
    education_levels = ['High School', 'Associate', 'Bachelor', 'Master', 'PhD']
    employment_status = ['Active', 'Active', 'Active', 'Active', 'Terminated', 'On Leave']

    hire_dates = generate_date_range(datetime(2015, 1, 1), END_DATE, n_records)

    data = {
        'employee_id': [f'EMP-{i:05d}' for i in range(1, n_records + 1)],
        'department': np.random.choice(DEPARTMENTS, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'job_title': np.random.choice(job_titles, n_records),
        'hire_date': hire_dates,
        'gender': np.random.choice(genders, n_records, p=[0.48, 0.48, 0.04]),
        'ethnicity': np.random.choice(ethnicities, n_records, p=[0.45, 0.15, 0.18, 0.12, 0.07, 0.03]),
        'age': np.random.randint(22, 65, n_records),
        'education': np.random.choice(education_levels, n_records, p=[0.1, 0.15, 0.45, 0.25, 0.05]),
        'salary': np.round(np.random.uniform(40000, 200000, n_records), 2),
        'performance_rating': np.round(np.random.uniform(1, 5, n_records), 1),
        'satisfaction_score': np.round(np.random.uniform(1, 5, n_records), 1),
        'engagement_score': np.round(np.random.uniform(1, 100, n_records), 0),
        'training_hours': np.random.randint(0, 200, n_records),
        'promotion_last_3_years': np.random.choice([0, 1], n_records, p=[0.75, 0.25]),
        'employment_status': np.random.choice(employment_status, n_records),
        'time_to_hire_days': np.random.randint(14, 120, n_records),
        'turnover_risk': np.round(np.random.uniform(0, 1, n_records), 2),
    }

    df = pd.DataFrame(data)
    df['tenure_years'] = np.round((END_DATE - pd.to_datetime(df['hire_date'])).dt.days / 365, 1)
    df['tenure_years'] = df['tenure_years'].clip(lower=0)

    return df

# =============================================================================
# 3. FINANCE DATA
# =============================================================================
def generate_finance_data(n_records=2000):
    """Generate financial data"""
    categories = ['Revenue', 'COGS', 'Operating Expenses', 'Marketing', 'R&D', 'Administrative', 'Depreciation', 'Interest']
    sub_categories = ['Salaries', 'Materials', 'Utilities', 'Rent', 'Software', 'Travel', 'Equipment', 'Services', 'Other']
    cost_centers = ['CC-100', 'CC-200', 'CC-300', 'CC-400', 'CC-500']

    data = {
        'transaction_id': [f'FIN-{i:06d}' for i in range(1, n_records + 1)],
        'date': generate_date_range(START_DATE, END_DATE, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'department': np.random.choice(DEPARTMENTS, n_records),
        'category': np.random.choice(categories, n_records),
        'sub_category': np.random.choice(sub_categories, n_records),
        'cost_center': np.random.choice(cost_centers, n_records),
        'budget_amount': np.round(np.random.uniform(10000, 500000, n_records), 2),
        'actual_amount': np.round(np.random.uniform(8000, 550000, n_records), 2),
        'forecast_amount': np.round(np.random.uniform(9000, 520000, n_records), 2),
        'quarter': [f'Q{((d.month - 1) // 3) + 1}' for d in generate_date_range(START_DATE, END_DATE, n_records)],
        'fiscal_year': np.random.choice([2022, 2023, 2024], n_records),
    }

    df = pd.DataFrame(data)
    df['variance'] = df['actual_amount'] - df['budget_amount']
    df['variance_percent'] = np.round((df['variance'] / df['budget_amount']) * 100, 2)
    df['forecast_accuracy'] = np.round(100 - abs((df['actual_amount'] - df['forecast_amount']) / df['actual_amount'] * 100), 2)

    return df

# =============================================================================
# 4. HEALTHCARE / OPERATIONS DATA
# =============================================================================
def generate_operations_data(n_records=3000):
    """Generate healthcare/operations flow data"""
    service_types = ['Outpatient', 'Inpatient', 'Emergency', 'Surgery', 'Diagnostic', 'Therapy', 'Consultation']
    departments_ops = ['Emergency', 'Radiology', 'Surgery', 'ICU', 'Pharmacy', 'Lab', 'Administration', 'Outpatient']
    priority_levels = ['Low', 'Medium', 'High', 'Critical']

    data = {
        'case_id': [f'CASE-{i:06d}' for i in range(1, n_records + 1)],
        'date': generate_date_range(START_DATE, END_DATE, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'department': np.random.choice(departments_ops, n_records),
        'service_type': np.random.choice(service_types, n_records),
        'priority': np.random.choice(priority_levels, n_records, p=[0.3, 0.4, 0.2, 0.1]),
        'wait_time_minutes': np.random.randint(5, 240, n_records),
        'service_time_minutes': np.random.randint(15, 480, n_records),
        'throughput': np.random.randint(1, 100, n_records),
        'capacity_utilization': np.round(np.random.uniform(0.4, 1.0, n_records), 2),
        'staff_count': np.random.randint(2, 20, n_records),
        'patient_volume': np.random.randint(10, 500, n_records),
        'satisfaction_score': np.round(np.random.uniform(1, 5, n_records), 1),
        'cost_per_case': np.round(np.random.uniform(100, 10000, n_records), 2),
        'readmission_rate': np.round(np.random.uniform(0, 0.2, n_records), 3),
        'bottleneck_flag': np.random.choice([0, 1], n_records, p=[0.85, 0.15]),
    }

    df = pd.DataFrame(data)
    df['total_time_minutes'] = df['wait_time_minutes'] + df['service_time_minutes']
    df['efficiency_score'] = np.round((df['service_time_minutes'] / df['total_time_minutes']) * 100, 2)

    return df

# =============================================================================
# 5. SUPPLY CHAIN DATA
# =============================================================================
def generate_supply_chain_data(n_records=2500):
    """Generate supply chain and inventory data"""
    products = ['Raw Material A', 'Raw Material B', 'Component X', 'Component Y', 'Finished Good 1', 'Finished Good 2', 'Packaging', 'Equipment']
    suppliers = [f'Supplier-{i:03d}' for i in range(1, 51)]
    warehouses = ['WH-North', 'WH-South', 'WH-East', 'WH-West', 'WH-Central']
    risk_levels = ['Low', 'Medium', 'High', 'Critical']

    data = {
        'inventory_id': [f'INV-{i:06d}' for i in range(1, n_records + 1)],
        'date': generate_date_range(START_DATE, END_DATE, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'product': np.random.choice(products, n_records),
        'supplier': np.random.choice(suppliers, n_records),
        'warehouse': np.random.choice(warehouses, n_records),
        'inventory_level': np.random.randint(0, 10000, n_records),
        'reorder_point': np.random.randint(100, 2000, n_records),
        'demand_forecast': np.random.randint(50, 5000, n_records),
        'lead_time_days': np.random.randint(1, 60, n_records),
        'supplier_delay_days': np.random.randint(0, 30, n_records),
        'order_quantity': np.random.randint(100, 5000, n_records),
        'unit_cost': np.round(np.random.uniform(1, 500, n_records), 2),
        'holding_cost': np.round(np.random.uniform(0.5, 10, n_records), 2),
        'stockout_count': np.random.randint(0, 20, n_records),
        'supplier_rating': np.round(np.random.uniform(1, 5, n_records), 1),
        'risk_level': np.random.choice(risk_levels, n_records, p=[0.5, 0.3, 0.15, 0.05]),
        'on_time_delivery_rate': np.round(np.random.uniform(0.7, 1.0, n_records), 2),
    }

    df = pd.DataFrame(data)
    df['inventory_value'] = np.round(df['inventory_level'] * df['unit_cost'], 2)
    df['days_of_supply'] = np.round(df['inventory_level'] / (df['demand_forecast'] / 30), 1)
    df['shortage_risk'] = (df['inventory_level'] < df['reorder_point']).astype(int)

    return df

# =============================================================================
# 6. FRAUD DATA
# =============================================================================
def generate_fraud_data(n_records=4000):
    """Generate fraud and anomaly detection data"""
    transaction_types = ['Purchase', 'Refund', 'Transfer', 'Withdrawal', 'Deposit', 'Payment']
    merchant_categories = ['Retail', 'Online', 'Travel', 'Entertainment', 'Utilities', 'Healthcare', 'Gas Station', 'Restaurant']
    device_types = ['Desktop', 'Mobile', 'Tablet', 'POS', 'ATM']

    data = {
        'transaction_id': [f'FRD-{i:06d}' for i in range(1, n_records + 1)],
        'date': generate_date_range(START_DATE, END_DATE, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'country': np.random.choice(COUNTRIES, n_records),
        'customer_id': [f'CUST-{random.randint(1, 2000):04d}' for _ in range(n_records)],
        'transaction_type': np.random.choice(transaction_types, n_records),
        'merchant_category': np.random.choice(merchant_categories, n_records),
        'amount': np.round(np.random.exponential(500, n_records), 2),
        'device_type': np.random.choice(device_types, n_records),
        'ip_risk_score': np.round(np.random.uniform(0, 100, n_records), 1),
        'velocity_24h': np.random.randint(1, 50, n_records),
        'distance_from_home': np.random.randint(0, 5000, n_records),
        'time_since_last_txn_minutes': np.random.randint(1, 10080, n_records),
        'failed_attempts': np.random.randint(0, 10, n_records),
        'is_weekend': np.random.choice([0, 1], n_records, p=[0.7, 0.3]),
        'is_night': np.random.choice([0, 1], n_records, p=[0.75, 0.25]),
        'is_international': np.random.choice([0, 1], n_records, p=[0.85, 0.15]),
    }

    df = pd.DataFrame(data)

    df['fraud_risk_score'] = np.round(
        (df['ip_risk_score'] * 0.3 +
         (df['velocity_24h'] / 50 * 100) * 0.2 +
         (df['distance_from_home'] / 5000 * 100) * 0.15 +
         (df['failed_attempts'] / 10 * 100) * 0.15 +
         df['is_night'] * 20 +
         df['is_international'] * 30) / 2, 1
    ).clip(0, 100)

    df['is_fraud'] = (df['fraud_risk_score'] > 70).astype(int) | np.random.choice([0, 1], n_records, p=[0.97, 0.03])
    df['is_anomaly'] = (df['fraud_risk_score'] > 50).astype(int)

    return df

# =============================================================================
# 7. PUBLIC IMPACT DATA
# =============================================================================
def generate_public_impact_data(n_records=1500):
    """Generate public impact data (housing, climate, health)"""
    categories = ['Housing', 'Climate', 'Health', 'Education', 'Employment', 'Infrastructure']
    indicators = ['Air Quality Index', 'Housing Affordability Index', 'Unemployment Rate', 'Life Expectancy',
                  'CO2 Emissions', 'Renewable Energy %', 'Hospital Beds per 1000', 'School Enrollment Rate',
                  'Income Inequality', 'Access to Clean Water']

    data = {
        'record_id': [f'PUB-{i:05d}' for i in range(1, n_records + 1)],
        'date': generate_date_range(START_DATE, END_DATE, n_records),
        'region': np.random.choice(REGIONS, n_records),
        'country': np.random.choice(COUNTRIES, n_records),
        'category': np.random.choice(categories, n_records),
        'indicator': np.random.choice(indicators, n_records),
        'value': np.round(np.random.uniform(10, 100, n_records), 2),
        'target_value': np.round(np.random.uniform(50, 100, n_records), 2),
        'previous_year_value': np.round(np.random.uniform(10, 95, n_records), 2),
        'population_affected': np.random.randint(10000, 10000000, n_records),
        'budget_allocated': np.round(np.random.uniform(100000, 50000000, n_records), 2),
        'budget_spent': np.round(np.random.uniform(80000, 48000000, n_records), 2),
        'projects_completed': np.random.randint(0, 100, n_records),
        'projects_in_progress': np.random.randint(0, 50, n_records),
        'satisfaction_rating': np.round(np.random.uniform(1, 5, n_records), 1),
        'trend_direction': np.random.choice(['Improving', 'Stable', 'Declining'], n_records, p=[0.4, 0.35, 0.25]),
        'priority_level': np.random.choice(['Low', 'Medium', 'High', 'Critical'], n_records, p=[0.2, 0.4, 0.3, 0.1]),
    }

    df = pd.DataFrame(data)
    df['year_over_year_change'] = np.round((df['value'] - df['previous_year_value']) / df['previous_year_value'] * 100, 2)
    df['target_achievement'] = np.round((df['value'] / df['target_value']) * 100, 2)
    df['budget_utilization'] = np.round((df['budget_spent'] / df['budget_allocated']) * 100, 2)

    return df

# =============================================================================
# MAIN EXECUTION
# =============================================================================
def main():
    """Generate all datasets and save to CSV"""
    base_path = get_base_path()

    print("=" * 60)
    print("Enterprise Intelligence Platform - Data Generation")
    print("=" * 60)

    datasets = [
        ('Sales', generate_sales_data, 'sales/sales_data.csv'),
        ('HR', generate_hr_data, 'hr/hr_data.csv'),
        ('Finance', generate_finance_data, 'finance/finance_data.csv'),
        ('Operations', generate_operations_data, 'healthcare/operations_data.csv'),
        ('Supply Chain', generate_supply_chain_data, 'supply_chain/supply_chain_data.csv'),
        ('Fraud', generate_fraud_data, 'fraud/fraud_data.csv'),
        ('Public Impact', generate_public_impact_data, 'public_impact/public_impact_data.csv'),
    ]

    for name, generator, filepath in datasets:
        print(f"\nGenerating {name} data...")
        df = generator()
        full_path = os.path.join(base_path, filepath)
        df.to_csv(full_path, index=False)
        print(f"  Saved: {filepath}")
        print(f"  Records: {len(df):,}")
        print(f"  Columns: {len(df.columns)}")

    print("\n" + "=" * 60)
    print("Data generation complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()
