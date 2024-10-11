import os
import sys
import dill

from src.exception import CustomException
from src.logger import logging

def save_object(obj_path, obj):
    try:
        
        with open(obj_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

        logging.info(f"Pickle file is created for {obj_path}")

    except Exception as e:
        raise CustomException
    

def load_object(file_path):
    try:
        
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)


        logging.info(f"Pickle file is loaded for {file_path}")

    except Exception as e:
        raise CustomException