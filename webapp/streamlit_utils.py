import streamlit as st
import logging
import math
from typing import Any, Optional
from streamlit_extras import switch_page_button
from config import (
    SURVEY_SUBMITTED_STATE_KEY,
    SUCCESS_PAGE,
    USER_ID_STATE_KEY,
    HOME_PAGE,
    CONSENT_PAGE,
    ERROR_MESSAGES_STATE_KEY,
    ALL_CONSENT_STATE_KEYS,
    CONSENT_QUESTIONS,
    VALID_CAPTCHA_ENTRY_STATE_KEY,
    ALL_REQUIRED_KEYS,
    conditional_keys,
)

WIDGET_SUFFIX: str = "widget"


# Disable the submit button after it is clicked
def disable_button() -> None:
    st.session_state.disabled = True


def disable_sidebar() -> None:
    # Disable the sidebar
    st.set_page_config(initial_sidebar_state="collapsed")

    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )


def store_in_session(key: str) -> None:
    st.session_state[key] = st.session_state[f"{key}_{WIDGET_SUFFIX}"]


def verify_user(current_page: str) -> bool:
    logging.info(f"Verifying user at {current_page}")
    if (
        SURVEY_SUBMITTED_STATE_KEY in st.session_state
        and st.session_state[SURVEY_SUBMITTED_STATE_KEY]
    ):
        logging.info("Answers submitted! Redirecting to Success")
        switch_page_button.switch_page(SUCCESS_PAGE)
        return False

    if (
        USER_ID_STATE_KEY not in st.session_state
        or st.session_state[USER_ID_STATE_KEY] is None
        or VALID_CAPTCHA_ENTRY_STATE_KEY not in st.session_state
        or not st.session_state[VALID_CAPTCHA_ENTRY_STATE_KEY]
    ):
        logging.info("Invalid user! Redirecting to home")
        switch_page_button.switch_page(HOME_PAGE)
        return False

    consent_responses: list[bool] = [
        st.session_state[state_key]
        for state_key in ALL_CONSENT_STATE_KEYS
        if state_key in st.session_state
    ]

    if current_page != CONSENT_PAGE and (
        len(consent_responses) != CONSENT_QUESTIONS
        or not all(consent_responses)
    ):
        logging.info(f"Consent not given! Redirecting to {CONSENT_PAGE} page.")
        st.session_state[ERROR_MESSAGES_STATE_KEY] = (
            "You did not provide consent for your data to be stored."
        )
        switch_page_button.switch_page(CONSENT_PAGE)

    return True


def display_error_messages():
    if ERROR_MESSAGES_STATE_KEY in st.session_state:
        logging.info(f"{st.session_state[ERROR_MESSAGES_STATE_KEY]}")
        st.error(st.session_state[ERROR_MESSAGES_STATE_KEY])
        del st.session_state[ERROR_MESSAGES_STATE_KEY]
    else:
        logging.info("No messages to display")


def load_from_session(keys: list[str]) -> None:

    # for key in st.session_state.keys():
    #     logging.info(f"{key=} {st.session_state[key]=}")

    for key in keys:
        if key in st.session_state:
            widget_session_key = f"{key}_{WIDGET_SUFFIX}"
            session_value = st.session_state[key]
            st.session_state[widget_session_key] = session_value
            # logging.info(
            #     f"Loading value {session_value} into widget "
            #     f"{widget_session_key}"
            # )
        else:
            logging.info(f"No value to load for session key {key}")


def check_required_fields(
    page_element_keys: list[str], give_hint: bool = False
) -> None:
    data: dict[str, Any] = {
        session_key: st.session_state[session_key]
        for session_key in page_element_keys
        if session_key in st.session_state
    }

    # Check conditional keys and remove those not showing
    for key, conditions in conditional_keys.items():
        depends_on_key = conditions["depends_on_key"]
        depends_on_response = conditions["depends_on_response"]

        if depends_on_key not in data:
            if key in page_element_keys:
                page_element_keys.remove(key)
        elif (
            data[depends_on_key] != depends_on_response
            and depends_on_response not in data[depends_on_key]
        ):
            if key in page_element_keys:
                page_element_keys.remove(key)

    # Reduce required keys to only those of current page
    required_keys = [
        key for key in ALL_REQUIRED_KEYS if key in page_element_keys
    ]
    missing_fields = []

    # Function to retrieve question number based on index
    def get_question_number(key):
        return page_element_keys.index(key) + 1

    for question_key in required_keys:
        if question_key not in data:
            missing_fields.append(
                (question_key, get_question_number(question_key))
            )
        elif data[question_key] == "Select":
            missing_fields.append(
                (question_key, get_question_number(question_key))
            )
        elif not data[question_key]:
            missing_fields.append(
                (question_key, get_question_number(question_key))
            )

    if missing_fields:
        if give_hint:
            question_numbers = ", ".join(
                str(question[1]) for question in missing_fields
            )
            raise ValueError(
                f"You did not fill in all required fields. "
                f"Please complete question(s) {question_numbers}."
            )
        else:
            raise ValueError(
                "You did not fill in all required fields."
                " Please go back and complete the survey."
            )


class QuestionGenerator:
    def __init__(self, section_number: int):
        self.section_number = section_number
        self.number = 0

    def generate_streamlit_element(
        self,
        question_text: str,
        question_type: str,
        options: Optional[list] = None,
        key: Optional[str] = None,
        help: Optional[str] = None,
    ) -> Any:
        """
        Returns the appropriate Streamlit input element
         based on the question type.

        Parameters:
            question_text (str): The text of the question.
            question_type (str): The type of the question.
            options (list): The list of options for multiple choice or select
                all questions.
            key (str): The key to identify the input element uniquely.

        Returns:
            Streamlit input element
        """
        self.number += 1
        question_text = f"{self.section_number}.{self.number}. {question_text}"

        if key in ALL_REQUIRED_KEYS:
            question_text += " :red[*]"

        widget_key: str = f"{key}_{WIDGET_SUFFIX}"
        if question_type == "multiple_choice" and options is not None:
            return st.selectbox(
                question_text,
                options,
                key=widget_key,
                on_change=store_in_session,
                args=(key,),
            )
        elif question_type == "select_all" and options is not None:
            return st.multiselect(
                question_text,
                options,
                key=widget_key,
                on_change=store_in_session,
                args=(key,),
            )
        elif question_type == "checkbox_select_all" and options is not None:
            # Calculate number of columns based on number of options
            num_options = len(options)
            num_columns = min(
                3, math.ceil(num_options / 4)
            )  # Maximum of 4 columns or ceil(options/8)
            # Display question text above columns
            st.write(question_text)
            st.write("")  # Add a space between question text and columns
            # Create columns based on number of columns
            columns = st.columns(num_columns)
            # Display options in grid format
            responses = []
            for i, option in enumerate(options):
                option_text_parts = option.split("/")
                checkbox_label = option_text_parts[0].strip()
                help_text = (
                    option_text_parts[1].strip()
                    if len(option_text_parts) > 1
                    else None
                )
                response = columns[i % num_columns].checkbox(
                    checkbox_label,
                    help=help_text,
                    key=f"{widget_key}_{checkbox_label}",
                )
                responses.append(response)
            return responses
        elif question_type == "likert" and options is not None:
            # scale labels e.g. ['Strongly Disagree', 'Disagree', 'Neutral',
            #  'Agree', 'Strongly Agree']
            likert_scale_labels = options
            return st.select_slider(
                question_text,
                likert_scale_labels,
                key=widget_key,
                on_change=store_in_session,
                args=(key,),
            )
        elif question_type == "likert_col" and options is not None:
            likert_scale_labels = options
            # Create two columns
            left_column, right_column = st.columns([1, 3])
            # Question text in the left column
            with left_column:
                st.write(question_text)
            # Likert scale slider in the right column
            with right_column:
                return st.select_slider(
                    "",
                    likert_scale_labels,
                    key=widget_key,
                    label_visibility="collapsed",
                    on_change=store_in_session,
                    args=(key,),
                )
        elif question_type == "text_area":
            return st.text_area(
                question_text,
                key=widget_key,
                on_change=store_in_session,
                args=(key,),
            )
        elif question_type == "radio" and options is not None:
            return st.radio(
                question_text,
                options,
                key=widget_key,
                on_change=store_in_session,
                args=(key,),
                help=help,
                index=None,
            )
        else:
            raise ValueError(f"Invalid question type: {question_type}")


# Example usage:
# response = generate_streamlit_element(question_text, question_type,
# options=options, key=question_key)
