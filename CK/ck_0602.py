# 进程

# 进程：一个程序运行起来后，代码+用到的资源称之为进程，它是操作系统分配资源的基本单元。
# 不仅可以通过线程完成多任务，进程也是可以的。

# 进程的状态：
# 工作中，任务数往往大于cpu的核数，即一定有一些任务正在执行，而另外一些任务在等待cpu进行执行，因此导致有了不
# 同的状态。
# 就绪状态：运行的条件都已经满足了，正在等待cpu执行
# 执行状态：cpu正在执行其功能
# 等待状态：等待某些条件满足，例如一个程序sleep了，此时就处理等待状态

# 多进程不共享全局变量

import time
from multiprocessing import Process


def work1():
    for i in range(10):
        print('this is task one !')
        time.sleep(0.5)


def work2():
    for i in range(10):
        print('this is task two !')
        time.sleep(0.5)


# 进程执行的时候，不加__name__ == '__main__'为什么会报错？(windows系统)
# 原因：无限递归
if __name__ == '__main__':
    # 创建2个进程
    p1 = Process(target=work1)
    p2 = Process(target=work2)

    p1.start()
    p2.start()

