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
    pass
    # raw_file_path = Image.open(r"C:\Users\deepa\Downloads\trail set\screenshot_990.png")
    

class TrainPipeline:
    def __init__(self):
        self.train_pipeline_config = TrainPipelineConfig()
        logging.info("Initializing the training pipeline")

    def image_spliting(self,filepath):
        try:
            
            logging.info("Image spliting is started for target image")
            img_file = Image.open(filepath)
            
        
            img_file = img_file.convert("L")                                                # convert function is used to convert image in grey image

            # For cropping the image
            img_start = [1,25,48,75,100,125,149]                                            # list of starting pixels
            img_stop = [1,48,72,98,123,148,175]                                             # list of stopping pixels
            # img_crop = [1,2,3,4,5,6,7]
            img_crop = {}

            for i in range(1,7):                                                            # loop for cropping each image and saving it to define location
                img_crop[i] = img_file.crop((img_start[i],0,img_stop[i],80))
                

            logging.info("Image spliting is completed for target image")

            
        except Exception as e:
            raise CustomException(e,sys)
        
        return (img_crop)


    def image_to_binary(self,img_crop):
        try:
            logging.info("Conversion from image to binary is started for target image")
            reshape_img_arr = {}
            reshape_img_arr_ini = {}
            crop_list = img_crop

            for i in range(1,7):                                                           # loop for each image get convert in binary         
                img = crop_list[i]
                img_arr = np.array(img)
                height, width = img_arr.shape
                for p in range(height):                                                    # binary conversion 
                    for q in range(width):
                        if img_arr[p][q] >= 128:
                            img_arr[p][q] = 0
                        else:
                            img_arr[p][q] = 1

                reshape_img_arr_ini[i] = img_arr.reshape(1,height*width)
                reshape_img_arr[i] = pd.DataFrame(reshape_img_arr_ini[i])
                
                
            logging.info("Image converted to binary")
              

        except Exception as e:
            raise CustomException(e,sys)
        
        return (reshape_img_arr) 
        




