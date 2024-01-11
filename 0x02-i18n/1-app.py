#!/usr/bin/env python3
"""Task 1: babel setup
"""

class Config:
    """Config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"



from flask import Flask,render_template
from flask_babel import Babel

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False

@app.route('/')
def hello() -> str:
    return render_template('1-index.html')


