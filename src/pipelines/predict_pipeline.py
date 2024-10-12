import os
import sys
import pandas as pd
import numpy as np

from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

from dataclasses import dataclass

from src.pipelines.train_pipeline import TrainPipeline


@dataclass
class PredictPipelineConfig:
    final_output_path = os.path.join(os.getcwd(),"artifacts")
    model_directory_path = os.path.join(os.getcwd(),"artifacts","model")



class PredictPipeline:
    def __init__(self):
        self.predict_pipeline_config = PredictPipelineConfig()
        logging.info("Initializing the predict pipeline")



    def get_prediction(self,df_char):
        try:
            logging.info("Prediction for target image is started")
            model_load = {}                                           # Assigning model_load with sudo list so we can use model_load[i] as multiple variable
            output_pred = {}
            final_output = ""
            all_df = df_char
            for i in range(1,7):
                model_path = f"{self.predict_pipeline_config.model_directory_path}\model_char_{i}.pkl"    # Path for model
                target_csv_file_df = all_df[i]


                model_load[i] = load_object(model_path)                             # Loading the model

                output_pred[i] = model_load[i].predict(target_csv_file_df.values)          # Prediction from model

                character = int(round(output_pred[i][0]))


                if character in [0,1,2,3,4,5,6,7,8,9]:                              # Decoding integer outputs in string  
                    final_output = final_output + str(character)
                else:
                    convet_to_char = chr(character+87)
                    final_output = final_output + convet_to_char

            print(final_output)

            logging.info("Prediction completed")

            
        except Exception as e:
            raise CustomException(e,sys)
        
        return final_output
        



