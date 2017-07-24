from threading import Thread
import time

class myThread(Thread):
    def run(self):
        time.sleep(4)
        Thread.run(self)
        print 'sunki is good'

    def Bar(self):
        print 'bar'

t1 = myThread(target=())
t1.start()
print 'over'