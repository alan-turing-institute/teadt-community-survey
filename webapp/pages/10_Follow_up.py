import streamlit as st
from email_validator import validate_email, EmailNotValidError
from config import (
    ADDITIONAL_INSIGHTS_STATE_KEY,
    WORKSHOP_INTEREST_STATE_KEY,
    PROJECT_INTEREST_STATE_KEY,
    EMAIL_INTEREST_STATE_KEY,
    EMAIL_STATE_KEY,
    ALL_SESSION_KEYS,
)
from utils import load_from_session, WIDGET_SUFFIX, store_in_session
import mongo_utils
from pymongo import MongoClient
from typing import Any

page_element_keys: list[str] = [
    ADDITIONAL_INSIGHTS_STATE_KEY,
    WORKSHOP_INTEREST_STATE_KEY,
    PROJECT_INTEREST_STATE_KEY,
    EMAIL_INTEREST_STATE_KEY,
    EMAIL_STATE_KEY,
]

load_from_session(page_element_keys)

st.title("Follow-Up")

st.header("Section 5: Final Open-Ended Question")

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
        # Validate.
        valid = validate_email(email)
        # Update with the normalized form.
        email = valid.email
        st.success("Valid email address.")

        client: MongoClient = mongo_utils.init_connection()
        if client:
            data: dict[str, Any] = {
                session_key: st.session_state[session_key]
                for session_key in ALL_SESSION_KEYS
                if session_key in st.session_state
            }

        mongo_utils.add_survey_results(client, data)
        st.success("Survey result saved successfully!")
    except EmailNotValidError as e:
        # Email is not valid, exception message is human-readable
        st.error(str(e))
