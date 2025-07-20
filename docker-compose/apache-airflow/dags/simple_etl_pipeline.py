from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def extract():
    print("📥 Extracting data...")

def transform():
    print("⚙️ Transforming data...")
    time.sleep(2)

def load():
    print("📤 Loading data into warehouse...")

with DAG(
    dag_id="simple_etl_pipeline",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "demo"]
) as dag:
    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3

dag.doc_md = __doc__
dag.is_paused_upon_creation = False