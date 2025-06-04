# mlflow-local
running mlflow in local file system with docker compose on Ubuntu 22.04

Run the docker compose file
----------------------------
Goto terminal >

1. be in the folder where the yaml file is
2. sudo docker compose up -d
3. mlruns is where all the ml runs would be found
4. backend - can be used for sqlliteDB later
5. check mlflow server running in localhost:5000
6. The test_mlflow.py can be used from a different project to set the tracking uri to this server and log experiments/models etc

