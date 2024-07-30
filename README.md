# Real-time Fraud Detection using Machine Learning

This is a Streamlit application for showcasing real-time fraud detection using machine learning algorithms.

## 🗿 History
Ever since the advent of internet the digital revolution has rising and has crept into all aspects to our
lives. One of the most important digital revolution happened in financial system and especially transacting money to
someone from any part of the world digitally. Digital transactions have become a part of daily life like purchasing a
product online, sending money to friends, depositing cash in bank account, investment purposes etc., They had a lot of
benefits so does pave way for fraudulent activities. People started using digital money transactions medium to launder
money and make the money look like it comes from a legal source.

## 🎯 Objective
The objective of this application is to find the patterns of transactions performed and help algorithms learn
those patterns in identifying the fraudulent transactions and flag them.

## 📌 Goals

- Exploratory analysis of data to extract the pattern of fraudulent activities.
- Build a machine learning model to classify fraud and non-fraud transactions.
- Reduce the false negatives by tuning the model.

## 📁 Dataset
The dataset used in this project is obtained from the file `PS_20174392719_1491204439457_log.csv`. 
It contains transaction logs with various features including `step, type, amount, nameOrig, nameDest, isFlaggedFraud, and isFraud`.

### Dataset description¶
`step` - maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).

`type` - CASH-IN, CASH-OUT, DEBIT, PAYMENT and TRANSFER.

`amount` - amount of the transaction in local currency.

`nameOrig` - customer who started the transaction

`oldbalanceOrg` - initial balance before the transaction

`newbalanceOrig` - new balance after the transaction

`nameDest` - customer who is the recipient of the transaction

`oldbalanceDest` - initial balance recipient before the transaction. Note that there is not information for customers that start with M (Merchants).

`newbalanceDest` - new balance recipient after the transaction. Note that there is not information for customers that start with M (Merchants).

`isFraud` - This is the transactions made by the fraudulent agents inside the simulation. In this specific dataset the fraudulent behavior of the agents aims to profit by taking control or customers accounts and try to empty the funds by transferring to another account and then cashing out of the system.

`isFlaggedFraud` - The business model aims to control massive transfers from one account to another and flags illegal attempts. An illegal attempt in this dataset is an attempt to transfer more than 200.000 in a single transaction.

## 📥 Installation

1. Clone the repository:

   `git clone https://github.com/your-username/your-project.git`

2. Navigate to the project directory:

   `cd your-project`

3. Create a virtual environment (optional but recommended):

   `python -m venv env source env/bin/activate`

4. Install the required dependencies:

   `pip install -r requirements.txt`

5. Set up the environment variables (if applicable):

   `export SECRET_KEY=your-secret-key`

   `export DATABASE_URL=your-database-url`

6. Run the Streamlit application:

   `streamlit run streamlit_app.py`

The application should now be running at `http://localhost:5000`.
