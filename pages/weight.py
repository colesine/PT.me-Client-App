import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import altair as alt
from navbar import navbar

# Set page config
st.set_page_config(page_title="Weight Analytics",
    initial_sidebar_state="collapsed")

# Predefined weight data by year and month
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

st.header("Weight Analytics")

# Define tabs for each time period
tabs = st.tabs(["DAILY", "MONTH", "YEAR"])

# Get the base dataset
df = get_weight_data()

# DAILY tab: Generate daily data with random variations
with tabs[0]:
    st.subheader("Daily View")
    # Use the last available monthly weight in 2024 as a base
    last_month_weight = WEIGHT_DATA['2024'][12]  # December weight for 2024
    daily_dates = pd.date_range(end=pd.Timestamp('2024-12-31'), periods=30)
    daily_weights = [last_month_weight + np.random.normal(0, 0.2) for _ in range(30)]
    
    # Create DataFrame for daily view
    df_daily = pd.DataFrame({
        'date': daily_dates,
        'weight': daily_weights
    })
    x_format = '%b %d'
    df_to_plot = df_daily

    # Plot chart for DAILY tab
    y_min = df_to_plot['weight'].min() - 1
    y_max = df_to_plot['weight'].max() + 1

    chart = alt.Chart(df_to_plot).mark_line().encode(
        x=alt.X('date:T', axis=alt.Axis(title='Date', format=x_format)),
        y=alt.Y('weight:Q', scale=alt.Scale(domain=[y_min, y_max]))
    ).properties(
        height=400,
        width='container'
    )

    points = chart.mark_circle(size=60).encode(
        tooltip=['date:T', 'weight:Q']
    )

    st.altair_chart(chart + points, use_container_width=True)

# MONTH tab: Use monthly data for 2024
with tabs[1]:
    st.subheader("Monthly View")
    df_monthly = df[df['date'].dt.year == 2024]
    x_format = '%b %Y'
    df_to_plot = df_monthly

    # Plot chart for MONTH tab
    y_min = df_to_plot['weight'].min() - 1
    y_max = df_to_plot['weight'].max() + 1

    chart = alt.Chart(df_to_plot).mark_line().encode(
        x=alt.X('date:T', axis=alt.Axis(title='Date', format=x_format)),
        y=alt.Y('weight:Q', scale=alt.Scale(domain=[y_min, y_max]))
    ).properties(
        height=400,
        width='container'
    )

    points = chart.mark_circle(size=60).encode(
        tooltip=['date:T', 'weight:Q']
    )

    st.altair_chart(chart + points, use_container_width=True)

# YEAR tab: Calculate the average weight per year
with tabs[2]:
    st.subheader("Yearly View")
    df_yearly = df.groupby(df['date'].dt.year).agg({'weight': 'mean'}).reset_index()
    df_yearly['date'] = pd.to_datetime(df_yearly['date'].astype(str))
    x_format = '%Y'
    df_to_plot = df_yearly

    # Plot chart for YEAR tab
    y_min = df_to_plot['weight'].min() - 1
    y_max = df_to_plot['weight'].max() + 1

    chart = alt.Chart(df_to_plot).mark_line().encode(
        x=alt.X('date:T', axis=alt.Axis(title='Date', format=x_format)),
        y=alt.Y('weight:Q', scale=alt.Scale(domain=[y_min, y_max]))
    ).properties(
        height=400,
        width='container'
    )

    points = chart.mark_circle(size=60).encode(
        tooltip=['date:T', 'weight:Q']
    )

    st.altair_chart(chart + points, use_container_width=True)

navbar()