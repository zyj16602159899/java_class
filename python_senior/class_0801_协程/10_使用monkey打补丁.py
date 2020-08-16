import time
import gevent
from gevent import monkey
# 使用monkey打补丁

# 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块
monkey.patch_all()


def test1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def test2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def test3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


# 一般使用此种方式：将所有任务都用列表包裹放到joinall中，更简洁方便。
gevent.joinall([gevent.spawn(test1, 5),
                gevent.spawn(test2, 5),
                gevent.spawn(test3, 5),
                ])
