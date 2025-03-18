import threading, time


class Mythread(threading.Thread):
    def __init__(self, a, b ):
        threading.Thread.__init__(self)
        self.a = a
        self.b = b


    def run(self):
        #Get lock to synchronize threads
        threadlock.acquire()
        for i in range(self.a, self.b + 1):
            print(i)
            time.sleep(1)
        # Free lock to release next thread
        threadlock.release()


threadlock = threading.Lock()

t1 = Mythread(1, 10)
t2 = Mythread(11, 20)
t1.start()
t2.start()