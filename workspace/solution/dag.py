import datetime as dt

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.docker.operators.docker import DockerOperator

"""
Exercise 2

Create a DAG which will run on your birthday to congratulate you.
"""

dag = DAG(
    dag_id="secrets2",
    description="Wishes you a happy birthday",
    default_args={"owner": "Airflow"},
    schedule_interval="@yearly",
    catchup=False,
    start_date=dt.datetime(2021, 1, 1),
)

task = DockerOperator(
    dag=dag,
    task_id="task",
    image="mylocalimage",
    container_name="task",
    auto_remove=True,
)

task
