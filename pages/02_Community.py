import streamlit as st
import pycountry
from db_utils import create_connection, insert_survey_result, create_table, query_data
from streamlit_extras.switch_page_button import switch_page

# reintroduce sidebar (collapse button will stay hidden as CSS cannot by dynamically altered)
st.set_page_config(initial_sidebar_state="expanded")


st.title("Part 1: Community Composition")
st.markdown(
    "This section explores your understanding and current practices around assurance of digital twins."
)


# Disable the submit button after it is clicked
def disable():
    st.session_state.disabled = True


# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Wrap your input elements and submit button in a form
with st.form("survey_form"):
    # Question 1.1
    sector = st.selectbox(
        "What sector best represents your field of work?",
        [
            "Select",
            "Aerospace",
            "Architecture",
            "Artificial Intelligence",
            "Automotive",
            "Aviation",
            "Construction",
            "Consumer Goods",
            "Defence",
            "Education",
            "Electronics",
            "Engineering",
            "Environment and Conservation",
            "Finance",
            "Food and Agriculture",
            "Freight",
            "Healthcare",
            "International Government",
            "Local Government",
            "Manufacturing",
            "Maritime",
            "Media",
            "Mining",
            "National Government",
            "Nuclear Energy",
            "Oil and Gas",
            "Place Leadership",
            "Rail",
            "Renewable Energy",
            "Smart Cities",
            "Supply Chain and Logistics",
            "Technology",
            "Telecommunications",
            "Transport",
            "Utilities",
            "Waste and Recycling",
            "Water",
        ],
        disabled="submitted" in st.session_state,
    )

    # Question 1.2
    countries = [country.name for country in pycountry.countries]
    location = st.selectbox(
        "Where is your organisation located?",
        countries,
        disabled="submitted" in st.session_state,
    )

    # Question 1.3
    role = st.selectbox(
        "What is your role within your organisation?",
        [
            "Select",
            "Developer/Engineer",
            "Project/Program Manager",
            "Executive/Decision-Maker",
            "Researcher/Academic",
            "Compliance Officer/Regulatory Affairs Manager",
            "Technical Manager/Lead Developer",
            "Industry Consultant/Advisor",
            "Ontology Engineer/Framework Architect",
            "Data Scientist/Analyst",
            "Middleware/API Developer",
            "Governance Specialist",
            "Semantic Web Technologist",
            "Platform Developer",
            "Other",
        ],
        disabled="submitted" in st.session_state,
    )

    # Question 1.4
    primary_responsibilities = st.multiselect(
        "What are your primary responsibilities?",
        [
            "Select",
            "Designing and Implementing",
            "Strategizing and Directing",
            "Ensuring Compliance",
            "Advising and Consulting",
            "Developing Tools and Frameworks",
            "Other",
        ],
        disabled="submitted" in st.session_state,
    )

    # Submit button for the form
    submitted = st.form_submit_button(
        "Submit", on_click=disable, disabled=st.session_state.disabled
    )
    if submitted:
        st.session_state["submitted"] = True  # Mark the form as submitted

# Actions to take after the form is submitted
if submitted:
    conn = create_connection("survey_results.db")
    if conn:
        create_table(conn)

        data = {
            "sector": sector,
            "location": location,
            "role": role,
            "responsibilities": ", ".join(
                primary_responsibilities
            ),  # Joining list into a string
        }
        insert_survey_result(conn, "assurance_survey", data)
        st.success("Survey result saved successfully!")
        conn.close()
    else:
        st.error("Could not connect to the database.")

    switch_page("Community_Results")
