import gevent
# 协程依赖于线程，线程依赖于进程


def test1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def test2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


def test3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.5)


g1 = gevent.spawn(test1, 5)
g2 = gevent.spawn(test2, 5)
g3 = gevent.spawn(test3, 5)
g1.join()
g2.join()
g3.join()
