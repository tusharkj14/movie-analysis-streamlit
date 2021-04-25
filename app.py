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
    """<p style='display: block; position: fixed; text-align: center; color: white; bottom: 10%; left:2%'>Maintained By Tushar Kanti Jaiswal</p>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """<a style='display: block; position: fixed; bottom: 5%; left:5%;' href="https://github.com/tusharkj14" target="_blank">Github</a>
    """,
    unsafe_allow_html=True,
)

st.sidebar.markdown(
    """<a style='display: block; position: fixed; bottom: 5%; left:10%;' href="https://linkedin.com/" target="_blank">LinkedIn</a>
    """,
    unsafe_allow_html=True,
)