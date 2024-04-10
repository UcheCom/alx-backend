#!/usr/bin/env python3
"""Module gets locale from request"""
from flask import Flask, render_template, g, request
from flask_babel import Babel


class Config(object):
    """Configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determines the best match with supported languages"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Hello world"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
