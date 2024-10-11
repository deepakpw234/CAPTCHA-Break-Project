from flask import Flask,request,render_template,Response,url_for,redirect
import pandas as pd
import numpy as np
from PIL import Image

from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines import train_pipeline
from src.pipelines.predict_pipeline import PredictPipeline

application = Flask(__name__)

app = application

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def predict_captcha():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = request.files['image']

        data = Image.open(data)

        training_pipe = TrainPipeline()
        training_pipe.image_spliting(data)

        path_for_predict_pipeline = training_pipe.image_to_binary()

        predict_pipeline = PredictPipeline()
        captcha = predict_pipeline.get_prediction(path_for_predict_pipeline)

    
        return render_template("home.html",captcha=captcha)

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080)