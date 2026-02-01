import streamlit as st
import duckdb

st.title("Decision Systems Lab")

con = duckdb.connect(":memory:")
con.execute("CREATE TABLE test (x INTEGER)")
con.execute("INSERT INTO test VALUES (1), (2), (3)")

st.write("DuckDB Test Query")
st.dataframe(con.execute("SELECT * FROM test").fetchdf())
