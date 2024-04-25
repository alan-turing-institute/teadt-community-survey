import streamlit as st
import plotly.graph_objects as go
from streamlit_extras.switch_page_button import switch_page
import mongo_utils
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import Cursor
import itertools

st.title("Part 2 Results: Current Practices")


# Function to query data for the Sankey chart
def query_sankey_data(client: MongoClient):
    # Query the database for the relevant columns in the assurance_survey table

    collection: Collection = mongo_utils.get_survey_collection(client)
    query_results: Cursor = collection.find(
        filter={},
        projection=["sector", "assurance_methods", "properties_assured"],
    )
    results_as_list: list[dict] = list(query_results)

    # Initialize lists for source, target, and value
    source = []
    target = []
    value = []

    # Unique lists for sectors, methods, and properties to build labels
    sectors: set[str] = {result["sector"] for result in results_as_list}
    methods: set[str] = set(
        itertools.chain.from_iterable(
            [
                result["assurance_methods"].split(",")
                for result in results_as_list
                if "assurance_methods" in result
            ]
        )
    )
    properties: set[str] = set(
        itertools.chain.from_iterable(
            [
                result["properties_assured"].split(",")
                for result in results_as_list
                if "properties_assured" in result
            ]
        )
    )

    # Label list combining sectors, methods, and properties
    label: list[str] = list(sectors) + list(methods) + list(properties)

    # Map sectors, methods, and properties to their index in the label list
    sector_index = {sector.strip(): i for i, sector in enumerate(sectors)}
    method_index = {
        method.strip(): i + len(sectors) for i, method in enumerate(methods)
    }
    property_index = {
        current_property.strip(): i + len(sectors) + len(methods)
        for i, current_property in enumerate(properties)
    }

    # Aggregate data
    for row in results_as_list:

        sector = row["sector"]
        if (
            "assurance_methods" in row
            and row["assurance_methods"] is not None
            and "properties_assured" in row
            and row["properties_assured"] is not None
        ):
            for method in row["assurance_methods"].split(", "):
                # Connect sector to method
                source.append(sector_index[sector.strip()])
                target.append(method_index[method.strip()])
                value.append(1)  # Increment the value for this connection by 1

                for current_property in row["properties_assured"].split(", "):
                    # Connect method to property
                    source.append(method_index[method.strip()])
                    target.append(property_index[current_property.strip()])
                    value.append(1)  # Increment the value for this connection by 1

    return source, target, value, label


# Function to create a Sankey chart
def create_sankey_chart(source, target, value, label):
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=label,
                ),
                link=dict(source=source, target=target, value=value),
            )
        ]
    )

    fig.update_layout(
        title_text="Flow from Sector to Assurance Methods to Properties " "Assured",
        font_size=10,
    )
    return fig


client: MongoClient = mongo_utils.init_connection()
if client:
    source, target, value, label = query_sankey_data(client)

    # Create and display the Sankey chart
    sankey_chart = create_sankey_chart(source, target, value, label)
    st.plotly_chart(sankey_chart)

else:
    st.error("Could not connect to the database.")

if st.button("Next"):
    # Redirect to the next section of the survey
    st.write("Redirecting to next part...")
    switch_page("Goals_Frameworks")
