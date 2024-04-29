import streamlit as st
from utils import generate_streamlit_element, load_from_session
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from survey_questions import questions
from config import (
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
)
from PIL import Image

# Set page configuration and sidebar state
st.set_page_config(initial_sidebar_state="expanded")

st.title("Section 4: High-Level Assurance Goals and Ethical Frameworks")
st.markdown(
    """
This section dives deeper into the frameworks and principles guiding the"
" ethical and trustworthy development of digital twins.
"""
)

# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define tags for the questions to be displayed
tags_to_display: list[str] = [
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
]
load_from_session(tags_to_display)

with st.container():
    responses = {}
    for tag in tags_to_display:
        responses[tag] = generate_streamlit_element(
            questions[tag]["question"],
            questions[tag]["type"],
            options=questions[tag].get("options"),
            key=tag,
        )

# Display an image
image_path = Image.open("webapp/img/gemini_principles.png")
st.image(image_path, caption="Illustration of Digital Twin Ethical Frameworks")

# Define tags for the questions to be displayed
tags_to_display = [
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
]
load_from_session(tags_to_display)

for tag in tags_to_display:
    responses[tag] = generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

# Actions to take after the form is submitted
if st.button("Continue"):
    switch_page("Communicating_Assurance")
