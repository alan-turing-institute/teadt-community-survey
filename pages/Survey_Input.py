import streamlit as st

st.markdown("# Survey Form Input :page_facing_up:")
st.sidebar.markdown("# Survey Form")

st.markdown("## Some Examples")
st.markdown("The following represent some options for input elements provided by [streamlit.io](https://streamlit.io/). The full list can be found here: [https://docs.streamlit.io/library/api-reference/widgets](https://docs.streamlit.io/library/api-reference/widgets)")

st.markdown("### Q1: A Radio Button")
genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

st.markdown("### Q2: A Generic Text Input")

title = st.text_input('Movie title', 'Life of Brian')

st.markdown("### Q3: A SelectBox")

choice = st.selectbox("Pick One", ["apples", "bananas", "carrots"])

st.markdown("### Q4: A Slider")

slider = st.slider("On a scale of 1 to 5, where `1` is 'strongly disagree' and `5` is 'strongly agree'...", 1, 5)

st.markdown("### Optional Comments")
txt = st.text_area(
    "Text to analyze",
    "Add freeform text to this box.",
    )

st.write(f'You wrote {len(txt)} characters.')

st.markdown("## Results")
st.dataframe(data = {
    "Q1": genre,
    "Q2": title,
    "Q3": choice,
    "Q4": slider
})

