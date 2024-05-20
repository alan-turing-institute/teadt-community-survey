import streamlit as st
from st_pages import hide_pages
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
    GOALS_FRAMEWORK_RESULTS_PAGE,
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
hide_pages(["Success"])

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
    VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
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
    value_of_guiding_principles = (
        question_generator.generate_streamlit_element(
            questions["value_of_guiding_principles"]["question"],
            questions["value_of_guiding_principles"]["type"],
            options=questions["value_of_guiding_principles"].get("options"),
            key=VALUE_OF_GUIDING_PRINCIPLES_STATE_KEY,
        )
    )
st.write("#")

with st.container():
    st.subheader("Assurance for Trustworthy and Ethical Digital Twins")

    st.info(
        """
    The Gemini Principles
     are a set of 9 high-level principles,
     [established by the Centre for
     Digital Built Britain](https://www.cdbb.cam.ac.uk/DFTG/GeminiPrinciples)
     in December 2018 to guide the management and sharing of data
     across the built environment.
     These principles serve as the foundation
     for developing a national digital twin and
     an overall framework for information management.
     Created with input from government, industry, and academia,
     the principles aim to align stakeholders on data use and
     ensure that these initiatives benefit the public good.
     \n\n We are interested in understanding
     how these principles resonate with you and
     what is needed to better implement them better in the future.
     """
    )
    # Display an image
    image_path = Image.open("img/gemini_principles.png")
    st.image(
        image_path,
        caption="Illustration of " "Digital Twin Ethical Frameworks",
    )

    # Define tags for the questions to be displayed
    tags_to_display = [
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

    st.write("#")
    st.markdown(
        questions["relevance_of_principles"]["question"],
        help="Choose 'Not Relevant' "
        "if a principle is not applicable to your sector or solution",
    )

    # for each gemini principles
    relevance_good = question_generator.generate_streamlit_element(
        "**Public Good**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_GOOD_STATE_KEY,
        help="Must be used to deliver genuine public benefit in perpetuity.",
    )

    relevance_value = question_generator.generate_streamlit_element(
        "**Value Creation**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_VALUE_STATE_KEY,
        help="Must enable value creation and performance improvement.",
    )

    relevance_insight = question_generator.generate_streamlit_element(
        "**Insight**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_INSIGHT_STATE_KEY,
        help="Must provide determinable insight into the built environment.",
    )

    relevance_security = question_generator.generate_streamlit_element(
        "**Security**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_SECURITY_STATE_KEY,
        help="Must enable security and be secure itself",
    )

    relevance_openness = question_generator.generate_streamlit_element(
        "**Openness**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_OPENNESS_STATE_KEY,
        help="Must be as open as possible",
    )

    relevance_quality = question_generator.generate_streamlit_element(
        "**Quality**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_QUALITY_STATE_KEY,
        help="Must be built on data of an appropriate quality",
    )

    relevance_federation = question_generator.generate_streamlit_element(
        "**Federation**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_FEDERATION_STATE_KEY,
        help="Must be based on a standard connected environment",
    )

    relevance_curation = question_generator.generate_streamlit_element(
        "**Curation**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_CURATION_STATE_KEY,
        help="Must have clear ownership, governance and regulation",
    )

    relevance_evolution = question_generator.generate_streamlit_element(
        "**Evolution**",
        "likert_col",
        options=questions["relevance_of_principles"].get("options"),
        key=RELEVANCE_EVOLUTION_STATE_KEY,
        help="Must be able to adapt as technology and society evolve",
    )

    st.write("#")

    all_relevance_keys = [
        relevance_curation,
        relevance_evolution,
        relevance_curation,
        relevance_federation,
        relevance_good,
        relevance_insight,
        relevance_openness,
        relevance_security,
        relevance_quality,
        relevance_value,
    ]
    if any([x != "Not Relevant" for x in all_relevance_keys]):
        st.markdown(questions["challenge_in_application"]["question"])
    if relevance_good != "Not Relevant":
        challenge_good = question_generator.generate_streamlit_element(
            "Public Good",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_GOOD_STATE_KEY,
        )
    if relevance_value != "Not Relevant":
        challenge_value = question_generator.generate_streamlit_element(
            "Value",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_VALUE_STATE_KEY,
        )
    if relevance_insight != "Not Relevant":
        challenge_insight = question_generator.generate_streamlit_element(
            "Insight",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_INSIGHT_STATE_KEY,
        )
    if relevance_security != "Not Relevant":
        challenge_security = question_generator.generate_streamlit_element(
            "Security",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_SECURITY_STATE_KEY,
        )
    if relevance_openness != "Not Relevant":
        challenge_openness = question_generator.generate_streamlit_element(
            "Openness",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_OPENNESS_STATE_KEY,
        )
    if relevance_quality != "Not Relevant":
        challenge_quality = question_generator.generate_streamlit_element(
            "Quality",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_QUALITY_STATE_KEY,
        )
    if relevance_federation != "Not Relevant":
        challenge_federation = question_generator.generate_streamlit_element(
            "Federation",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_FEDERATION_STATE_KEY,
        )
    if relevance_curation != "Not Relevant":
        challenge_curation = question_generator.generate_streamlit_element(
            "Curation",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_CURATION_STATE_KEY,
        )
    if relevance_evolution != "Not Relevant":
        challenge_evolution = question_generator.generate_streamlit_element(
            "Evolution",
            "likert_col",
            options=questions["challenge_in_application"].get("options"),
            key=CHALLENGE_EVOLUTION_STATE_KEY,
        )

    st.write("#")
    choice_challenging = [
            "Slightly",
            "Moderately",
            "Very",
            "Extremely challenging"]
    vars_challenging = [
        'challenge_good', 'challenge_value',
        'challenge_security', 'challenge_openness',
        'challenge_insight', 'challenge_federation',
        'challenge_curation', 'challenge_evolution',
        'challenge_quality']
    vars_challenging = [locals()[var] for
                        var in vars_challenging if var in locals()]
    any_challenging = bool(set(vars_challenging) & set(choice_challenging))
    print(vars_challenging)
    print(any_challenging)
    if any_challenging:
        operationalization_challenges = (
            question_generator.generate_streamlit_element(
                questions["operationalization_challenges"]["question"],
                questions["operationalization_challenges"]["type"],
                options=questions[
                    "operationalization_challenges"].get("options"),
                key=OPERATIONALIZATION_CHALLENGES_STATE_KEY,
            )
        )

# Actions to take after the form is submitted
if st.button("Continue"):
    try:
        check_required_fields(all_page_elements, give_hint=True)
        switch_page(GOALS_FRAMEWORK_RESULTS_PAGE)
    except ValueError as e:
        # Exception message is human-readable
        st.error(str(e))
