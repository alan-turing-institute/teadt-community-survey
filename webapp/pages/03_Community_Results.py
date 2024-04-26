import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from plot_utils import plot_pie_chart
import mongo_utils
from pymongo import MongoClient

st.title("Part 1 Results: Community Composition")

client: MongoClient = mongo_utils.init_connection()
if client:

    # Query data
    sector_data = mongo_utils.get_field_values(client, "sector")
    location_data = mongo_utils.get_field_values(client, "location")
    role_data = mongo_utils.get_field_values(client, "role")

    # Create columns for layout
    col1, col2, col3 = st.columns(3)

    # Plot pie charts and display them in their respective columns
    with col1:
        sector_chart = plot_pie_chart(
            sector_data["sector"], "Sectors Distribution"
        )
        st.pyplot(sector_chart)

    with col2:
        location_chart = plot_pie_chart(
            location_data["location"], "Locations Distribution"
        )
        st.pyplot(location_chart)

    with col3:
        role_chart = plot_pie_chart(role_data["role"], "Roles Distribution")
        st.pyplot(role_chart)

else:
    st.error("Could not connect to the database.")

if st.button("Continue"):
    # Redirect to the next section of the survey
    st.write("Redirecting to next part...")
    switch_page("Current_Practices")
