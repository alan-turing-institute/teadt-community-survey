import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from db_utils import create_connection, insert_survey_result, create_table, query_data


st.title("Assurance and Ethics Capabilities")

# Initialize session state for showing additional content
if 'show_def' not in st.session_state:
    st.session_state.show_def = False
if 'show_def' not in st.session_state:
    st.session_state.show_def = False
if 'continue_clicked' not in st.session_state:
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
        "2.1 What do you understand assurance to mean in the context of developing & applying digital twinning technology?"
    )

    # Submit button for assurance definition
    submit_1 = st.form_submit_button("Submit Definition", on_click=disable, disabled=st.session_state.disabled)
    if submit_1:
        st.session_state['submit_1'] = True  # Mark the form as submitted
        st.session_state.show_def = True

# If the response to the first question is submitted, show the rest of the content
if st.session_state.show_def:
    st.markdown("""
    :::info
    **Background & Definition of Assurance:** *Assurance involves communicating reasons and evidence that help people understand and evaluate the trustworthiness of a claim (or series of claims) about a system or technology.*
    :::
    """, unsafe_allow_html=True)

    if st.button('Continue'):
        st.session_state.continue_clicked = True

if st.session_state.continue_clicked:   
    # Use a container for the rest of the questions to allow dynamic updates
    container = st.container()
    with container:
        st.subheader("Current Assurance Practices")
        # Question 2.2
        governance_requirements = st.text_area(
            "2.2 What governance or legal requirements does your organization adhere to/reference for assurance in digital twin projects (e.g., ISO standards, GDPR)?"
        )
        
        # Question 2.3
        assurance_methods = st.multiselect(
            "2.3 Which of the following assurance methods do you currently implement (if any)?",
            ["Risk Assessment", "Impact Assessment", "Bias Audit", "Compliance Audit", 
            "Conformity Assessment", "Formal Verification", "Model Cards", "None"],
            help="Based on recommendations outlined in the DSIT Practitioner Guide to AI Assurance."
        )
        
        # Question 2.4
        # Display the question above the matrix
        st.markdown("2.4 Indicate all properties of your digital twin that you aim to assure with each method?")

        # Define your project lifecycle stages
        project_stages =  ["Accuracy", "Fairness", "Privacy", "Robustness", "Transparency", "Other"]

        # Dynamically set row names based on the selection made in 2.3
        questions = assurance_methods if assurance_methods else ["None selected"]

        # Create columns for the labels, matching the layout for the checkboxes
        label_cols = st.columns(len(project_stages) + 1)  # +1 for the question label column

        # Skip the first column intended for question labels
        for col, stage in zip(label_cols[1:], project_stages):  # Start from 1 to skip the question label column
            with col:
                # Display the labels horizontally without rotation
                st.markdown(f'<p style="margin-bottom: -20px; text-align: center; font-size: 14px; margin-left: -60px;">{stage}</p>', unsafe_allow_html=True)
        # Iterate over each question/item
        for question in questions:
            # Create a row for each question with an additional column for the question label
            cols = st.columns(len(project_stages) + 1)  # +1 for the question label column
            
            # Write the question label in the first column of the row
            cols[0].write(question)
            
            # Iterate over each project stage to create a checkbox in each column
            for col, stage in zip(cols[1:], project_stages):  # Correctly reference 'stage' here
                with col:
                    # Ensure each checkbox has a unique key by combining 'question' and 'stage'
                    st.checkbox(" ", key=f"{question}_{stage}", label_visibility='collapsed')

        # Question 2.5
        assurance_execution = st.radio(
            "2.5 Are your assurance methods carried out internally or by an external partner?",
            ["Internal", "Third-party"], index=None
        )
        
        # Question 2.6
        existing_resources = st.text_area(
            "2.6 Are you aware of any existing resources to support your use of Assurance techniques and/or technical standards?"
        )

        st.subheader("Ethics Capabilities")

        # Question 2.7
        ethics_framework = st.radio(
            "2.7 Does your organisation have an established definition or framework for 'trustworthy' and 'ethical' digital twins?",
            ["Yes", "No", "Don't know"], index=None  # Set default selection to avoid None
        )

        # Follow-up questions based on the response to 2.7
        if ethics_framework == "Yes":
            ethics_definition = st.text_area(
                "2.7b Please describe your organisation's definition or framework for 'trustworthy' digital twins."
            )
            framework_development = st.text_area(
                "2.7c How was this definition or framework developed (e.g., in-house, through consultancy, collaborative industry efforts)?"
            )

    # Submit button for the rest of the survey
    if st.button("Submit & See Results"):
        conn = create_connection('survey_results.db')
        if conn:
            create_table(conn)

            # Update the data dictionary to match the questions from this section
            data = {
                "assurance_meaning": assurance_meaning,
                "governance_requirements": governance_requirements,
                "assurance_methods": ', '.join(assurance_methods),  # Joining list into a string for multiselect
                "assurance_execution": assurance_execution,
                "existing_resources": existing_resources,
                "ethics_framework": ethics_framework,
                "ethics_definition": ethics_definition if ethics_framework == "Yes" else None,  # Conditional based on ethics_framework response
                "framework_development": framework_development if ethics_framework == "Yes" else None  # Conditional based on ethics_framework response
            }
            # Assuming 'insert_survey_result' is a function you've defined to insert data into your database
            insert_survey_result(conn, "assurance_survey", data)  # Update table name as needed
            st.success("Survey result saved successfully!")
            conn.close()
        else:
            st.error("Could not connect to the database.")
        
        switch_page("Survey_Capabilities_Results")
