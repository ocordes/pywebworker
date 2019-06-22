"""

src/workerapp.py

written by: Oliver Cordes 2019-06-16
changed by: Oliver Cordes 2019-06-16


"""

from pkg_resources import resource_string, resource_filename

import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_socketio import SocketIO

from pywebworker.threads import WorkerThreads
from pywebworker.utils import GlobalData


# some details about the programmers

__author__  = 'Oliver Cordes'
__email__   = 'ocordes@astro.uni-bonn.de'
__version__ = '0.0.1'
__copyright__ = '2019 by {}'.format(__author__)



bootstrap = Bootstrap()

# since we are working from a module directory, manually set
# the root_path of all internal ressources
flask_app = Flask('WebWorker', root_path=resource_filename(__name__, ''))

socketio = SocketIO(flask_app, manage_session=False)

# initialize the flask modules
bootstrap.init_app(flask_app)


workerthreads = WorkerThreads()

globaldata = GlobalData()


@flask_app.context_processor
def utility_processor():
    return { 'app_name': 'WebWorker',
             'app_version': __version__,
             'app_copyright': __copyright__ }


class WebWorkerApp(object):
    def __init__(self, title=None):


        self._title = title

        self._running = False


    def run(self):
        socketio.run(flask_app,
                    host='0.0.0.0',
                    port=5000,
                    debug=True)


    def start(self):
        self._running = True


    def stop(self):
        self._running = False



    @property
    def is_running(self):
        return self._running

    # decorator handling
    def maintask(self, f):
        print('Register main task:', f.__name__)

        workerthreads.register_main_thread(f, self)

        return f


    def register_worker(self, worker, worker_config):
        workerthreads.register_worker(worker)


    def run_workers(self):
        workerthreads.run_workers()


    def wait_worker_done(self):
        workerthreads.wait_worker_done()
