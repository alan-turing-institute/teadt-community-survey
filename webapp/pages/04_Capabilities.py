import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import mongo_utils
from pymongo import MongoClient
from config import USER_ID_STATE_KEY


st.title("Current Assurance Practices and Understanding ")
st.markdown(
    "This section explores your understanding and current practices around assurance of "
    "digital twins. "
)

# Initialize session state for showing additional content
if "show_def" not in st.session_state:
    st.session_state.show_def = False
if "show_def" not in st.session_state:
    st.session_state.show_def = False
if "continue_clicked" not in st.session_state:
    st.session_state.continue_clicked = False


# Disable the submit button after it is clicked
def disable():
    st.session_state.disabled = True


# Initialize disabled for form_submit_button to False
st.session_state.disabled = False

# Start with the first question in its own form
with st.form("question_1_form"):
    # Question 2.1
    assurance_meaning = st.text_area(
        "2.1 What do you understand assurance to mean in the context of developing & "
        "applying digital twinning technology?"
    )

    # Submit button for assurance definition
    submit_1 = st.form_submit_button(
        "Submit Definition", on_click=disable, disabled=st.session_state.disabled
    )
    if submit_1:
        st.session_state["submit_1"] = True  # Mark the form as submitted
        st.session_state.show_def = True

# If the response to the first question is submitted, show the rest of the content
if st.session_state.show_def:
    st.markdown(
        """
    :::info
    **Background & Definition of Assurance:** *Assurance involves communicating reasons"
    " and evidence that help people understand and evaluate the trustworthiness of a "
    "claim (or series of claims) about a system or technology.*
    :::
    """,
        unsafe_allow_html=True,
    )

    definition_open = st.radio(
        "Would you consider open documentation and justification of assurance "
        "activities "
        "to be an integral component of the assurance process in digital twinning "
        "technology?",
        [
            "Yes, and it was included in my initial definition of assurance.",
            "Yes, but I did not include it in my initial definition of assurance.",
            "No, I do not view it as an integral component.",
            "I don’t know",
        ],
        index=None,
    )

    if definition_open:
        if st.button("Continue"):
            st.session_state.continue_clicked = True

if st.session_state.continue_clicked:
    # Use a container for the rest of the questions to allow dynamic updates
    container = st.container()
    with container:
        st.subheader("Current Assurance Practices")
        # Question 2.2
        assurance_methods = st.multiselect(
            "2.3 Which of the following assurance methods do you currently implement "
            "(if any)?",
            [
                "Risk Assessment",
                "Impact Assessment",
                "Bias Audit",
                "Compliance Audit",
                "Conformity Assessment",
                "Formal Verification",
                "Model Cards",
                "None",
            ],
            help="Based on recommendations outlined in the DSIT Practitioner Guide to "
            "AI Assurance.",
        )

        if assurance_methods:
            # Question 2.4
            # Define your project lifecycle stages
            properties_assured = st.multiselect(
                "2.4 Which of the following properties (or goals) do you currently "
                "assure, with any of the mechanisms previously selected?",
                [
                    "Accuracy",
                    "Fairness",
                    "Privacy",
                    "Robustness",
                    "Transparency",
                    "Other",
                ],
            )

        # Question 2.5
        governance_requirements = st.multiselect(
            "2.5 What governance or legal requirements does your organization adhere to"
            "/reference for assurance in digital twin projects (e.g., ISO standards, "
            "GDPR)?",
            ["option 1", "option 2", "option 3"],
        )

    # Submit button for the rest of the survey
    if st.button("Submit & See Results"):
        client: MongoClient = mongo_utils.init_connection()
        if client:

            # Update the data dictionary to match the questions from this section
            data = {
                "_id": st.session_state[USER_ID_STATE_KEY],
                "assurance_meaning": assurance_meaning,
                "governance_requirements": ", ".join(governance_requirements),
                "assurance_methods": ", ".join(
                    assurance_methods
                ),  # Joining list into a string for multiselect
                "properties_assured": ", ".join(properties_assured),
            }
            # Assuming 'insert_survey_result' is a function you've defined to insert 
            # data into your database
            mongo_utils.add_survey_results(client, data)  # Update table name as needed
            st.success("Survey result saved successfully!")
        else:
            st.error("Could not connect to the database.")

        switch_page("Capabilities_Results")
