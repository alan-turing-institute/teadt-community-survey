import streamlit as st
from utils import generate_streamlit_element
from streamlit_extras.switch_page_button import switch_page
from survey_questions import questions
from config import (
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
)
from utils import load_from_session
import logging

logging.info("Loading the community page")

page_element_keys: list[str] = [
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
]

load_from_session(page_element_keys)

# reintroduce sidebar (collapse button will stay hidden as CSS cannot by
# dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")


st.title("Part 1: Community Composition")
st.markdown(
    "Here we aim to understand the diverse backgrounds"
    "within the digital twin community."
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

# TODO(cptanalatriste): There's a bug when the user does not modify the
# default value.
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

tag = ESTABLISHED_DT_STATE_KEY
established_dt = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = TYPE_DT_STATE_KEY
type_dt = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = NO_DT_REASON_STATE_KEY
no_dt_reason = generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

# Actions to take after the form is submitted
if st.button("Continue"):
    switch_page("Community_Results")
