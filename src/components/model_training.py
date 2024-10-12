import os
import sys
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

from dataclasses import dataclass

@dataclass
class ModelTrainerConfig:
    model_path_char_ = [1,os.path.join(os.getcwd(),'artifacts',"model","model_char_1.pkl"),
                        os.path.join(os.getcwd(),'artifacts',"model","model_char_2.pkl"),
                        os.path.join(os.getcwd(),'artifacts',"model","model_char_3.pkl"),
                        os.path.join(os.getcwd(),'artifacts',"model","model_char_4.pkl"),
                        os.path.join(os.getcwd(),'artifacts',"model","model_char_5.pkl"),
                        os.path.join(os.getcwd(),'artifacts',"model","model_char_6.pkl")
                        ]

    model_directory_path = os.path.join(os.getcwd(),'artifacts',"model")
    os.makedirs(model_directory_path,exist_ok=True)


class ModelTrainer:
    def __init__(self):
        self.model_tranier_config = ModelTrainerConfig()

    def train_test_split_and_model_trainer(self,trasform_data_path):
        try:
            df_char_ = {}  # Assigning for using multiple varible
            X_char_ = {}
            y_char_ = {}

            X_train_char_ = {}
            X_test_char_= {}

            y_train_char_ = {}
            y_test_char_ = {}

            y_pred_char_ = {}

            logging.info("Train Test and Model Training started")
            percentage = 0.1                                                           # Test size for the 1st character
            for i in range(1,7):
                df_char_[i] = pd.read_csv(rf"{trasform_data_path}\char_{i}.csv")       # Creating the DataFrame for each charater from CSV
                height, width = df_char_[i].shape
                X_char_[i] = df_char_[i].drop(str(width-1),axis=1)                     # dropping the target column
                y_char_[i] = df_char_[i][str(width-1)]                                 # Selecting the target column

                # print(df_char_[i])
                # print(X_char_[i])
                # print(y_char_[i])

                # Train Test Split 
                X_train_char_[i], X_test_char_[i], y_train_char_[i], y_test_char_[i] = train_test_split(X_char_[i],y_char_[i], test_size=percentage,random_state=42)

                percentage = 0.2                                                       # This is giving 0.2 as we want test size to be 0.2 from 2nd character 

                rf = RandomForestRegressor()                                           # Selecting the Random Regressor Model
                rf.fit(X_train_char_[i].values,y_train_char_[i].values)                              # Fitting in the Model

                y_pred_char_[i] = rf.predict(X_test_char_[i].values)                          # Prediction from the Model

                score = r2_score(y_test_char_[i],y_pred_char_[i])

                print("\n")
                print("=============================================")
                print(f"Prediction and Error value for character: {i}")
                print(f"Mean absolute error is: {mean_absolute_error(y_test_char_[i],y_pred_char_[i])}")
                print(f"Mean square error is: {mean_squared_error(y_test_char_[i],y_pred_char_[i])}")
                print(f"Root Mean square error is: {np.sqrt(mean_squared_error(y_test_char_[i],y_pred_char_[i]))}")
                print("\n")
                print(f"The R2_Score is: {score}")
                print("=============================================")

                '''
                =============================================
                Prediction and Error value for character: 1
                Mean absolute error is: 0.17055555555555552
                Mean square error is: 0.05403888888888899
                Root Mean square error is: 0.23246266127894388


                The R2_Score is: 0.9995072441742654
                =============================================
                '''

                save_object(self.model_tranier_config.model_path_char_[i], rf)       # Saving the Model
                
            logging.info("Train Test Split and Model Training Completed")

        except Exception as e:
            raise CustomException(e,sys)




    