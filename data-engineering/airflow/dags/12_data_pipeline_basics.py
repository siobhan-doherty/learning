import pandas as pd
import os
from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.models import Variable


default_args = {
    'owner': 'siobhan.doherty'
}

def read_csv_file():
    insurance_path = Variable.get(
        "INSURANCE_CSV_PATH", 
        default_var="datasets/insurance.csv"
    )
    if not os.path.exists(insurance_path):
        raise FileNotFoundError(f"Insurance file not found at: {insurance_path}")
    
    df = pd.read_csv(insurance_path)
    print(f"Dataset shape: {df.shape}")

    return df.to_json()

def remove_null_values(ti):
    json_data = ti.xcom_pull(task_ids='read_csv_file')
    df = pd.read_json(json_data)
    df = df.dropna()
    print(f"After removing nulls: {df.shape}")

    return df.to_json()

with DAG(
    dag_id = 'data_pipeline_basics',
    description = 'Running a Python pipeline', 
    default_args = default_args,
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@once',
    tags = ['python', 'transform', 'pipeline'],
    catchup = False
) as dag:
    
    read_csv_file_task = PythonOperator(
        task_id = 'read_csv_file',
        python_callable = read_csv_file
    )

    remove_null_values_task = PythonOperator(
        task_id = 'remove_null_values',
        python_callable = remove_null_values
    )

read_csv_file_task >> remove_null_values_task
