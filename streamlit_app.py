import numpy as np
import pandas as pd
import streamlit as st

# Header
st.title("Real-time Fraud Detection using Machine Learning")
st.image("static/images/cyber-theft-senior-fraud-GIF.gif", width=300)

# Sidebar menu
st.sidebar.title("Control Panel")
st.sidebar.markdown("This is a sidebar menu.")
option = st.sidebar.selectbox(
    "Choose an option:",
    ("Option 1", "Option 2", "Option 3")
)

# Play with dataframes
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

