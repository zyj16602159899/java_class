# gevent

# 协程存在于线程之中，线程默认不会等待协程执行。
# spawn：开启协程(第一个参数为协程要执行的任务)
# join:让线程等待协程执行

# 协程之间切换的条件：
# gevent.sleep()：协程耗时等待的情况下才会替换

# gevent的补丁
# gevent.monkey.patch_all()

# 首先考虑：协程 > 线程 > 进程


import time
import gevent
from gevent import monkey


monkey.patch_all()

def work1():
    for i in range(100):
        print('---work1---{}'.format(i))
        # gevent.sleep(0.1)
        time.sleep(0.01)

def work2():
    for i in range(100):
        print('---work2---{}'.format(i))
        # gevent.sleep(0.1)
        time.sleep(0.01)


# 创建2个协程
g1 = gevent.spawn(work1)
g2 = gevent.spawn(work2)

g1.join()
g2.join()