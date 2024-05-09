import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from plot_utils import plot_pie_chart
import mongo_utils
from pymongo import MongoClient
from streamlit_utils import (
    verify_user,
    display_error_messages,
    check_required_fields,
)
from config import (
    CURRENT_PRACTICES_PAGE,
    COMMUNITY_RESULTS_PAGE,
    SECTOR_STATE_KEY,
    ROLE_STATE_KEY,
    TYPE_DT_STATE_KEY,
)
from st_pages import hide_pages

# Verify user and display necessary UI components
verify_user(COMMUNITY_RESULTS_PAGE)
display_error_messages()
hide_pages(["Success"])

st.title("Results: Your Representation")
page_element_keys = [SECTOR_STATE_KEY, ROLE_STATE_KEY, TYPE_DT_STATE_KEY]

# Check if section has been filled in and retrieve relevant input fields
try:
    check_required_fields(page_element_keys, give_hint=True)
    current_user_sector = st.session_state[SECTOR_STATE_KEY]
    current_user_role = st.session_state[ROLE_STATE_KEY]

    # Retrieve data from database and output info/graphics
    client: MongoClient = mongo_utils.init_connection()
    if client:
        # Query data for charts
        sector_data = mongo_utils.get_field_values(client, "sector")
        role_data = mongo_utils.get_field_values(client, "role")

        # Counting responses that match the current user's profile
        query = {
            SECTOR_STATE_KEY: current_user_sector,
            ROLE_STATE_KEY: current_user_role,
        }
        response_data = mongo_utils.count_responses(client, query)

        # Assign the highest count to the variable profile_count
        profile_max_name = max(response_data, key=response_data.get)
        profile_max_value = response_data[profile_max_name]
        profile_min_name = min(response_data, key=response_data.get)
        profile_min_value = response_data[profile_min_name]

        # Providing feedback based on the count
        st.write("Based on your profile:")
        if response_data["sector"] > 1:
            message = f"""
                :white_check_mark: We've had
                **{response_data['sector']}** responses
                from digital twin practitioners in your sector.
                Continue filling in the pulse check
                and find out how your answers compare against theirs!
                """
        elif profile_max_value > 1:
            message = f"""
                :white_check_mark: We've had {profile_max_value}
                responses from people
                with a similar {profile_max_name}

                :warning: But we have had few responses from your sector.
                Help us enhance representation
                by sharing this survey with others.
                Improved representation will allow you
                 to more effectively compare
                your responses with those of your peers
                 when we share the results!
                """
        else:
            message = """
                :warning: We had too few responses
                 from people with your profile
                to share detailed results. Help us enhance representation
                by sharing this survey with others.
                Improved representation will allow you
                 to more effectively compare
                your responses with those of your peers
                 when we share the results!
                """
        st.write(message)

        st.write("#")

        # Displaying the Sector Distribution Pie Chart
        sector_chart = plot_pie_chart(
            sector_data["sector"],
            current_user_sector,
            "Sectors represented in our dataset so far",
        )
        st.pyplot(sector_chart)

    else:
        st.error("Could not connect to the database.")


except ValueError as e:
    # Exception message is human-readable
    st.warning(e)
    st.info(
        "This page will show personalized insights based on your profile, "
        "please make sure to fill in the previous sections."
    )


if st.button("Continue"):
    # Redirect to the next section of the survey
    switch_page(CURRENT_PRACTICES_PAGE)
