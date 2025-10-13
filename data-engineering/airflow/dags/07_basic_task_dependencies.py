from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'siobhan.doherty'
}

with DAG(
    dag_id = 'bash_operator_basic_dependencies',
    description = 'DAG with multiple tasks and dependencies',
    default_args = default_args,
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@once', 
    catchup = False
) as dag:

    taskA = BashOperator(
        task_id = 'taskA',
        bash_command = 'echo TASK A has executed!'
    )

    taskB = BashOperator(
        task_id = 'taskB',
        bash_command = 'echo TASK B has executed!'
    )

taskA >> taskB
