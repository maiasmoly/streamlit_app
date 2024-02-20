# Introduction to my Streamlit app

## Data Vizualizer

[Link to the streamlit apllication](https://maiasmoly-streamlit-app-app-rselz7.streamlit.app/)

This app allows you to choose a csv file and display information about it such as:

1. The data itself
2. The shape of the data set
3. The data types of each column

After selecting a column that you want to observe, the data visualizer will

1. If the column holds numerical data, it will give a five number summary of the data and display a histogram showing the distribution of the data.
2. If the column holds categorical data, it will display a barplot showing the distribution of the data. 

## CI with Jenkins

This streamlit app is built and deployed using google cloud build using an instance of Jenkins to run a CI/CD pipeline.
Everytime a change to the streamlit app is pushed to its github repository, the jenkins pipeline is automatically triggered and a new image is built of the updated app. This new image is automatically deployed using cloud run where the changes made are instantly reflected. 

Here is a link to a video demonstration of the Jenkins pipline: [Link](https://youtu.be/NEwxHaSqZTQ)