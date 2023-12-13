#!/usr/bin/python3
"""
Start a flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hbnb_filter', strict_slashes=False)
def display_html():
    """display a HTML page like 6-index.html'"""
    return render_template('10-hbnb_filters.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
