import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import mongo_utils
from pymongo import MongoClient
from streamlit_utils import (
    verify_user,
    display_error_messages,
    check_required_fields,
)
from st_pages import hide_pages
from plot_utils import horizontal_bar_labels
from collections import Counter

# Config imports
from config import (
    CURRENT_PRACTICES_PAGE,
    COMMUNITY_RESULTS_PAGE,
    SECTOR_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
)

# Verify user and display necessary UI components
verify_user(COMMUNITY_RESULTS_PAGE)
display_error_messages()
hide_pages(["Success"])

st.title("Results: Your Practice")
page_element_keys = [SECTOR_STATE_KEY, ASSURANCE_MECHANISMS_STATE_KEY]

# Check if section has been filled in and retrieve relevant input fields
try:
    check_required_fields(page_element_keys, give_hint=True)
    current_user_sector = st.session_state[SECTOR_STATE_KEY]
    current_user_assurance_mechanisms = st.session_state[
        ASSURANCE_MECHANISMS_STATE_KEY
    ]
    # Retrieve data from database and output info/graphics
    client: MongoClient = mongo_utils.init_connection()
    if client:
        # Query data
        assurance_data = mongo_utils.get_field_values(
            client, "assurance_mechanisms", {"sector": current_user_sector}
        )
        response_lists = assurance_data["assurance_mechanisms"]
        # Preprocess data
        filtered_responses = [
            item
            for sublist in response_lists
            for item in sublist
            if item != "Other (Please specify)"
        ]
        response_counts = Counter(filtered_responses)
        top_assurance_mechanisms = response_counts.most_common(5)
        # Determine user's overlap with top three sector mechanisms
        user_overlap = set(current_user_assurance_mechanisms) & set(
            [mech[0] for mech in top_assurance_mechanisms]
        )

        # Compare number of distinct assurance mechanisms applied
        technique_counts_per_person = [
            len(set(sublist)) for sublist in response_lists
        ]
        current_user_technique_count = len(
            set(current_user_assurance_mechanisms)
        )

        distribution_of_techniques = Counter(technique_counts_per_person)
        technique_list = []
        for count, freq in distribution_of_techniques.items():
            technique_list.extend([count] * freq)

        # Calculate the percentile
        user_percentile = np.percentile(
            technique_list, current_user_technique_count, interpolation="lower"
        )

        # Calculate the average to compare with the user's count
        average_techniques = round(np.mean(technique_list))

        st.write(
            f"""
            We are comparing your answer against
            {len(response_lists)} entries from sector {current_user_sector}:
            """
        )

        # Determine feedback message based on comparison with average
        if current_user_technique_count < average_techniques:
            message = f"""
            :warning:  You are currently implementing
            {current_user_technique_count} distinct assurance
            mechansims, which is fewer than
            {user_percentile}% of your peers.
            """
        elif current_user_technique_count == average_techniques:
            message = f"""
            :white_check_mark:  You are currently implementing
            {current_user_technique_count} distinct assurance
            mechansims, which is an average
            amount compared to your peers.
            """
        else:
            message = f"""
            :white_check_mark:  You are currently implementing
            {current_user_technique_count} distinct assurance
            mechansims, which is more
            than {100 - user_percentile}% of your peers.
            """

        st.write(message)

        # Feedback on user's choice compared to sector
        if user_overlap:
            st.write(
                f"""
                :white_check_mark:  You've selected assurance mechanisms
                that are commonly used in your sector:
                {', '.join(user_overlap)}.
                This aligns well with sector standards shown below.
                """
            )
        else:
            st.write(
                """
                :white_check_mark:  Your selected assurance mechanisms
                are not commonly reported in your sector.
                Explore popular options below.
                """
            )

        top_assurance_mechanisms = [
            {"name": x[0].split(" (")[0], "value": x[1]}
            for x in top_assurance_mechanisms
        ]

        st.markdown("### Top Assurance Mechanisms in Your Sector")
        bar_chart = horizontal_bar_labels(top_assurance_mechanisms)
        st.plotly_chart(bar_chart)

    else:
        st.error("Could not connect to the database.")
except ValueError as e:
    # Exception message is human-readable
    st.warning(e)
    st.info(
        "This page will show personalized insights"
        " based on your assurance practices, "
        "please make sure to fill in the previous sections."
    )

if st.button("Continue"):
    # Redirect to the next section of the survey
    switch_page(CURRENT_PRACTICES_PAGE)
