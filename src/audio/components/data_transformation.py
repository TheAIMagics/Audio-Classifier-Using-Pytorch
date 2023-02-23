import os
import sys
import torch
import torchaudio
from pathlib import Path
import matplotlib.pyplot as plt
from src.audio.constants import *
from src.audio.logger import logging
from src.audio.exception import CustomException
from src.audio.entity.config_entity import *
from src.audio.entity.artifact_entity import *

class DataTransformation:
    def __init__(self, data_transformation_config: DataTransformationConfig,
     data_ingestion_artifact: DataIngestionArtifacts)-> None:
        try:
            self.data_transformation_config = data_transformation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise CustomException(e, sys)

    def load_audio_files(self,path: str, label:str):
        dataset = []
        walker = sorted(str(p) for p in Path(path).glob(f'*.wav'))
        for i, file_path in enumerate(walker):
            path, filename = os.path.split(file_path)
            speaker, _ = os.path.splitext(filename)
            speaker_id, utterance_number = speaker.split("_nohash_")
            utterance_number = int(utterance_number)
            # Load audio
            waveform, sample_rate = torchaudio.load(file_path)
            dataset.append([waveform, sample_rate, label, speaker_id, utterance_number])
        return dataset

    def create_spectrogram_images(self,trainloader, label_dir):
        try:
            directory = os.path.join(self.data_transformation_config.images_dir,label_dir)
            
            if(os.path.isdir(directory)):
                print("Data exists for", label_dir)
            else:
                os.makedirs(directory, mode=0o777, exist_ok=True)
                
                for i, data in enumerate(trainloader):

                    waveform = data[0]
                    sample_rate = data[1][0]
                    label = data[2]
                    ID = data[3]

                    # create transformed waveforms
                    spectrogram_tensor = torchaudio.transforms.Spectrogram()(waveform)     
                    path_to_save_img = os.path.join(directory,f"spec_img{i}.png")
                    plt.imsave(path_to_save_img, spectrogram_tensor[0].log2()[0,:,:].numpy(), cmap='viridis')
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self) ->DataTransformationArtifacts:
        try:
            logging.info("Initiating the data transformation component...")
            dog_file_path = os.path.join(self.data_ingestion_artifact.data_folder_path,'data','dog','00f0204f_nohash_0.wav')
            cat_file_path = os.path.join(self.data_ingestion_artifact.data_folder_path,'data','cat','00b01445_nohash_0.wav')

            train_dog = self.load_audio_files(dog_file_path[:-22],'dog')
            train_cat = self.load_audio_files(cat_file_path[:-22],'cat')
            logging.info(f'Length of dog dataset: {len(train_dog)}')
            logging.info(f'Length of cat dataset: {len(train_cat)}')
            trainloader_dog = torch.utils.data.DataLoader(train_dog, batch_size=1,
                                            shuffle=True, num_workers=0)
            trainloader_cat= torch.utils.data.DataLoader(train_cat, batch_size=1,
                                            shuffle=True, num_workers=0)
            self.create_spectrogram_images(trainloader_dog, 'dog')
            self.create_spectrogram_images(trainloader_cat, 'cat')

            data_transformation_artifact = DataTransformationArtifacts(
                images_folder_path = self.data_transformation_config.images_dir,
                test_folder_path=self.data_transformation_config.test_dir
            )
            logging.info('Data transformation is completed Successfully.')
            return data_transformation_artifact
        except Exception as e:
            raise CustomException(e, sys)