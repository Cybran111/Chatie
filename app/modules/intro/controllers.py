__author__ = 'cybran'

# Import flask dependencies
from flask import Blueprint, request, render_template, flash, session, redirect, url_for

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_intro = Blueprint('intro', __name__, url_prefix='/')

# Set the route and accepted methods
@mod_intro.route('/')
def intro():
    return render_template('intro/intro.html')