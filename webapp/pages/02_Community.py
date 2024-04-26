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
    "Here we aim to understand the diverse backgrounds"
    "within the digital twin community."
)


# Disable the submit button after it is clicked
def disable():
    st.session_state.disabled = True


# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define the tags of questions to display in this section
tags_to_display = ["sector", "location", "role", "primary_responsibilities"]

# Wrap your input elements in a container
with st.container():
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

    tag = "established_dt"
    established_dt = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

    tag = "type_dt"
    type_dt = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

    tag = "no_dt_reason"
    no_dt_reason = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

# Actions to take after the form is submitted
if st.button("Continue"):
    client: MongoClient = mongo_utils.init_connection()
    if client:
        data: dict[str, Any] = {
            "_id": st.session_state[USER_ID_STATE_KEY],
            "sector": sector,
            "location": location,
            "role": role,
            "primiary_responsibilities": ", ".join(
                primary_responsibilities
            ),  # Joining list into a string
            "established_dt": established_dt,
            "type_dt": type_dt,
            "no_dt_reason": ", ".join(no_dt_reason),
        }

        mongo_utils.add_survey_results(client, data)
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Community_Results")
