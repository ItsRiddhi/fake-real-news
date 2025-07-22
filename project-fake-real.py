import os
import streamlit as st
import pickle

with open("news.pkl",'rb') as f:
    model = pickle.load(f)

st.title("Real Vs Fake News Classifer")

text = st.text_input("Enter the Text")

if st.button("Analyze"):
    pred = model.predict([text])
    if pred == 'Real':
        st.info("News is Real")
    else:
        st.info("News is Fake")