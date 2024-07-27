# routes/home_routes.py
from flask import Blueprint, render_template

user_bp = Blueprint('home', __name__)


@user_bp.route('/')
def home():
    return render_template('index.html')


@user_bp.route('/about')
def about():
    return render_template('about.html')
