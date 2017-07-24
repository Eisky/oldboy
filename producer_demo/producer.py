from threading import Thread
import time
from Queue import Queue


class procuder(Thread):
    def __init__(self, name, queue):
        '''

        :param name: name of producer
        :param queue: maxsize of queue
        '''
        self.__name = name
        self.__queue = queue
        super(procuder, self).__init__()  # execute baseclass init function

    def run(self):
        while True:
            if self.__queue.full():
                time.sleep(1)
            else:
                self.__queue.put('steamed dumpling')
                time.sleep(1)
                print '%s produce steamed dumpling' % (self.__name)

        #Thread.run()


class consumer(Thread):
    '''

           :param name: name of consumer
           :param queue: maxsize of queue
           '''
    def __init__(self,name,queue):
        self.__name = name
        self.__queue = queue
        super(consumer, self).__init__()

    def run(self):
        if self.__queue.empty():
            time.sleep(1)
        else:
            self.__queue.get()
            print '%s consume steamed dumpling' % (self.__name)
            #Thread.run()


que = Queue(maxsize=10)
a1 = procuder('sunki',que)
a1.start()
a2 = procuder('demi',que)
a2.start()
a3 = procuder('yuki',que)
a3.start()
for item in range(10):
    name = 'sun%d' % (item)
    temp = consumer(name,que)
    temp.start()

