#!/usr/bin/env python3
"""Basic Flask and Babel app setup with internationalization support"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
from pytz import timezone
import pytz.exceptions


class Config(object):
    """Configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """Determines the best match with supported languages"""
    local = request.args.get('locale', '')
    if local in app.config['LANGUAGES']:
        return local

    if g.user:
        local = g.user.get('locale')
        if local in app.config['LANGUAGES']:
            return local

    local = request.headers.get('locale', None)
    if local in app.config['LANGUAGES']:
        return local
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@babel.timezoneselector
def get_timezone() -> str:
    """This determines and returns the timezone"""
    tz = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        tz = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


def get_user():
    """This gets user dict or None"""
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """This executes before any request"""
    user = get_user()
    g.user = user


@app.route('/')
def get_index() -> str:
    """Handles / route"""
    g.time = format_datetime()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
