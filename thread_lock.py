"""
线程锁示例
"""
from threading import Thread, Lock
from time import sleep
lock = Lock()
a = b = 0


def value():
    while True:
        # print("我来上锁啦")
        # lock.acquire()
        if a != b:
            print("a = %d, b=%d" % (a, b))
        # lock.release()


t = Thread(target=value)
t.start()

while True:
    # print("我也来上锁啦")
    lock.acquire()
    a += 1
    print(a)
    b += 1
    print(b)
    lock.release()
