import streamlit as st
import sqlite3
import matplotlib.pyplot as plt

# Function to plot a pie chart
def plot_pie_chart(data, title, figsize=(4, 4)):  # Adjusted figsize to make plots smaller
    counts = data.value_counts()
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    ax.set_title(title)
    return fig