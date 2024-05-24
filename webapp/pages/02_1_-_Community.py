import streamlit as st
from st_pages import hide_pages
from datetime import datetime

from streamlit_utils import (
    verify_user,
    check_required_fields,
    QuestionGenerator,
)
from streamlit_extras.switch_page_button import switch_page
from survey_questions import questions
from config import (
    START_TIMESTAMP_STATE_KEY,
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    TYPE_DT_OTHER_STATE_KEY,
    PURPOSE_DT_STATE_KEY,
    PURPOSE_DT_OTHER_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
    COMMUNITY_PAGE,
    COMMUNITY_RESULTS_PAGE,
    REQUIRED_MESSAGE,
)
from streamlit_utils import load_from_session, display_error_messages
import logging

logging.info("Loading the community page")

page_element_keys: list[str] = [
    SECTOR_STATE_KEY,
    LOCATION_STATE_KEY,
    ROLE_STATE_KEY,
    RESPONSIBILITIES_STATE_KEY,
    ESTABLISHED_DT_STATE_KEY,
    TYPE_DT_STATE_KEY,
    TYPE_DT_OTHER_STATE_KEY,
    PURPOSE_DT_STATE_KEY,
    PURPOSE_DT_OTHER_STATE_KEY,
    NO_DT_REASON_STATE_KEY,
]

SECTION_NUM = 1

load_from_session(page_element_keys)

verify_user(COMMUNITY_PAGE)
display_error_messages()

# Record start time (to later compute total duration)
st.session_state[START_TIMESTAMP_STATE_KEY] = str(
    datetime.today().replace(microsecond=0))

# reintroduce sidebar (collapse button will stay hidden as CSS cannot by
# dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")
hide_pages(["Success"])


st.title(f"Part {SECTION_NUM}: Community Composition")
st.warning(
    "Here we aim to understand the diverse backgrounds"
    " within the digital twin community."
)

st.markdown(REQUIRED_MESSAGE, unsafe_allow_html=True)

# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

question_generator = QuestionGenerator(SECTION_NUM)

# Define the tags of questions to display in this section
# Generate Streamlit elements and assign responses to variables
tag: str = SECTOR_STATE_KEY
sector = question_generator.generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = LOCATION_STATE_KEY
location = question_generator.generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)
tag = ROLE_STATE_KEY
role = question_generator.generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = RESPONSIBILITIES_STATE_KEY
primary_responsibilities = question_generator.generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = ESTABLISHED_DT_STATE_KEY
established_dt = question_generator.generate_streamlit_element(
    questions[tag]["question"],
    questions[tag]["type"],
    options=questions[tag].get("options"),
    key=tag,
)

tag = TYPE_DT_STATE_KEY
if (established_dt == "Yes") or (
    established_dt == "Indirectly "
    "(We support clients or provide components for digital twins)"
):
    type_dt = question_generator.generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )
    if "Other (Please specify)" in type_dt:
        tag = TYPE_DT_OTHER_STATE_KEY
        type_dt = question_generator.generate_streamlit_element(
            questions[tag]["question"],
            questions[tag]["type"],
            key=tag,
        )
    tag = PURPOSE_DT_STATE_KEY
    purpose_dt = question_generator.generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )
    if "Other (Please specify)" in purpose_dt:
        tag = PURPOSE_DT_OTHER_STATE_KEY
        purpose_dt = question_generator.generate_streamlit_element(
            questions[tag]["question"],
            questions[tag]["type"],
            key=tag,
        )

if established_dt == "No":
    tag = NO_DT_REASON_STATE_KEY
    no_dt_reason = question_generator.generate_streamlit_element(
        questions[tag]["question"],
        questions[tag]["type"],
        options=questions[tag].get("options"),
        key=tag,
    )

# Actions to take after the form is submitted
if st.button("Continue"):
    try:
        check_required_fields(page_element_keys, give_hint=True)
        switch_page(COMMUNITY_RESULTS_PAGE)
    except ValueError as e:
        # Exception message is human-readable
        st.error(str(e))
