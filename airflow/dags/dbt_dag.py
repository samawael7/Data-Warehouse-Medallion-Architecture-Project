from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# تعريف الـ DAG
with DAG(
    dag_id='dbt_pipeline',                    # اسم الـ DAG
    start_date=datetime(2026, 1, 1),          # تاريخ البداية
    schedule_interval='@daily',               # بيشتغل كل يوم
    catchup=False                             # متشغلش الأيام اللي فاتت
) as dag:

    # شغل dbt run
    dbt_run = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/dbt && dbt run --profiles-dir /opt/airflow/.dbt',
    )

    # شغل dbt test بعد الـ run
    dbt_test = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/dbt && dbt test --profiles-dir /opt/airflow/.dbt',
    )

    # الترتيب: الأول dbt run وبعدين dbt test
    dbt_run >> dbt_test