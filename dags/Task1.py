from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(dag_id='task_on_table', start_date=datetime(2022, 1, 1), 
        schedule_interval='@daily',  catchup=False) as dag:

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                email TEXT NOT NULL
            );
        '''
    )
    
    insert_values = PostgresOperator(
        task_id = 'insert_values',
        postgres_conn_id='postgres',
        sql = '''
                INSERT INTO users VALUES
                ('amit','shukla','india','cseamit@gmail.com'),
                ('sam','curran','australia','sam@gmail.com'),
                ('Sumit','Sharma','India','sumit@gmail.com') ;    
        '''
    )
    
    select_values = PostgresOperator(
        task_id = "select_values",
        postgres_conn_id='postgres',
        sql='''
            SELECT * FROM users;
        '''
    )
    
    create_table >> insert_values >> select_values
    
    
