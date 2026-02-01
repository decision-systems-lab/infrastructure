import streamlit as st
import duckdb
import pandas as pd

# --- CONFIG ---
DB_PATH = "/app/data/duckdb/decision_systems.duckdb"
TABLE_NAME = "telco_churn_clean"

# --- CONNECT TO DUCKDB ---
con = duckdb.connect(database=DB_PATH, read_only=True)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Command Center Dashboard",
    layout="wide"
)
st.title("🏗 Command Center Dashboard – Telco Churn")

# --- LOAD DATA FUNCTION ---
@st.cache_data
def load_data():
    try:
        df = con.execute(f"SELECT * FROM {TABLE_NAME}").df()
        return df
    except duckdb.CatalogException:
        st.warning(f"Table '{TABLE_NAME}' not found in DuckDB!")
        return pd.DataFrame()

# --- REFRESH BUTTON ---
if st.button("🔄 Refresh DB"):
    st.cache_data.clear()
    st.success("Cache cleared! Data will reload on next access.")

df = load_data()

# --- DASHBOARD ---
if not df.empty:
    # --- TOP KEY METRICS ---
    st.subheader("📌 Key Metrics")
    total_customers = len(df)
    churn_count = df['churn'].sum() if 'churn' in df.columns else 0
    churn_rate = churn_count / total_customers if total_customers > 0 else 0
    avg_tenure = df['tenure'].mean() if 'tenure' in df.columns else 0
    avg_monthly_charges = df['monthly_charges'].mean() if 'monthly_charges' in df.columns else 0

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Customers", total_customers)
    col2.metric("Churn Count", churn_count)
    col3.metric("Churn Rate", f"{churn_rate:.1%}")
    col4.metric("Avg Tenure (months)", f"{avg_tenure:.1f}")
    col4.metric("Avg Monthly Charges", f"${avg_monthly_charges:.2f}")

    # --- Layout: Numeric & Categorical Columns ---
    col1, col2 = st.columns(2)

    # --- Column 1: Numeric Overview ---
    with col1:
        st.subheader("📊 Numeric Columns")
        numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        if numeric_cols:
            for col in numeric_cols:
                st.markdown(f"**{col}**")
                st.bar_chart(df[col].value_counts())
        else:
            st.info("No numeric columns detected.")

    # --- Column 2: Categorical Overview ---
    with col2:
        st.subheader("📂 Categorical Columns")
        cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()
        if cat_cols:
            for col in cat_cols:
                st.markdown(f"**{col}**")
                st.bar_chart(df[col].value_counts())
        else:
            st.info("No categorical columns detected.")

    # --- Bottom: Summary Stats ---
    st.subheader("📋 Dataset Summary")
    st.write(df.describe(include="all").T)

    # --- Missing Values Heatmap ---
    st.subheader("❌ Missing Values Heatmap")
    import seaborn as sns
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.heatmap(df.isnull(), cbar=False, cmap="magma", yticklabels=False, ax=ax)
    st.pyplot(fig)

else:
    st.info("No data available. Make sure the DuckDB table is populated.")
