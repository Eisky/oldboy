import threading
import time

num = 0
#num1 = 0


def run(x):
    time.sleep(1)
    global num
    #global num1
    samp.acquire()
    time.sleep(0.001)
    num += 1
    #samp.acquire()
    #num1+=2
    #samp.release()
    samp.release()
    #time.sleep(0.01)
    print '%s' % num



samp = threading.BoundedSemaphore(4)
for i in range(200):
    t = threading.Thread(target=run, args=[i])
    t.start()
