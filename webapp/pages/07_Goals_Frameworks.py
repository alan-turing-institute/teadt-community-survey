import streamlit as st
from streamlit_utils import (
    QuestionGenerator,
    load_from_session,
    verify_user,
    display_error_messages,
    check_required_fields,
)
from PIL import Image
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
    GOALS_FRAMEWORK_PAGE,
    COMMUNICATING_ASSURANCE_PAGE,
    REQUIRED_MESSAGE,
)

all_page_elements = [
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
]

verify_user(GOALS_FRAMEWORK_PAGE)
display_error_messages()


# Set page configuration and sidebar state
st.set_page_config(initial_sidebar_state="expanded")

SECTION_NUM = 4

st.title(
    f"Section {SECTION_NUM}: High-Level Assurance Goals and Ethical Frameworks"
)
st.warning(
    """
This section dives deeper into the frameworks and principles guiding the"
 ethical and trustworthy development of digital twins.
"""
)
st.markdown(REQUIRED_MESSAGE, unsafe_allow_html=True)


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

question_generator = QuestionGenerator(SECTION_NUM)
with st.container():
    ethical_framework_existence = (
        question_generator.generate_streamlit_element(
            questions["ethical_framework_existence"]["question"],
            questions["ethical_framework_existence"]["type"],
            options=questions["ethical_framework_existence"].get("options"),
            key=ETHICAL_FRAMEWORK_EXISTENCE_STATE_KEY,
        )
    )

    if ethical_framework_existence is not None:
        if (
            ethical_framework_existence == "Yes  / Something similar"
            or ethical_framework_existence.startswith("No, but")
        ):
            framework_description = (
                question_generator.generate_streamlit_element(
                    questions["framework_description"]["question"],
                    questions["framework_description"]["type"],
                    options=questions["framework_description"].get("options"),
                    key=FRAMEWORK_DESCRIPTION_STATE_KEY,
                )
            )

            framework_development = (
                question_generator.generate_streamlit_element(
                    questions["framework_development"]["question"],
                    questions["framework_development"]["type"],
                    options=questions["framework_development"].get("options"),
                    key=FRAMEWORK_DEVELOPMENT_STATE_KEY,
                )
            )
st.write("#")

with st.container():
    st.subheader("Assurance for Connected Digital Twins")
    # Display an image
    image_path = Image.open("img/gemini_principles.png")
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

    value_of_guiding_principles = (
        question_generator.generate_streamlit_element(
            questions["value_of_guiding_principles"]["question"],
            questions["value_of_guiding_principles"]["type"],
            options=questions["value_of_guiding_principles"].get("options"),
            key=VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
        )
    )

    familiarity_with_gemini_principles = (
        question_generator.generate_streamlit_element(
            questions["familiarity_with_gemini_principles"]["question"],
            questions["familiarity_with_gemini_principles"]["type"],
            options=questions["familiarity_with_gemini_principles"].get(
                "options"
            ),
            key=FAMILIARITY_WITH_GEMINI_PRINCIPLES_STATE_KEY,
        )
    )

    st.write(questions["relevance_of_principles"]["question"])
    # for each gemini principles
    relevance_good = question_generator.generate_streamlit_element(
        "Public Good",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_GOOD_STATE_KEY,
    )

    relevance_value = question_generator.generate_streamlit_element(
        "Value Creation",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_VALUE_STATE_KEY,
    )

    relevance_insight = question_generator.generate_streamlit_element(
        "Insight",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_INSIGHT_STATE_KEY,
    )

    relevance_security = question_generator.generate_streamlit_element(
        "Security",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_SECURITY_STATE_KEY,
    )

    relevance_openness = question_generator.generate_streamlit_element(
        "Openness",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_OPENNESS_STATE_KEY,
    )

    relevance_quality = question_generator.generate_streamlit_element(
        "Quality",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_QUALITY_STATE_KEY,
    )

    relevance_federation = question_generator.generate_streamlit_element(
        "Federation",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_FEDERATION_STATE_KEY,
    )

    relevance_curation = question_generator.generate_streamlit_element(
        "Curation",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_CURATION_STATE_KEY,
    )

    relevance_evolution = question_generator.generate_streamlit_element(
        "Evolution",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_EVOLUTION_STATE_KEY,
    )

    st.write("#")
    st.write(questions["challenge_in_application"]["question"])
    challenge_good = question_generator.generate_streamlit_element(
        "Good",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_GOOD_STATE_KEY,
    )

    challenge_value = question_generator.generate_streamlit_element(
        "Value",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_VALUE_STATE_KEY,
    )

    challenge_insight = question_generator.generate_streamlit_element(
        "Insight",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_INSIGHT_STATE_KEY,
    )

    challenge_security = question_generator.generate_streamlit_element(
        "Security",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_SECURITY_STATE_KEY,
    )

    challenge_openness = question_generator.generate_streamlit_element(
        "Openness",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_OPENNESS_STATE_KEY,
    )

    challenge_quality = question_generator.generate_streamlit_element(
        "Quality",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_QUALITY_STATE_KEY,
    )

    challenge_federation = question_generator.generate_streamlit_element(
        "Federation",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_FEDERATION_STATE_KEY,
    )

    challenge_curation = question_generator.generate_streamlit_element(
        "Curation",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_CURATION_STATE_KEY,
    )

    challenge_evolution = question_generator.generate_streamlit_element(
        "Evolution",
        "likert_col",
        options=questions["challenge_in_application"].get("options"),
        key=CHALLENGE_EVOLUTION_STATE_KEY,
    )

    st.write("#")
    operationalization_challenges = (
        question_generator.generate_streamlit_element(
            questions["operationalization_challenges"]["question"],
            questions["operationalization_challenges"]["type"],
            options=questions["operationalization_challenges"].get("options"),
            key=OPERATIONALIZATION_CHALLENGES_STATE_KEY,
        )
    )

# Actions to take after the form is submitted
if st.button("Continue"):
    try:
        check_required_fields(all_page_elements, give_hint=True)
        switch_page(COMMUNICATING_ASSURANCE_PAGE)
    except ValueError as e:
        # Exception message is human-readable
        st.error(str(e))
