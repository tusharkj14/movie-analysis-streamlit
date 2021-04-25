import streamlit as st
from predict import predict
from explore import explore
from text_p import text_processing
import nltk
# nltk.data.path.append('/app/.heroku/python/nltk_data')


page = st.sidebar.selectbox("Explore Or Predict", ("Explore", "Predict"))


if page == "Predict":
    predict()
else:
    explore()

st.sidebar.markdown(
    """<div style='display: inline; position: fixed; bottom: 5%;'>
        <p style ='text-align: centre;'>Maintained By Tushar Kanti Jaiswal</p>
        <p style ='left: 10%'>
        <a href="https://github.com/tusharkj14" target="_blank">Github</a>
        <a href="https://www.linkedin.com/in/tushar-jaiswal14b/" target="_blank">LinkedIn</a>
        </p>
        </div>
    """,
    unsafe_allow_html=True,
)




