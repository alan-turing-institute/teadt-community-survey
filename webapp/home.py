import streamlit as st
import random
import string
from captcha.image import ImageCaptcha
from PIL import Image
from config import (
    USER_ID_STATE_KEY,
    CONSENT_PAGE,
    VALID_CAPTCHA_ENTRY_STATE_KEY,
    CAPTCHA_TEXT_STATE_KEY,
)
import uuid
from streamlit_extras.switch_page_button import switch_page  # type: ignore
import logging
from streamlit_utils import disable_sidebar

logging.basicConfig()
# TODO(cgavidia): Level should be customisable
logging.getLogger().setLevel(logging.INFO)

# Define the constants
length_captcha = 4
width = 200
height = 150

disable_sidebar()

# Logo and Navigation
col_l, col_m, col_r = st.columns((3, 2, 3))
with col_l:
    st.image(Image.open("webapp/img/Alan_Turing_Institute_logo.png"))
with col_r:
    st.image(Image.open("webapp/img/DTH logo_primary_CMYK (2).jpg"))

st.write("#")

# Title
st.markdown("# Welcome!")

st.markdown("# Community Pulse Check: " "Assurance of Digital Twin Systems")

st.write("#")

# Description
st.markdown(
    "<h2 style='text-align: center;'>"
    "Are you confident that digital twins are trustworthy and ethical?</h2>",
    unsafe_allow_html=True,
)

st.write("#")
st.markdown(
    "The Alan Turing Institute's TRIC-DT and CPC DT Hub are conducting a "
    "community pulse check on the topic of' Assurance of Digital Twin "
    "Systems'."
)
st.markdown(
    "Are you developing, deploying or overseeing digital twin technologies"
    " or systems? We want to hear from business leaders, developers, "
    "and researchers to help us understand your perspective,"
    " current challenges, and needs when it comes to assuring "
    "digital twins."
    " By participating, you join a select group of professionals "
    "contributing to the responsible evolution of digital twin technologies. "
    "Your expertise will shape industry standards "
    "and fosters a collaborative environment where knowledge sharing enhances "
    "community practices."
)

# TODO reactive this for stage 2 data collection
# st.markdown(
#     "The Community Pulse Check is a dynamic survey "
#     "that allows you to see some of the results immediately, "
#     "providing instant feedback on how your experiences and views align"
#     " with those of your peers. "
# )

st.markdown(
    "- Participating will take approximately 15 – 20 minutes\n"
    "- It can be completed entirely anonymously if you choose.",
    unsafe_allow_html=True,
)


st.markdown(
    "<h3 style='text-align: center;'>"
    "Take 15 minutes to share your approach and pain points"
    " and help us build assurance tools "
    "that promote trustworthy and ethical digital twins.</h3>",
    unsafe_allow_html=True,
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
if (
    VALID_CAPTCHA_ENTRY_STATE_KEY not in st.session_state
    or st.session_state[VALID_CAPTCHA_ENTRY_STATE_KEY] is False
):
    st.session_state[VALID_CAPTCHA_ENTRY_STATE_KEY] = False

    with captcha_cont.container():
        # Setup the captcha widget
        if CAPTCHA_TEXT_STATE_KEY not in st.session_state:
            st.session_state[CAPTCHA_TEXT_STATE_KEY] = "".join(
                random.choices(
                    string.ascii_uppercase + string.digits, k=length_captcha
                )
            )

        st.caption("Please verify you are human.")
        col1, col2 = st.columns(2)
        captcha_image: ImageCaptcha = ImageCaptcha(width=width, height=height)
        data = captcha_image.generate(st.session_state[CAPTCHA_TEXT_STATE_KEY])
        col1.image(data)
        user_provided_text: str = col2.text_input("Enter captcha text")

        if st.button("Verify the code"):
            user_provided_text = user_provided_text.replace(" ", "")
            # If the captcha is correct, set 'controllo' session state to True
            # TODO(cptanalatriste)REMOVE LATER!
            # logging.info(
            #     f"{st.session_state[CAPTCHA_TEXT_STATE_KEY].lower()=} "
            #     f"{user_provided_text.lower().strip()=}"
            # )

            if (
                st.session_state[CAPTCHA_TEXT_STATE_KEY].lower()
                == user_provided_text.lower().strip()
            ):
                del st.session_state[CAPTCHA_TEXT_STATE_KEY]
                st.session_state[VALID_CAPTCHA_ENTRY_STATE_KEY] = True
                st.session_state[USER_ID_STATE_KEY] = str(uuid.uuid4())
                logging.info(
                    f"Id for user: " f"{st.session_state[USER_ID_STATE_KEY]=}"
                )
            else:
                del st.session_state[VALID_CAPTCHA_ENTRY_STATE_KEY]
                st.error("Incorrect text. Please try again.")

# Show "Let's Start!" button if captcha is verified
if (
    VALID_CAPTCHA_ENTRY_STATE_KEY in st.session_state
    and st.session_state[VALID_CAPTCHA_ENTRY_STATE_KEY]
):
    captcha_cont.empty()
    st.success("Success!")
    st.write("#")

    if st.button("Let's Start!"):
        # Redirect to the next section of the survey
        st.write("Redirecting to the Community Pulse Check...")
        switch_page(CONSENT_PAGE)
