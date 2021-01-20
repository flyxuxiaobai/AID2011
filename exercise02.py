from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()
l = []


def value1():
    for i in range(65, 91):
        lock1.acquire()
        print(chr(i))
        lock2.release()


def value2():
    for i in range(1, 53, 2):
        lock2.acquire()
        print(i)
        print(i+1)
        lock1.release()


t1 = Thread(target=value1)
t2 = Thread(target=value2)
lock1.acquire()
t1.start()
t2.start()
print(l)
