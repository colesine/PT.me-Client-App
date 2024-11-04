import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import altair as alt

# Set page config
st.set_page_config(page_title="Weight Analytics", layout="wide")

WEIGHT_DATA = {
    '2022': {month: 80 - (month * 0.2) for month in range(1, 13)},
    '2023': {month: 77.6 - (month * 0.1) for month in range(1, 13)},
    '2024': {
        1: 76.5, 2: 76.2, 3: 75.8, 4: 75.5, 5: 75.1, 6: 74.8,
        7: 74.5, 8: 74.3, 9: 74.0, 10: 73.8, 11: 73.5, 12: 73.2
    }
}

def get_weight_data():
    data = []
    for year, months in WEIGHT_DATA.items():
        for month, weight in months.items():
            date = pd.Timestamp(f"{year}-{month:02d}-01")
            data.append({'date': date, 'weight': weight})
    return pd.DataFrame(data)

# Create metrics class to track last updated
class Metric:
    def __init__(self, name, value, last_updated):
        self.name = name
        self.value = value
        self.last_updated = last_updated

st.header("Weight")

# Time period selector
period = st.radio(
    "Select time period",
    ["DAILY", "MONTH", "YEAR"],
    horizontal=True
)

# Get the fixed dataset
df = get_weight_data()

# Filter and process data based on the selected period
if period == "DAILY":
    # Generate daily data for the last 30 days of the most recent month
    last_month_data = df[df['date'].dt.year == 2024].iloc[-1]
    start_weight = last_month_data['weight']
    
    # Create daily variations around the monthly average
    daily_dates = pd.date_range(end=pd.Timestamp('2024-12-31'), periods=30)
    daily_weights = [start_weight + np.random.normal(0, 0.1) for _ in range(30)]
    
    # Create new DataFrame for daily view
    df = pd.DataFrame({
        'date': daily_dates,
        'weight': daily_weights
    })
    x_format = '%b %d'
elif period == "MONTH":
    # For monthly view, we'll use all months of 2024
    df = df[df['date'].dt.year == 2024]
    x_format = '%b %Y'
elif period == "YEAR":
    # For yearly view, we'll use the average of each year
    df = df.groupby(df['date'].dt.year).agg({'weight': 'mean'}).reset_index()
    df['date'] = pd.to_datetime(df['date'].astype(str))
    x_format = '%Y'

# Round weight values to 2 decimal places
df['weight'] = df['weight'].round(2)

# Calculate y-axis range
y_min = df['weight'].min() - 1  # Subtract 1 to give some padding
y_max = df['weight'].max() + 1  # Add 1 to give some padding

# Create an Altair chart with custom x-axis format
chart = alt.Chart(df).mark_line().encode(
    x=alt.X('date:T', axis=alt.Axis(title='Date', format=x_format)),
    y=alt.Y('weight:Q', scale=alt.Scale(domain=[y_min, y_max]))
).properties(
    height=400,
    width='container'
)

# Add points to the chart
points = chart.mark_circle(size=60).encode(
    tooltip=['date:T', 'weight:Q']
)

# Combine line and points
final_chart = (chart + points)

# Display the chart in Streamlit
st.altair_chart(final_chart, use_container_width=True)

    
# Add hover tooltip using custom JavaScript
st.markdown("""
    <style>
    .tooltip {
        position: absolute;
        background-color: white;
        border: 1px solid gray;
        padding: 5px;
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# Custom CSS to match the design
st.markdown("""
    <style>
    .stButton button {
        width: 100%;
        text-align: left;
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
    }
    /* Color coding for different metric types */
    .stButton:nth-child(1) button, .stButton:nth-child(4) button {
        background-color: #fefce8;
    }
    .stButton:nth-child(2) button, .stButton:nth-child(3) button {
        background-color: #dcfce7;
    }
    .stButton:nth-child(5) button, .stButton:nth-child(6) button {
        background-color: #fee2e2;
    }
    </style>
""", unsafe_allow_html=True)