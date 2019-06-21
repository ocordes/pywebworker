"""

example/demo2.py

written by: Oliver Cordes 2019-06-21
changed by: Oliver Cordes 2019-06-21
"""


import time


from pywebworker.workerapp import WebWorkerApp
from pywebworker.threads import WorkThread
from pywebworker.utils import print


app = WebWorkerApp()


max_workers = 4


worker_config = { 'messages' : True,
                  'progress' : ['Progress', 'Download'] }


class Worker(WorkThread):
    def __init__(self, nr):
        WorkThread.__init__(self)

        self.nr = nr


    def run(self):
        print('({}) Download meter ...'.format(self.nr))

        for i in range(10):
            print('({}) Download ({}%)'.format(self.nr, i*10))
            time.sleep(1)


        print('({})Download complete!'.format(self.nr))



@app.maintask
def main():
    print('Starting main task ...')
    while app.is_running:
        # spawn max workers

        nr_workers = max_workers
        for i in range(nr_workers):
            worker = Worker(i)
            app.register_worker(worker, worker_config)

        app.run_workers()
        app.wait_worker_done()

        time.sleep(1)
        print('Running')

    print('Stopping main task!')
