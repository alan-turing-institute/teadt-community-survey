import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import mongo_utils
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
    SATISFACTION_PAGE,
    COMMUNITY_RESULTS_PAGE,
    SECTOR_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
)

# Verify user and display necessary UI components
verify_user(COMMUNITY_RESULTS_PAGE)
display_error_messages()
hide_pages(["Success"])


def display_top_elements(
    state_key, title, client, filter, user_elements, feedback_group, top_n
):
    # Query data
    data = mongo_utils.get_field_values(client, state_key, filter)
    response_lists = data[state_key]
    # Preprocess data
    filtered_responses = [
        item
        for sublist in response_lists
        for item in sublist
        if item != "Other (Please specify)"
    ]
    response_counts = Counter(filtered_responses)
    # Filter out the "None" option
    filtered_counts = Counter(
        {k: v for k, v in response_counts.items() if k != "None"}
    )
    top_elements = filtered_counts.most_common(top_n)
    # Determine user's overlap with top sector elements
    user_overlap = set(user_elements) & set([elem[0] for elem in top_elements])
    # Compare number of distinct elements applied
    element_counts_per_person = [
        len(set(sublist)) for sublist in response_lists
    ]
    current_user_element_count = len(set(user_elements))
    distribution_of_elements = Counter(element_counts_per_person)
    element_list = []
    for count, freq in distribution_of_elements.items():
        element_list.extend([count] * freq)
    # Calculate the average to compare with the user's count
    average_elements = round(np.mean(element_list))

    st.markdown(f"### Top {title} in Your Sector")
    # Determine feedback message based on comparison with average
    if current_user_element_count < average_elements:
        message = f""":warning: You are currently implementing
         {current_user_element_count} distinct {title.lower()},
         which is fewer than average compared to your peers.
        """
    elif current_user_element_count == average_elements:
        message = f""":white_check_mark: You are currently
         implementing {current_user_element_count} distinct
         {title.lower()}, which is an average amount compared to your peers.
        """
    else:
        message = f""":white_check_mark: You are currently
         implementing {current_user_element_count} distinct
         {title.lower()}, which is more than average
         compared to your peers.
         """
    st.write(message)
    # Feedback on user's choice compared to sector
    if user_overlap:
        st.write(
            f""":white_check_mark: You've selected
              {title.lower()} that are commonly used:
                {', '.join(user_overlap)}.
                """
        )
    else:
        st.write(
            f""":white_check_mark: Your selected {title.lower()}
             are not commonly reported {feedback_group}.
             Explore popular options below."""
        )
    top_elements = [
        (x[0].split(" (")[0], x[1]) for x in top_elements
    ]  # Change from dictionary to tuple
    bar_chart = horizontal_bar_labels(top_elements)
    st.plotly_chart(bar_chart)


st.title("Results: Your Practice")
page_element_keys = [
    SECTOR_STATE_KEY,
    ASSURANCE_MECHANISMS_STATE_KEY,
    ASSURED_PROPERTIES_STATE_KEY,
]

# Check if section has been filled in and retrieve relevant input fields
try:
    check_required_fields(page_element_keys, give_hint=True)
    current_user_sector = st.session_state[SECTOR_STATE_KEY]
    current_user_assurance_mechanisms = st.session_state[
        ASSURANCE_MECHANISMS_STATE_KEY
    ]
    current_user_assured_properties = st.session_state[
        ASSURED_PROPERTIES_STATE_KEY
    ]

    # Retrieve data from database and output info/graphics
    client = mongo_utils.init_connection()
    if client:
        # check how many submissions already
        total_response_count = mongo_utils.check_response_count(
            client, threshold=10
        )

        # check if data will be displayed grouped by sector
        query = {SECTOR_STATE_KEY: current_user_sector}
        response_data = mongo_utils.count_responses(client, query)
        filter = {}
        feedback_group = "across all sectors"
        response_match = response_data.get(SECTOR_STATE_KEY, 0)
        if response_match > 3:
            filter = {"sector": current_user_sector}
            feedback_group = f"in your sector {current_user_sector}"
        else:
            response_match = total_response_count
        st.write(
            f"""We are comparing your answer against
              {response_match} entries {feedback_group}."""
        )

        # Display top assurance mechanisms
        display_top_elements(
            ASSURANCE_MECHANISMS_STATE_KEY,
            "Assurance Mechanisms",
            client,
            filter,
            current_user_assurance_mechanisms,
            feedback_group,
            5,
        )

        # Display top assured principles
        display_top_elements(
            ASSURED_PROPERTIES_STATE_KEY,
            "Assured Principles",
            client,
            filter,
            current_user_assured_properties,
            feedback_group,
            3,
        )

    else:
        st.error("Could not connect to the database.")

except ValueError:
    # Exception message is human-readable
    st.info(
        "This page will show personalized insights"
        " based on your assurance practices, "
        "please make sure to fill in the previous sections."
    )

if st.button("Continue"):
    # Redirect to the next section of the survey
    switch_page(SATISFACTION_PAGE)
