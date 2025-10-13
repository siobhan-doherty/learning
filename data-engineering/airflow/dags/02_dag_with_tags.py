from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'siobhan.doherty',
}

with DAG(
    dag_id = 'hello_world_with_tags',
    description = 'Our second "Hello World" DAG!',
    default_args = default_args,
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@daily',
    tags = ['beginner', 'bash', 'hello world'],
    catchup = False
) as dag:
    
    hello_task = BashOperator(
        task_id = 'hello_world_task_two',
        bash_command = 'echo Hello world once again!',
    )

