import streamlit as st
from utils import generate_streamlit_element
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from survey_questions import questions
from pymongo import MongoClient
import mongo_utils
from config import USER_ID_STATE_KEY
from typing import Any

# Reintroduce sidebar (collapse button will stay hidden as CSS cannot be dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")

st.title("Part 3: Satisfaction with Assurance Practices")
st.markdown(
    "This section assesses the community’s satisfaction levels with current assurance processes, "
    "infrastructure, and support resources."
)

# Disable the submit button after it is clicked
def disable():
    st.session_state.disabled = True

# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define the tags of questions to display in this section
tags_to_display = ["integrate_assurance", "communication_impact", "link_assurance_activities", "satisfaction_justification"]

# Wrap your input elements and submit button in a form
with st.form("survey_form"):
    # Generate Streamlit elements and assign responses to variables
    responses = {}
    for tag in tags_to_display:
        responses[tag] = generate_streamlit_element(
            questions[tag]["question"],
            questions[tag]["type"],
            options=questions[tag].get("options"),
            key=tag
        )

    # Submit button for the form
    submitted = st.form_submit_button("Submit", on_click=disable, disabled=st.session_state.disabled)
    if submitted:
        st.session_state["submitted"] = True  # Mark the form as submitted

# Actions to take after the form is submitted
if submitted:
    client: MongoClient = mongo_utils.init_connection()
    if client:
        data: dict[str, Any] = {
            "_id": st.session_state[USER_ID_STATE_KEY]
        }
        data.update({tag: responses[tag] for tag in tags_to_display})
        mongo_utils.add_survey_results(client, data)
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Community_Results")
