"""

pywebworker/utils.py

written by: Oliver Cordes 2019-06-21
changed by: Oliver Cordes 2019-06-21

"""

import sys

import threading

transfer_messages = []

transfer_message_lock = threading.Lock()


def get_messages():
    global transfer_messages
    transfer_message_lock.acquire()
    msgs = transfer_messages
    transfer_messages = []
    transfer_message_lock.release()
    sys.stdout.write(msgs)
    return ['Hallo', 'Berta']
    #return msgs


def print(*vars):
    global transfer_messages
    s = ' '.join([str(i) for i in vars])
    transfer_message_lock.acquire()
    transfer_messages.append(s)
    transfer_message_lock.release()
    sys.stdout.write(s+'\n')
    sys.stdout.flush()
