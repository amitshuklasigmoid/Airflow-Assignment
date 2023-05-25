# Rithish's Review
**Q1**

- Created a postgres connection in the airflow ui and supplied the conn_id in the postgres operator.
- Created a supermarket table and inserted few values in it.

**Q2**

- Modified to contain the environment variables for email - smtp host, smtp user, smtp password, smtp port, smtp mail from.
- Ran the email using email operator

**Q3**

- Created a slack webhook token and provided the token details in host and password part.
- Provided the connection id in the slack webhook operator. One of the task had trigger rule set to `all_success` and other had set it to `all_failed`.

# Dhruv's Review
**Q1**

- Created dags with PostgresOperator.
- In the Airflow UI, added a connection in admin to postgres and specified the connection id in the postgres operator.
- Modified the docker compose file to map the 5432 port of postgres container to 5432 port of host.
- Created a supermarket table and inserted few values in it.

**Q2**

- Created email task with `EmailOperator` and an always succeeding task with `PythonOperator'.
- Modified the `airflow.cfg` to contain the app-password and email details. Attached the config file with the config file of the docker container using volumes mapping.

**Q3**

- Created slack task with `SlackWebhookOperator` and a simple task with `PythonOperator`.
- Made a connection in admin to http with slack webhook token in the password.
- Provided the connection id in the slack operator.
