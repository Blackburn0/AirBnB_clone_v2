#!/usr/bin/python3
""" Renders a Web page with the list of all the States stores on the DB
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the current session with the DB """
    storage.close()


@app.route('/states', strict_slashes=False)
def display_states_list():
    """ Renders the list of states in a web page """
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states=states_list)


@app.route('/states/<id>', strict_slashes=False)
def display_a_state(id):
    """ Displays the details of the state with the specified ID """
    states = storage.all(State).values()
    for state in states:
        if id == state.id:
            return render_template('9-states.html', state=state)
    return "<H1>Not found!</H1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
