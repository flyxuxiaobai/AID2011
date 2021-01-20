"""
卖票模拟线程
"""

from threading import Thread
from time import sleep

t = ["T%d" % i for i in range(1, 501)]


class Sell_ticket(Thread):
    def __init__(self, window, ticket):
        self.window = window
        self.ticket = ticket
        super().__init__()

    def run(self):
        while self.ticket:
            if len(self.ticket)< 10:
                sleep(1)
            else:
                sleep(0.1)
            print("%s ----%s" % (self.window, self.ticket.pop()))


if __name__ == '__main__':
    for i in range(1, 11):
        t = Sell_ticket({"window": "W%d" % i})
        t.start()
