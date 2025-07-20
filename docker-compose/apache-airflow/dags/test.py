from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    "test",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    t1 = EmptyOperator(task_id="first_task")

dag.doc_md = __doc__
dag.is_paused_upon_creation = False