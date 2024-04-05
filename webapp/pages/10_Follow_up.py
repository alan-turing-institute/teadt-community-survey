import streamlit as st
from email_validator import validate_email, EmailNotValidError


st.title("Follow-Up")

st.header("Section 5: Final Open-Ended Question")

# Open-ended question
st.subheader("1. Additional Insights")
additional_insights = st.text_area(
    "Is there anything else pertinent to the assurance of digital twins, which has not"
    " been covered, that you think is significant?",
    help="Your insights are valuable to us. Feel free to share any thoughts or"
    " experiences."
)

# Email input for follow-ups
st.subheader("Interested in Follow-Ups?")

# Checkbox for workshop interest
workshop_interest = st.checkbox(
    "I would like to join a more in-depth workshop to learn about assurance methodology"
    " & build my own assurance case under the guidance of experts.",
    "I would like to be kept up-to-date on the TEA-DT project and the outcomes of this survey."
)

email = st.text_input("Enter your email:")
st.markdown("*We'll only use your email to contact you regarding follow-ups.*")

if st.button("Submit"):
    try:
        # Validate.
        valid = validate_email(email)
        # Update with the normalized form.
        email = valid.email
        st.success("Valid email address.")
    except EmailNotValidError as e:
        # Email is not valid, exception message is human-readable
        st.error(str(e))
