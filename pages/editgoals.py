import streamlit as st

# Set page config
st.set_page_config(page_title="Edit Goals",
    initial_sidebar_state="collapsed")

# Goal options
goal_options = [
    "Run 5km",
    "Lose 2kg",
    "Do 50 pushups",
    "Cycle 10km",
    "Swim 1km",
    "Lift 100kg",
    "Meditate for 30 minutes"
]

# Ensure initial goals are available in session state
if 'goals' not in st.session_state:
    st.session_state.goals = ["Run 5km", "Lose 2kg", "Do 50 pushups"]

# Title
st.title("Edit My Goals")

# Helper functions to update session state on selection change
def update_goal1():
    st.session_state.goals[0] = st.session_state.goal1

def update_goal2():
    st.session_state.goals[1] = st.session_state.goal2

def update_goal3():
    st.session_state.goals[2] = st.session_state.goal3

# Dropdowns for editing goals
st.selectbox("Select Goal 1", options=goal_options, index=goal_options.index(st.session_state.goals[0]), key="goal1", on_change=update_goal1)
st.selectbox("Select Goal 2", options=goal_options, index=goal_options.index(st.session_state.goals[1]), key="goal2", on_change=update_goal2)
st.selectbox("Select Goal 3", options=goal_options, index=goal_options.index(st.session_state.goals[2]), key="goal3", on_change=update_goal3)

# Save Goals and Return to Goals Page
if st.button("Save and Return to Goals"):
    st.switch_page("app.py")