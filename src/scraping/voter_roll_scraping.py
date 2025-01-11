from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
import base64
import re
import selenium
from urllib.parse import urlparse
import numpy as np
import pandas as pd

from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import cv2
import time
import geckodriver_autoinstaller
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
chromedriver_autoinstaller.install()
from pathlib import Path
from PIL import Image
from io import BytesIO
from selenium.webdriver.support.ui import WebDriverWait

from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines.predict_pipeline import PredictPipeline
from src.exception import CustomException
from src.logger import logging


@dataclass
class WebScrapingConfig:
    captcha_folder_path = os.path.join(os.getcwd(),"artifacts","ECI")
    os.makedirs(captcha_folder_path,exist_ok=True)
    captcha_file_path = os.path.join(os.getcwd(),"artifacts","ECI","captcha.png")


class ECIVoterRollScraping:
    def __init__(self):
        self.web_scaping_config = WebScrapingConfig()



    def get_eci_captcha(self, data_url, save_directory, default_filename):
        '''
        Saves a Data URL as an image file.

        Parameters:
            data_url (str): The Data URL to decode and save.
            save_directory (str): Directory where the image will be saved.
            default_filename (str): Base name for the saved image file.

        Returns:
            str: Path to the saved image file.
        '''
        # Regular expression to parse Data URLs
        data_url_pattern = re.compile(r'data:(?P<mediatype>[\w/+-]+(?:\.[\w/+.-]+)*);base64,(?P<data>.+)')

        match = data_url_pattern.match(data_url)
        if not match:
            raise ValueError("Invalid Data URL format.")

        mediatype = match.group('mediatype')
        data = match.group('data')

        # Determine file extension from MIME type
        mime_to_extension = {
            'image/jpg': '.jpg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/bmp': '.bmp',
            'image/svg+xml': '.svg',
            'image/webp': '.webp',
            # Add more MIME types and extensions as needed
        }

        file_extension = mime_to_extension.get(mediatype, '')  # Default to no extension if unknown
        if not file_extension:
            print(f"Warning: Unrecognized MIME type '{mediatype}'. Saving without extension.")

        # Decode the base64 data
        try:
            image_data = base64.b64decode(data)
        except base64.binascii.Error as e:
            raise ValueError("Error decoding base64 data.") from e

        # Ensure the save directory exists
        os.makedirs(save_directory, exist_ok=True)

        # Create a unique filename
        filename = f"{default_filename}{file_extension}"
        save_path = os.path.join(save_directory, filename)

        # Handle filename conflicts by appending a number
        counter = 1
        while os.path.exists(save_path):
            filename = f"{default_filename}_{counter}{file_extension}"
            save_path = os.path.join(save_directory, filename)
            counter += 1

        # Write the binary data to the file
        with open(save_path, 'wb') as f:
            f.write(image_data)

        print(f"Image successfully saved to {save_path}")
        return save_path
    



if __name__ == "__main__":

    captcha_folder_path = os.path.join(os.getcwd(),"artifacts","ECI")
    os.makedirs(captcha_folder_path,exist_ok=True)
    captcha_file_path = os.path.join(os.getcwd(),"artifacts","ECI","captcha")
    captcha_file_path_for_model = os.path.join(os.getcwd(),"artifacts","ECI","captcha.jpg")

    chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')  # Run Chrome in headless mode
#     chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
#     chrome_options.add_argument('--no-sandbox')  # Bypass OS security model
#     chrome_options.add_argument('--log-level=3')  # Suppress logging


    driver = webdriver.Chrome(options=chrome_options)


    # Open the target webpage
    url = 'https://voters.eci.gov.in/download-eroll'  
    driver.get(url)
    
    for i in range(1):
    # Locate the image element (update the selector as per the website structure)
        driver.implicitly_wait(1)
        sample_url = driver.find_element(By.XPATH, '//*[@id="textContent"]/div[2]/div[2]/div[5]/div/div/div[2]/img[1]')

        # Get the image source URL
        image_url = sample_url.get_attribute('src')
        
        # Example Data URL (a small red dot PNG)
        data_url = image_url

        web_scraping = ECIVoterRollScraping()
        web_scraping.get_eci_captcha(
            data_url,
            save_directory=captcha_folder_path,
            default_filename=captcha_file_path
        )


        train_pipe = TrainPipeline()
        img_crop=train_pipe.image_spliting(captcha_file_path_for_model)
        df_char = train_pipe.image_to_binary(img_crop)


        predict_pipe = PredictPipeline()
        captcha = predict_pipe.get_prediction(df_char)

        print(captcha)
        print(type(captcha))
        os.remove(captcha_file_path_for_model)


