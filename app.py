import streamlit as st
import pickle
import numpy as np
import pandas as pd

pipe = pickle.load(open('decision.pkl', 'rb'))
df = pickle.load(open('churn.pkl', 'rb'))

st.title('Churn Prediction For Bank Customers')

credit_score = st.number_input('Credit Score')

country = st.selectbox('Country',df['country'].unique())

gender = st.selectbox('Gender',df['gender'].unique())

age = st.number_input('Age')

balance = st.number_input('Balance')

product = st.selectbox('Product Number', [1,2,3,4])

active_number = st.selectbox('Active Member', ['Yes', 'No'])

if active_number=='Yes':
    active_number=1
else:
    active_number=0

if st.button('Predict'):
    query = np.array([credit_score, country, gender, age, balance, product, active_number])
    query = query.reshape([1,7])

    if pipe.predict(query)==1:
        st.subheader('The Customer Left the Bank')
    else:
        st.subheader('The Customer Stay with the Bank')