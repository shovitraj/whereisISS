
import requests
import pandas as pd 
import time
import plotly.express as px



def location():
    df = pd.DataFrame(columns=['Latitude','Longitude'])
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
    time.sleep(2)
    return df

def plot(df):
    df = location()
    fig = px.scatter_geo(df, 
                    lat='Latitude',
                    lon='Longitude',
                    projection="natural earth")
    fig.update_geos(
                resolution=50,
                lataxis_showgrid=True, 
                lonaxis_showgrid=True,
                showcountries=True,
                landcolor = 'LightGreen',
                showocean=True,
                oceancolor = 'LightBlue')
    return fig
    
def location_count(n):
    count = 0
    while count <= n:
        df = pd.DataFrame(columns=['Latitude','Longitude'])
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
    time.sleep(1)
    count +=1
    
    return df


    

       
