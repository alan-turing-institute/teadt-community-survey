import streamlit as st
from streamlit_extras.switch_page_button import switch_page  # type: ignore
import mongo_utils
from pymongo import MongoClient
from config import USER_ID_STATE_KEY

st.title("Assurance and Ethics Capabilities")
st.markdown(
    "Diving deeper into the frameworks and principles guiding the ethical and "
    "trustworthy development of digital twins "
)


# Define the label functions for each slider
def format_label_3_1(value):
    labels = {
        1: "Not valuable at all",
        2: "Slightly valuable",
        3: "Moderately valuable",
        4: "Very valuable",
        5: "Extremely valuable",
    }
    return labels.get(value, "")


def format_label_3_2(value):
    labels = {
        1: "Not important at all",
        2: "Slightly important",
        3: "Moderately important",
        4: "Very important",
        5: "Extremely important",
    }
    return labels.get(value, "")


def format_label_3_3(value):
    labels = {
        1: "Not difficult at all",
        2: "Slightly difficult",
        3: "Moderately difficult",
        4: "Very difficult",
        5: "Extremely difficult",
    }
    return labels.get(value, "")


def format_label_3_4(value):
    labels = {
        1: "Very unsatisfied",
        2: "Somewhat unsatisfied",
        3: "Neutral",
        4: "Somewhat satisfied",
        5: "Very satisfied",
    }
    return labels.get(value, "")


st.title("Assurance Goals & Frameworks")
st.markdown(
    "Diving deeper into the frameworks and principles guiding the ethical and "
    "trustworthy development of digital twins "
)

container = st.container()
with container:
    st.subheader("Current Assurance Practices")
    # Question 3.1
    ethics_framework = st.radio(
        "3.1 Does your organisation have an established definition or framework for "
        "'trustworthy' and 'ethical' digital twins?",
        ["Yes", "No", "I don't know"],
        index=None,
    )

    if ethics_framework == "Yes":
        ethics_definition = st.text_area(
            "3.1b If yes, please describe your organisation's definition or framework"
            " for 'trustworthy' digital twins."
        )

        framework_development = st.radio(
            "3.1c How was this definition or framework developed?",
            [
                "Consensus-based process (e.g. collaborative efforts of industry "
                "consortia)",
                "Internal governance process",
                "Developed by an external consultant",
                "Reused existing framework",
                "Adapted existing framework",
            ],
            index=None,
        )

        framework_url = st.text_area(
            "3.1d If your framework is publicly available, please provide a link."
        )

# Question 3.2
value_ethical_principles = st.slider(
    "3.2 How valuable do you find ethical principles in general, such as the "
    "Gemini principles?",
    1,
    5,
    key="3_1",
)

# Question 3.2b
if value_ethical_principles < 3:
    value_low_explain = st.text_area(
        "Please explain why you currently rate the value of guiding principles as low?"
    )


st.subheader("The Gemini Principles")
# [TODO] Insert picture of Gemini Principles

# [TODO next two questions should be per principle]
# Question 3.3
importance_gemini_principles = st.slider(
    "Considering your own digital twin product, please rate the importance of "
    "the Gemini principles in assuring its trustworthiness and ethical use.",
    1,
    5,
    key="3_2",
)

# Question 3.4
st.subheader("3.3 Operationalizing Principles Difficulty")
difficulty_operationalizing = st.slider(
    "Please rate how difficult you find it to operationalize the following principle"
    " within your digital twin product.",
    1,
    5,
    key="3_3",
)

# Question 3.5
main_challenges = st.text_area(
    "For those rated very difficult or extremely difficult to operationalize, "
    "what are the main challenges you face?"
)


# Submit button for the rest of the survey
if st.button("Submit & See Results"):
    client: MongoClient = mongo_utils.init_connection()
    if client:

        # Update the data dictionary to match the questions from this section
        data = {
            "_id": st.session_state[USER_ID_STATE_KEY],
            "ethics_framework": ethics_framework,
            "ethics_definition": (
                ethics_definition if ethics_framework == "Yes" else None
            ),  # Conditional based on ethics_framework response
            "framework_development": (
                framework_development if ethics_framework == "Yes" else None
            ),  # Conditional based on ethics_framework response
        }
        # Assuming 'insert_survey_result' is a function you've defined to insert data
        # into your database
        mongo_utils.add_survey_results(client, data)  # Update table name as needed
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Attitudes")
