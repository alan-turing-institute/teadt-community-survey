import streamlit as st
from streamlit_extras.switch_page_button import switch_page  # type:ignore
from config import (
    CONSENT_STATE_KEY,
    ALL_CONSENT_STATE_KEYS,
    CONSENT_PAGE,
    COMMUNITY_PAGE,
)
from streamlit_utils import (
    load_from_session,
    WIDGET_SUFFIX,
    store_in_session,
    verify_user,
    disable_sidebar,
    display_error_messages,
)

verify_user(CONSENT_PAGE)
display_error_messages()
disable_sidebar()

st.title("Participant Information for the TEA-DT Survey")

# Display the survey and project information
st.markdown(
    """
### About the Survey
This survey is a key part of the Trustworthy and Ethical Assurance for Digital
 Twins (TEA-DT) project, which focuses on enhancing the development and
 application
 of digital twins (DTs) through ethical assurance. The survey aims to gather
 insights
 from DT practitioners like you to understand the current landscape of
 practices, needs,
 and perceptions around building trustworthy and ethical DTs. Your
 participation will
 help us identify how DT projects can be better supported to integrate ethical
 principles effectively.
""")

st.info(
    """
    ### What is Trustworthy and Ethical Assurance?
    Trustworthy and ethical assurance refers to clear
    methods and tools that ensure data-driven technologies are
    designed, developed and deployed reliably and ethically.
    This approach is essential for building trust and transparency
    in increasingly complex technological environments.
    """
)
st.markdown(
    """
 ### The TEA-DT Project

The TEA-DT project is spearheaded by researchers at the Alan Turing Institute
 and the University of York. It revolves around the Trustworthy and Ethical
 Assurance (TEA)
 Platform, an innovative tool designed to guide users in defining,
 operationalizing, and
 implementing ethical principles within DT projects. 

 The survey data will significantly influence the TEA-DT project by:

- Providing insights into the current landscape of
 digital twin assurance practices and
 the challenges practitioners face.
- Highlighting opportunities to enhance the TEA Platform
 to better serve the digital twin community.
- Inform the development of accessible and reproducible standards for
assuring digital twin technologies.

This information will help shape the project's direction and
 the production of guidance materials, ultimately cultivating
 a robust assurance ecosystem for DT research and innovation.

### Data Collection and Use
We are committed to ensuring the anonymity of all survey participants.
The survey will collect information related to occupational backgrounds,
such as sector,
 job title, organization location, and role, to understand the diversity
 within the digital
 twin community. No personal or sensitive data will be collected.
The collected data will be analysed to identify trends, patterns, and insights
 relevant to the assurance of digital twins. Findings from the survey will
 contribute
 to the broader scoping research of the TEA-DT project and may be used in
 published
 articles, reports, and presentations to share knowledge and best practices
 within
 the digital twin community. To ensure the confidentiality of participant
 responses,
 any shared data will unlink responses and aggregate data where needed to
 protect
 individual identities.
The Alan Turing Institute is the data controller for this survey. The legal
basis
for processing your data in this survey is your consent, which you provide by
participating in the survey. Raw data will be stored securely, and access will
be
limited to authorized members of the research team. Participants have the
right to
withdraw from the survey at any time without any adverse consequences.


### Further Information and Contact
This survey is overseen by the Alan Turing Institute. If you have any questions
or require further information about the survey or the TEA-DT project, please
contact us at digitaltwins@turing.ac.uk.
Your insights are invaluable to us, and we thank you for contributing to the
advancement of trustworthy and ethical digital twins.


**Your insights are invaluable to us, and we thank you for contributing to
the advancement of trustworthy and ethical digital twins.**
"""
)

st.markdown("## Informed Consent")
st.markdown(
    "Please take some time to read through the statements on the consent form"
    " below before agreeing to take part in the survey."
)

# Consent questions - all must be checked 'Yes' to proceed
consent_questions: list[str] = [
    "I understand and consent to participating in this survey.",
    "I understand that my participation in this survey is voluntary.",
    "I understand that I will not benefit directly from participating in this "
    "research.",
    "The purpose and nature of this study and the survey have been explained "
    "to me above and I am able to contact someone to ask questions.",
    "I understand that participation in this survey involves answering "
    "questions on my views and my work with regard to the assurance of digital"
    " twins, and will include discussing my own perceptions and attitudes"
    " about current methods or techniques.",
    "I understand that if I withdraw during the survey my responses will be"
    " deleted. I understand that after I complete the survey, I will not be"
    " able to withdraw my responses.",
    "I understand that in any report or use of the results of this research my"
    " identity will remain anonymous. I understand that my name will not be"
    " recorded.",
    "I understand that a copy of my survey results will be stored securely "
    "by The Alan Turing Institute and retained for a period of at least 5 "
    "years.",
    "I understand that all information I provide for this survey will be "
    "treated securely and confidentially.",
    "I understand that I am free to contact any of the people involved in the "
    "research to seek further clarification and information.",
]

load_from_session(ALL_CONSENT_STATE_KEYS)

# Create a toggle for each consent statement
consent_given = [
    st.toggle(
        statement,
        value=False,
        key=f"{CONSENT_STATE_KEY}_{i}_{WIDGET_SUFFIX}",
        on_change=store_in_session,
        args=(f"{CONSENT_STATE_KEY}_{i}",),
    )
    for i, statement in enumerate(consent_questions)
]

# Check if all checkboxes are checked
if all(consent_given):
    st.success("All consent given. Proceed to the next section of the survey.")
    st.error(
        """
        ⚠️ Please Note:

    - We do not collect personal identifiers. Therefore **closing the browser
     tab results in permanent data loss**.
    - **Switching WiFi networks** during the survey will cause a restart
     and loss of all progress.
    - For optimal performance, **use a laptop or desktop**;
     mobile device compatibility is limited.

        """)
    # If all checkboxes are checked, show the 'Next' button
    if st.button("Next"):
        # Redirect to the next section of the survey
        st.write("Redirecting to the next section...")
        switch_page(COMMUNITY_PAGE)

else:
    st.write("Please check check all statements to proceed.")
