from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.empty import EmptyOperator
from airflow.operators.email import EmailOperator

default_args = {
    'owner' :'admin',
    'retries': 5,
    'retry_delay' : timedelta(minutes=5)
}

with DAG(dag_id='task_on_email', start_date=datetime(2022, 1, 1), 
         default_args=default_args, schedule_interval='@daily',  catchup=False
        ) as dag:
    
    dummy_task = EmptyOperator(
        task_id = "dummy_task"
    )
    
    send_email = EmailOperator(
        task_id='send_email',
        to='amitshukla@sigmoidanalytics.com',
        subject='Airflow Alert',
        html_content=""" <h3>Email Test Airflow </h3> """,
        conn_id="email_smtp"
    )
    
    dummy_task >> send_email

    
