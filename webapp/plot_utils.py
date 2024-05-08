import matplotlib.pyplot as plt
from collections import Counter
from matplotlib.cm import get_cmap


# Function to plot a pie chart
def plot_pie_chart(data: list, current_user_sector, title, figsize=(4, 4)):
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
    colormap = get_cmap("Pastel1")  # Pastel2 is also available
    colors = colormap.colors[: len(pie_data)]

    fig, ax = plt.subplots()
    ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors
    )
    ax.axis(
        "equal"
    )  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.set_title(title, pad=25)
    return fig
