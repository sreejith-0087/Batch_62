import threading, time


class Mythread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name


    def run(self):
        for i in range(1, 11):
            print(f"{i}.{self.name}")
            time.sleep(1)

t1 = Mythread('Ajith')
t2 = Mythread('Jinu')
t1.start()
t2.start()

