import matplotlib.pyplot as plt
from collections import Counter
import numpy as np


# Function to plot a pie chart
def plot_pie_chart(
    data: list, title, figsize=(4, 4)
):  # Adjusted figsize to make plots smaller
    counts = Counter(data)
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(
        [float(value) for value in counts.values()],
        labels=counts.keys(),
        autopct="%1.1f%%",
        startangle=140,
    )
    ax.set_title(title)
    return fig
