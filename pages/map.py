import numpy as np
import pandas as pd
import streamlit as st


pickup_latitude= 73.9798156
dropoff_latitude = 73.8803331
pickup_longitude = -40.7614327
dropoff_longitude = -40.6513111


data = {
    'lat': [pickup_latitude, dropoff_latitude],
    'lon': [pickup_longitude, dropoff_longitude]
}
df = pd.DataFrame(data)

st.dataframe(df)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.dataframe(df)

st.map(df, zoom=-10)
