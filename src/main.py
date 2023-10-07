# Importing libraries
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd 
import pickle
import os

# scaler and label_encoder import
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder


## Function to Load machine Learning Components to re-use
def Ml_components(fp):
    with open(fp, 'rb') as f:
        object = pickle.load(f)
        return(object)

# Loading the Machine Learning Components
DIRPATH = os.path.dirname(os.path.realpath(__file__))
ml_core_fp = os.path.join(DIRPATH, 'src','ML_Model.pkl') 
ml_components_dict = Ml_components(fp=ml_core_fp)

## The Label Encoder Part
# (type alias) label_encoder: Any

label_encoder = ml_components_dict['label_encoder']

# scaler loading
scaler = ml_components_dict['scaler']

# Model loading

model = ml_components_dict['model']

# FastAPI Instance Creating
app = FastAPI(title = ' Sepsis Prediction API', description = 'API for Sepsis Prediction')

     # Defining Input Variable
""""""
'PG: Plasma glucose'

'PL: Blood Work Result-1 (mu U/ml)'

'PBL: Blood Pressure (mm Hg)'

'SK: Blood Work Result-2 (mm)'

'TS: Blood Work Result-3 (mu U/ml)'

'BMI: Body mass index (weight in kg/(height in m)^2'
                      
'BD2: Blood Work Result-4 (mu U/ml)'

'Age: patients age (years)'

'Insurance: If a patient holds a valid insurance card'

""    

# Endpoint creation for the Prediction

@app.get('/predict')

def predict (PRG: float,PL: float,BP: float,SK: float,TS:float,BMI: float,BD2: float,Age: float,Insurance: float):  
    
# Prepare the feature and put them in a notebook
     df = pd.DataFrame({
        'PG':[PG],
        'PL':[PL],
        'PBL':[PBL],
        'SK':[SK],
        'TS':[TS],
        'BMI':[BMI],
        'BD2':[BD2],
        'Age':[Age],
        'Insurance':[Insurance]
    })
      
     # scaling the Input
     df_scaled = scaler.transform(df)
     
     # Prediction
     raw_prediction = model.predict(df_scaled)
     if raw_prediction == 0:
    
        return {f'The patient will not develop Sepsis'}

     elif raw_prediction == 1:

        return {f'The Patient will develop Sepsis'}

     else:
        return {'Error'}


if __name__ == '__main__':
    uvicorn.run('main:app',reload = True)