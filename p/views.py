from django.shortcuts import render
from django.http import HttpResponse

import threading, thread
from time import sleep
import logging

lg = logging.getLogger(__name__)

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the p index.")



def test(request, op=None, var=None):
    lg.debug("%s tested"%(op))
    if op == 'threading1':
        if type(var) is not int:
            var = 3
        i = 0
        while i < var:
            aw = AsyncWork(10)
            aw.start()
            i += 1
    elif op == 'threading2':
        threading.Thread(target=async_print, args=('Hellow World!',))
    elif op == 'thread':
        thread.start_new_thread(async_print, ('Hellowaaa', ))
    elif op == 'exception':
        try:
            1/0
        except ZeroDivisionError as err:
            lg.exception('')
    return HttpResponse("%s tested"%(op))


def async_print(msg):
    sleep(1)
    lg.debug('in async_print: %s'%(str(msg)))
    

class AsyncWork(threading.Thread):
    def __init__(self, var):
        threading.Thread.__init__(self)
        self.var = var if type(var) is int else 10
        
    def run(self):
        '''
        functions:
        'daemon', 'getName', 'ident', 'isAlive', 'isDaemon', 'is_alive', 'join', 'name', 'run', 'setDaemon', 'setName', 'start', 'var'
        For daemon, using while True here
'''
        i = self.var 
        while i > 0:
            #print '%s:  %d left'%(self.getName(),i)
            lg.debug('%s:  %d left'%(self.name,i))
            sleep(1)
            i -= 1
 
