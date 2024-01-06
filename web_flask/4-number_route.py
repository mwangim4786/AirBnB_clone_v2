#!/usr/bin/python3
"""Script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Return string Hello HBNB! when route is queried
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb_flask():
    """Return string HBNB! when route is queried
    """
    return 'HBNB'

@app.route('/c/<text>')
def c_is_fun(text):
    """Return reformatted text
    """
    return 'C ' + text.replace('_', ' ')

@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Reformat text based on optional variable
    """
    return 'Python ' + text.replace('_', ' ')

@app.route('/number/<int:n>')
def number(n=None):
    """display n is a number only if n is an integer
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
