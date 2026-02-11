# Decision Systems Lab — Infrastructure (Phase 0)

> For hands-on setup and usage, see [`README.md`](README.md).

This repository contains the foundational infrastructure for projects under the **Decision Systems Lab**.

## What is the Decision Systems Lab?
An exploratory lab focused on learning how to build **production-grade decision systems** systems that go beyond prediction to recommend, justify, and monitor actions in regulated, high-stakes environments.

## Phase 0 Objective
Establish a reproducible, containerized ML environment that mirrors real-world production setups.

## Scope
- Dockerized development stack
- Public / proxy SaaS and Telco datasets
- Automated data ingestion pipelines
- Command Center dashboards for observability

## Core Principles
- Decisions > predictions
- Production-first, notebook-second
- Defensible by design
- Explainability and auditability built-in

----

**Reproducibility as a Requirement**

In production-grade ML, Docker is used to solve the "Methods Reproducibility" crisis. By encapsulating the entire OS, drivers, and library dependencies, we ensure that a decision system behaves identically during research and real-world deployment (Boettiger, 2015).

Modern MLOps (Machine Learning Operations) frameworks consider containerization a significant step in scaling ML pipelines and ensuring their consistency across their respective development, staging, and production environments (Sarcouncil, 2025). The adoption of containerization eliminates dependency issues and allows for the automated monitoring and self-healing required in high-stakes environments (Kim et al., 2022).

**References**
Boettiger, C. (2015). An introduction to Docker for reproducible research. ACM SIGOPS Operating Systems Review, 49(1), 71–79. https://doi.org/10.1145/2723872.2723882

Kim, B. S., Lee, S. H., Lee, Y. R., Park, Y. H., & Jeong, J. (2022). Design and Implementation of Cloud Docker Application Architecture Based on Machine Learning in Container Management for Smart Manufacturing. Applied Sciences, 12(13), 6737. https://doi.org/10.3390/app12136737

Sarcouncil Journal of Engineering and Computer Sciences. (2025). MLOps in the Enterprise Cloud: Orchestrating Machine Learning Pipelines. https://sarcouncil.com/download-article/SJECS-443-2025-545-551.pdf


