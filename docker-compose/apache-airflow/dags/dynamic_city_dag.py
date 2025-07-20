from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
}

cities = ["Jakarta", "Tokyo", "Berlin"]

def print_city(city):
    print(f"📍 Processing city: {city}")

with DAG(
    dag_id="dynamic_city_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    tags=["dynamic"]
) as dag:
    for city in cities:
        task = PythonOperator(
            task_id=f"process_{city.lower()}",
            python_callable=print_city,
            op_args=[city],
        )

dag.doc_md = __doc__
dag.is_paused_upon_creation = False
