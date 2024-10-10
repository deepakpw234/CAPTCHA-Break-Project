from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

from src.logger import logging



if __name__=="__main__":
    logging.info("Main File - Data Ingestion Started")
    data_ingestion = DataIngestion()
    path_for_data_transformation = data_ingestion.initiate_data_ingestion()
    logging.info("Main File - Data Ingestion Ended")

    
    logging.info("Main File - Data Transforamtion Started")
    data_transformation = DataTransformation()
    path_for_model_trainer = data_transformation.image_to_binary_conversion(path_for_data_transformation)
    logging.info("Main File - Data Transforamtion Ended")
