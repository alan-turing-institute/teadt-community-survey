import streamlit as st
from db_utils import create_connection
import plotly.graph_objects as go
import pandas as pd
from streamlit_extras.switch_page_button import switch_page 

st.title("Part 2 Results: Current Practices")

# Function to query data for the Sankey chart
def query_sankey_data(conn):
    # Query the database for the relevant columns in the assurance_survey table
    df = pd.read_sql("SELECT sector, assurance_methods, properties_assured FROM assurance_survey", conn)
    
    # Initialize lists for source, target, and value
    source = []
    target = []
    value = []
    
    # Unique lists for sectors, methods, and properties to build labels
    sectors = df['sector'].unique().tolist()
    methods = df['assurance_methods'].str.split(', ').explode().unique().tolist()
    properties = df['properties_assured'].str.split(', ').explode().unique().tolist()
    
    # Label list combining sectors, methods, and properties
    label = sectors + methods + properties
    
    # Map sectors, methods, and properties to their index in the label list
    sector_index = {sector: i for i, sector in enumerate(sectors)}
    method_index = {method: i + len(sectors) for i, method in enumerate(methods)}
    property_index = {property: i + len(sectors) + len(methods) for i, property in enumerate(properties)}
    
    # Aggregate data
    for _, row in df.iterrows():
        sector = row['sector']
        if pd.notna(row['assurance_methods']) and pd.notna(row['properties_assured']):
            for method in row['assurance_methods'].split(', '):
                # Connect sector to method
                source.append(sector_index[sector])
                target.append(method_index[method])
                value.append(1)  # Increment the value for this connection by 1
                
                for property in row['properties_assured'].split(', '):
                    # Connect method to property
                    source.append(method_index[method])
                    target.append(property_index[property])
                    value.append(1)  # Increment the value for this connection by 1
    
    return source, target, value, label

# Function to create a Sankey chart
def create_sankey_chart(source, target, value, label):
    fig = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=label,
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        ))])

    fig.update_layout(title_text="Flow from Sector to Assurance Methods to Properties Assured", font_size=10)
    return fig

conn = create_connection('mock_survey_results.db')
if conn:
    source, target, value, label = query_sankey_data(conn)

    # Create and display the Sankey chart
    sankey_chart = create_sankey_chart(source, target, value, label)
    st.plotly_chart(sankey_chart)

    conn.close()
else:
    st.error("Could not connect to the database.")

if st.button('Next'):
    # Redirect to the next section of the survey
    st.write("Redirecting to next part...")  
    switch_page("Goals_Frameworks")
