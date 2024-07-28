# Real-time Fraud Detection using Machine Learning

This is a Flask web application for real-time fraud detection using machine learning algorithms.

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
