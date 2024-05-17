import streamlit as st
from st_pages import hide_pages
import pandas as pd
import numpy as np
from pymongo import MongoClient
import mongo_utils
from plot_utils import plot_principles_2d
from streamlit_utils import (
    verify_user,
    display_error_messages,
    check_required_fields,
    map_response_to_int,
)
from streamlit_extras.switch_page_button import switch_page  # type: ignore
from config import (
    RELEVANCE_GOOD_STATE_KEY,
    RELEVANCE_VALUE_STATE_KEY,
    RELEVANCE_INSIGHT_STATE_KEY,
    RELEVANCE_SECURITY_STATE_KEY,
    RELEVANCE_OPENNESS_STATE_KEY,
    RELEVANCE_QUALITY_STATE_KEY,
    RELEVANCE_FEDERATION_STATE_KEY,
    RELEVANCE_CURATION_STATE_KEY,
    RELEVANCE_EVOLUTION_STATE_KEY,
    CHALLENGE_GOOD_STATE_KEY,
    CHALLENGE_VALUE_STATE_KEY,
    CHALLENGE_INSIGHT_STATE_KEY,
    CHALLENGE_SECURITY_STATE_KEY,
    CHALLENGE_OPENNESS_STATE_KEY,
    CHALLENGE_QUALITY_STATE_KEY,
    CHALLENGE_FEDERATION_STATE_KEY,
    CHALLENGE_CURATION_STATE_KEY,
    CHALLENGE_EVOLUTION_STATE_KEY,
    COMMUNICATING_ASSURANCE_PAGE,
    SECTOR_STATE_KEY,
    GOALS_FRAMEWORK_PAGE,
)

# List of keys for relevance and challenge
relevance_keys = [
    RELEVANCE_GOOD_STATE_KEY,
    RELEVANCE_VALUE_STATE_KEY,
    RELEVANCE_INSIGHT_STATE_KEY,
    RELEVANCE_SECURITY_STATE_KEY,
    RELEVANCE_OPENNESS_STATE_KEY,
    RELEVANCE_QUALITY_STATE_KEY,
    RELEVANCE_FEDERATION_STATE_KEY,
    RELEVANCE_CURATION_STATE_KEY,
    RELEVANCE_EVOLUTION_STATE_KEY,
]

challenge_keys = [
    CHALLENGE_GOOD_STATE_KEY,
    CHALLENGE_VALUE_STATE_KEY,
    CHALLENGE_INSIGHT_STATE_KEY,
    CHALLENGE_SECURITY_STATE_KEY,
    CHALLENGE_OPENNESS_STATE_KEY,
    CHALLENGE_QUALITY_STATE_KEY,
    CHALLENGE_FEDERATION_STATE_KEY,
    CHALLENGE_CURATION_STATE_KEY,
    CHALLENGE_EVOLUTION_STATE_KEY,
]

# Verify user and display necessary UI components
verify_user(GOALS_FRAMEWORK_PAGE)
display_error_messages()
hide_pages(["Success"])

st.title("Results: Your Practice")
page_element_keys = [SECTOR_STATE_KEY] + relevance_keys

try:
    check_required_fields(page_element_keys, give_hint=True)

    current_user_sector = st.session_state[SECTOR_STATE_KEY]

    client: MongoClient = mongo_utils.init_connection()
    if client:
        # check if data will be displayed grouped by sector
        query = {
            SECTOR_STATE_KEY: st.session_state[SECTOR_STATE_KEY],
        }
        response_data = mongo_utils.count_responses(client, query)
        filter = {}
        feedback_group = "across all sectors"
        if response_data["sector"] > 1:
            filter = {"sector": current_user_sector}
            feedback_group = "with that"
            f" of your peers in sector {current_user_sector}"

        # Retrieve all data first
        all_data = {
            key: mongo_utils.get_field_values(client, key, filter).get(key, [])
            for key in relevance_keys + challenge_keys
        }

        # Now apply the mapping function
        ratings_data = {
            key: [
                map_response_to_int(response, key)
                for response in all_data[key]
            ]
            for key in relevance_keys + challenge_keys
        }

        # Calculating averages and preparing data for plotting
        data = []
        for key in relevance_keys:
            challenge_key = "challenge" + key[len("relevance"):]
            relevant_data = [
                val for val in ratings_data[key] if val is not None
            ]
            challenge_data = [
                val for val in ratings_data[challenge_key] if val is not None
            ]
            if (
                relevant_data and challenge_data
            ):  # Ensure data is present for both dimensions
                avg_relevance = np.mean(relevant_data)
                avg_challenge = np.mean(challenge_data)
                item_name = (
                    key.replace("relevance", "").replace("_", " ").title()
                )
                data.append(
                    {
                        "Item": item_name,
                        "Relevance": avg_relevance,
                        "Challenge": avg_challenge,
                    }
                )

        user_data = []
        for key in relevance_keys:
            challenge_key = "challenge" + key[len("relevance"):]
            if key in st.session_state and challenge_key in st.session_state:
                user_relevance = map_response_to_int(
                    st.session_state[key], key
                )
                user_challenge = map_response_to_int(
                    st.session_state[challenge_key], challenge_key
                )
                if user_relevance is not None and user_challenge is not None:
                    item_name = (
                        key.replace("relevance", "").replace("_", " ").title()
                    )
                    user_data.append(
                        {
                            "Item": item_name,
                            "Relevance": user_relevance,
                            "Challenge": user_challenge,
                        }
                    )

        st.markdown(
            "### Compare your assessment of the Gemini Principles"
            f" {feedback_group}!"
        )
        df = pd.DataFrame(data)
        user_df = pd.DataFrame(user_data)
        st.plotly_chart(plot_principles_2d(df, user_df))

except ValueError:
    st.info(
        "This page will show personalized insights"
        " on perceptions of the Gemini Principles amongst your peers."
        " Please make sure to fill in the previous sections."
    )


if st.button("Continue"):
    # Redirect to the next section of the survey
    switch_page(COMMUNICATING_ASSURANCE_PAGE)
