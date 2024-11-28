import streamlit as st
from streamlit_utils import disable_sidebar

disable_sidebar()

st.success(
    "Thank you for participating in our survey. "
    "Your response has been recorded."
)
