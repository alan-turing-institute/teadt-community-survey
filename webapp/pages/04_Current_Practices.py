import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from utils import generate_streamlit_element, disable_button, load_from_session
from survey_questions import questions
from config import (
    ASSURANCE_MEANING_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURANCE_MECHANISM_OTHER_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    ASSURED_PROPERTIES_OTHER_STATE_KEY,
    ASSET_DATA_SHARING_STATE_KEY,
    PARTNER_TRUST_DIFFICULTY_STATE_KEY,
    PARTNER_TRUST_CHALLENGES_STATE_KEY,
    RELIANCE_ON_EVIDENCE_STATE_KEY,
)

page_element_keys: list[str] = [
    ASSURANCE_MEANING_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURANCE_MECHANISM_OTHER_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
    ASSURED_PROPERTIES_OTHER_STATE_KEY,
    ASSET_DATA_SHARING_STATE_KEY,
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

# Initialize session state for showing additional content / disabling buttons
if "disabled" not in st.session_state:
    st.session_state.disabled = False
if "show_def" not in st.session_state:
    st.session_state.show_def = False
if "continue_clicked" not in st.session_state:
    st.session_state.continue_clicked = False

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

# Disable the button after it's clicked once
if submit_definition_clicked:
    st.session_state.disabled = True

if submit_definition_clicked:
    st.session_state["submit_1"] = True
    st.session_state.show_def = True

# If the response to the first question is submitted, show the rest
if st.session_state.show_def:
    st.markdown(
        """
    :::info
    **Background & Definition of Assurance:**
    :::
    """,
        unsafe_allow_html=True,
        help="This definition follows the Department of Science, Innovation, "
        'and Technology\'s "Introduction to AI Assurance"',
    )
    st.markdown(
        """
    :::info
    Assurance is the process of measuring, evaluating and communicating
    something about a system or product (e.g. a digital twin).
    
    This can include a range of activities such as conducting a system audit,
    validating a dataset, carrying out training around ethical practices or
    achieving certified compliance with a specific standard.
    :::
    """,
        unsafe_allow_html=True,
    )

    if st.button("Understood"):
        st.session_state.continue_clicked = True

if st.session_state.continue_clicked:
    # Use a container for the rest of the questions to allow dynamic updates
    container = st.container()
    with container:
        st.subheader("Current Assurance Practices")
        # Generate Streamlit elements for the rest of the questions
        assurance_mechanisms = generate_streamlit_element(
            questions["assurance_mechanisms"]["question"],
            questions["assurance_mechanisms"]["type"],
            options=questions["assurance_mechanisms"].get("options"),
            key=ASSURANCE_MECHANISMS_STATE_KEY,
        )

        if "Other (Please specify)" in assurance_mechanisms:
            tag = ASSURANCE_MECHANISM_OTHER_STATE_KEY
            assurance_mechanism_other = st.text_area("Please specify")

        assured_properties = generate_streamlit_element(
            questions["assured_properties"]["question"],
            questions["assured_properties"]["type"],
            options=questions["assured_properties"].get("options"),
            key=ASSURED_PROPERTIES_STATE_KEY,
        )

        if "Other (Please specify)" in assured_properties:
            tag = ASSURED_PROPERTIES_OTHER_STATE_KEY
            assured_properties_other = st.text_area("Please specify")

        st.subheader("Assurance for Connected Digital Twins")
        asset_data_sharing = generate_streamlit_element(
            questions["asset_data_sharing"]["question"],
            questions["asset_data_sharing"]["type"],
            options=questions["asset_data_sharing"].get("options"),
            key=ASSET_DATA_SHARING_STATE_KEY,
        )

        if asset_data_sharing == "Yes":
            partner_trust_difficulty = generate_streamlit_element(
                questions["partner_trust_difficulty"]["question"],
                questions["partner_trust_difficulty"]["type"],
                options=questions["partner_trust_difficulty"].get("options"),
                key=PARTNER_TRUST_DIFFICULTY_STATE_KEY,
            )

            partner_trust_challenges = generate_streamlit_element(
                questions["partner_trust_challenges"]["question"],
                questions["partner_trust_challenges"]["type"],
                options=questions["partner_trust_challenges"].get("options"),
                key=PARTNER_TRUST_CHALLENGES_STATE_KEY,
            )

            reliance_on_evidence = generate_streamlit_element(
                questions["reliance_on_evidence"]["question"],
                questions["reliance_on_evidence"]["type"],
                options=questions["reliance_on_evidence"].get("options"),
                key=RELIANCE_ON_EVIDENCE_STATE_KEY,
            )

    # Submit button for the rest of the survey
    if st.button("Continue"):
        switch_page("Current_Practices_Results")
