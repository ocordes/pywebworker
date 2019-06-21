"""

pywebworker/threads.py

written by: Oliver Cordes 2019-06-21
changed by: Oliver Cordes 2019-06-21

"""

from threading import Thread


class WorkThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.running = True


    def set_running(self, status):
        self.running = status



class WorkerThreads(object):
    def __init__(self):
        self._worker_threads = []
        self._main_thread_func = None
        self._main_thread = None
        self._app = None


    def register_main_thread(self, f, app):
        self._main_thread_func = f
        self._main_thread = Thread(target=f)
        self._app = app


    def start_main_thread(self):
        if self._app.is_running:
            print('task is already running')
        else:
            self._app.start()
            self._main_thread = Thread(target=self._main_thread_func)
            self._main_thread.start()


    def stop_main_thread(self):
        self._app.stop()


    def register_worker(self, worker):
        self._worker_threads.append(worker)


    def run_workers(self):
        for w in self._worker_threads:
            w.start()


    def wait_worker_done(self):
        for w in self._worker_threads:
            w.join()

        # now start with an empty thread list
        self._worker_threads = []
