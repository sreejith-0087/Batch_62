import _thread, time

t1 = True
t2 = True

def dis(name):
    global t1
    for i in range(1, 11):
        print(f"{i}.{name}")
        time.sleep(1)
    t1 = False


def dis1(name):
    global t2
    for i in range(1, 11):
        print(f"{i}.{name}")
        time.sleep(1)
    t2 = False


_thread.start_new_thread(dis, ('Ajith',))
_thread.start_new_thread(dis1, ('Jinu',))

while t1 or t2:
    pass