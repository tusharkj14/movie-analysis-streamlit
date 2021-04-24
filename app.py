import streamlit as st
from predict import predict
from explore import explore
from text_p import text_processing
import nltk
nltk.data.path.append('path_to_nltk_data')


page = st.sidebar.selectbox("Explore Or Predict", ("Explore", "Predict"))

if page == "Predict":
    predict()
else:
    explore()
