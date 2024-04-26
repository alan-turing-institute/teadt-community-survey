import streamlit as st
import random
import string
from captcha.image import ImageCaptcha
from PIL import Image
from config import USER_ID_STATE_KEY
import uuid
from streamlit_extras.switch_page_button import switch_page  # type: ignore

if USER_ID_STATE_KEY not in st.session_state:
    st.session_state[USER_ID_STATE_KEY] = str(uuid.uuid4())

# Define the constants
length_captcha = 4
width = 200
height = 150

# Initialize session states
if not st.session_state.get("controllo", False):
    st.session_state["controllo"] = False

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
col_l, col_m, col_r = st.columns((3, 2, 3))
with col_l:
    st.image(Image.open("webapp/img/Alan_Turing_Institute_logo.png"))
with col_r:
    st.image(Image.open("webapp/img/DTHub_logo.jpg"))

st.write("#")

# Title
st.markdown(
    "# Welcome to the Community Pulse Check"
    "on Assurance of Digital Twin Systems"
)

# Description
st.markdown(
    "Are you confident that digital twins are trustworthy and ethical?"
    "Share your approaches and challenges in ensuring"
    "and promoting trustworthiness across the digital twin "
    "ecosystem, and help shape the future assurance standards."
)

# Funding
st.caption(
    "This work is conducted as a part of the Trustworthy and Ethical "
    "Assurance of Digital Twins project, and is generously funded by "
    "an award from the UKRI’s Arts and Humanities Research Council "
    "as part of the BRAID programme. "
    "You can read more about the project here:"
    " https://www.turing.ac.uk/research/research-projects/"
    "trustworthy-and-ethical-assurance-digital-twins-tea-dt "
)
# Logo and Navigation
col_foot_l, col_foot_m, col_foot_r = st.columns((3, 2, 3))
with col_foot_l:
    st.image(Image.open("webapp/img/BRAIDLogo_RGB_Landscape-tag.png"))
with col_foot_r:
    st.image(Image.open("webapp/img/UKRI%20logo.png"))

st.write("#")
st.write("#")

# Captcha
# Define a container to encapsulate captcha and user input fields
captcha_cont = st.empty()
# Render captcha only if it's not verified yet
if not st.session_state["controllo"]:

    with captcha_cont.container():
        # Setup the captcha widget
        if "Captcha" not in st.session_state:
            st.session_state["Captcha"] = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits, k=length_captcha
                )
            )
            print("the captcha is: ", st.session_state["Captcha"])

        st.caption("Please verify you are human.")
        col1, col2 = st.columns(2)
        image = ImageCaptcha(width=width, height=height)
        data = image.generate(st.session_state["Captcha"])
        col1.image(data)
        captcha_text = col2.text_input("Enter captcha text")

        if st.button("Verify the code"):
            print(captcha_text, st.session_state["Captcha"])
            captcha_text = captcha_text.replace(" ", "")
            # If the captcha is correct, set 'controllo' session state to True
            if (
                st.session_state["Captcha"].lower()
                == captcha_text.lower().strip()
            ):
                del st.session_state["Captcha"]
                st.session_state["controllo"] = True

# Show "Let's Start!" button if captcha is verified
if st.session_state["controllo"]:
    captcha_cont.empty()
    st.success("Success!")
    st.write("#")

    if st.button("Let's Start!"):
        # Redirect to the next section of the survey
        st.write("Redirecting to the Community Pulse Check...")
        switch_page("Consent")
