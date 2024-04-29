import streamlit as st
from survey_questions import questions
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from config import (
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
)
from utils import load_from_session, WIDGET_SUFFIX, store_in_session

page_element_keys: list[str] = [
    COMMUNICATION_METHODS_STATE_KEY,
    NEED_FOR_VISUAL_TOOL_STATE_KEY,
    BENEFITS_OF_VISUAL_TOOL_STATE_KEY,
    REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,
    PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,
    SUPPORT_FOR_ASSURANCE_STATE_KEY,
]
load_from_session(page_element_keys)

# Set the page configuration and title
st.set_page_config(page_title="Communicating Assurance", layout="wide")
st.title("Section 5: Communicating Assurance")

# Introduction to the section
st.markdown(
    """
Assurance of your digital twin involves more than just implementing the right"
" technologies and processes.
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

# Display each question using the utility function to handle different
# input types
communication_methods = st.selectbox(
    questions["communication_methods"]["question"],
    options=questions["communication_methods"]["options"],
    on_change=store_in_session,
    args=(COMMUNICATION_METHODS_STATE_KEY,),
    key=f"{COMMUNICATION_METHODS_STATE_KEY}_{WIDGET_SUFFIX}",
)

need_for_visual_tool = st.radio(
    questions["need_for_visual_tool"]["question"],
    options=questions["need_for_visual_tool"]["options"],
    on_change=store_in_session,
    args=(NEED_FOR_VISUAL_TOOL_STATE_KEY,),
    key=f"{NEED_FOR_VISUAL_TOOL_STATE_KEY}_{WIDGET_SUFFIX}",
)

if need_for_visual_tool == "Yes":
    benefits_of_visual_tool = st.text_area(
        questions["benefits_of_visual_tool"]["question"],
        on_change=store_in_session,
        args=(BENEFITS_OF_VISUAL_TOOL_STATE_KEY,),
        key=f"{BENEFITS_OF_VISUAL_TOOL_STATE_KEY}_{WIDGET_SUFFIX}",
    )

if need_for_visual_tool == "No":
    reasons_against_visual_tool = st.text_area(
        questions["reasons_against_visual_tool"]["question"],
        on_change=store_in_session,
        args=(REASONS_AGAINST_VISUAL_TOOL_STATE_KEY,),
        key=f"{REASONS_AGAINST_VISUAL_TOOL_STATE_KEY}_{WIDGET_SUFFIX}",
    )

preparedness_for_argument = st.selectbox(
    questions["preparedness_for_argument"]["question"],
    options=questions["preparedness_for_argument"]["options"],
    on_change=store_in_session,
    args=(PREPAREDNESS_FOR_ARGUMENT_STATE_KEY,),
    key=f"{PREPAREDNESS_FOR_ARGUMENT_STATE_KEY}_{WIDGET_SUFFIX}",
)

support_for_assurance = st.multiselect(
    questions["support_for_assurance"]["question"],
    options=questions["support_for_assurance"]["options"],
    on_change=store_in_session,
    args=(SUPPORT_FOR_ASSURANCE_STATE_KEY,),
    key=f"{SUPPORT_FOR_ASSURANCE_STATE_KEY}_{WIDGET_SUFFIX}",
)

# Submit button for the form
submitted = st.button("Continue")

# Actions to take after the form is submitted, such as saving responses or
# navigating
if submitted:
    switch_page("Follow_up")
