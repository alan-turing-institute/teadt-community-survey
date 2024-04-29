import streamlit as st
import random
import string
from captcha.image import ImageCaptcha
from PIL import Image
from config import USER_ID_STATE_KEY
import uuid
from streamlit_extras.switch_page_button import switch_page  # type: ignore
import logging

logging.basicConfig()

logging.basicConfig()
# TODO(cgavidia): Level should be customisable
logging.getLogger().setLevel(logging.INFO)


if USER_ID_STATE_KEY not in st.session_state:
    st.session_state[USER_ID_STATE_KEY] = str(uuid.uuid4())
    logging.info(f"Id for user: {st.session_state[USER_ID_STATE_KEY]=}")

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
    st.image(Image.open("webapp/img/DTH logo_primary_CMYK (2).jpg"))

st.write("#")

# Title
st.markdown(
    "# Welcome to the Community Pulse Check "
    "on Assurance of Digital Twin Systems"
)

# Description
st.markdown(
    "Are you confident that digital twins are trustworthy and ethical?"
)
st.markdown(
    "Take 15 minutes to share your approaches and pain points for assuring"
    " trustworthiness of digital twinning technology "
    "ecosystem, and help shape the future assurance standards."
)

st.markdown(
    "The Alan Turing Institute's TRIC-DT and CPC DT Hub are conducting a "
    "community pulse check on the topic of' Assurance of Digital Twin "
    "Systems'. We designed this pulse check with support from the "
    "Responsible Technology Adoption Unit to ensure alignment with "
    "national AI assurance guidelines from the "
    "Department for Science, Innovation, and Technology (DSIT). "
    "Are you developing, deploying or overseeing digital twin technologies"
    " or systems? We want to hear from business leaders, developers, "
    "and researchers to help us understand your perspective,"
    " current challenges, and needs when it comes to assuring "
    "digital twins."
    "Although digital twins promise vast societal benefits, "
    "their increasing reliance on various forms of AI "
    "and their role in safety-critical settings pose significant challenges."
    " These challenges must be addressed to ensure their "
    "ethical and trustworthy development. "
    "We are creating an open-source and community-based online tool "
    "that will assist users and project teams to define, put into practice, "
    "and implement ethical principles as assurance goals. "
    "Your opinions and experiences are crucial in developing this tool,"
    " ensuring it addresses industry pain points, "
    "and setting standards that enhance transparency and trust."
)

st.markdown(
    "The Community Pulse Check is a dynamic survey "
    "that allows you to see some of the results immediately, "
    "providing instant feedback on how your experiences and views align"
    " with those of your peers. "
)

st.markdown(
    "Participating will take approximately 15 – 20 minutes "
    "and can be completed entirely anonymously if you choose."
)

st.markdown(
    "By participating, you join a select group of professionals "
    "contributing to the responsible evolution of digital twin technologies. "
    "Your expertise does more than shape industry standards; "
    "it fosters a collaborative environment where knowledge sharing "
    "enhances community practices."
    "As we collectively contribute, we refine and enrich the standards "
    "that will benefit everyone in this transformative field."
)

# Funding
st.caption(
    "This work is conducted as a part of the Trustworthy and Ethical "
    "Assurance of Digital Twins project, and is generously funded by "
    "an award from the UKRI’s Arts and Humanities Research Council "
    "as part of the BRAID programme. The survey questions were designed with"
    " support from Centre for Assuring Autonomy and the Responsible Technology"
    " Adoption Unit to ensure alignment with national AI assurance guidelines "
    "from the Department for Science, Innovation, and Technology (DSIT)."
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

col_small_l, col_small_m, col_small_r = st.columns((3, 2, 3))
with col_small_l:
    st.image(
        Image.open("webapp/img/RTAU_BLK_MASTER_AW.png"),
        width=100,
    )
with col_small_m:
    st.image(
        Image.open("webapp/img/" "thumbnail_CfAA_Logo_Landscape_RGB.jpg"),
        width=200,
    )


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

        st.caption("Please verify you are human.")
        col1, col2 = st.columns(2)
        image = ImageCaptcha(width=width, height=height)
        data = image.generate(st.session_state["Captcha"])
        col1.image(data)
        captcha_text = col2.text_input("Enter captcha text")

        if st.button("Verify the code"):
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
