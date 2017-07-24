from threading import Thread
import time
for i in range(2):
    def Foo(x):
        for item in range(13):
            print item
            time.sleep(1)
            if item == 9:
                break


t1 = Thread(target=Foo(2))
t1.setDaemon(True)
t1.start()
t1.join(5)
print 'after'
