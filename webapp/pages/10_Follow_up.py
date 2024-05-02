import streamlit as st
from config import (
    ADDITIONAL_INSIGHTS_STATE_KEY,
    WORKSHOP_INTEREST_STATE_KEY,
    PROJECT_INTEREST_STATE_KEY,
    EMAIL_INTEREST_STATE_KEY,
    EMAIL_STATE_KEY,
    ALL_SESSION_KEYS,
    SURVEY_SUBMITTED_STATE_KEY,
    FOLLOW_UP_PAGE,
    ALL_REQUIRED_KEYS,
)
from streamlit_utils import (
    load_from_session,
    WIDGET_SUFFIX,
    store_in_session,
    verify_user,
    display_error_messages,
    check_required_fields,
)
import mongo_utils
from pymongo import MongoClient
from typing import Any

verify_user(FOLLOW_UP_PAGE)
display_error_messages()

page_element_keys: list[str] = [
    ADDITIONAL_INSIGHTS_STATE_KEY,
    WORKSHOP_INTEREST_STATE_KEY,
    PROJECT_INTEREST_STATE_KEY,
    EMAIL_INTEREST_STATE_KEY,
    EMAIL_STATE_KEY,
]

load_from_session(page_element_keys)

st.title("Follow-Up")
SECTION_NUM = 6

st.header(f"Section {SECTION_NUM}: Final Open-Ended Question")

# Open-ended question
st.subheader("1. Additional Insights")
additional_insights = st.text_area(
    "Is there anything else pertinent to the assurance of digital twins, "
    "which has not"
    " been covered, that you think is significant?",
    help="Your insights are valuable to us. Feel free to share any thoughts or"
    " experiences.",
    on_change=store_in_session,
    args=(ADDITIONAL_INSIGHTS_STATE_KEY,),
    key=f"{ADDITIONAL_INSIGHTS_STATE_KEY}_{WIDGET_SUFFIX}",
)

# Email input for follow-ups
st.subheader("Interested in Follow-Ups?")

# Checkbox for workshop interest
workshop_interest = st.checkbox(
    "I would like to join a more in-depth workshop to learn about assurance"
    " methodology"
    " & build my own assurance case under the guidance of experts.",
    on_change=store_in_session,
    args=(WORKSHOP_INTEREST_STATE_KEY,),
    key=f"{WORKSHOP_INTEREST_STATE_KEY}_{WIDGET_SUFFIX}",
)
project_interest = st.checkbox(
    "I would like to be kept up-to-date on the TEA-DT project and "
    "the outcomes of this survey.",
    on_change=store_in_session,
    args=(PROJECT_INTEREST_STATE_KEY,),
    key=f"{PROJECT_INTEREST_STATE_KEY}_{WIDGET_SUFFIX}",
)
email_interest = st.checkbox(
    "I would like to be emailed my responses to this form (or download below)",
    on_change=store_in_session,
    args=(EMAIL_INTEREST_STATE_KEY,),
    key=f"{EMAIL_INTEREST_STATE_KEY}_{WIDGET_SUFFIX}",
)

email = st.text_input(
    "Enter your email:",
    on_change=store_in_session,
    args=(EMAIL_STATE_KEY,),
    key=f"{EMAIL_STATE_KEY}_{WIDGET_SUFFIX}",
)
st.markdown("*We'll only use your email to contact you regarding follow-ups.*")

if st.button("Submit"):
    try:
        check_required_fields(ALL_REQUIRED_KEYS)

        client: MongoClient = mongo_utils.init_connection()
        if client:
            data: dict[str, Any] = {
                session_key: st.session_state[session_key]
                for session_key in ALL_SESSION_KEYS
                if session_key in st.session_state
            }

        mongo_utils.add_survey_results(client, data)
        st.session_state[SURVEY_SUBMITTED_STATE_KEY] = True

    except ValueError as e:
        # Exception message is human-readable
        st.error(str(e))

verify_user(FOLLOW_UP_PAGE)
