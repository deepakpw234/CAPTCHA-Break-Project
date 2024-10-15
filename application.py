from flask import Flask,request,render_template,Response,url_for
import pandas as pd
import numpy as np
from PIL import Image
import os
import sys



from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines.predict_pipeline import PredictPipeline
from src.exception import CustomException
from src.logger import logging

application = Flask(__name__)

app = application

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route("/")
def index():
    logging.info("Request in the get phase of index function")
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def predict_captcha():
    try:
        if request.method == "GET":
            logging.info("Request in the get phase of predict captcha function")
            return render_template("home.html")
        
        else:
            logging.info("Request in the POST phase of predict captcha function and routing started")
            if 'image' not in request.files:
                return render_template("home.html", error="No file part in the request.")

            file = request.files['image']
            logging.info(f"The file value is: {file}")

            if file.filename == '':
                return render_template("home.html", error="No file selected for uploading.")
            
            try:
                logging.info("Uploaded image is openeing")
                data = Image.open(file)
                logging.info(f"the data value is {data}")
            except Exception as e:
                return render_template("home.html", error="Invalid image file.")


            logging.info("opened image go to trainig pipeline")
            train_pipe = TrainPipeline()
            img_crop=train_pipe.image_spliting(data)
            df_char = train_pipe.image_to_binary(img_crop)


            predict_pipe = PredictPipeline()
            captcha = predict_pipe.get_prediction(df_char)

            logging.info(f"captcha is predicted and it is {captcha} , and type of it {type(captcha)}")

            return render_template("home.html",captcha=captcha)
        
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
