


![captcha project v1](https://github.com/user-attachments/assets/dd7a2700-b69a-4e27-8a0f-ae0c33f53756)
# 1. CAPTCHA Break Model

This project focuses on developing a CAPTCHA-breaking model that converts CAPTCHA images into text. We utilised a Random Forest regressor to accurately perform conversion, achieving an impressive accuracy of 99.99%. As part of a broader initiative, this model aims to automate CAPTCHA recognition using machine learning techniques, allowing for the breaking of CAPTCHAs across multiple websites and facilitating the automation of web scraping processes.


## 2.  Table of content

1. CAPTCHA scraping and Dataset
2. Data ingestion
3. Data transformation
4. Model training
5. Training and prediction pipeline

#### 2.1: CAPTCHA scraping and Dataset
- In this project, the dataset is created from the CAPTCHA images themselves. First, a large number of CAPTCHA images were scraped from the Election Commission of India website, and then the team organized and labeled them into folders to make the dataset suitable for training and prediction. This process ensures a custom-built dataset, enhancing the model’s accuracy and performance in CAPTCHA recognition and prediction.
- Sample CAPTCHA image
  
  ![screenshot_996](https://github.com/user-attachments/assets/7123ee34-7360-43b4-9484-421e75c3600f)
- You can check out the CAPTCHA scraping code by [clicking here](https://github.com/deepakpw234/CAPTCHA-Break-Project/blob/main/notebook/CAPTCHA%20Break%20-%20Web%20Scrapping.ipynb)
- You can download the dataset by [clicking here](https://github.com/deepakpw234/Project-Datasets/blob/main/Captcha%20Dataset.zip)

#### 2.2: Data ingestion
- In this section of the project, the dataset is first downloaded from the GitHub repository and then unzipped to prepare it for further data transformation and analysis. This step ensures that the raw data is readily accessible and in the appropriate format before undergoing any preprocessing or transformation procedures.
- You can check out the data ingestion code by [clicking here](https://github.com/deepakpw234/CAPTCHA-Break-Project/blob/main/src/components/data_ingestion.py)

#### 2.2: Data transformation
- In this section of the project, the ingested data undergoes a transformation process, where it is converted into a binary format to ensure it is suitable for the model to effectively fit and make accurate predictions. This transformation is crucial for optimizing the model's performance and ensuring that the input data aligns with the expected binary format to fit in the model.
- You can check out the data transformation code by [clicking here](https://github.com/deepakpw234/CAPTCHA-Break-Project/blob/main/src/components/data_transformation.py)

#### 2.2: Model training
- First, the transformed data is divided into training and testing sets to ensure proper evaluation. After this, a model is trained on each of the six characters present in the CAPTCHA image individually. For the training process, Random Forest Regression is employed to predict the characters, with the goal of achieving the highest possible accuracy.\
 =============================================\
Accuracy and Error value for character: 1
1. Mean absolute error is: 0.17055555555555552
2. Mean square error is: 0.05403888888888899
3. Root Mean square error is: 0.23246266127894388

   The R2_Score is: 0.9999072441742654\
 =============================================
- You can check out the model training code by [clicking here](https://github.com/deepakpw234/CAPTCHA-Break-Project/blob/main/src/components/model_training.py)

#### 2.2: Training and prediction pipeline
- The training and prediction pipeline is designed to handle any new CAPTCHA. In this process, the new image is first split into six individual characters. Each character is then converted into its binary representation. Saved trained model are loaded and use to predict the CAPTCHA text by using these binary inputs for each character, providing an accurate prediction of the original CAPTCHA text.
- Sample captcha prediction
![Screenshot (55)](https://github.com/user-attachments/assets/3c3e9fff-b24b-4866-a55a-2dc1b7182484)

## Project structure

- ![Screenshot 2024-10-16 071035](https://github.com/user-attachments/assets/c6bf5b0b-feb3-4a8b-8052-dfc12644fe87)

## Installation

#### Prerequisites

- dill==0.3.9
- Flask==3.0.3
- ImageHash==4.3.1
- numpy==2.1.2
- pandas==2.2.3
- pillow==10.4.0
- scikit-learn==1.5.2
- selenium==4.25.0
- urllib3==2.2.3
- Werkzeug==3.0.4

#### Steps
Step 1: Clone the repository
```bash
git clone https://github.com/deepakpw234/CAPTCHA-Break-Project.git
```
Step 2: Change into the project directory
```bash
cd CAPTCHA-Break-Project
```
Step 3: Create and activate a virtual environment
```bash
conda create -n captcha_env python==3.11 -y
conda activate captcha_env
```
Step 4: Install dependencies
```bash
pip install -r requirements.txt
```
Step 5: Run the project
```bash
python main.py
```
Step 6: Run the flask application
```bash
python application.py
```



# Hi, I'm Deepak Pawar! 👋


## 🚀 About Me
I'm a Data Scientist with over 2 years of experience in leveraging data analytics, statistical modelling, and
machine learning to drive actionable insights and business growth. Proficient in leveraging Python, SQL, Scikit-Learn and
Machine Learning techniques to solve complex data problems and enhance predictive analytics. Strong background in
data preprocessing, feature engineering, and model evaluation, with a proven track record of optimizing model
performance and scalability. Also, Expertise in developing and deploying end-to-end data science solutions within CI/CD
pipelines, ensuring seamless integration and continuous delivery of models and applications.

## 🛠 Skills
- Languages – Python, C Programming
- Libraries – Pandas, NumPy, Scikit-Learn, TensorFlow, Py Torch, Transformers, Hugging face Library
- Visualization Tools – Matplotlib, Seaborn, Power BI
- Databases – SQL, MongoDB
- Clouds – Amazon Web Service (AWS), Microsoft Azure
- Misc – GitHub Action, Docker, Flask, Jupyter Notebook, Office 365


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/deepakpw234)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/deepak-pawar-92a2a5b5/)


## Authors

- [@deepakpw234](https://www.github.com/deepakpw234)


