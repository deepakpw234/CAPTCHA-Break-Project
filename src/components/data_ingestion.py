import urllib.request
import pandas as pd
import numpy as np
import os
import sys
import urllib
import zipfile

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    dataset = os.path.join(os.getcwd(),"artifacts")
    os.makedirs(dataset,exist_ok=True)

    data_zip_file_name = os.path.join(os.getcwd(),"artifacts","dataset.zip")



class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Data Ingestion Started")

            github_url = "https://github.com/deepakpw234/Project-Datasets/raw/refs/heads/main/Captcha%20Dataset.zip"

            urllib.request.urlretrieve(github_url,self.data_ingestion_config.data_zip_file_name)

            logging.info("Dataset is downloaded from git in zip format")
            logging.info("Unzipping of Dataset is started")

            with zipfile.ZipFile("artifacts\dataset.zip","r") as zip_ref:
                zip_ref.extractall("artifacts")
            
            logging.info("Dataset is unzipped")

            logging.info("Data Ingestion is completed")

        except Exception as e:
            raise CustomException(e,sys)
        
        return os.path.join(os.getcwd(),"artifacts","Captcha Dataset")




        

