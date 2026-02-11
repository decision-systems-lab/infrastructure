import streamlit as st
import duckdb
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIG ---
DB_PATH = "/app/data/duckdb/decision_systems.duckdb"
TABLE_NAME = "telco_churn_clean"

# --- PAGE CONFIG ---
st.set_page_config(page_title="Command Center", layout="wide")
st.title("🔍 Discovery Lab")
st.markdown(f"Exploring table: `{TABLE_NAME}`")

# --- DATABASE CONNECTION ---
def get_connection():
    return duckdb.connect(database=DB_PATH, read_only=True)

@st.cache_data
def load_full_data():
    with get_connection() as con:
        df = con.execute(f"SELECT * FROM {TABLE_NAME}").df()
        # Clean column names (strip spaces and lowercase)
        df.columns = [c.strip().lower() for c in df.columns]
        return df

df = load_full_data()

# --- SIDEBAR: TABLE INVENTORY ---
st.sidebar.header("📋 Table Inventory")
if st.sidebar.button("Show All Tables"):
    with get_connection() as con:
        tables = con.execute("SHOW TABLES").df()
        st.sidebar.write(tables)

st.sidebar.divider()
st.sidebar.write(f"**Total Rows:** {df.shape[0]:,}")
st.sidebar.write(f"**Total Columns:** {df.shape[1]}")

# --- MAIN INTERFACE: TABS ---
tab1, tab2, tab3 = st.tabs(["🧬 Schema Profile", "📊 Value Distribution", "💻 SQL Lab"])

# --- TAB 1: SCHEMA PROFILE ---
with tab1:
    st.subheader("Field Metadata & Health")
    
    # Calculate health metrics
    null_counts = df.isnull().sum()
    null_pct = (null_counts / len(df)) * 100
    dtype_df = pd.DataFrame({
        "Data Type": df.dtypes.astype(str),
        "Missing Values": null_counts,
        "Missing %": null_pct.map("{:.2f}%".format),
        "Unique Values": df.nunique()
    })
    
    st.dataframe(dtype_df, use_container_width=True)
    
    st.subheader("Statistical Summary")
    st.dataframe(df.describe(include='all').T, use_container_width=True)

# --- TAB 2: VALUE DISTRIBUTION ---
with tab2:
    st.subheader("Feature Inspection")
    
    selected_col = st.selectbox("Select a column to analyze:", df.columns)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.write(f"**Top 10 Values for `{selected_col}`**")
        st.write(df[selected_col].value_counts().head(10))
        
    with col2:
        fig, ax = plt.subplots(figsize=(10, 5))
        if df[selected_col].dtype in ['int64', 'float64']:
            # Numerical Distribution
            sns.histplot(df[selected_col], kde=True, color="teal", ax=ax)
            ax.set_title(f"Histogram of {selected_col}")
        else:
            # Categorical Distribution
            sns.countplot(data=df, y=selected_col, order=df[selected_col].value_counts().index[:15], palette="viridis", ax=ax)
            ax.set_title(f"Top 15 Categories in {selected_col}")
        
        st.pyplot(fig)

# --- TAB 3: SQL LAB ---
with tab3:
    st.subheader("Ad-hoc SQL Console")
    st.info("Write standard SQL to query the DuckDB file directly.")
    
    default_query = f"SELECT * FROM {TABLE_NAME} WHERE tenure > 50 LIMIT 5"
    user_query = st.text_area("SQL Query Editor", value=default_query, height=150)
    
    if st.button("Run Query"):
        try:
            with get_connection() as con:
                query_result = con.execute(user_query).df()
                st.success(f"Returned {len(query_result)} rows")
                st.dataframe(query_result, use_container_width=True)
        except Exception as e:
            st.error(f"SQL Error: {e}")