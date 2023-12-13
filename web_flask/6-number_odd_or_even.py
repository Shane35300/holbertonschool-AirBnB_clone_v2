#!/usr/bin/python3
"""
Start a flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""

    message = "Hello HBNB!"
    return message


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display 'hbnb'"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C ' followed by the value of the text variable"""

    # Replace underscores with spaces in the text
    formatted_text = text.replace('_', ' ')
    return 'C {}'.format(formatted_text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_route(text='is_cool'):
    if text:
        modified_text = text.replace('_', ' ')
        return 'Python {}'.format(modified_text)
    else:
        return 'Python is cool'


@app.route('/number_template/<n>', strict_slashes=False)
def number(n):
    try:
        int_value = int(n)
        return render_template('5-number.html', value=int_value)
    except ValueError:
        return render_template('404.html'), 404


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    try:
        int_value = int(n)
        if int_value % 2 == 0:
            return render_template('6-number_odd_or_even.html',
                                   value=int_value, odd_even='even')
        else:
            return render_template('6-number_odd_or_even.html',
                                   value=int_value, odd_even='odd')
    except ValueError:
        return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
