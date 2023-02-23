import os
import torch
from datetime import datetime

ARTIFACTS_DIR: str = "artifacts"

S3_BUCKET_DATA_URI = "s3://speech-classifier/data/"

# constants related to data ingestion
DATA_INGESTION_ARTIFACTS_DIR: str = "data_ingestion"
S3_DATA_FOLDER_NAME: str = "data.zip"
UNZIPPED_FOLDER_NAME: str = "unzip"
DATA_DIR_NAME: str = "data"

