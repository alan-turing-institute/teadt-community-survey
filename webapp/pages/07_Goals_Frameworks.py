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
 ethical and trustworthy development of digital twins.
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
    ethical_framework_existence = generate_streamlit_element(
            questions["ethical_framework_existence"]["question"],
            questions["ethical_framework_existence"]["type"],
            options=questions["ethical_framework_existence"].get("options"),
            key=ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
        )
    
    if ethical_framework_existence == 'Yes' or ethical_framework_existence.startswith('No, but'):
        framework_description = generate_streamlit_element(
            questions["framework_description"]["question"],
            questions["framework_description"]["type"],
            options=questions["framework_description"].get("options"),
            key=FRAMEWORK_DESCRIPTION_STATE_KEY,
        )

        framework_development = generate_streamlit_element(
            questions["framework_development"]["question"],
            questions["framework_development"]["type"],
            options=questions["framework_development"].get("options"),
            key=FRAMEWORK_DEVELOPMENT_STATE_KEY,
        )
st.write("#")
with st.container():
    st.subheader("Assurance for Connected Digital Twins")
    # Display an image
    image_path = Image.open("webapp/img/gemini_principles.png")
    st.image(image_path, caption="Illustration of Digital Twin Ethical Frameworks")

    # Define tags for the questions to be displayed
    tags_to_display = [
        VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
        FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
    ]
    load_from_session(tags_to_display)

    value_of_guiding_principles = generate_streamlit_element(
            questions["value_of_guiding_principles"]["question"],
            questions["value_of_guiding_principles"]["type"],
            options=questions["value_of_guiding_principles"].get("options"),
            key=VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
        )

    familiarity_with_gemini_principles = generate_streamlit_element(
            questions["familiarity_with_gemini_principles"]["question"],
            questions["familiarity_with_gemini_principles"]["type"],
            options=questions["familiarity_with_gemini_principles"].get("options"),
            key=FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
        )
# Actions to take after the form is submitted
if st.button("Continue"):
    switch_page("Communicating_Assurance")
