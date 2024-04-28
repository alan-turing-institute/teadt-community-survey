import streamlit as st
from utils import generate_streamlit_element, load_from_session
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from survey_questions import questions
from config import (
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
    RELEVANCE_GOOD_STATE_KEY,
    RELEVANCE_VALUE_STATE_KEY,
    RELEVANCE_INSIGHT_STATE_KEY,
    RELEVANCE_SECURITY_STATE_KEY,
    RELEVANCE_OPENNESS_STATE_KEY,
    RELEVANCE_QUALITY_STATE_KEY,
    RELEVANCE_FEDERATION_STATE_KEY,
    RELEVANCE_CURATION_STATE_KEY,
    RELEVANCE_EVOLUTION_STATE_KEY,
    CHALLENGE_GOOD_STATE_KEY,
    CHALLENGE_VALUE_STATE_KEY,
    CHALLENGE_INSIGHT_STATE_KEY,
    CHALLENGE_SECURITY_STATE_KEY,
    CHALLENGE_OPENNESS_STATE_KEY,
    CHALLENGE_QUALITY_STATE_KEY,
    CHALLENGE_FEDERATION_STATE_KEY,
    CHALLENGE_CURATION_STATE_KEY,
    CHALLENGE_EVOLUTION_STATE_KEY,
    OPERATIONALIZATION_CHALLENGES_STATE_KEY,
)

from PIL import Image

# Set page configuration and sidebar state
st.set_page_config(initial_sidebar_state="expanded")

st.title("Section 4: High-Level Assurance Goals and Ethical Frameworks")
st.markdown(
    """
This section dives deeper into the frameworks and principles guiding the"
 ethical and trustworthy development of digital twins.
"""
)

# Initialize disabled for form_submit_button to False
if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Define tags for the questions to be displayed
tags_to_display: list[str] = [
    ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    FRAMEWORK_DESCRIPTION_STATE_KEY,
    FRAMEWORK_DEVELOPMENT_STATE_KEY,
]
load_from_session(tags_to_display)

with st.container():
    ethical_framework_existence = generate_streamlit_element(
        questions["ethical_framework_existence"]["question"],
        questions["ethical_framework_existence"]["type"],
        options=questions["ethical_framework_existence"].get("options"),
        key=ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
    )

    if ethical_framework_existence is not None:
        if (ethical_framework_existence == "Yes" 
            or ethical_framework_existence.startswith("No, but")):
            
            framework_description = generate_streamlit_element(
                questions["framework_description"]["question"],
                questions["framework_description"]["type"],
                options=questions["framework_description"].get("options"),
                key=FRAMEWORK_DESCRIPTION_STATE_KEY,
            )

            framework_development = generate_streamlit_element(
                questions["framework_development"]["question"],
                questions["framework_development"]["type"],
                options=questions["framework_development"].get("options"),
                key=FRAMEWORK_DEVELOPMENT_STATE_KEY,
            )
st.write("#")

with st.container():
    st.subheader("Assurance for Connected Digital Twins")
    # Display an image
    image_path = Image.open("webapp/img/gemini_principles.png")
    st.image(
        image_path,
        caption="Illustration of " "Digital Twin Ethical Frameworks",
    )

    # Define tags for the questions to be displayed
    tags_to_display = [
        VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
        FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
        RELEVANCE_GOOD_STATE_KEY,
        RELEVANCE_VALUE_STATE_KEY,
        RELEVANCE_INSIGHT_STATE_KEY,
        RELEVANCE_SECURITY_STATE_KEY,
        RELEVANCE_OPENNESS_STATE_KEY,
        RELEVANCE_QUALITY_STATE_KEY,
        RELEVANCE_FEDERATION_STATE_KEY,
        RELEVANCE_CURATION_STATE_KEY,
        RELEVANCE_EVOLUTION_STATE_KEY,
        CHALLENGE_GOOD_STATE_KEY,
        CHALLENGE_VALUE_STATE_KEY,
        CHALLENGE_INSIGHT_STATE_KEY,
        CHALLENGE_SECURITY_STATE_KEY,
        CHALLENGE_OPENNESS_STATE_KEY,
        CHALLENGE_QUALITY_STATE_KEY,
        CHALLENGE_FEDERATION_STATE_KEY,
        CHALLENGE_CURATION_STATE_KEY,
        CHALLENGE_EVOLUTION_STATE_KEY,
        OPERATIONALIZATION_CHALLENGES_STATE_KEY,
    ]
    load_from_session(tags_to_display)

    value_of_guiding_principles = generate_streamlit_element(
        questions["value_of_guiding_principles"]["question"],
        questions["value_of_guiding_principles"]["type"],
        options=questions["value_of_guiding_principles"].get("options"),
        key=VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
    )

    familiarity_with_gemini_principles = generate_streamlit_element(
        questions["familiarity_with_gemini_principles"]["question"],
        questions["familiarity_with_gemini_principles"]["type"],
        options=questions["familiarity_with_gemini_principles"].get("options"),
        key=FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
    )

    st.write(questions["relevance_of_principles"]["question"])
    # for each gemini principles
    relevance_good = generate_streamlit_element(
        "Public Good",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_GOOD_STATE_KEY,
    )

    relevance_value = generate_streamlit_element(
        "Value Creation",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_VALUE_STATE_KEY,
    )

    relevance_insight = generate_streamlit_element(
        "Insight",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_INSIGHT_STATE_KEY,
    )

    relevance_security = generate_streamlit_element(
        "Security",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_SECURITY_STATE_KEY,
    )

    relevance_openness = generate_streamlit_element(
        "Openness",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_OPENNESS_STATE_KEY,
    )

    relevance_quality = generate_streamlit_element(
        "Quality",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_QUALITY_STATE_KEY,
    )

    relevance_federation = generate_streamlit_element(
        "Federation",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_FEDERATION_STATE_KEY,
    )

    relevance_curation = generate_streamlit_element(
        "Curation",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_CURATION_STATE_KEY,
    )

    relevance_evolution = generate_streamlit_element(
        "Evolution",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_EVOLUTION_STATE_KEY,
    )

    st.write("#")
    st.write(questions["challenge_in_application"]["question"])
    challenge_good = generate_streamlit_element(
        "Good",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_GOOD_STATE_KEY,
    )

    challenge_value = generate_streamlit_element(
        "Value",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_VALUE_STATE_KEY,
    )

    challenge_insight = generate_streamlit_element(
        "Insight",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_INSIGHT_STATE_KEY,
    )

    challenge_security = generate_streamlit_element(
        "Security",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_SECURITY_STATE_KEY,
    )

    challenge_openness = generate_streamlit_element(
        "Openness",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_OPENNESS_STATE_KEY,
    )

    challenge_quality = generate_streamlit_element(
        "Quality",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_QUALITY_STATE_KEY,
    )

    challenge_federation = generate_streamlit_element(
        "Federation",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_FEDERATION_STATE_KEY,
    )

    challenge_curation = generate_streamlit_element(
        "Curation",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_CURATION_STATE_KEY,
    )

    challenge_evolution = generate_streamlit_element(
        "Evolution",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_EVOLUTION_STATE_KEY,
    )

    st.write("#")
    operationalization_challenges = generate_streamlit_element(
        questions["operationalization_challenges"]["question"],
        questions["operationalization_challenges"]["type"],
        options=questions["operationalization_challenges"].get("options"),
        key=OPERATIONALIZATION_CHALLENGES_STATE_KEY,
    )


# Actions to take after the form is submitted
if st.button("Continue"):
    switch_page("Communicating_Assurance")
