#!/usr/bin/python3
"""
Start a flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == '__main__':
    """ Run the application on 0.0.0.0, port 5000 """
    app.run(host='0.0.0.0', port=5000)
