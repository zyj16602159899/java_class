import greenlet
import time


def work1():
    for i in range(10):
        print('---work1---{}'.format(i))
        g2.switch()

def work2():
    for i in range(10):
        print('---work2---{}'.format(i))
        g1.switch()


g1 = greenlet.greenlet(work1)
g2 = greenlet.greenlet(work2)

g1.switch()