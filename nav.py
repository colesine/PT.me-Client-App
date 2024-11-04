import streamlit as st

pages = {
    "Your account": [
        st.Page("dashboard.py", title="Dashboard"),
        st.Page("workouts.py", title="Workouts"),
]
}

pg = st.navigation(pages)
pg.run()
