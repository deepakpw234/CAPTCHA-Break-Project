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



    def get_prediction(self,target_csv_path):
        try:
            logging.info("Prediction for target image is started")
            model_load = [1,2,3,4,5,6,7]                                            # Assigning model_load with sudo list so we can use model_load[i] as multiple variable
            output_pred = [1,2,3,4,5,6,7]
            final_output = ""
            for i in range(1,7):
                target_csv_file = f"{target_csv_path}\char_{i}.csv"                 # Path for target csv file
                model_path = f"{self.predict_pipeline_config.model_directory_path}\model_char_{i}.pkl"    # Path for model
                target_csv_file_df = pd.read_csv(target_csv_file)

                model_load[i] = load_object(model_path)                             # Loading the model

                output_pred[i] = model_load[i].predict(target_csv_file_df)          # Prediction from model

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
        

if __name__=="__main__":
    train_pipeline = TrainPipeline()
    train_pipeline.image_spliting()
    path_for_predict_pipeline = train_pipeline.image_to_binary()

    predict_pipeline = PredictPipeline()
    predict_pipeline.get_prediction(path_for_predict_pipeline)

