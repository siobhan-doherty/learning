from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'siobhan.doherty'
}

def print_function():
    print("The simplest possible Python operator!")

with DAG(
    dag_id = 'python_operator_basic',
    description = 'Python operators in DAGs',
    default_args = default_args, 
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@daily',
    tags = ['simple', 'python'],
    catchup = False
) as dag:
    task = PythonOperator(
        task_id = 'python_task', 
        python_callable = print_function
    )

