import numpy as np
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load the model
model = pickle.load(open('./model/XGBoost_model.pkl', 'rb'))

# Load the encoders
flat_type_ohe = pickle.load(open('./encoder/flat_type_ohe.pkl', 'rb'))
storey_ohe = pickle.load(open('./encoder/storey_ohe.pkl', 'rb'))
town_looe = pickle.load(open('./encoder/town_looe.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    # Receive inputs from user
    town = request.form.get('town_value')
    flat_type = request.form.get('flat-type_value')
    floor_area = float(request.form.get('floor-area_value'))
    yos = int(request.form.get('year-of-sale_value'))
    storey_range = request.form.get('storey-range_value')
    lcy = int(request.form.get('lease-commence-year_value'))

    # Pre-processing
    col_names = ['town', 'flat_type', 'floor_area_sqm', 'year_of_sale', 'storey', 'year_lease_commence']
    storey_class = {
        '01 TO 03': 'LOW',
        '04 TO 06': 'LOW',
        '07 TO 09': 'MID',
        '10 TO 12': 'MID',
        '13 TO 15': 'HIGH',
        '16 TO 18': 'HIGH',
        '19 TO 21': 'VERY HIGH',
        '22 TO 24': 'VERY HIGH',
        '25 TO 27': 'VERY HIGH'
    }
    storey = storey_class[storey_range]

    df = pd.DataFrame([[town, flat_type, floor_area, yos, storey, lcy]])
    df.columns = col_names

    # Encode the town using leave one out encoder
    df_enc_town = town_looe.transform(df['town'])
    df_enc_town.rename(columns= {'town': 'town_enc'}, inplace= True)
    df = pd.concat([df, df_enc_town], axis= 1)

    # Encode the flat type with one hot encoding
    df_flat_type_ohe = pd.DataFrame(flat_type_ohe.transform(df['flat_type'].values.reshape(-1, 1)).toarray())
    df_flat_type_ohe.columns = flat_type_ohe.get_feature_names_out(['flat_type'])
    df = pd.concat([df, df_flat_type_ohe], axis= 1)

    # Encode the storey range with one hot encoding
    df_storey_ohe = pd.DataFrame(storey_ohe.transform(df['storey'].values.reshape(-1, 1)).toarray())
    df_storey_ohe.columns = storey_ohe.get_feature_names_out(['storey'])
    df = pd.concat([df, df_storey_ohe], axis= 1)

    # Drop unnecessary columns
    df.drop(columns= ['town', 'flat_type', 'storey'], inplace= True)

    # Prediction
    y_pred = model.predict(df)
    prediction = round(y_pred[0])

    return render_template('index.html', prediction_text=f'Estimated resale flat price is SGD {prediction:,}')

if __name__ == '__main__':
    app.run()