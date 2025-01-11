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