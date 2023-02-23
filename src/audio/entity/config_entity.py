import os, sys
from dataclasses import dataclass
from from_root import from_root
from src.audio.constants import *

@dataclass
class DataIngestionConfig:
    data_ingestion_artifact_dir: str = os.path.join(from_root(), ARTIFACTS_DIR,DATA_INGESTION_ARTIFACTS_DIR)
    download_dir = os.path.join(data_ingestion_artifact_dir, DATA_DIR_NAME)
    zip_data_path : str = os.path.join(download_dir, S3_DATA_FOLDER_NAME)
    unzip_data_dir: str = os.path.join(data_ingestion_artifact_dir, UNZIPPED_FOLDER_NAME)

@dataclass
class DataTransformationConfig:
    data_transformation_artifact_dir: str = os.path.join(from_root(), ARTIFACTS_DIR,DATA_TRANSFORMATION_ARTIFACTS_DIR)
    images_dir = os.path.join(data_transformation_artifact_dir,IMAGES_DIR)
    test_dir = os.path.join(data_transformation_artifact_dir,TEST_DIR)

@dataclass
class ModelTrainerConfig:
    model_trainer_artifact_dir: str = os.path.join(from_root(), ARTIFACTS_DIR,MODEL_TRAINER_ARTIFACTS_DIR)
    model_path: str = os.path.join(model_trainer_artifact_dir,MODEL_NAME )
    transformer_object_path: str = os.path.join(model_trainer_artifact_dir, TRANSFORM_OBJECT_NAME)
