from dataclasses import dataclass

# Data ingestion artifacts
@dataclass
class DataIngestionArtifacts:
    data_folder_path: str

# Data transformation artifacts
@dataclass
class DataTransformationArtifacts:
    images_folder_path: str
    test_folder_path:str

# Model trainer artifacts
@dataclass
class ModelTrainerArtifacts:
    model_path: str
    result: dict
    transformer_object_path: str