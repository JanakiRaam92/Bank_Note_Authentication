from types import MethodDescriptorType
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome all"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    predection=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The prediction value is "+str(predection)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    predection=classifier.predict(df_test)
    return "The prediction value is "+str(list(predection))

if __name__=='__main__':
    app.run()