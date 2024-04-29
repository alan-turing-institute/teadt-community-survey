import streamlit as st
import logging
from typing import Any, Optional
from streamlit_extras.switch_page_button import switch_page
from st_pages import hide_pages
from config import ALL_SESSION_KEYS, SURVEY_SUBMITTED_SESSION_KEY, SUCCESS_PAGE

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


def verify_user() -> bool:

    # hide_pages([SUCCESS_PAGE])

    if (
        SURVEY_SUBMITTED_SESSION_KEY in st.session_state
        and st.session_state[SURVEY_SUBMITTED_SESSION_KEY]
    ):
        switch_page(SUCCESS_PAGE)
        return False

    return True


def load_from_session(keys: list[str]) -> None:

    for key in st.session_state.keys():
        logging.info(f"{key=} {st.session_state[key]=}")

    for key in keys:
        if key in st.session_state:
            widget_session_key = f"{key}_{WIDGET_SUFFIX}"
            session_value = st.session_state[key]
            st.session_state[widget_session_key] = session_value
            logging.info(
                f"Loading value {session_value} into widget "
                f"{widget_session_key}"
            )
        else:
            logging.info(f"No value to load for session key {key}")


def generate_streamlit_element(
    question_text: str,
    question_type: str,
    options: Optional[list] = None,
    key: Optional[str] = None,
) -> Any:
    """
    Returns the appropriate Streamlit input element based on the question type.

    Parameters:
        question_text (str): The text of the question.
        question_type (str): The type of the question.
        options (list): The list of options for multiple choice or select
            all questions.
        key (str): The key to identify the input element uniquely.

    Returns:
        Streamlit input element
    """

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
            index=None,
        )
    else:
        raise ValueError(f"Invalid question type: {question_type}")


# Example usage:
# response = generate_streamlit_element(question_text, question_type,
# options=options, key=question_key)
