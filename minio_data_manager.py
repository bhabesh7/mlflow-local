from minio import Minio
from minio.error import S3Error
import os



MINIO_ROOT_USER="minioadmin"
MINIO_ROOT_PASSWORD="minioadmin"
AWS_ACCESS_KEY_ID="minioadmin"
AWS_SECRET_ACCESS_KEY="minioadmin"
MLFLOW_S3_ENDPOINT_URL="http://minio:9009"


def upload_file_to_minio(
    file_path: str,
    bucket_name: str,
    object_name: str = None,
    minio_endpoint: str = "localhost:9009",
    access_key: str = "minioadmin",
    secret_key: str = "minioadmin",
    secure: bool = False
):
    """
    Uploads a file to a MinIO bucket.

    :param file_path: Path to the local file to upload.
    :param bucket_name: Name of the bucket to upload to.
    :param object_name: Name of the object in MinIO (defaults to file name).
    :param minio_endpoint: MinIO server endpoint.
    :param access_key: MinIO access key.
    :param secret_key: MinIO secret key.
    :param secure: Use HTTPS if True, HTTP if False.
    """
    client = Minio(
        minio_endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure
    )

    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)

    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        client.fput_object(bucket_name, object_name, file_path)
        print(f"File '{file_path}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
    except S3Error as err:
        print(f"Failed to upload file: {err}")

def download_file_from_minio(
    bucket_name: str,
    object_name: str,
    file_path: str,
    minio_endpoint: str = "localhost:9000",
    access_key: str = "minioadmin",
    secret_key: str = "minioadmin",
    secure: bool = False
):
    """
    Downloads a file (artifact) from a MinIO bucket.

    :param bucket_name: Name of the bucket to download from.
    :param object_name: Name of the object in MinIO.
    :param file_path: Local path to save the downloaded file.
    :param minio_endpoint: MinIO server endpoint.
    :param access_key: MinIO access key.
    :param secret_key: MinIO secret key.
    :param secure: Use HTTPS if True, HTTP if False.
    """
    client = Minio(
        minio_endpoint,
        access_key=access_key,
        secret_key=secret_key,
        secure=secure
    )

    try:
        client.fget_object(bucket_name, object_name, file_path)
        print(f"File '{object_name}' from bucket '{bucket_name}' downloaded to '{file_path}'.")
    except S3Error as err:
        print(f"Failed to download file: {err}")

# Example usage:
# upload_file_to_minio("test.txt", "data")
if __name__ == "__main__":
    # Download 'data/train/train_FD001.txt' from MinIO to local file 'downloaded_train_FD001.txt'
    download_file_from_minio(
        bucket_name="data",
        object_name="train/train_FD001.txt",
        file_path="downloaded_train_FD001.txt",
        minio_endpoint="localhost:9009",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )
    
    print("File downloaded successfully.")