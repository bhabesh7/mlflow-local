# import mlflow

# mlflow.set_tracking_uri("http://localhost:5000")

# with mlflow.start_run():
#     mlflow.log_param("learning_rate", 0.01)
#     mlflow.log_metric("accuracy", 0.95)
#     mlflow.log_metric("loss", 0.05)
#     mlflow.log_artifact("example_model.pkl")
#     mlflow.log_artifact("example_data.csv")