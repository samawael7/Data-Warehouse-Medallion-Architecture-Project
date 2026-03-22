# 🏗️ Data Warehouse — Medallion Architecture Project

An end-to-end Data Warehouse project built using the **Medallion Architecture** (Bronze → Silver → Gold), powered by **SQL Server**, **dbt Core**, and **Apache Airflow** on Docker.

Inspired by the Data with Baraa tutorial, extended with dbt Core, 
Apache Airflow, and Docker for a production-grade pipeline.

---



## 🚀 Key Highlights

- Built a Medallion Architecture pipeline (Bronze → Silver → Gold)
- Designed a Star Schema with fact and dimension tables
- Implemented data cleaning, validation, and deduplication logic
- Used dbt Core for modular transformations, testing, and documentation
- Orchestrated the pipeline using Apache Airflow DAGs
- Containerized the environment using Docker for reproducibility

## 📊 Data Flow

<img width="1197" height="757" alt="Data Flow Diagram" src="https://github.com/user-attachments/assets/3ea3bdd7-b5ef-4f2f-8dfa-8b848789e1d4" />

---

## 🏅 Medallion Architecture

<img width="1263" height="751" alt="Data Medallion Archeticture" src="https://github.com/user-attachments/assets/d39d6fb1-606c-464b-9a92-33cfbc0c3672" />

---

## 🗂️ Project Structure
```
├── SQL Scripts/          # Bronze & Silver stored procedures + Gold views
├── datawarehouse/        # dbt Core project (Silver & Gold models)
│   ├── models/
│   │   ├── silver/       # 6 dbt models for data cleaning & transformation
│   │   └── gold/         # 3 dbt models (dim_customers, dim_products, fact_sales)
│   ├── macros/           # Custom schema generation macro
│   └── tests/            # dbt data tests
├── airflow/              # Apache Airflow DAGs & Docker setup
│   ├── dags/
│   │   └── dbt_dag.py    # DAG to orchestrate dbt run & dbt test
│   └── docker-compose.yml
└── docs/                 # Architecture diagrams
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| SQL Server | Data Warehouse database |
| dbt Core | Data transformation & testing |
| Apache Airflow | Pipeline orchestration |
| Docker | Containerized Airflow environment |
| Git | Version control |

---

## 🥉 Bronze Layer
- Raw data loaded from CSV files using SQL Server **Stored Procedures**
- Sources: CRM (customers, products, sales) + ERP (customers, locations, categories)
- No transformations applied — raw data preserved as-is

## 🥈 Silver Layer
- Data cleaning & transformation via **Stored Procedures** and **dbt models**
- Deduplication using `ROW_NUMBER()` window function
- Standardization of gender, marital status, country codes, product lines
- Date validation and sales amount recalculation

## 🥇 Gold Layer

A business-oriented Star Schema designed for analytics and reporting:

- dim_customers — unified customer dimension combining CRM and ERP data
- dim_products — enriched product dimension with category hierarchy
- fact_sales — transactional fact table capturing sales metrics

The model enables efficient querying for KPIs such as revenue, customer segmentation, and product performance.

---

## ⚙️ dbt Pipeline
```bash
# Run all models
dbt run

# Run data tests
dbt test

# Generate documentation
dbt docs generate
dbt docs serve
```

---

## 🔄 Airflow Orchestration

The dbt pipeline is orchestrated using **Apache Airflow** running on Docker:
```
dbt_run → dbt_test
```

Scheduled to run daily, ensuring the Silver and Gold layers are always up to date.

---

## 🚀 Getting Started

### Prerequisites
- SQL Server
- Python 3.8+
- Docker Desktop
- dbt Core (`pip install dbt-sqlserver`)

### Run the dbt Pipeline
```bash
cd datawarehouse
dbt run
dbt test
```

### Run Airflow
```bash
cd airflow
docker-compose up -d
```

Access the Airflow UI at `http://localhost:8085`
