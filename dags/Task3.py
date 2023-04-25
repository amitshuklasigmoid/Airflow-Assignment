import random
from datetime import datetime
from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.contrib.operators.slack_webhook_operator import SlackWebhookOperator


def _random_fail():
    random_number = random.randint(1, 100)
    if(random_number<=50):
        raise Exception("number less than 50, so fail")

with DAG('task_on_slack_integration',
    start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily',  catchup=False
    ) as dag:
    
    dummy_task = PythonOperator(
        task_id='dummy_task',
        python_callable=_random_fail
    )

    slack_msg_success = ":large_blue_circle: Your task is successfully completed "
    slack_msg_failure = ":red_circle: Your task has been failed "

    slack_integration_success = SlackWebhookOperator(
        task_id='slack_integration_success',
        http_conn_id='slack',
        message=slack_msg_success,
        trigger_rule='all_success'
    )


    slack_integration_failure = SlackWebhookOperator(
        task_id='slack_integration_failed',
        http_conn_id='slack',
        message=slack_msg_failure,
        trigger_rule='all_failed'
    )


    dummy_task >> [slack_integration_success,slack_integration_failure]