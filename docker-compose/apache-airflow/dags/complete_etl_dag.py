from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

# Dummy extract function
def extract(**kwargs):
    data = {
        'id': [1, 2, 3],
        'name': ['alice', 'bob', 'charlie']
    }
    df = pd.DataFrame(data)
    output_path = '/tmp/extracted_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Extracted data written to {output_path}")
    return output_path

# Dummy transform function
def transform(ti, **kwargs):
    input_path = ti.xcom_pull(task_ids='extract_task')
    df = pd.read_csv(input_path)
    df['name'] = df['name'].str.upper()
    output_path = '/tmp/transformed_data.csv'
    df.to_csv(output_path, index=False)
    print(f"Transformed data written to {output_path}")
    return output_path

# Dummy load function
def load(ti, **kwargs):
    input_path = ti.xcom_pull(task_ids='transform_task')
    df = pd.read_csv(input_path)
    final_path = '/tmp/final_output.csv'
    df.to_csv(final_path, index=False)
    print(f"Final loaded data written to {final_path}")

default_args = {
    'start_date': datetime(2025, 1, 1),
}

with DAG(
    dag_id='dummy_etl_pipeline',
    default_args=default_args,
    schedule_interval=None,  # Manual trigger
    catchup=False,
    tags=['example', 'etl', 'dummy'],
) as dag:

    extract_task = PythonOperator(
        task_id='extract_task',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform_task',
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id='load_task',
        python_callable=load,
    )

    extract_task >> transform_task >> load_task

dag.doc_md = __doc__
dag.is_paused_upon_creation = False
