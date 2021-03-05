import streamlit as st
import datetime
import requests
import numpy as np
import pandas as pd

st.image('Picture1.png')


st.markdown("<h1 style='text-align: center; color: dark-red;'>MARSEILLE DEEP TAXI</h1>", unsafe_allow_html=True)

'''
# When
'''
st.date_input('')
st.time_input('')


'''
# Where
'''




# PU lon ----------------------------------------------------------------
pickup_longitude = st.number_input('Insert a pickup_longitude',value=-73)

# st.write('The current pickup_longitude is ', pickup_longitude)
# PU lat ----------------------------------------------------------------
pickup_latitude = st.number_input('Insert a pickup_latitude',value=43)

# st.write('The current pickup_latitude is ', pickup_latitude)
# DO lat ----------------------------------------------------------------
dropoff_longitude = st.number_input('Insert a dropoff_longitude',value=-74)

# st.write('The current dropoff_longitude is ', dropoff_longitude)
# DO lat ----------------------------------------------------------------
dropoff_latitude = st.number_input('Insert a dropoff_latitude',value=42)

# st.write('The current dropoff_latitude is ', dropoff_latitude)




df = pd.DataFrame(
    {
        'lat':[pickup_latitude,dropoff_latitude],
        'lon':[pickup_longitude,dropoff_longitude]
    }
)


'''
# Who
'''

st.radio('', [1,2,3,4])

'''
# Maps
'''
st.map(df)

url = 'http://taxifare.lewagon.ai/predict_fare/'



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
price = round(response.json()['prediction'],0)



'''
# Let's go
'''
st.subheader('Estimated Price')
st.code('$'+str(price))

st.button('Order your Taxi Fire')




