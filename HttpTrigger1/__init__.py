import logging
import pickle
import json
import joblib
import numpy as np
import pandas as pd
import sklearn


import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    with open('pickle_demo.pkl','rb') as picky:
        model=pickle.load(picky)
        
    spx = float(req.params.get('SPX'))
    uso = float(req.params.get('USO'))
    slv = float(req.params.get('SLV'))
    eur = float(req.params.get('EURUSD'))
    
    X_new = [[spx,uso,slv,eur]]
   
    
    pred = model.predict(X_new)


    
    return func.HttpResponse(f"The predicted gold price is {pred} dollars")
    
