import streamlit as st
from navbar import navbar

# Define a function to create the workout card
def workout_card(set_number, exercise_name, target_data, rpe):
    # Create a container for the card
    with st.container():
        # Header row with set number, exercise name, and arrow
        header_col1, header_col2, header_col3 = st.columns([1, 8, 1])
        
        with header_col1:
            st.write(f"### {set_number}")
        with header_col2:
            st.write(f"### {exercise_name}")
        with header_col3:
            st.write("### ➔")  # Arrow icon

        st.divider()
        
        # Table header row for Set, Target, Weight, and Reps
        table_header_col1, table_header_col2, table_header_col3, table_header_col4, table_header_col5, table_header_col6 = st.columns([1, 2, 2, 2, 2, 1])
        table_header_col1.write("Set")
        table_header_col2.write("Target")
        table_header_col3.write("RPE")
        table_header_col4.write("Weight")
        table_header_col5.write("Reps")
        
        # Table rows for each set
        for i, target in enumerate(target_data, start=1):
            checkbox_key = f"checkbox_{set_number}_{i}"
            weight_key = f"weight_{set_number}_{i}"
            reps_key = f"reps_{set_number}_{i}"

            # Initialize the checkbox state if it doesn't exist
            if checkbox_key not in st.session_state:
                st.session_state[checkbox_key] = False

            # Check if the mark_all_completed_flag is set
            if st.session_state.get("mark_all_completed_flag", False):
                st.session_state[checkbox_key] = True

            # Get the current checkbox state
            done_checked = st.session_state[checkbox_key]

            # Create row columns
            row_col1, row_col2, row_col3, row_col4, row_col5, row_col6 = st.columns([1, 2, 2, 2, 2, 1])
            row_col1.write(i)
            row_col2.write(target)
            row_col3.write(f"{rpe}")

            # Disable inputs if checkbox is checked
            weight_disabled = done_checked
            reps_disabled = done_checked

            row_col4.text_input("Weight", key=weight_key, placeholder="kg", disabled=weight_disabled, label_visibility="collapsed")
            row_col5.text_input("Reps", key=reps_key, placeholder="reps", disabled=reps_disabled, label_visibility="collapsed")

            # Place the checkbox in the last column
            with row_col6:
                st.checkbox("Done", key=checkbox_key, label_visibility="collapsed")

# Function to set the mark_all_completed_flag
def mark_all_completed():
    st.session_state["mark_all_completed_flag"] = True

# Example usage of the workout card
st.title("WORKOUTS")
workout_card(1, "Bench Press (Barbell)", ["80kg x 5", "80kg x 5", "80kg x 5"], 7)
workout_card(2, "Incline Dumbbell Press", ["30kg x 5", "30kg x 5", "30kg x 5"], 7)
workout_card(3, "Cable Chest Fly", ["28kg x 5", "28kg x 5", "28kg x 5"], 7)

# Button to mark all rows as completed
if st.button("Mark as Completed", use_container_width=True):
    mark_all_completed()
    st.rerun()

st.session_state["mark_all_completed_flag"] = False
    
navbar()