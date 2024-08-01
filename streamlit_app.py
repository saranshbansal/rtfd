import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.preprocessing import LabelEncoder

from config import sidebar_options, team_members, pt, model_evaluations
from model.simulations import fig, df

# Page config
st.set_page_config(page_title="RTFD - BoA", page_icon=":money_with_wings:")

# Sidebar menu
st.sidebar.title("Real-time Fraud Detection using Machine Learning")
st.sidebar.caption("by Team FinAPI")
selected_label = st.sidebar.selectbox("Menu", list(sidebar_options.keys()))
page_index = sidebar_options[selected_label]

# ML model
model = joblib.load('model/fraud_detector.joblib')


# Function to preprocess input data
def preprocess_data(data):
    input_df = data.copy()
    preprocessed_data = pd.DataFrame()
    le = LabelEncoder()
    preprocessed_data['step'] = input_df['step']
    preprocessed_data['type'] = le.fit_transform(input_df['type'])
    preprocessed_data['amount'] = np.log1p(input_df['amount'])
    preprocessed_data['oldbalanceOrg'] = input_df['oldbalanceOrg']
    preprocessed_data['newbalanceOrig'] = input_df['newbalanceOrig']
    preprocessed_data['oldbalanceDest'] = input_df['oldbalanceDest']
    preprocessed_data['newbalanceDest'] = input_df['newbalanceDest']
    return preprocessed_data


# Function to make predictions using the loaded model
def predict(data):
    preprocessed_data = preprocess_data(data)
    model_predictions = model.predict(preprocessed_data)
    return model_predictions


# Main content based on the selected page
if page_index == 1:
    st.header("Real-time Fraud Detection using ML")
    st.image("static/images/cyber-theft-senior-fraud-GIF.gif", width=500)

    st.subheader("🗿 History")
    st.write('''
            With the advent of digital transactions, the possibility of money laundering have also soared up with 
            the use of tech. Millions of investigators are on the field fighting against the fraudulent transactions. In the 
            current industry we have a large inflow of false positives hits and it consumes a long time to clear the false 
            positive hits. Customers across the world using fintech platforms demand lightning fast services. Hence 
            automating the hits with machine learning and reducing the false positive hits is our aim. But not at the cost of 
            leaving out the false negatives. Hence we need to be more mindful about false negatives when we try to reduce the 
            false positives.
    ''')
    st.subheader("📌 Objective")
    st.write('''
             The objective of this project is to serve as a pluggable middleware that detects transaction 
             patterns and aids machine learning algorithms in identifying these patterns, thereby enabling the 
             real-time flagging of fraudulent transactions. It utilizes a dataset containing transaction records and 
             aims to build models that can accurately classify fraudulent transactions.
    ''')
    st.subheader("🎯 Goals")
    st.write("- Exploratory analysis of global data to extract the pattern of fraudulent activities.")
    st.write("- Re-use/Build a machine learning model to classify fraud and non-fraud transactions.")
    st.write("- Provide real-time feedback to end users about potential fraudulent transactions and ask for consent "
             "before approving the transaction.")
    st.write("- Reduce the false positives by feeding back customer responses and tuning the model.")
    st.write("- Provide an end-user driven ruleset modification to support variety of domains.")

    st.subheader("📁 Dataset")
    st.write("The dataset used in this project is obtained from: https://www.kaggle.com/datasets/ealaxi/paysim1. It "
             "contains transaction logs with various features including `step, type, amount, nameOrig, nameDest, "
             "isFlaggedFraud, and isFraud`.")
elif page_index == 2:
    st.title("Payments Simulator")
    st.subheader("This section offers controls to simulate user-initiated payments, allowing for the assessment of "
                 "potential fraud.")
    st.write("You can adjust various parameters to simulate different scenarios, including both fraudulent and "
             "legitimate transactions.")

    # Transaction details from users
    _type = st.selectbox(label='Select payment type', options=pt)
    step = st.slider('Step', min_value=1)
    amount = st.number_input('Amount', min_value=0.0)
    oldbalanceOrg = st.number_input('Source Account')
    newbalanceOrig = oldbalanceOrg - amount
    oldbalanceDest = st.number_input('Destination Account')
    newbalanceDest = oldbalanceDest + amount

    # Create a df from the input data
    input_data = pd.DataFrame({'type': [_type],
                               'step': [step],
                               'amount': [amount],
                               'oldbalanceOrg': [oldbalanceOrg],
                               'newbalanceOrig': [newbalanceOrig],
                               'oldbalanceDest': [oldbalanceDest],
                               'newbalanceDest': [newbalanceDest]
                               })

    # Make predictions on button click
    if st.button('Predict'):
        predictions = predict(input_data)

        if predictions[0] == 1:
            st.warning("Our analysis indicates a significant risk of fraud based on the algorithm's findings.")

            # Customer consent to block or approve transaction
            st.write("Would you like to place a request to block the transaction?")
            confirm = st.checkbox("Yes, I am sure")
            reject = st.checkbox("No")

            if confirm and reject:
                st.warning("Please select only one option.")
            elif confirm:
                st.write("Transaction block request raised successfully. Our team will review the request and take "
                         "appropriate action.")
            elif reject:
                st.write("Transaction complete!")
            else:
                st.info("Please make a selection to proceed.")
        else:
            st.success("Transaction is safe.")

elif page_index == 3:
    st.title("Analytics")
    st.subheader("This section offers insights and analytics on fraud detection, leveraging historical transaction "
                 "data and feedback from the model.")
    st.info("Please note that the data is intended for simulation purposes only and is not dynamically generated.")

    # Plot simulated data
    st.pyplot(fig)

elif page_index == 4:
    st.title("Dataset")
    st.subheader("This section offers insights and analytics on dataset used to train the model. The dataset used in "
                 "this project is obtained from: https://www.kaggle.com/datasets/ealaxi/paysim1.")

    st.caption("First few rows of the processed dataframe")
    st.table(df.head())

    st.caption("Evaluating accuracy of different classifiers")
    st.table(pd.DataFrame(model_evaluations))

elif page_index == 5:
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
