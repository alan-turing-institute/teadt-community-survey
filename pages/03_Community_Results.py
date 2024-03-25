import streamlit as st
from streamlit_extras.switch_page_button import switch_page 
from db_utils import create_connection, query_data
from plot_utils import plot_pie_chart

st.title("Part 1 Results: Community Composition")

conn = create_connection('survey_results.db')
if conn:

    # Query data
    sector_data = query_data(conn, 'sector')
    location_data = query_data(conn, 'location')
    role_data = query_data(conn, 'role')

    # Create columns for layout
    col1, col2, col3 = st.columns(3)

    # Plot pie charts and display them in their respective columns
    with col1:
        sector_chart = plot_pie_chart(sector_data['sector'], 'Sectors Distribution')
        st.pyplot(sector_chart)

    with col2:
        location_chart = plot_pie_chart(location_data['location'], 'Locations Distribution')
        st.pyplot(location_chart)

    with col3:
        role_chart = plot_pie_chart(role_data['role'], 'Roles Distribution')
        st.pyplot(role_chart)

    conn.close()
else:
    st.error("Could not connect to the database.")

if st.button('Next'):
        # Redirect to the next section of the survey
        st.write("Redirecting to next part...")  
        switch_page("Capabilities")