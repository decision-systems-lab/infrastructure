# src/ingestion/ingest_telco_churn.py
import duckdb
import pandas as pd
from pathlib import Path

# -------------------------------
# Paths
# -------------------------------
# Docker container path for persistent DuckDB storage
DB_PATH = Path("infrastructure/data/duckdb/decision_systems.duckdb")

# Raw CSV location
RAW_CSV = Path("infrastructure/data/raw/telco_customer_churn.csv")

# -------------------------------
# Read raw dataset
# -------------------------------
df = pd.read_csv(RAW_CSV)

# -------------------------------
# Minimal cleaning
# -------------------------------
# 1. Normalize column names
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

# 2. Convert numeric columns
df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
df['monthlycharges'] = pd.to_numeric(df['monthlycharges'], errors='coerce')
df['totalcharges'] = pd.to_numeric(df['totalcharges'], errors='coerce')

# 3. Handle missing values (simple example)
df.fillna({'totalcharges': 0}, inplace=True)

# 4. Encode target
df['churn'] = df['churn'].map({'Yes': 1, 'No': 0})

# -------------------------------
# Write to DuckDB
# -------------------------------
# Connect or create DB
con = duckdb.connect(database=DB_PATH, read_only=False)

# Create or replace table
con.execute("CREATE TABLE IF NOT EXISTS telco_churn_clean AS SELECT * FROM df")

# Optional: check row count
print("Rows in DuckDB table:", con.execute("SELECT COUNT(*) FROM telco_churn_clean").fetchone()[0])

con.close()
