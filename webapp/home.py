import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from config import USER_ID_STATE_KEY
import uuid
import logging

logging.basicConfig()

logging.basicConfig()
# TODO(cgavidia): Level should be customisable
logging.getLogger().setLevel(logging.DEBUG)


if USER_ID_STATE_KEY not in st.session_state:
    st.session_state[USER_ID_STATE_KEY] = str(uuid.uuid4())

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

# st.sidebar.markdown("# TEA-DT Survey")

st.markdown("# Welcome to our TEA-DT Survey")
st.markdown(
    "This is a [streamlit](https://streamlit.io) app, which can be easily "
    "edited to gather and present data. It is written in Python and compiled "
    "into HTML, "
    "CSS, and Javascript. As such, it can also support backend data analysis "
    "(e.g. "
    "quantitative and qualititative analysis of the survey data."
)

st.caption(
    "Read more about the options on the streamlit documentation site:"
    "[https://docs.streamlit.io/](https://docs.streamlit.io/)"
)

if st.button("Next"):
    # Redirect to the next section of the survey
    st.write("Redirecting to the survey...")
    switch_page("Community")
