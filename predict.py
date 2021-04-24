import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt
from text_p import text_processing
from joblib import dump, load
import nltk
# nltk.data.path.append('/app/.heroku/python/nltk_data')

def predict():
    model = load('sentiment_analysis.joblib')

    st.write("""
    ## Enter a Brief Movie Review
    """)

    input_to_predict = st.text_area("Enter the review of any movie.", height=100)

    if input_to_predict:
        prediction = model.predict([input_to_predict])

        if prediction == 0:
            st.subheader("Negative Review")

        else:
            st.subheader("Positive Review")

    with st.beta_expander('See Metrics'):
        st.image('images/confusion_matrix.png', caption='Confusion Matrix for a test dataset with 5000 values')
        st.write("Acuuracy over the test set is : 86.54%" )


def main():
    predict()


if __name__ == '__main__':
    main()