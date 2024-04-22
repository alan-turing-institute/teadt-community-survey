import streamlit as st

def generate_streamlit_element(question_text, question_type, options=None, key=None):
    """
    Returns the appropriate Streamlit input element based on the question type.
    
    Parameters:
        question_text (str): The text of the question.
        question_type (str): The type of the question.
        options (list): The list of options for multiple choice or select all questions.
        key (str): The key to identify the input element uniquely.
        
    Returns:
        Streamlit input element
    """
    if question_type == "multiple_choice":
        return st.selectbox(question_text, options, key=key)
    elif question_type == "select_all":
        return st.multiselect(question_text, options, key=key)
    elif question_type == "likert":
        # Implement Likert scale if needed
        pass
    if question_type == "text_area":
        return st.text_area(question_text, key=key)
    elif question_type == "radio":
        return st.radio(question_text, options, key=key)
    elif question_type == "open_ended":
        return st.text_input(question_text, key=key)
    else:
        raise ValueError(f"Invalid question type: {question_type}")

# Example usage:
# response = get_input_element(question_text, question_type, options=options, key=question_key)
