import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title('Data Visualizer')
st.header("Vizualize any column of a data set and see it's distribution!")

# Display file uploader:
uploaded_file = st.file_uploader("Choose a file to upload! Make sure it's a csv!")

if uploaded_file is not None:
    # Read in chosen csv file
    df = pd.read_csv(uploaded_file)
    df = pd.DataFrame(df)

    # Display the chosen data
    st.subheader("The Data:")
    st.write(df)

    # Display relevant statistics:
    st.subheader("Some Stats:")
    st.write("The size of our data frame is ", df.shape)
    st.write(f'Here are the data types of each of the columns:')
    st.write(df.dtypes)
            
    # Print a select box that has each column as an option: 
    st.subheader('Observing the Columns:')       
    chosen_col = st.selectbox("Choose a column to observe", df.columns)

    
    # Decide whether the column contains numerical or categorical variables
    col_type = df[chosen_col].dtype
    if col_type == 'object' or col_type == 'category' or len(df[chosen_col].unique()) < 10:
        st.write('Categorical data! So here is a barplot of the distribution:')
        fig = plt.figure(figsize=(10, 4))
        sns.barplot(data = df, x = df[chosen_col].unique(), y = df[chosen_col].value_counts()).set(title = f"Barplot of {chosen_col}")
        st.pyplot(fig)

    elif col_type == 'int64' or col_type == 'float64' or col_type == 'int32' or col_type == 'float32':
        # Print a five number summary of the chosen column:
        st.write(f'You chose {chosen_col}! Here is a five number summary of {chosen_col}:')
        st.write(df[chosen_col].describe().loc[['min', '25%', '50%', '75%', 'max']])
        # Plot a histogram of the numerical data
        st.write("Numerical data! So here is a histogram of the distribution:")
        fig = plt.figure(figsize=(10, 4))
        sns.distplot(df[chosen_col]).set(title = f"Distribution of {chosen_col}")
        st.pyplot(fig)

   
