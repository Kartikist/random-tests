import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")



st.title("Happiness index plot")


optionx =  st.selectbox("Select data for x axis:", options=["gdp", "happiness", "generosity"],key="optx")
xdf = df[f"{optionx}"]


optiony =  st.selectbox("Select data for x axis:", options=["gdp", "happiness", "generosity"], key="opty")
ydf = df[f"{optiony}"]

figure = px.scatter(x=xdf, y=ydf, labels={"x":f"{optionx}", "y":f"{optiony}"})
st.plotly_chart(figure)



