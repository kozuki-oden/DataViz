import pandas as pd
import plotly.express as px
import streamlit as st


st.title("DataViz - A data visualization app")
st.subheader("Dataset-")
st.sidebar.subheader("Settings")

uploaded_file = st.sidebar.file_uploader(label="Upload csv file", type=['csv'])

dataframe = pd.DataFrame([1, 2, 3])
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

select_chart = st.sidebar.selectbox(
    label="Select a chart type",
    options=['None', 'Line Plots', 'Scatter Plots', 'Histogram Plots', 'Bar Plots', 'Box Plots', 'Violin Plots']
)

cols = dataframe.columns

if select_chart == 'Line Plots':
    st.sidebar.subheader("Line Plots Features")
    select_x = st.sidebar.selectbox('X axis', options=cols)
    select_y = st.sidebar.selectbox('Y axis', options=cols)
    variation = st.sidebar.selectbox('Enter Feature for Color Variation', options=cols)
    plot1 = px.line(dataframe, x=select_x, y=select_y, color=variation)
    st.plotly_chart(plot1)

elif select_chart == 'Scatter Plots':
    st.sidebar.subheader("Scatter Plot Features")
    select_x = st.sidebar.selectbox('X axis', options=cols)
    select_y = st.sidebar.selectbox('Y axis', options=cols)
    variation = st.sidebar.selectbox('Enter Feature for Color Variation', options=cols)
    plot2 = px.scatter(dataframe, x=select_x, y=select_y, color=variation)
    st.plotly_chart(plot2)

elif select_chart == 'Histogram Plots':
    st.sidebar.subheader("Histogram Plot Features")
    select_x = st.sidebar.selectbox('X axis', options=cols)
    select_y = st.sidebar.selectbox('Y axis', options=cols)
    variation = st.sidebar.selectbox('Enter Feature for Color Variation', options=cols)
    plot3 = px.histogram(dataframe, x=select_x, y=select_y, color=variation)
    st.plotly_chart(plot3)

elif select_chart == 'Bar Plots':
    st.sidebar.subheader("Bar Plot Features")
    select_x = st.sidebar.selectbox('X axis', options=cols)
    select_y = st.sidebar.selectbox('Y axis', options=cols)
    variation = st.sidebar.selectbox('Enter Feature for Color Variation', options=cols)
    plot4 = px.bar(dataframe, x=select_x, y=select_y, color=variation)
    st.plotly_chart(plot4)

elif select_chart == 'Box Plots':
    st.sidebar.subheader("Box Plot Features")
    select_x = st.sidebar.selectbox('X axis', options=cols)
    select_y = st.sidebar.selectbox('Y axis', options=cols)
    variation = st.sidebar.selectbox('Enter Feature for Color Variation', options=cols)
    plot5 = px.box(dataframe, x=select_x, y=select_y, color=variation)
    st.plotly_chart(plot5)

elif select_chart == 'Violin Plots':
    st.sidebar.subheader("Box Plot Features")
    select_x = st.sidebar.selectbox('X axis', options=cols)
    select_y = st.sidebar.selectbox('Y axis', options=cols)
    variation = st.sidebar.selectbox('Enter Feature for Color Variation', options=cols)
    plot6 = px.violin(dataframe, x=select_x, y=select_y, color=variation)
    st.plotly_chart(plot6)
