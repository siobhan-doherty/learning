import time
from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'siobhan.doherty'
}

def task_a():
    print("TASK A executed!")

def task_b():
    time.sleep(5)
    print("TASK B executed!")

def task_c():
    print("TASK C executed!")

def task_d():
    print("TASK D executed!")

with DAG(
    dag_id = 'python_operator_dependencies', 
    description = 'Python operators in DAGs',
    default_args = default_args, 
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@daily',
    tags = ['dependencies', 'python']
) as dag:
    taskA = PythonOperator(
        task_id = 'task_a', 
        python_callable = task_a
    )

    taskB = PythonOperator(
        task_id = 'task_b', 
        python_callable = task_b
    )

    taskC = PythonOperator(
        task_id = 'task_c', 
        python_callable = task_c
    )

    taskD = PythonOperator(
        task_id = 'task_d', 
        python_callable = task_d
    )

taskA >> [taskB, taskC]
[taskB, taskC] >> taskD
