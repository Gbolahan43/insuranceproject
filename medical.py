# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 04:49:38 2024

@author: Excellus
"""

import pandas as pd
import streamlit as st
import pickle
#import xgboost as xgb

filename = 'naivebayes_model.sav'
model = pickle.load(open(filename,'rb'))

st.title('Medical Insurance Purchase Prediction App')
st.subheader("""This app takes in certain variables to enable prediction whether or not a medical insurance will be purchased""")

def user_input():
    Gender = st.selectbox('What is your gender', options=['Male', 'Female'], index=0)
    Age = st.number_input('How old are you?', min_value=10, max_value=50)
    EstimatedSalary = st.number_input('What is your estimated salary ($)', min_value=0.0, max_value=500000.0, step=1000.0, format='%f')
    
    # Map 'Male' to 1 and 'Female' to 0
    gender_mapping = {'Male': 1, 'Female': 0}
    
    data = {
        'Gender': gender_mapping[Gender],
        'Age': Age,
        'EstimatedSalary': EstimatedSalary
    }
    
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input()

def prediction():
    predict_ = model.predict(df)
    result = ''
    if predict_ == 0:
        result = 'Not Purchased'
    else:
        result = 'Purchased'
    return result

# Prediction button
if st.button("Predict"):
    result = prediction()
    st.success('Thank you for filling this form. This medical insurance will {}'.format(result))
    st.write('Have a nice day')