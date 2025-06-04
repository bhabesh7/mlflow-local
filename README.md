# mlflow-local
running mlflow in local file system with docker compose on Ubuntu 22.04


since now we are using MINIO + mlflow
--------------------------------------
1. Run docker compose up on the yml file (changed ports as in my local machine some ports were taken)
2. Once this is running login to minio and then create an S3 bucket "mlflow-artifacts"
3. Now logon to localhost:5000 to access mlfow
4. Important: In the Jupyter notebook --> make sure you have these credentials before logging model.
# MinIO credentials (same as your Docker Compose)
os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9009"  # Use localhost, not "minio"



Only mlflow-local steps
-------------------------

Important --> In terminal set write permissions for the folders so that external systems can write to it
-----------------------------------------------------------------
mkdir -p mlruns backend (if not already created)
chmod -R 777 mlruns backend


Important --> Two commands to create a docker user group and then adding the $USER to the docker user group. 
----------------------------------------------------------------------------------------------------------
This helps prevent running docker compose commands as sudo
Also it solves problem of mlruns folder access from non sudo python code while logging models
------->>>>
sudo groupadd docker
sudo usermod -aG docker $USER


test --> docker ps --> should work (no need for sudo  )


Run the docker compose file
----------------------------
Goto terminal >

1. be in the folder where the yaml file is
2. sudo docker compose up -d
3. mlruns is where all the ml runs would be found
4. backend - can be used for sqlliteDB later
5. check mlflow server running in localhost:5000
6. The test_mlflow.py can be used from a different project to set the tracking uri to this server and log experiments/models etc



