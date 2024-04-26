import streamlit as st
from utils import generate_streamlit_element
from streamlit_extras.switch_page_button import switch_page
from survey_questions import questions
from pymongo import MongoClient
import mongo_utils
from config import (
    USER_ID_STATE_KEY,
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
)
from typing import Any
from utils import load_from_session, disable_button
import logging

logging.info("Loading the community page")

page_element_keys: list[str] = [
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
]

load_from_session(page_element_keys)

# reintroduce sidebar (collapse button will stay hidden as CSS cannot by
# dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")


st.title("Part 1: Community Composition")
st.markdown(
    "This section explores your understanding and current practices around "
    "assurance "
    "of digital twins."
)

# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define the tags of questions to display in this section
tags_to_display = ["sector", "location", "role", "primary_responsibilities"]

# Generate Streamlit elements and assign responses to variables
tag: str = SECTOR_STATE_KEY
sector = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = LOCATION_STATE_KEY
location = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)
tag = ROLE_STATE_KEY
role = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = RESPONSIBILITIES_STATE_KEY
primary_responsibilities = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

# Submit button for the form
submitted = st.button(
    "Submit", on_click=disable_button, disabled=st.session_state.disabled
)


if submitted:
    st.session_state["submitted"] = True  # Mark the form as submitted

    # Actions to take after the form is submitted
    client: MongoClient = mongo_utils.init_connection()
    if client:
        page_responses: dict[str, Any] = {
            USER_ID_STATE_KEY: st.session_state[USER_ID_STATE_KEY],
            SECTOR_STATE_KEY: sector,
            LOCATION_STATE_KEY: location,
            ROLE_STATE_KEY: role,
            RESPONSIBILITIES_STATE_KEY: ", ".join(
                primary_responsibilities
            ),  # Joining list into a string
        }

        mongo_utils.add_survey_results(client, page_responses)
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Community_Results")
