import streamlit as st
import pandas as pd
import numpy as np

st.markdown("# Survey Results")
st.sidebar.markdown("# Survey Results")

st.markdown("The following page could be populated with all the data gathered from the survey. There are various elements available on streamlit's documentation: [https://docs.streamlit.io/library/api-reference/charts](https://docs.streamlit.io/library/api-reference/charts)")
st.markdown("## An Example Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)
