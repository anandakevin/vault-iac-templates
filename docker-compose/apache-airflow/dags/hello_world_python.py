from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def hello():
    print("👋 Hello from Airflow!")

with DAG(
    dag_id="hello_world_python",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["demo"]
) as dag:
    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=hello
    )

dag.doc_md = __doc__
dag.is_paused_upon_creation = False