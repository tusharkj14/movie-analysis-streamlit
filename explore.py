import streamlit as st
import numpy as np 
import pandas as pd
from text_p import text_processing
pd.set_option("display.max_colwidth",200)
import nltk
nltk.data.path.append('/app/.heroku/python/nltk_data')

@st.cache
def load_data(name_of_csv):
    return pd.read_csv(name_of_csv)

def explore():
    st.title("Movie Review Exploration")
    df = load_data('Sentiment/Train.csv')
    
    placeholder_old = st.empty()
    placeholder = st.empty()

        
    st.sidebar.header("Dataset Exploration")


    if st.sidebar.button("Negative Review Examples"):
        placeholder_old.markdown("<h3 style='text-align: center; color: white;'>5 Examples of negative reviews</h3>", unsafe_allow_html=True)
        if not st.sidebar.checkbox("Hide dataframe"):
            placeholder.table(df[df['label']==0].head(5))
    
    if st.sidebar.button("Positive Review Examples"):
        placeholder_old.markdown("<h3 style='text-align: center; color: white;'>5 Examples of positive reviews</h3>", unsafe_allow_html=True)
        if not st.sidebar.checkbox("Hide dataframe"):
            placeholder.table(df[df['label']==1].head(5))
    
    
    # st.markdown("<h3 style='text-align: center; color: white;'>Length of Negative Movie Reviews vs Length of Positive Movie Reviews</h3>", unsafe_allow_html=True)
    st.image('images/Negative vs Positive.png', caption='Length of Negative Movie Reviews vs Length of Positive Movie Reviews')

    with st.beta_expander('See Text Processing'):
        my_slider_val = st.slider('Index of Review Text', 0, 50000)
        st.write("Before Processing")
        st.write(df['text'].iloc[my_slider_val])
        # placeholder_new = st.empty()
        if st.checkbox("Process Text Data"):
            processed = text_processing(df['text'].iloc[my_slider_val])
            st.write("After Processing :")
            st.write(" ".join(processed))

    with st.beta_expander('Reviews'):
        
        
        st.write( """
        #### No. of Positive Reviews : {}
        #### No. of Negative Reviews : {}
        """ .format(df['label'].value_counts()[0] , df['label'].value_counts()[1]))

    
def main():
    explore()


if __name__ == '__main__':
    main()