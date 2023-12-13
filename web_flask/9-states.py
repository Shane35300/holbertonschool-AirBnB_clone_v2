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


@app.route('/states', strict_slashes=False)
def states_list():
    """Route to display a list of states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """Route to display a list of cities by states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    # Triez les villes de chaque État
    for state in sorted_states:
        if state.id == id:
            state_name = 'State: {}'.format(state.name)
            city_name = 'Cities:'
            state.cities = sorted(state.cities, key=lambda x: x.name)

            return render_template('9-states.html',
                                   state_name=state_name,
                                   city_name=city_name,
                                   state_cities=state.cities)

    return render_template('9-states.html', state_name='Not found!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
