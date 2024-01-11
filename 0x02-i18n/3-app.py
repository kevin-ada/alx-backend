#!/usr/bin/env python3
from flask import Flask, render_template,request
from flask_babel import Babel
"""task 2: Get Locale Request"""

class Config:
    """Creation of a custom class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)



@babel.localeselector
def get_locale():
    """Returns a list of accepted languages"""

    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def hello() -> str:
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(debug=True)