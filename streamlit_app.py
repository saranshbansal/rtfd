import numpy as np
import pandas as pd
import streamlit as st

from config import sidebar_options, team_members

# Cool tab icon
st.set_page_config(page_title="RTFD - BoA", page_icon=":money_with_wings:", layout="wide")

# Sidebar menu
st.sidebar.title("Real-time Fraud Detection using Machine Learning")
selected_label = st.sidebar.selectbox("", list(sidebar_options.keys()))
page_index = sidebar_options[selected_label]

# Main content based on the selected page
if page_index == 1:
    left_co, cent_co, last_co = st.columns(3)
    with cent_co:
        st.image("static/images/cyber-theft-senior-fraud-GIF.gif", width=500)
    st.subheader("🗿 History")
    st.write("Ever since the advent of the internet, the digital revolution has permeated all aspects of our lives. "
             "One of the most significant impacts has been on the financial system, particularly in facilitating "
             "digital transactions worldwide. Digital transactions have become an integral part of daily life, "
             "whether purchasing products online, sending money to friends, depositing cash into bank accounts, "
             "or investing. While these digital transactions offer numerous benefits, they also provide opportunities "
             "for fraudulent activities. Some individuals use digital transaction methods to launder money, "
             "making illicit funds appear to come from legitimate sources.")
    st.subheader("📌 Objective")
    st.write("The objective of this application is to find the patterns of transactions performed and "
             "help algorithms learn those patterns in identifying the fraudulent transactions and flag them.")
    st.subheader("🎯 Goals")
    st.write("- Exploratory analysis of data to extract the pattern of fraudulent activities.")
    st.write("- Build a machine learning model to classify fraud and non-fraud transactions.")
    st.write("- Reduce the false negatives by tuning the model.")
elif page_index == 2:
    st.title("Make Payments")
    st.subheader("This section allows users to make payments through various methods.")
    st.write("Users can enter payment details, select a payment method, and complete the transaction.")
elif page_index == 3:
    st.title("Analytics")
    st.subheader("This section provides insights and analytics related to fraud detection.")
    st.write("It could include graphs, charts, or data visualizations.")

    # Example: Display a line chart
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
elif page_index == 4:
    st.title("Meet the team")
    st.markdown("""
        <style>
        .team-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-around;
        }
        .team-member {
            text-align: center;
            margin: 20px;
        }
        .team-member img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
            object-fit: cover;
        }
        .team-member h3 {
            margin-top: 10px;
            font-size: 1.2em;
        }
        .team-member p {
            margin-top: 5px;
            color: grey;
            font-size: 1em;
        }
        </style>
    """, unsafe_allow_html=True)
    # Display team members in a grid layout
    st.markdown('<div class="team-container">', unsafe_allow_html=True)
    left_co, right_co = st.columns(2)
    for index, member in enumerate(team_members, start=1):
        if index < 3:
            with left_co:
                # Load local image
                img = member["image_path"]
                # Display team member
                st.markdown(f"""
                    <div class="team-member">
                        <img src={img} alt="Alt Text" />
                        <h3>{member['name']}</h3>
                        <p>{member['designation']}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            with right_co:
                # Load local image
                img = member["image_path"]
                # Display team member
                st.markdown(f"""
                    <div class="team-member">
                        <img src={img} alt="Alt Text" />
                        <h3>{member['name']}</h3>
                        <p>{member['designation']}</p>
                    </div>
                """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
