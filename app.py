import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Choose a file to upload! Make sure it's a csv!")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    st.write("Above is our data frame from the uploaded data! Here are some summary statistics:")
    st.write("The size of our data frame is ", df.shape)
    st.write(df.describe())


