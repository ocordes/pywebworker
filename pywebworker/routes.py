"""

src/routes.py

written by: Oliver Cordes 2019-06-16
changed by: Oliver Cordes 2019-06-22


"""


from pywebworker.workerapp import socketio, flask_app, workerthreads, globaldata

from flask import render_template, session, request, jsonify


@flask_app.route('/products', methods=['GET'])
@flask_app.route('/users', methods=['GET'])
@flask_app.route('/reports', methods=['GET'])
@flask_app.route('/index', methods=['GET'])
@flask_app.route('/', methods=['GET'])
def index():
    return render_template('index.html', debug=True, title='Dashboard')


@flask_app.route('/orders', methods=['GET'])
def base():
    return render_template('base.html', debug=True, title='Orders')



@flask_app.route('/ajax/start_thread', methods=['GET'])
def start_thread():
    workerthreads.start_main_thread()
    return jsonify(msg='Thread-Start: OK')


@flask_app.route('/ajax/stop_thread', methods=['GET'])
def stop_thread():
    workerthreads.stop_main_thread()
    return jsonify(msg='Thread-Stop: OK')


@flask_app.route('/ajax/running', methods=['GET'])
def running():
    return jsonify(status=workerthreads.is_running)


@flask_app.route('/ajax/messages', methods=['GET'])
def messages():
    return jsonify(msgs=globaldata.get_messages())
