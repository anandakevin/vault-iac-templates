from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="hello_world_bash",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    task = BashOperator(
        task_id="say_hello",
        bash_command="echo Hello World",
    )

dag.doc_md = __doc__
dag.is_paused_upon_creation = False