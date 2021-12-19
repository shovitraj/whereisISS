
import requests
import pandas as pd 
import plotly.express as px
import streamlit as st
from Footer import Footer
import datetime as dt 
import time
from data import plot

Footer()
# while True:
Today_Date = str(dt.datetime.now().date())
Current_Time = str(dt.datetime.now().time())
st.sidebar.header('Current ISS position')
num = st.sidebar.slider('Number of ISS locations', min_value=1, max_value=50)
delay = st.sidebar.slider('Delay time in seconds', min_value=1, max_value=60)
st.header('Where is ISS?')


df = pd.DataFrame(columns=['Latitude','Longitude'])




count = 0
if num == 1:
    url = 'http://api.open-notify.org/iss-now.json'
    r = requests.get(url)
    iss_location=r.json()
    lat = float(iss_location['iss_position']['latitude'])
    lon = float(iss_location['iss_position']['longitude'])
    df = df.append(
    dict(
    Latitude=lat,
    Longitude=lon),
    ignore_index=True
    )
    
    st.sidebar.table(df)
    fig = plot(df)
    st.plotly_chart(fig)
else:
    st.sidebar.markdown(f'<div style="color: blue; font-size: largest"> Last {num} positions. </div>',
        unsafe_allow_html=True)
    table = st.sidebar.table(df)
    for i in range(num):
        url = 'http://api.open-notify.org/iss-now.json'
        r = requests.get(url)
        iss_location=r.json()
        lat = float(iss_location['iss_position']['latitude'])
        lon = float(iss_location['iss_position']['longitude'])
        df = df.append(
        dict(
        Latitude=lat,
        Longitude=lon),
        ignore_index=True
        )
        table = table.add_rows(df.tail(1))
        time.sleep(delay)
        
    fig2 = px.scatter_geo(df, 
                    lat='Latitude',
                    lon='Longitude',
                    projection="natural earth")
    fig2.update_geos(
                resolution=50,
                lataxis_showgrid=True, 
                lonaxis_showgrid=True,
                showcountries=True,
                landcolor = 'LightGreen',
                showocean=True,
                oceancolor = 'LightBlue')
    st.plotly_chart(fig2)

    

st.sidebar.subheader('Last Updated')
st.sidebar.markdown(f'<div style="color: blue; font-size: largest"> Date:  {Today_Date}  </div>',
        unsafe_allow_html=True)
st.sidebar.markdown(f'<div style="color: blue; font-size: largest"> Time:{Current_Time} </div>',
        unsafe_allow_html=True)
