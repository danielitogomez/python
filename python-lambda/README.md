# python-lambda
Restart ECS Fargate with lambda function with python

1. Basic settings:
- Configure the Handler as lambda_function.restart_service

2. Cron configuration
- On Rules into cloudwatch:

  Step 1: Create rule

  Step 2: Configure the Event Source

  Step 3: Configure the Targets in Function Lambda, them the name of your function

  Step 4: Configure input as Constant (JSON text) and give {    "cluster": "",    "service_name": "" }
