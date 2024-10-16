from flask import Flask,request,render_template,Response,url_for
import pandas as pd
import numpy as np
from PIL import Image
import os
import sys
from werkzeug.utils import secure_filename



from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines.predict_pipeline import PredictPipeline
from src.exception import CustomException
from src.logger import logging

application = Flask(__name__)

app = application

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    


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
            
            
            logging.info("Uploaded image is openeing")

            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save the uploaded file to the server
            file.save(filepath)


            logging.info(f"the data value is {filepath}")
            

            logging.info("opened image go to trainig pipeline")
            train_pipe = TrainPipeline()
            img_crop=train_pipe.image_spliting(filepath)
            df_char = train_pipe.image_to_binary(img_crop)


            predict_pipe = PredictPipeline()
            captcha = predict_pipe.get_prediction(df_char)

            logging.info(f"captcha is predicted and it is {captcha} , and type of it {type(captcha)}")

            # Remove the uploaded file after processing to save space
            os.remove(filepath)

            return render_template("home.html",captcha=captcha)
        
    except Exception as e:
        raise CustomException(e,sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)
