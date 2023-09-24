#!/usr/bin/python3
"""
Starts a Flask web application that displays a list of states and cities.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def list_states():
    """
    Handles the /states route and displays a list of states.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """
    Handles the /states/<id> route and displays a list of cities in a state.
    """
    state = storage.get(State, id)
    if state:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def close_session(exception):
    """
    Closes the SQLAlchemy session after each request.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
