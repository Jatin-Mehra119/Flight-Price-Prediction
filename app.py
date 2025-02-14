import streamlit as st
import pandas as pd
import joblib

model_path = "Flight_price_predictor.pkl" # model path
model = joblib.load(model_path)

# Interface 

st.title("Flight Price Prediction")

airline = st.selectbox('Airline', ['Air India', 'IndiGo', 'Jet Airways', 'SpiceJet', 'Vistara', 'GoAir', 'Trujet', 'StarAir', 'AirAsia'])
flight = st.text_input('Flight : Number')
source_city = st.selectbox('Departure City', ['Bangalore', 'Delhi', 'Kolkata', 'Chennai', 'Mumbai', 'Hyderabad'])
destination_city = st.selectbox('Destination City', ['Bangalore', 'Delhi', 'Kolkata', 'Chennai', 'Mumbai', 'Hyderabad'])
departure_time = st.selectbox('Departure Time', ['Early Morning', 'Morning', 'Afternoon', 'Early Evening', 'Evening', 'Night', 'Late Night'])
arrival_time = st.selectbox('Arrival Time', ['Early Morning', 'Morning', 'Afternoon', 'Early Evening', 'Evening', 'Night', 'Late Night'])
stop_type = st.selectbox('Number of Stops', ['zero', 'one', 'two+'])
duration = st.number_input('Duration (hours)', min_value=0.0, max_value=24.0, step=0.5)
seat_class = st.selectbox('Class Type ', ['economy', 'business'])
days_left = st.number_input('Days Left', min_value=0, max_value=50, step=1)

# Create a DataFrame from user input
input_data = pd.DataFrame({
    'airline': [airline],
    'source_city': [source_city],
    'departure_time': [departure_time],
    'stop_type': [stop_type],
    'arrival_time': [arrival_time],
    'destination_city': [destination_city],
    'class': [seat_class],
    'duration': [duration],
    'days_left': [days_left]
})

# Make prediction
if st.button('Predict'):
    if source_city != destination_city:
        prediction = model.predict(input_data)
        st.write(f"Predicted Ticket Price: {prediction[0]}")
    else:
        st.error("Source and destination cities can't be the same!")
