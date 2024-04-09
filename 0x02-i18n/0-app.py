#!/usr/bin/env python3
"""Module is basic Flask app setup"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Hello world"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0", debug=True)
