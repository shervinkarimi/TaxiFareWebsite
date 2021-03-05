import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd

'''
# TaxiFareModel front
'''

st.markdown('''
Enter your coordinnates
''')



# PU lon ----------------------------------------------------------------
pickup_longitude = st.number_input('Insert a pickup_longitude')

st.write('The current pickup_longitude is ', pickup_longitude)
# PU lat ----------------------------------------------------------------
pickup_latitude = st.number_input('Insert a pickup_latitude')

st.write('The current pickup_latitude is ', pickup_latitude)
# DO lat ----------------------------------------------------------------
dropoff_longitude = st.number_input('Insert a dropoff_longitude')

st.write('The current dropoff_longitude is ', dropoff_longitude)
# DO lat ----------------------------------------------------------------
dropoff_latitude = st.number_input('Insert a dropoff_latitude')

st.write('The current dropoff_latitude is ', dropoff_latitude)


st.markdown('''

Maps

''')
df = pd.DataFrame(
    {
        'lat':[pickup_latitude,dropoff_latitude],
        'lon':[pickup_longitude,dropoff_longitude]
    }
)
st.map(df)



url = 'http://taxifare.lewagon.ai/predict_fare/'

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Taxi Fare Estimation')


input_data= {
        "dropoff_latitude":dropoff_latitude, 
        "dropoff_longitude":dropoff_longitude, 
        "key":"2015-01-27 13:08:24.0000002", 
        "passenger_count":1, 
        "pickup_datetime":"2015-01-27 13:08:24 UTC", 
        "pickup_latitude":pickup_latitude,
        "pickup_longitude":pickup_longitude}

#url ='http://taxifare.lewagon.ai/predict_fare/?key=2012-10-06%2012:10:20.0000001&pickup_datetime=2012-10-06%2012:10:20%20UTC&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2'
response = requests.get(url,params=input_data)
st.write(response.json()['prediction'])