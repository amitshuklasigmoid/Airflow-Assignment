# Airflow-Assignment
## 1) Create a dag with following tasks:
- Task to create a simple table
- Task to insert few custom values in to the created table in previous step.
- Task to select the values from the table

I have created a table as users, added few values into it and then using command line, we can see values inserted into the table.
I have also created a postgres connection for connecting with postgres.
<img width="1428" alt="Screenshot 2023-04-25 at 2 28 10 PM" src="https://user-images.githubusercontent.com/122515454/234227110-c103d500-5b16-451b-980f-780d30a24f36.png">

<img width="848" alt="Screenshot 2023-04-25 at 2 29 05 PM" src="https://user-images.githubusercontent.com/122515454/234227350-0ac74a48-0a21-4937-9522-725353130263.png">

## 2) Create a dag with following tasks:
- A dummy task which always succeeds
- Upon successful completion of the task your setup of airflow environment should be such that it sends an email alert to your sigmoid mail id. Schedule the dag to run daily.

I have created a connection as email_smtp for connecting with smtp and added connection type as email, added required fields such as login, password and host name.
I have generated password from google app passwords for my gmail account.
<img width="1422" alt="Screenshot 2023-04-25 at 2 33 01 PM" src="https://user-images.githubusercontent.com/122515454/234228318-e8c08703-0884-458a-bd7f-6db8f13cb5b9.png">

<img width="631" alt="Screenshot 2023-04-25 at 2 33 20 PM" src="https://user-images.githubusercontent.com/122515454/234228399-0a3226a5-4703-46a3-ad51-b46b7282f7c1.png">

## 3) Create a dag with following tasks:
- A dummy task which can succeed/fail.
- Upon success/failure send an alert message to slack workspace.
I have created a connection as slack for connecting with slack workspace and added host as https://hooks.slack.com/services and added password that i have generated using slack api webhook.

If dummy task got successed then it will send a success message into slack workspcace.
<img width="1421" alt="Screenshot 2023-04-25 at 2 35 50 PM" src="https://user-images.githubusercontent.com/122515454/234229024-efc7fbd8-b88d-4ab5-8f1b-8dced8377a72.png">

<img width="1439" alt="Screenshot 2023-04-25 at 2 36 30 PM" src="https://user-images.githubusercontent.com/122515454/234229212-87e1c854-fe96-4e4e-950a-d6c634eb1782.png">


If dummy task got failed then it will send a failure message into slack workspcace.
<img width="1424" alt="Screenshot 2023-04-25 at 2 36 55 PM" src="https://user-images.githubusercontent.com/122515454/234229306-18e08297-cf0f-4cf9-8601-a727bc13a5fb.png">

<img width="1435" alt="Screenshot 2023-04-25 at 2 38 40 PM" src="https://user-images.githubusercontent.com/122515454/234229792-8f0e3404-b705-4ecc-94a1-b572d1eb4ed3.png">

# My all connections for all the given tasks

<img width="1440" alt="Screenshot 2023-04-25 at 2 40 17 PM" src="https://user-images.githubusercontent.com/122515454/234230177-f7726506-5d32-4fcb-a2c9-5b582fa323ea.png">
