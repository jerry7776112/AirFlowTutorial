from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}

with DAG(
    dag_id='dag_with_cron_expression_v02',
    default_args=default_args,
    start_date=datetime(2023, 10, 30),
    schedule_interval='0 0 * * *'
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo dag with cron expression!'
    )
    task1