import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import mongo_utils
from pymongo import MongoClient
from config import USER_ID_STATE_KEY
from utils import generate_streamlit_element, disable_button, load_from_session
from survey_questions import questions
from config import (
    USER_ID_STATE_KEY,
    ASSURANCE_MEANING_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    PARTNER_TRUST_DIFFICULTY_STATE_KEY,
    PARTNER_TRUST_CHALLENGES_STATE_KEY,
    RELIANCE_ON_EVIDENCE_STATE_KEY,
)

page_element_keys: list[str] = [
    ASSURANCE_MEANING_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    PARTNER_TRUST_DIFFICULTY_STATE_KEY,
    PARTNER_TRUST_CHALLENGES_STATE_KEY,
    RELIANCE_ON_EVIDENCE_STATE_KEY,
]

load_from_session(page_element_keys)

st.title("Current Assurance Practices and Understanding ")
st.markdown(
    "This section explores your understanding and current practices around "
    "assurance of "
    "digital twins. "
)

# Initialize session state for showing additional content
if "show_def" not in st.session_state:
    st.session_state.show_def = False
if "continue_clicked" not in st.session_state:
    st.session_state.continue_clicked = False


# Initialize disabled for form_submit_button to False
st.session_state.disabled = False


# Question 2.1
assurance_meaning = generate_streamlit_element(
    questions["assurance_meaning"]["question"],
    questions["assurance_meaning"]["type"],
    key=ASSURANCE_MEANING_STATE_KEY,
)

# Submit button for assurance definition
submit_definition_clicked = st.button(
    "Submit Definition",
    on_click=disable_button,
    disabled=st.session_state.disabled,
)
if submit_definition_clicked:
    st.session_state["submit_1"] = True  # Mark the form as submitted
    st.session_state.show_def = True

# If the response to the first question is submitted, show the rest of the
# content
if st.session_state.show_def:
    st.markdown(
        """
    :::info
    **Background & Definition of Assurance:**
    *Assurance is the process of measuring, evaluating and communicating
    something about a system or product (e.g. a digital twin).
    (Following the definition of the Department of Science, Innovation, and
    Technology's "Introduction to AI Assurance")
    This can include a range of activities such as conducting a system audit,
    validating a dataset, carrying out training around ethical practices or
    achieving certified compliance with a specific standard.*
    :::
    """,
        unsafe_allow_html=True,
    )

    if st.button("Continue"):
        st.session_state.continue_clicked = True

if st.session_state.continue_clicked:
    # Use a container for the rest of the questions to allow dynamic updates
    container = st.container()
    with container:
        st.subheader("Current Assurance Practices")
        # Generate Streamlit elements for the rest of the questions
        for tag in page_element_keys:
            if tag != ASSURANCE_MEANING_STATE_KEY:
                _ = generate_streamlit_element(
                    questions[tag]["question"],
                    questions[tag]["type"],
                    options=questions[tag].get("options"),
                    key=tag,
                )

    # Submit button for the rest of the survey
    if st.button("Submit & See Results"):
        client: MongoClient = mongo_utils.init_connection()
        if client:

            # Update the data dictionary to match the questions from this
            # section
            data = {
                USER_ID_STATE_KEY: st.session_state[USER_ID_STATE_KEY],
                ASSURANCE_MEANING_STATE_KEY: assurance_meaning,
                # TODO(cptanalatriste): Persistence is broken here. Fix later!
                # "governance_requirements": ", ".join(
                #     st.session_state["governance_requirements"]
                # ),
                # "assurance_methods": ", ".join(
                #     st.session_state["assurance_methods"]
                # ),
                # "properties_assured": ", ".join(
                #     st.session_state["properties_assured"]
                # ),
            }
            # Assuming 'insert_survey_result' is a function you've defined to
            # insert
            # data into your database
            mongo_utils.add_survey_results(
                client, data
            )  # Update table name as needed
            st.success("Survey result saved successfully!")
        else:
            st.error("Could not connect to the database.")

        # TODO(saranas): Please check if this page transition logic is right.
        switch_page("Current_Practices_Results")
