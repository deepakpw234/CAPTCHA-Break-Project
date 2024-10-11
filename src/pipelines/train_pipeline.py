import os
import sys
import pandas as pd
import numpy as np
from PIL import Image

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass


@dataclass
class TrainPipelineConfig:
    target_char_pipeline_path = os.path.join(os.getcwd(),"artifacts","pipeline")
    target_char_directory_path = os.path.join(os.getcwd(),"artifacts","pipeline","char")
    target_char_csv_path = os.path.join(os.getcwd(),"artifacts","pipeline","csv")


    target_char_path = [1,os.path.join(os.getcwd(),"artifacts","pipeline","char","char_1.jpg"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","char","char_2.jpg"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","char","char_3.jpg"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","char","char_4.jpg"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","char","char_5.jpg"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","char","char_6.jpg")
                           ]
    
    target_char_csv = [1,os.path.join(os.getcwd(),"artifacts","pipeline","csv","char_1.csv"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","csv","char_2.csv"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","csv","char_3.csv"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","csv","char_4.csv"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","csv","char_5.csv"),
                           os.path.join(os.getcwd(),"artifacts","pipeline","csv","char_6.csv")
                           ]
    
    raw_file_path = Image.open(r"C:\Users\deepa\Downloads\trail set\screenshot_990.png")

    os.makedirs(target_char_pipeline_path,exist_ok=True)
    os.makedirs(target_char_directory_path,exist_ok=True)
    os.makedirs(target_char_csv_path,exist_ok=True)
    


class TrainPipeline:
    def __init__(self):
        self.train_pipeline_config = TrainPipelineConfig()
        logging.info("Initializing the training pipeline")

    def image_spliting(self):
        try:
            logging.info("Image spliting is started for target image")
            img_file = self.train_pipeline_config.raw_file_path
            img_file = img_file.convert("L")                                                # convert function is used to convert image in grey image

            img_start = [1,25,48,75,100,125,149]                                            # list of starting pixels
            img_stop = [1,48,72,98,123,148,175]                                             # list of stopping pixels

            for i in range(1,7):                                                            # loop for cropping each image and saving it to define location
                img_crop = img_file.crop((img_start[i],0,img_stop[i],80))
                img_crop.save(self.train_pipeline_config.target_char_path[i])

            logging.info("Image spliting is completed for target image")

        except Exception as e:
            raise CustomException(e,sys)


    def image_to_binary(self):
        try:
            logging.info("Conversion from image to binary is started for target image")
            for i in range(1,7):                                                           # loop for each image get convert in binary         
                img = Image.open(self.train_pipeline_config.target_char_path[i])
                img_arr = np.array(img)
                height, width = img_arr.shape
                for p in range(height):                                                    # binary conversion 
                    for q in range(width):
                        if img_arr[p][q] >= 128:
                            img_arr[p][q] = 0
                        else:
                            img_arr[p][q] = 1
                reshape_img_arr = img_arr.reshape(1,height*width)
                reshape_img_arr = pd.DataFrame(reshape_img_arr)
                reshape_img_arr.to_csv(self.train_pipeline_config.target_char_csv[i],header=True,index=True)   # Saving it to in csv

            logging.info("Image converted to binary and save in csv")

            return self.train_pipeline_config.target_char_csv_path    

        except Exception as e:
            raise CustomException(e,sys)
        
        




