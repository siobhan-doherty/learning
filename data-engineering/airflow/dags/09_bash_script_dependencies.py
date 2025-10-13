from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'siobhan.doherty'
}

with DAG(
    dag_id = 'bash_script_dependencies',
    description = 'DAG with multiple tasks and dependencies part III',
    default_args = default_args,
    start_date = datetime(2024, 1, 1),
    schedule_interval = '@daily',
    tags = ['scripts', 'template search'],
    catchup = False
) as dag:

    taskA = BashOperator(
        task_id = 'taskA',
        bash_command = 'bash bash_scripts/task_a.sh'
    )

    taskB = BashOperator(
        task_id = 'taskB',
        bash_command = 'bash bash_scripts/task_b.sh'
    )

    taskC = BashOperator(
        task_id = 'taskC',
        bash_command = 'bash bash_scripts/task_c.sh'
    )

    taskD = BashOperator(
        task_id = 'taskD',
        bash_command = 'bash bash_scripts/task_d.sh'
    )

    taskE = BashOperator(
        task_id = 'taskE',
        bash_command = 'bash bash_scripts/task_e.sh'
    )

    taskF = BashOperator(
        task_id = 'taskF',
        bash_command = 'bash bash_scripts/task_f.sh'
    )

    taskG = BashOperator(
        task_id = 'taskG',
        bash_command = 'bash bash_scripts/task_g.sh'
    )

taskA >> taskB >> taskE
taskA >> taskC >> taskF
taskA >> taskD >> taskG
