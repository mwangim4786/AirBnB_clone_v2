#!/usr/bin/python3
"""Script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Return string Hello HBNB! when route is queried
    """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb_flask():
    """Return string HBNB! when route is queried
    """
    return 'HBNB'

if __name__ == '__main__':i
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
