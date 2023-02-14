# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:18:03 2023

@author: user
"""
import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('trained_model.sav', 'rb'))
heart_disease_model= pickle.load(open('trained_model2.sav', 'rb'))

with st.sidebar:
    selected=option_menu("MULTIPLE DISEASE PREDICTION",
                         ["DIABETES PREDICTION","HEART DISEASE PREDICTION"],
                         icons=["activity","heart"],
                         default_index=0)
    
if (selected=="DIABETES PREDICTION"):
    st.title("DIABETES PREDICTION SYSTEM")
    col1,col2=st.columns(2)
    
    with col1:
     Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
     Glucose = st.text_input('Glucose Level')
    with col1:
     BloodPressure = st.text_input('Blood Pressure value')
    with col2:
     SkinThickness = st.text_input('Skin Thickness value')
    with col1:
     Insulin = st.text_input('Insulin Level')
    with col2:
     BMI = st.text_input('BMI value')
    with col1:
     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
     Age = st.text_input('Age')
    
    d_diagnosis = ''
    
    
    if st.button('Diabetes Test Result'):
        input_data=[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

        input_data_as_numpy_array = np.asarray(input_data)

        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        diab_prediction = diabetes_model.predict( input_data_reshaped)
        
        if (diab_prediction[0] == 0):
          d_diagnosis= 'The person is not diabetic'
        else:
          d_diagnosis= 'The person is diabetic'
        
    st.success(d_diagnosis)
    
if (selected=="HEART DISEASE PREDICTION"):
    st.title("HEART DISEASE PREDICTION SYSTEM")
    
    col1,col2,col3=st.columns(3)
    
    with col1:
     age=st.text_input('Age')
    with col2:
     sex= st.text_input('Gender: 0 for Male/ 1 for female')
    with col3:
     cp= st.text_input('Chest Pain Types')
    with col1:
     trestbps= st.text_input('Resting Blood Pressure')
    with col2:
     chol = st.text_input('Cholestrol')
    with col3:
     fbs = st.text_input('Fasting Blood Sugar')
    with col1:
     restecg= st.text_input('Resting electrocardiographic measurement ')
    with col2:
     thalach = st.text_input('Maximum heart rate')
    with col3:
     exang = st.text_input('Exercise induced angina')
    with col1:
     oldpeak = st.text_input('Asymptomatic chest pain')
    with col2:
     slope = st.text_input('ST/HR slope')
    with col3:
     ca = st.text_input('Calcium')
    with col2:
     thal= st.text_input('Thalassemia')
    
    
    h_diagnosis = ''
   
   
    if st.button('Heart Disease Test Result'):
        input_data1=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        input_data_as_numpy_array1 = np.asarray(input_data1)

        input_data_reshaped1 = input_data_as_numpy_array1.reshape(1,-1)
        heart_prediction = heart_disease_model.predict( input_data_reshaped1)
       
       
        if (heart_prediction[0] == 0):
         h_diagnosis= 'The person does not have a heart disease'
        else:
         h_diagnosis= 'The person has a heart disease'
       
    st.success(h_diagnosis)
    
    

    