import time
from datetime import datetime
from airflow import DAG 
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'siobhan.doherty'
}

def greet_hello(name):
    print("Hello, {name}!".format(name=name))

def greet_goodbye(name, city):
    print("Hello, {name} from {city}".format(name=name, city=city))

with DAG(
    dag_id = 'python_operator_parameters', 
    description = 'Python operators in DAGs',
    default_args = default_args, 
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@daily',
    tags = ['parameters', 'python']
) as dag:
    taskA = PythonOperator(
        task_id = 'greet_hello', 
        python_callable = greet_hello,
        op_kwargs = { 'name': 'Jane' }
    )

    taskB = PythonOperator(
        task_id = 'greet_goodbye', 
        python_callable = greet_goodbye,
        op_kwargs = { 'name': 'John', 'city': 'London' }
    )

taskA >> taskB
