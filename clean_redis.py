import datetime
import json
import pathlib
import airflow
import requests
from vars import *
from redis import Redis
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
import datetime as dt

r = Redis(redis_config["redis_host"], redis_config["redis_port"], redis_config["redis_db"])

dag = DAG(
    dag_id="remove_transaction_id",
    start_date=dt.datetime(year=2022, month=7, day=4),
    schedule_interval="@day",
)

start = EmptyOperator(task_id="Start")


def _clean_redis():
    r.flushall()


clean_redis = PythonOperator(
    task_id="clean_redis",
    python_callable=_clean_redis,
    dag=dag
)

notify = BashOperator(
    task_id="notify",
    bash_command='echo "All transaction_ids have been cleaned."',
    dag=dag
)

clean_redis >> notify
