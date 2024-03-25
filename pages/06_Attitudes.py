import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from db_utils import create_connection, insert_survey_result, create_table, query_data

st.title("Attitudes and Perceptions")

st.header("Section 3: Attitudes and Perceptions")

# Define the label functions for each slider
def format_label_3_1(value):
    labels = {
        1: "Not valuable at all",
        2: "Slightly valuable",
        3: "Moderately valuable",
        4: "Very valuable",
        5: "Extremely valuable"
    }
    return labels.get(value, "")

def format_label_3_2(value):
    labels = {
        1: "Not important at all",
        2: "Slightly important",
        3: "Moderately important",
        4: "Very important",
        5: "Extremely important"
    }
    return labels.get(value, "")

def format_label_3_3(value):
    labels = {
        1: "Not difficult at all",
        2: "Slightly difficult",
        3: "Moderately difficult",
        4: "Very difficult",
        5: "Extremely difficult"
    }
    return labels.get(value, "")

def format_label_3_4(value):
    labels = {
        1: "Very unsatisfied",
        2: "Somewhat unsatisfied",
        3: "Neutral",
        4: "Somewhat satisfied",
        5: "Very satisfied"
    }
    return labels.get(value, "")

# Question 3.1
st.subheader("3.1 Ethical Principles Value")
value_ethical_principles = st.slider(
    "How valuable do you find ethical principles in general, such as the Gemini principles?",
    1, 5, format_func=format_label_3_1, key='3_1'
)

# Question 3.2
st.subheader("3.2 Importance of Gemini Principles")
importance_gemini_principles = st.slider(
    "Considering your own digital twin product, please rate the importance of the Gemini principles in assuring its trustworthiness and ethical use.",
    1, 5, format_func=format_label_3_2, key='3_2'
)

# Question 3.3
st.subheader("3.3 Operationalizing Principles Difficulty")
difficulty_operationalizing = st.slider(
    "Please rate how difficult you find it to operationalize the following principle within your digital twin product.",
    1, 5, format_func=format_label_3_3, key='3_3'
)

# Question 3.4
st.subheader("3.4 Satisfaction with Integration")
satisfaction_integration = st.slider(
    "How satisfied are you with the current level of integration between your assurance processes and the actual development lifecycle of your digital twins?",
    1, 5, format_func=format_label_3_4, key='3_4'
)

# Actions to take after the form is submitted
if st.button("Submit & See Results"):  
    conn = create_connection('survey_results.db')
    if conn:
        create_table(conn)

        # Update the data dictionary to match the questions from the "Attitudes and Perceptions" section
        data = {
            "value_ethical_principles": value_ethical_principles,
            "importance_gemini_principles": importance_gemini_principles,
            "difficulty_operationalizing": difficulty_operationalizing,
            "satisfaction_integration": satisfaction_integration
        }
        insert_survey_result(conn, "assurance_survey", data)
        st.success("Survey result saved successfully!")
        conn.close()
    else:
        st.error("Could not connect to the database.")
    
    switch_page("Attitudes_Results")
