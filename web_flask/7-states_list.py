#!/usr/bin/python3
"""
Starts a Flask web application that displays a list of states.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Handles the /states_list route and displays a list of states.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_session(exception):
    """
    Closes the SQLAlchemy session after each request.
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
