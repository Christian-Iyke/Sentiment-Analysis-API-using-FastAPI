# Importing libraries
from typing import Union
from fastapi import FastAPI
import uvicorn
import pandas as pd 
import pickle
import os

# scaler and label_encoder import
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# load ml components

cwd = os.getcwd()
relative_path = "src\\ML_Model.pkl"


absolute_path = os.path.join(cwd, relative_path)
print(absolute_path)

#ML components Reading

with open(absolute_path, "rb") as f:
    ml_components = pickle.load(f)



## Function to Load machine Learning Components to re-use
#def Ml_components(fp):
    #with open(fp, 'rb') as f:
        #object = pickle.load(f)
        #return(object)

# Loading the Machine Learning Components
#DIRPATH = os.path.dirname(os.path.realpath(__file__))
#ml_core_fp = os.path.join(DIRPATH, 'src','ML_Model.pkl') 
#ml_components_dict = Ml_components(fp=ml_core_fp)

## The Label Encoder Part

label_encoder = ml_components['label_encoder']

# scaler loading
scaler = ml_components['scaler']

# Model loading

model = ml_components['model']

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

# Endpoint for checking if the API is online

@app.get('/status')
async def status():
    return{'message':'Online'}



# Endpoint creation for the Prediction

@app.get('/predict')

async def predict (PG: float,PL: float,BPL: float,SK: float,TS:float,BMI: float,BD2: float,Age: float,Insurance: float):  
    
# Prepare the feature and put them in a notebook
     df = pd.DataFrame({
        'PG':[PG],
        'PL':[PL],
        'BPL':[BPL],
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
    

    #Run the FastAPI Application on host '0.0.0.0' and port 8000
     uvicorn.run("main:app", host="0.0.0.0", port = 8000, reload = True)

