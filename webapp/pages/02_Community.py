import streamlit as st
from utils import generate_streamlit_element
from streamlit_extras.switch_page_button import switch_page
from survey_questions import questions
from pymongo import MongoClient
import mongo_utils
from config import USER_ID_STATE_KEY
from typing import Any

# reintroduce sidebar (collapse button will stay hidden as CSS cannot by
# dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")


st.title("Part 1: Community Composition")
st.markdown(
    "This section explores your understanding and current practices around "
    "assurance "
    "of digital twins."
)


# Disable the submit button after it is clicked
def disable():
    st.session_state.disabled = True


# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define the tags of questions to display in this section
tags_to_display = ["sector", "location", "role", "primary_responsibilities"]

# Wrap your input elements and submit button in a form
with st.form("survey_form"):
    # Generate Streamlit elements and assign responses to variables
    tag = "sector"
    sector = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )
    tag = "location"
    location = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )
    tag = "role"
    role = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

    tag = "primary_responsibilities"
    primary_responsibilities = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

    # Submit button for the form
    submitted = st.form_submit_button(
        "Submit", on_click=disable, disabled=st.session_state.disabled
    )
    if submitted:
        st.session_state["submitted"] = True  # Mark the form as submitted

# Actions to take after the form is submitted
if submitted:
    client: MongoClient = mongo_utils.init_connection()
    if client:
        data: dict[str, Any] = {
            "_id": st.session_state[USER_ID_STATE_KEY],
            "sector": sector,
            "location": location,
            "role": role,
            "responsibilities": ", ".join(
                primary_responsibilities
            ),  # Joining list into a string
        }

        mongo_utils.add_survey_results(client, data)
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Community_Results")
