#!/usr/bin/python3
"""
Start a flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Route to display a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Route to display a list of cities by states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    # Triez les villes de chaque État
    for state in sorted_states:
        state.cities = sorted(state.cities, key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
