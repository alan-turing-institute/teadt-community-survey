import streamlit as st
from survey_questions import questions
from streamlit_utils import (
    QuestionGenerator,
    load_from_session,
    verify_user,
    display_error_messages,
    check_required_fields,
)
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from PIL import Image
from config import (
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY,
    COMMUNICATING_ASSURANCE_PAGE,
    FOLLOW_UP_PAGE,
    REQUIRED_MESSAGE,
)

verify_user(COMMUNICATING_ASSURANCE_PAGE)
display_error_messages()


page_element_keys: list[str] = [
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY,
]
load_from_session(page_element_keys)

SECTION_NUM = 5
# Set the page configuration and title
st.set_page_config(page_title="Communicating Assurance", layout="wide")
st.title(f"Section {SECTION_NUM}: Communicating Assurance")

# Introduction to the section
st.markdown(
    """
Assurance of your digital twin involves more than just implementing the right
 technologies and processes.
It also requires demonstrating to all stakeholders that your actions
are backed by evidence and clearly support broader goals of trustworthiness
and ethics.
This is especially relevant in the context of connected digital twins,
when data is shared across multiple organizations.
This section of our survey assesses your capabilities and potential needs
for demonstrating and communicating your project's assurance strategies
effectively to both internal teams and external partners.
"""
)
st.markdown(REQUIRED_MESSAGE, unsafe_allow_html=True)

question_generator = QuestionGenerator(SECTION_NUM)

# Display each question using the utility function to handle different
# input types
communication_methods = question_generator.generate_streamlit_element(
    questions["communication_methods"]["question"],
    questions["communication_methods"]["type"],
    options=questions["communication_methods"].get("options"),
    key=COMMUNICATION_METHODS_STATE_KEY,
)

st.write("#")
st.subheader("A New Responsible Research And Innovation Tool")

st.markdown(
    """One way to present a structured argument that clearly shows
how your assurance measures meet ethical goals is to use graph notation
to create a visual map. This visual approach simplifies complex information
and standardizes assurance communication, allowing stakeholders to see the
direct connections between actions and outcomes.
"""
)

# Display an image
image_path = Image.open("img/aba_example_case.png")
st.image(image_path, width=600)

need_for_visual_tool = question_generator.generate_streamlit_element(
    questions["need_for_visual_tool"]["question"],
    questions["need_for_visual_tool"]["type"],
    options=questions["need_for_visual_tool"].get("options"),
    key=NEED_FOR_VISUAL_TOOL_STATE_KEY,
)

if need_for_visual_tool == "Yes":
    benefits_of_visual_tool = question_generator.generate_streamlit_element(
        questions["benefits_of_visual_tool"]["question"],
        questions["benefits_of_visual_tool"]["type"],
        options=questions["benefits_of_visual_tool"].get("options"),
        key=BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    )

if need_for_visual_tool == "No":
    reasons_against_visual_tool = (
        question_generator.generate_streamlit_element(
            questions["reasons_against_visual_tool"]["question"],
            questions["reasons_against_visual_tool"]["type"],
            options=questions["reasons_against_visual_tool"].get("options"),
            key=REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
        )
    )

preparedness_for_argument = question_generator.generate_streamlit_element(
    questions["preparedness_for_argument"]["question"],
    questions["preparedness_for_argument"]["type"],
    options=questions["preparedness_for_argument"].get("options"),
    key=PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
)

support_for_assurance = question_generator.generate_streamlit_element(
    questions["support_for_assurance"]["question"],
    questions["support_for_assurance"]["type"],
    options=questions["support_for_assurance"].get("options"),
    key=SUPPORT_FOR_ASSURANCE_STATE_KEY,
)

if "Other (Please specify)" in support_for_assurance:
    tag = SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY
    support_for_assurance_other = (
        question_generator.generate_streamlit_element(
            questions[tag]["question"],
            questions[tag]["type"],
            options=questions[tag].get("options"),
            key=SUPPORT_FOR_ASSURANCE_OTHER_STATE_KEY,
        )
    )

# Actions to take after the form is submitted, such as saving responses or
# navigating
if st.button("Continue"):
    try:
        check_required_fields(page_element_keys, give_hint=True)
        switch_page(FOLLOW_UP_PAGE)
    except ValueError as e:
        # Exception message is human-readable
        st.error(str(e))
