import os
import subprocess
import sys
from threading import Thread

from flask import Flask, render_template, redirect, url_for
from flask.cli import with_appcontext

app = Flask(__name__)

# Global variable to store the Streamlit process
streamlit_process = None


def run_streamlit():
    """
    Runs the Streamlit app in a separate process.
    """
    global streamlit_process
    streamlit_process = subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "streamlit_app.py"],
        env=os.environ.copy(),
    )


@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
