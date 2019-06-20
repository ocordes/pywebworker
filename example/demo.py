"""

example/demo.py

written by: Oliver Cordes 2019-06-16
changed by: Oliver Cordes 2019-06-16
"""


import time


from pywebworker.workerapp import WebWorkerApp



app = WebWorkerApp()


def worker1(self):

    print('Download meter ...')

    for i in range(10):
        print('Download ({}%)'.format(i*10))
        time.sleep(1)


    print('Download complete!')





@app.maintask
def main():
    print('main task')
    pass
