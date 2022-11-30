import pickle
import streamlit as st

# Reading Model
diabets_model = pickle.load(open('diabets_model2.sav', 'rb'))

# Web Tittle
st.title('Diabetes Prediction Data Mining')


Pregnancies = st.text_input('Input Pragnancies Value')
Glucose = st.text_input('Input Glucose Value')
BloodPressure = st.text_input('Input Blood Pressure Value')
SkinThickness = st.text_input('Input Skin Thickness Value')
Insulin = st.text_input('Input Insulin Value')
BMI = st.text_input('Input BMI Value')
DiabetesPedigreeFunction = st.text_input('Input Diabetes Pedigree Value')
Age = st.text_input('Input Age')

# Code for Prediction
diab_diag = ' '

if st.button('Predict Diabetes Test'):
    diab_prediction = diabets_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
    if(diab_prediction[0] == 1):
        diab_diag = 'Patient Have Diabetes'
    else:
        diab_diag = 'Patient Have No Diabetes'
    st.success(diab_diag)
