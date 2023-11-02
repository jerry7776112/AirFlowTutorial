from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# 設定重置時間5分鐘&延遲2分鐘(每次等待重置的時間)
default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)

}


with DAG(
    dag_id='our_first_dag_v5',
    default_args=default_args,
    description='This is our first dag that we write',
    # 設定從甚麼時候啟動及按時啟動
    # 2021年7月29日開始每天凌晨兩點啟動
    start_date=datetime(2021, 7, 29, 2),
    schedule_interval='@daily'

) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo Hello World. This is the first task!"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command='echo Hey, I am task2 and will be running after task1!'
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command='echo Hey, I am task3 and will be running after task1 at the same time as task2!'
    )

# 設定 task2 在 task1 後執行
# task1.set_downstream(task2)

# task3 在task1後與task2同時執行
# 第一種方法
# task1.set_downstream(task2)
# task1.set_downstream(task3)

# 第二種方法
# task1 >> task2
# task1 >> task3

# 第三種方法
task1 >> [task2, task3]