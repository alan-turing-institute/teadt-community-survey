import streamlit as st
from utils import generate_streamlit_element, disable_button, load_from_session
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from survey_questions import questions
from pymongo import MongoClient
import mongo_utils
from config import USER_ID_STATE_KEY
from typing import Any
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
    "ethical_framework_existence",
    "framework_description",
    "framework_development",
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
    "value_of_guiding_principles",
    "familiarity_with_gemini_principles",
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
    client: MongoClient = mongo_utils.init_connection()
    if client:
        data: dict[str, Any] = {"_id": st.session_state[USER_ID_STATE_KEY]}
        data.update({tag: responses[tag] for tag in tags_to_display})
        mongo_utils.add_survey_results(client, data)
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Communicating_Assurance")
