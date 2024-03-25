import streamlit as st
from db_utils import create_connection
import plotly.graph_objects as go
import pandas as pd

st.title("Part 2 Results: Current Practices")

# Function to query data for the Sankey chart
def query_sankey_data(conn):
    # Query the database for all rows in the assurance_survey table
    df = pd.read_sql("SELECT * FROM assurance_survey", conn)
    
    # Define your assurance methods and properties
    assurance_methods = ["Risk Assessment", "Impact Assessment", "Bias Audit", "Compliance Audit", 
                         "Conformity Assessment", "Formal Verification", "Model Cards", "None"]
    project_stages = ["Accuracy", "Fairness", "Privacy", "Robustness", "Transparency", "Other"]
    
    # Initialize lists for source, target, and value
    source = []
    target = []
    value = []
    
    # Label list combining methods and properties
    label = assurance_methods + project_stages
    
    # Map method and property to their index in the label list
    method_index = {method: i for i, method in enumerate(assurance_methods)}
    property_index = {property: i + len(assurance_methods) for i, property in enumerate(project_stages)}
    
    # Aggregate data
    for index, row in df.iterrows():
        for method in assurance_methods:
            for property in project_stages:
                column_name = f"{method}_{property}".replace(" ", "_").lower()
                if row[column_name]:  # If the method-property combination was selected
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

    fig.update_layout(title_text="Assurance Methods to Properties", font_size=10)
    return fig

conn = create_connection('survey_results.db')
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
    switch_page("Needs")
