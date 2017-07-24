import threading
import time


def producer():
    print 'I am making baozi, do not push or I will get angry'
    event.wait()
    event.clear()
    print 'sb is coming for baozi...'
    print 'making a baozi for sb...'
    time.sleep(3)
    event.set()
    print 'your baozi is ready'



def consumer():
    print 'I am waiting for baozi'
    event.set()
    time.sleep(2)
    print 'demi:waiting for baozi to be ready'
    while True:
        if event.isSet():


            break
        else:
            print 'haimeihao'
            time.sleep(2)

    print 'thanks..'


event = threading.Event()

a = threading.Thread(target=producer)
b = threading.Thread(target=consumer)
a.start()
b.start()
