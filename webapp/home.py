import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from config import USER_ID_STATE_KEY
import uuid
from PIL import Image


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

# Logo and Navigation
col1, col2, col3 = st.columns((3, 2, 3))
with col1:
    st.image(Image.open("webapp/img/Alan_Turing_Institute_logo.png"))
with col3:
    st.image(Image.open("webapp/img/DTHub_logo.jpg"))

st.write("#")

# Title
st.markdown("# Welcome to the Community Pulse Check on Assurance of Digital Twin Systems")

# Description
st.markdown(
    "Are you confident that digital twins are trustworthy and ethical? Share your approaches and challenges in ensuring and promoting trustworthiness across the digital twin ecosystem, and help shape the future assurance standards. "
)

if st.button("Next"):
    # Redirect to the next section of the survey
    st.write("Redirecting to the survey...")
    switch_page("Community")


# Funding
st.caption(
    "This work is conducted as a part of the Trustworthy and Ethical Assurance of Digital Twins project, and is generously funded by an award from the UKRI’s Arts and Humanities Research Council as part of the BRAID programme. You can read more about the project here: https://www.turing.ac.uk/research/research-projects/trustworthy-and-ethical-assurance-digital-twins-tea-dt "
)
