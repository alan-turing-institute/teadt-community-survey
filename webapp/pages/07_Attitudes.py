import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from pymongo import MongoClient
import mongo_utils
from config import USER_ID_STATE_KEY


def format_label_agree(value):
    labels = {
        1: "Strongly Disagree",
        2: "Disagree",
        3: "Neutral",
        4: "Agree",
        5: "Strongly Agree",
    }
    return labels.get(value, "")


def format_label_satisfied(value):
    labels = {
        1: "Very unsatisfied",
        2: "Somewhat unsatisfied",
        3: "Neutral",
        4: "Somewhat satisfied",
        5: "Very satisfied",
    }
    return labels.get(value, "")


st.title("Satisfaction with assurance practices ")
st.markdown(
    "Here we want to assess the community’s satisfaction levels with current assurance "
    "processes, infrastructure and support resources "
)

st.markdown("To what extent do you agree with the following statements")
agree_integration = st.slider(
    "Our assurance activities extend beyond mere checklist compliance and are "
    "substantively integrated into our operational practices",
    1,
    5,
    key="agree1",
)
agree_communicate = st.slider(
    "The way we communicate our assurance activities significantly contributes to "
    "building and maintaining trust and confidence among our stakeholders.",
    1,
    5,
    key="agree2",
)
agree_linking = st.slider(
    "We can clearly link specific assurance activities directly to higher-level "
    "principles guiding our system's trustworthiness and ethical standards.",
    1,
    5,
    key="agree3",
)

lifecycle_stages = st.multiselect(
    "4.2. At which stages in the project lifecycle are you implementing assurance?",
    [
        "Project planning",
        "Problem formulation",
        "Data extraction & procurement",
        "Data analysis",
        "Preprocessing & feature engineering",
        "Model selection & training",
        "Model testing & validation",
        "Model reporting",
        "System implementation",
        "User training",
        "System use & monitoring",
        "Model updating & deprovisioning",
        "all of the above",
    ],
)

satisfaction_docs = st.slider(
    "4.3. How satisfied are you currently with justification and documentation around "
    "your assurance process?",
    1,
    5,
    key="satisfied",
)

# Actions to take after the form is submitted
if st.button("Submit & See Results"):
    client: MongoClient = mongo_utils.init_connection()
    if client:

        # Update the data dictionary to match the questions from the "Attitudes and
        #  Perceptions" section
        data = {
            "_id": st.session_state[USER_ID_STATE_KEY],
            "agree_integration": agree_integration,
            "agree_communicate": agree_communicate,
            "agree_linking": agree_linking,
            "lifecycle_stages": ",".join(lifecycle_stages),
            "satisfaction_docs": satisfaction_docs,
        }
        mongo_utils.add_survey_results(client, data)
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Follow_up")
