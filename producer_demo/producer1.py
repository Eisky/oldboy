import threading
import Queue
import random
import time


def Producer(name, que):
    while True:
        if que.qsize() < 3:
            que.put('dumpling')
            print '%s:made a dumpling' % name
        elif que.qsize() > 6:
            break

    time.sleep(random.randrange(3))


def Consumer(name, que):
    while True:
        try:
            que.get_nowait()
            print '%s:got a dumpling' % name
        except Exception:
            print 'no dumpling left'
    time.sleep(random.randrange(3))


que = Queue.Queue()
p1 = threading.Thread(target=Producer, args=['chef1', que])
p2 = threading.Thread(target=Producer, args=['chef2', que])
p1.start()
p2.start()

c1 = threading.Thread(target=Consumer, args=['sunki', que])
c2 = threading.Thread(target=Consumer, args=['demi', que])
c1.start()
c2.start()
