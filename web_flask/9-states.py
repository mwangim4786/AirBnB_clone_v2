
#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    """Render template with states in sorted order by name
    """
    path = '9-states.html'
    states = storage.all(State)
    return render_template(path, states=states)

# Route for '/states/<id>'
@app.route('/states/<id>')
def states_by_id(id):
    """Render template with states id if exists
    """

    path = '9-states.html'
    # Loop through all states
    for state in storage.all("State").values():
        # check if current state id matches requested state id
        if state.id == id:
            return render_template(path, state=state)
    return render_template(path)


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)

