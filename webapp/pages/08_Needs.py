import streamlit as st
from streamlit_sortables import sort_items
from streamlit_extras.switch_page_button import switch_page
import mongo_utils
from pymongo import MongoClient
from config import USER_ID_STATE_KEY


st.header("Section 4: Needs and Challenges")

st.header("Section 4: Needs and Challenges")

# Question 4.1
st.subheader("4.1 Biggest Challenges")
biggest_challenges = st.multiselect(
    "What are the biggest challenges you face when trying to assure digital twins for "
    "adherence to trustworthy and ethical principles?",
    [
        "Lack of resources",
        "Lack of skills",
        "Lack of awareness of available assurance techniques",
        "Lack of guidance on which techniques to apply to a given use-case",
        "Lack of guidance on how to apply relevant existing techniques",
        "Lack of clearly signposted best practice in AI assurance",
        "Lack of regulatory clarity as to which techniques will be adequate to be "
        "regulatory compliant",
        "Lack of internal demand",
        "Lack of external demand",
        "Concern around international interoperability",
        "Lack of mechanisms (e.g., certification) for external recognition for using AI"
        "assurance techniques",
        "Other",
    ],
    key="4_1",
)
if "Other" in biggest_challenges:
    other_challenge = st.text_area(
        "Please explain the other biggest challenges:", key="4_1_other"
    )

# Question 4.2
st.subheader("4.2 Type of Support")
type_of_support = st.multiselect(
    "What type of support might help you implement digital twin assurance practices and"
    " operationalise to ethical principles?",
    [
        "Examples of effective digital twin assurance practices",
        "Toolkit of digital twin assurance methods and tools",
        "Guidance on selecting the right assurance practices for digital twins",
        "Guidance on applying technical standards to digital twin projects",
        "Learning and development resources on digital twin assurance",
        "Development of new assurance practices for digital twins",
        "Creation of more technical standards specific to digital twins",
        "Clearer understanding of regulatory expectations for digital twins",
        "Illustrations of the value added by digital twin assurance",
        "More certification programs focused on digital twin assurance",
    ],
    key="4_2",
)

# Follow-up for 4.2, only if more than one option is selected
if len(type_of_support) > 1:
    st.subheader(
        "4.2b Rank the Impact of Support Types from Top (High Impact) to Bottom "
        "(Low Impact)"
    )
    # Instructions for ranking
    st.write("Please drag and drop the selected options to rank them:")

    original_items = type_of_support
    sorted_items = sort_items(original_items)

# Question 4.3
st.subheader("4.3 Ethical Issues or Risks")
ethical_issues = st.text_area(
    "In your experience, what ethical issues or risks are unique or amplified in "
    "digital twin technology?",
    key="4_3",
)

# Submit button for the "Needs and Challenges" section
if st.button("Submit & See Results"):
    client: MongoClient = mongo_utils.init_connection()
    if client:

        # Update the data dictionary to match the questions from the "Needs and
        # Challenges" section
        data = {
            "_id": st.session_state[USER_ID_STATE_KEY],
            "biggest_challenges": ", ".join(
                biggest_challenges
            ),  # Joining list into a string for multiselect
            "type_of_support": ", ".join(
                type_of_support
            ),  # Joining list into a string for multiselect
            "sorted_support_types": (
                ", ".join(sorted_items) if type_of_support else None
            ),  # Conditional based on type_of_support response
            "ethical_issues": ethical_issues,
        }
        # Assuming 'insert_survey_result' is a function you've defined to insert data 
        # into your database
        mongo_utils.add_survey_results(client, data)  # Update table name as needed
        st.success("Survey result saved successfully!")
    else:
        st.error("Could not connect to the database.")

    switch_page("Attitudes")
