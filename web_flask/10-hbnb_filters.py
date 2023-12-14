#!/usr/bin/python3
"""
Start a flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()


@app.route('/hbnb_filter', strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html'"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    sorted_amenities = sorted(amenities, key=lambda x: x.name)

    # Triez les villes de chaque État
    for state in sorted_states:
        state.cities = sorted(state.cities, key=lambda x: x.name)

    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           amenities=sorted_amenities)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
