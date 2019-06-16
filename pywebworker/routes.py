"""

src/routes.py

written by: Oliver Cordes 2019-06-16
changed by: Oliver Cordes 2019-06-16


"""


from pywebworker.workerapp import socketio, flask_app

from flask import render_template, session, request, jsonify

@flask_app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
