from flask import Flask,request,render_template,Response
import pandas as pd
import numpy as np
from PIL import Image

from src.pipelines.train_pipeline import TrainPipeline
from src.pipelines.predict_pipeline import PredictPipeline
from src.exception import CustomException

application = Flask(__name__)

app = application

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home",methods=["GET","POST"])
def predict_captcha():
    try:
        if request.method == "GET":
            return render_template("home.html")
        
        else:
            data = request.files['image']

            data = Image.open(data)


            train_pipe = TrainPipeline()
            img_crop=train_pipe.image_spliting(data)
            df_char = train_pipe.image_to_binary(img_crop)


            predict_pipe = PredictPipeline()
            captcha = predict_pipe.get_prediction(df_char)

            return render_template("home.html",captcha=captcha)
        
    except Exception as e:
        raise CustomException

if __name__ == "__main__":
    app.run(host="0.0.0.0")