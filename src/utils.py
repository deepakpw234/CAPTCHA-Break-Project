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