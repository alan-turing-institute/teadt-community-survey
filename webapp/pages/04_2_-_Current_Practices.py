import streamlit as st
from st_pages import hide_pages
from streamlit_extras.switch_page_button import switch_page
from streamlit_utils import (
    QuestionGenerator,
    disable_button,
    load_from_session,
    verify_user,
    display_error_messages,
    check_required_fields,
)
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
    CURRENT_PRACTICES_PAGE,
    CURRENT_PRACTICES_RESULTS_PAGE,
    REQUIRED_MESSAGE,
)

verify_user(CURRENT_PRACTICES_PAGE)
display_error_messages()

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

SECTION_NUM = 2


load_from_session(page_element_keys)
hide_pages(["Success"])

st.title("Current Assurance Practices and Understanding ")
st.warning(
    "This section explores your understanding and current practices around "
    "assurance of "
    "digital twins. "
)
st.markdown(REQUIRED_MESSAGE, unsafe_allow_html=True)


# Initialize session state for showing additional content / disabling buttons
if "disabled" not in st.session_state:
    st.session_state.disabled = False
if "show_def" not in st.session_state:
    st.session_state.show_def = False
if "continue_clicked" not in st.session_state:
    st.session_state.continue_clicked = False

# Question 2.1
question_generator = QuestionGenerator(SECTION_NUM)

assurance_meaning = question_generator.generate_streamlit_element(
    questions["assurance_meaning"]["question"],
    questions["assurance_meaning"]["type"],
    key=ASSURANCE_MEANING_STATE_KEY,
)

# Submit button for assurance definition
submit_definition_clicked = st.button(
    "Submit",
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
    **For the purpose of this survey we will assume the following definition:**
    """,
        help="This definition follows the Department of Science, Innovation, "
        'and Technology\'s "Introduction to AI Assurance"',
    )
    st.info(
        """
    Assurance is the process of measuring, evaluating and communicating
    something about a system or product (e.g. a digital twin).

    This can include a range of activities such as conducting a system audit,
    validating a dataset, carrying out training around ethical practices or
    achieving certified compliance with a specific standard.
    """
    )

    if st.button("Proceed"):
        st.session_state.continue_clicked = True

if st.session_state.continue_clicked:
    # Use a container for the rest of the questions to allow dynamic updates
    container = st.container()
    with container:
        st.subheader("Current Assurance Practices")
        # Generate Streamlit elements for the rest of the questions
        assurance_mechanisms = question_generator.generate_streamlit_element(
            questions["assurance_mechanisms"]["question"],
            questions["assurance_mechanisms"]["type"],
            options=questions["assurance_mechanisms"].get("options"),
            key=ASSURANCE_MECHANISMS_STATE_KEY,
        )

        if "Other (Please specify)" in assurance_mechanisms:
            tag = ASSURANCE_MECHANISM_OTHER_STATE_KEY
            assurance_mechanism_other = (
                question_generator.generate_streamlit_element(
                    questions[tag]["question"],
                    questions[tag]["type"],
                    key=ASSURANCE_MECHANISM_OTHER_STATE_KEY,
                )
            )

        assured_properties = question_generator.generate_streamlit_element(
            questions["assured_properties"]["question"],
            questions["assured_properties"]["type"],
            options=questions["assured_properties"].get("options"),
            key=ASSURED_PROPERTIES_STATE_KEY,
        )

        if "Other (Please specify)" in assured_properties:
            tag = ASSURED_PROPERTIES_OTHER_STATE_KEY
            assured_properties_other = (
                question_generator.generate_streamlit_element(
                    questions[tag]["question"],
                    questions[tag]["type"],
                    key=ASSURED_PROPERTIES_OTHER_STATE_KEY,
                )
            )

        st.subheader("Assurance for Connected Digital Twins")
        asset_data_sharing = question_generator.generate_streamlit_element(
            questions["asset_data_sharing"]["question"],
            questions["asset_data_sharing"]["type"],
            options=questions["asset_data_sharing"].get("options"),
            key=ASSET_DATA_SHARING_STATE_KEY,
            help="""
            In the context of digital twins, **asset-related data**
             refers to the digital representation of information
             pertaining to the characteristics, status,
             and usage of physical assets in real-time.
            """,
        )

        if asset_data_sharing == "Yes":
            partner_trust_difficulty = (
                question_generator.generate_streamlit_element(
                    questions["partner_trust_difficulty"]["question"],
                    questions["partner_trust_difficulty"]["type"],
                    options=questions["partner_trust_difficulty"].get(
                        "options"
                    ),
                    key=PARTNER_TRUST_DIFFICULTY_STATE_KEY,
                )
            )

            partner_trust_challenges = (
                question_generator.generate_streamlit_element(
                    questions["partner_trust_challenges"]["question"],
                    questions["partner_trust_challenges"]["type"],
                    options=questions["partner_trust_challenges"].get(
                        "options"
                    ),
                    key=PARTNER_TRUST_CHALLENGES_STATE_KEY,
                )
            )

            reliance_on_evidence = (
                question_generator.generate_streamlit_element(
                    questions["reliance_on_evidence"]["question"],
                    questions["reliance_on_evidence"]["type"],
                    options=questions["reliance_on_evidence"].get("options"),
                    key=RELIANCE_ON_EVIDENCE_STATE_KEY,
                )
            )

    # Submit button for the rest of the survey
    if st.button("Continue"):
        try:
            check_required_fields(page_element_keys, give_hint=True)
            switch_page(CURRENT_PRACTICES_RESULTS_PAGE)
        except ValueError as e:
            # Exception message is human-readable
            st.error(str(e))
