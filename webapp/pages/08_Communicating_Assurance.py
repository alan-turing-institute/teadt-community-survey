import streamlit as st
from survey_questions import questions
from streamlit_extras.switch_page_button import switch_page  # type: ignore

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

# Begin a form for the survey inputs
with st.form("evidence_based_assurance_form"):
    # Display each question using the utility function to handle different
    # input types
    communication_methods = st.selectbox(
        questions["communication_methods"]["question"],
        options=questions["communication_methods"]["options"],
        key="communication_methods",
    )

    need_for_visual_tool = st.radio(
        questions["need_for_visual_tool"]["question"],
        options=questions["need_for_visual_tool"]["options"],
        key="need_for_visual_tool",
    )

    if need_for_visual_tool == "Yes":
        benefits_of_visual_tool = st.text_area(
            questions["benefits_of_visual_tool"]["question"],
            key="benefits_of_visual_tool",
        )

    if need_for_visual_tool == "No":
        reasons_against_visual_tool = st.text_area(
            questions["reasons_against_visual_tool"]["question"],
            key="reasons_against_visual_tool",
        )

    preparedness_for_argument = st.selectbox(
        questions["preparedness_for_argument"]["question"],
        options=questions["preparedness_for_argument"]["options"],
        key="preparedness_for_argument",
    )

    support_for_assurance = st.multiselect(
        questions["support_for_assurance"]["question"],
        options=questions["support_for_assurance"]["options"],
        key="support_for_assurance",
    )

    # Submit button for the form
    submitted = st.form_submit_button("Continue")

# Actions to take after the form is submitted, such as saving responses or
# navigating
if submitted:
    switch_page("Follow_up")
