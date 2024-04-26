import streamlit as st
import logging

WIDGET_SUFFIX: str = "widget"


# Disable the submit button after it is clicked
def disable_button() -> None:
    st.session_state.disabled = True


def store_in_session(key: str) -> None:
    st.session_state[key] = st.session_state[f"{key}_{WIDGET_SUFFIX}"]


def load_from_session(keys: list[str]) -> None:

    for key in st.session_state.keys():
        logging.debug(f"{key=} {st.session_state[key]=}")

    for key in keys:
        if key in st.session_state:
            widget_session_key = f"{key}_{WIDGET_SUFFIX}"
            session_value = st.session_state[key]
            st.session_state[widget_session_key] = session_value
            logging.debug(
                f"Loading value {session_value} into widget "
                f"{widget_session_key}"
            )
        else:
            logging.debug(f"No value to load for session key {key}")


def generate_streamlit_element(
    question_text, question_type, options=None, key=None
):
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
    if question_type == "multiple_choice":
        return st.selectbox(
            question_text,
            options,
            key=widget_key,
            on_change=store_in_session,
            args=[key],
        )
    elif question_type == "select_all":
        return st.multiselect(
            question_text,
            options,
            key=widget_key,
            on_change=store_in_session,
            args=[key],
        )
    elif question_type == "likert":
        # scale labels e.g. ['Strongly Disagree', 'Disagree', 'Neutral',
        #  'Agree', 'Strongly Agree']
        likert_scale_labels = options
        return st.select_slider(
            question_text,
            likert_scale_labels,
            key=widget_key,
            on_change=store_in_session,
            args=[key],
        )
    elif question_type == "text_area":
        return st.text_area(
            question_text,
            key=widget_key,
            on_change=store_in_session,
            args=[key],
        )
    elif question_type == "radio":
        return st.radio(
            question_text,
            options,
            key=widget_key,
            on_change=store_in_session,
            args=[key],
        )
    else:
        raise ValueError(f"Invalid question type: {question_type}")


# Example usage:
# response = generate_streamlit_element(question_text, question_type,
# options=options, key=question_key)
