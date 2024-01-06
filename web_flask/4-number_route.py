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

@app.route('/number/<int:n>')
def number(n=None):
    """display n is a number only if n is an integer
    """
    return str(n) + ' is a number'

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
