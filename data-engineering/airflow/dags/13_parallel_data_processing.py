import pandas as pd
import os 
from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator
from airflow.models import Variable


default_args = {
    'owner': 'siobhan.doherty'
}

def get_insurance_path():
    insurance_path = Variable.get(
        "INSURANCE_CSV_PATH",
        default_var = "datasets/insurance.csv"
    )

    if not insurance_path.startswith('/'):
        dag_dir = os.path.dirname(os.path.abspath(__file__))
        insurance_path = os.path.join(dag_dir, insurance_path)
    
    return insurance_path

def get_output_path(filename):
    output_dir = Variable.get(
        "OUTPUT_DIR",
        default_var = "output"
    )

    if not output_dir.startswith('/'):
        dag_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(dag_dir, output_dir)

    os.makedirs(output_dir, exist_ok=True)
    
    return os.path.join(output_dir, filename)

def read_csv_file():
    insurance_path = get_insurance_path()

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

def groupby_smoker(ti):
    json_data = ti.xcom_pull(task_ids='remove_null_values')
    df = pd.read_json(json_data)

    smoker_df = df.groupby('smoker').agg({
        'age': 'mean',
        'bmi': 'mean',
        'charges': 'mean'
    }).reset_index()

    output_path = get_output_path('grouped_by_smoker.csv')
    smoker_df.to_csv(output_path, index=False)
    print(f"Smoker grouping saved to {output_path}")

def groupby_region(ti):
    json_data = ti.xcom_pull(task_ids='remove_null_values')
    df = pd.read_json(json_data)

    region_df = df.groupby('region').agg({
        'age': 'mean',
        'bmi': 'mean',
        'charges': 'mean'
    }).reset_index()

    output_path = get_output_path('grouped_by_region.csv')
    region_df.to_csv(output_path, index=False)
    print(f"Region grouping saved to {output_path}")

with DAG(
    dag_id = 'parallel_data_processing',
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

    groupby_smoker_task = PythonOperator(
        task_id = 'groupby_smoker',
        python_callable = groupby_smoker
    )

    groupby_region_task = PythonOperator(
        task_id = 'groupby_region',
        python_callable = groupby_region
    )

read_csv_file_task >> remove_null_values_task >> [groupby_smoker_task, groupby_region_task]

