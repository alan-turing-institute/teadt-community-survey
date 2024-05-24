import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import Counter
from matplotlib.cm import get_cmap
from plotly.subplots import make_subplots
import plotly.express as px


def get_colors_from_colormap(num_colors):
    colormap = get_cmap("Pastel1")  # Get the colormap
    # Generate colors from the colormap
    colors = [colormap(i) for i in np.linspace(0, 1, num_colors)]
    return colors


# Function to plot a pie chart
def plot_pie_chart(data: list, current_user_sector, title, figsize=(3, 3)):
    # Count occurrences
    sector_counts = Counter(data)

    # Prepare the pie chart data
    total = sum(sector_counts.values())
    threshold = 0.1 * total
    pie_data = {}
    other_sum = 0

    for sector, count in sector_counts.items():
        if count >= threshold or sector == current_user_sector:
            pie_data[sector] = count
        else:
            other_sum += count

    if other_sum > 0:
        pie_data["Other"] = other_sum

    # Plotting the pie chart
    labels = pie_data.keys()
    sizes = pie_data.values()
    # Get pastel colormap
    num_items = len(pie_data)  # Number of colors needed
    colors = get_colors_from_colormap(num_items)

    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors
    )
    ax.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title(title, pad=25)
    return fig


def horizontal_bar_labels(categories):
    subplots = make_subplots(
        rows=len(categories),
        cols=1,
        subplot_titles=[x[0] for x in categories],
        shared_xaxes=True,
        print_grid=False,
        vertical_spacing=(0.45 / len(categories)),
    )
    subplots["layout"].update(
        width=550,
        plot_bgcolor="#fff",
    )

    # add bars for the categories
    for k, x in enumerate(categories):
        subplots.add_trace(
            dict(
                type="bar",
                orientation="h",
                y=[x[0]],
                x=[x[1]],
                text=["{:,.0f}".format(x[1])],
                hoverinfo="text",
                textposition="auto",
                marker=dict(
                    color="#7030a0",
                ),
            ),
            k + 1,
            1,
        )

    # update the layout
    subplots["layout"].update(
        showlegend=False,
    )
    for x in subplots["layout"]["annotations"]:
        x["x"] = 0
        x["xanchor"] = "left"
        x["align"] = "left"
        x["font"] = dict(
            size=12,
        )

    # hide the axes
    for axis in subplots["layout"]:
        if axis.startswith("yaxis") or axis.startswith("xaxis"):
            subplots["layout"][axis]["visible"] = False

    # update the margins and size
    subplots["layout"]["margin"] = {
        "l": 0,
        "r": 0,
        "t": 20,
        "b": 1,
    }
    height_calc = 45 * len(categories)
    height_calc = max([height_calc, 350])
    subplots["layout"]["height"] = height_calc
    subplots["layout"]["width"] = height_calc

    return subplots


def plot_principles_2d(df, user_df=None):
    # Add a column to distinguish the datasets
    df["Dataset"] = "Sector Data"
    if user_df is not None:
        user_df["Dataset"] = "Your Data"

    # Combine the datasets if user data is available
    combined_df = pd.concat([df, user_df]) if user_df is not None else df

    # Create jittered x and y coordinates
    jitter_strength = 0.1  # Adjust the jitter strength as needed
    combined_df["Challenge_jittered"] = combined_df["Challenge"] + np.random.uniform(-jitter_strength, jitter_strength, size=len(combined_df))
    combined_df["Relevance_jittered"] = combined_df["Relevance"] + np.random.uniform(-jitter_strength, jitter_strength, size=len(combined_df))

    # Create a scatter plot with jittered values
    fig = px.scatter(
        combined_df,
        x="Challenge_jittered",
        y="Relevance_jittered",
        text="Item",
        hover_name="Item",
        color="Dataset",
        range_x=[0, 6],
        range_y=[1, 6],
        color_discrete_map={
            "Sector Data": "blue",  # Specify colors for better control
            "Your Data": "red",
        },
    )

    # Update the text position and marker properties
    fig.update_traces(
        textposition="top center",
        marker=dict(size=12, opacity=0.4)
    )

    # Customize axis ticks using the mapping
    relevance_mapping = {
        "Not Relevant": 1,
        "Slightly Relevant": 2,
        "Moderately Relevant": 3,
        "Very Relevant": 4,
        "Extremely Relevant": 5,
    }
    challenge_mapping = {
        "Not challenging at all": 1,
        "Slightly challenging": 2,
        "Moderately challenging": 3,
        "Very challenging": 4,
        "Extremely challenging": 5,
    }
    total_min_x = min(min(df["Challenge"]), min(user_df["Challenge"])) - 0.2
    total_max_x = max(max(df["Challenge"]), max(user_df["Challenge"])) + 0.2
    total_min_y = min(min(df["Relevance"]), min(user_df["Relevance"])) - 0.2
    total_max_y = max(max(df["Relevance"]), max(user_df["Relevance"])) + 0.2

    fig.update_layout(
        xaxis_title="Degree of Challenge",
        yaxis_title="Degree of Relevance",
        xaxis=dict(
            tickmode="array",
            tickvals=list(challenge_mapping.values()),
            ticktext=list(challenge_mapping.keys()),
            range=[total_min_x, total_max_x],
        ),
        yaxis=dict(
            tickmode="array",
            tickvals=list(relevance_mapping.values()),
            ticktext=list(relevance_mapping.keys()),
            range=[total_min_y, total_max_y],
        ),
    )

    return fig
