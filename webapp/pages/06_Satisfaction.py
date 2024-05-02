import streamlit as st
from streamlit_utils import (
    SurveyQuestion,
    load_from_session,
    verify_user,
    display_error_messages,
    check_required_fields,
)
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from survey_questions import questions
from config import (
    INTEGRATE_ASSURANCE_STATE_KEY,
    COMMUNICATION_IMPACT_STATE_KEY,
    LINK_ASSURANCE_ACTIVITIES_STATE_KEY,
    SATISFACTION_JUSTIFICATION_STATE_KEY,
    SATISFACTION_PAGE,
    GOALS_FRAMEWORK_PAGE,
    REQUIRED_MESSAGE,
)

SECTION_NUM = 3

verify_user(SATISFACTION_PAGE)
display_error_messages()

# Define the tags of questions to display in this section
tags_to_display = [
    INTEGRATE_ASSURANCE_STATE_KEY,
    COMMUNICATION_IMPACT_STATE_KEY,
    LINK_ASSURANCE_ACTIVITIES_STATE_KEY,
    SATISFACTION_JUSTIFICATION_STATE_KEY,
]
load_from_session(tags_to_display)

# Reintroduce sidebar (collapse button will stay hidden as CSS cannot be
#  dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")

st.title("Part 3: Satisfaction with Assurance Practices")
st.markdown(
    "This section assesses the community’s satisfaction levels with current"
    " assurance processes, "
    "infrastructure, and support resources."
)
st.markdown(REQUIRED_MESSAGE, unsafe_allow_html=True)

question_generator = SurveyQuestion()

# Generate Streamlit elements and assign responses to variables
responses = {}
for tag in tags_to_display:
    responses[tag] = question_generator.generate_streamlit_element(
        SECTION_NUM,
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

# Submit button for the form
submitted = st.button("Continue")

# Actions to take after the form is submitted
if st.button("Continue"):
    try:
        check_required_fields(tags_to_display)
        switch_page(GOALS_FRAMEWORK_PAGE)
    except ValueError as e:
        # Exception message is human-readable
        st.error(str(e))
