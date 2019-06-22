"""

pywebworker/utils.py

written by: Oliver Cordes 2019-06-21
changed by: Oliver Cordes 2019-06-21

"""

import sys

import threading

max_lines = 10

class GlobalData(object):
    msg_lock = threading.Lock()

    def __init__(self):
        self._messages = []


    def get_messages(self):
        self.msg_lock.acquire()
        msgs = self._messages
        #self._messages = []
        self.msg_lock.release()
        return msgs


    def print(self, *vars):
        s = ' '.join([str(i) for i in vars])
        self.msg_lock.acquire()
        self._messages.append(s)
        if len(self._messages) > max_lines:
            self._messages.pop(0)
        self.msg_lock.release()

        print(s,flush=True)
