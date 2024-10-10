import pandas as pd
import numpy as np
import os
import sys
from PIL import Image

from src.exception import CustomException
from src.logger import logging

from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    tranform_data = os.path.join(os.getcwd(),"artifacts","transform_data")
    os.makedirs(tranform_data,exist_ok=True)


class DataTransformation:
    def __init__(self):
        self.data_transform_config = DataTransformationConfig()

    def image_to_binary_conversion(self, dataset_path):
        try:
            logging.info("Image to binary strated")
            var = 1
            for directory in os.listdir(dataset_path):
                m = "w"
                ind = True
                h = True
                for folder in os.listdir(os.path.join(dataset_path,directory)):
                    for file in os.listdir(os.path.join(dataset_path,directory,folder)):
                        path = os.path.join(dataset_path,directory,folder,file)
                        img = Image.open(path)
                        img_arr = np.array(img)
                        height, width = img_arr.shape
                        for i in range(height):
                            for j in range(width):
                                if img_arr[i][j] >= 128:
                                    img_arr[i][j] = 0
                                else:
                                    img_arr[i][j] = 1
                        reshape_img_arr = img_arr.reshape(1,height*width)
                        reshape_img_arr = pd.DataFrame(reshape_img_arr)
                        if folder in ["0","1","2","3","4","5","6","7","8","9"]:
                            reshape_img_arr[height*width] = ord(folder)-48
                            reshape_img_arr.to_csv(rf"{self.data_transform_config.tranform_data}\char_{var}.csv", mode=m, index=ind, header= h)
                        if folder in ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]:
                            reshape_img_arr[height*width] = ord(folder)-55
                            reshape_img_arr.to_csv(rf"{self.data_transform_config.tranform_data}\char_{var}.csv", mode=m, index=ind, header= h)
                        m = "a"
                        ind = True
                        h = False
                print(f"Stage-{var} Image to binary conversion completed")
                logging.info(f"Stage-{var} Image to binary conversion completed")
                var = var + 1
            
            logging.info("All Image to binary conversion completed")

        except Exception as e:
            raise CustomException(e,sys)
        

        return self.data_transform_config.tranform_data


