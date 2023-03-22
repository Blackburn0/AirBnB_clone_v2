#!/usr/bin/python3
"""Displays 'Hello HBNB!' on the web page using Flask"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """ C is fun """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is_cool"):
    """ Python is cool """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0")
