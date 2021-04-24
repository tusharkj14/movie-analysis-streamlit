import streamlit as st
from predict import predict
from explore import explore
from text_p import text_processing


page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

if page == "Predict":
    predict()
else:
    explore()
