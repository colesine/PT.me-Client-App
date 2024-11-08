import streamlit as st

# Set page config
st.set_page_config(page_title="My Goals",
    initial_sidebar_state="collapsed")



# Initialize session state for goals
if 'goals' not in st.session_state:
    st.session_state.goals = ["Run 5km", "Lose 2kg", "Do 50 pushups"]

# Display goals
st.title("My Goals")
for i, goal in enumerate(st.session_state.goals):
    st.markdown(f"### Goal {i + 1}: {goal}")

# Edit Goals Button
if st.button("Edit Goals"):
    st.switch_page("edit-goals.py")