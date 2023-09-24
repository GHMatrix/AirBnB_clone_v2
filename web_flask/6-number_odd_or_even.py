#!/usr/bin/python3
"""
This script starts a Flask web application with seven routes.
"""

from flask import Flask, render_template
from urllib.parse import unquote

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display 'C' followed by the value of the text variable"""
    text = unquote(text).replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display 'Python' followed by the
    value of the text variable (or default)"""
    text = unquote(text).replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page with 'Number: n' if n is an integer"""
    return render_template('6-number_template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display an HTML page with 'Number: n is even|odd' if n is an integer"""
    if n % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return render_template(
            '6-number_odd_or_even.html', number=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
