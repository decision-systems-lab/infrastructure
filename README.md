# Decision Systems Lab  
## Phase 0 — Infrastructure Foundation

![Phase 0 Status](https://img.shields.io/badge/Phase%200-Complete-brightgreen?style=for-the-badge)
<!-- ![Phase 1 Status](https://img.shields.io/badge/Phase%201-Pending-lightgrey?style=for-the-badge) -->

Decision Systems Lab is an exploratory environment for building **production-grade decision systems** that move beyond prediction to recommend, justify, and monitor actions in high-stakes environments.

Phase 0 establishes the infrastructure required to build those systems correctly.

---

In Phase 0, we create a **reproducible, containerized ML environment** that mirrors real-world production setups.

## 🏗 What Was Built

### 1️⃣ Containerized Development Stack
- Docker + Docker Compose setup
- Streamlit application service
- Persistent DuckDB database
- Volume-mapped data directories
- Makefile workflow abstraction
- Reproducibility validated via `docker compose up`

### 2️⃣ Data Layer
- Raw Telco Customer Churn dataset from https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- Automated ingestion script: src/ingestion/ingest_telco_churn.py
- Cleaned data persisted in: data/duckdb/decision_systems.duckdb
- Persistence verified across container restarts

### 3️⃣ Command Center Dashboard
Streamlit dashboard providing:

- Intuitive view of the dataset
- Feature inspection options
- SQL console to quickly view the data

Accessible at: http://localhost:8501

## ✅ Phase 0 Status

**Complete. Infrastructure validated. Ready for Phase 1.**

> For research context and references behind Phase 0, see [`README_ACADEMIC.md`](README_ACADEMIC.md).


