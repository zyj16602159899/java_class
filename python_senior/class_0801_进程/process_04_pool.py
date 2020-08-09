from multiprocessing import Pool
import os
import time
import random


# 进程池Pool
# 当创建的子进程数量比较多时，手动去创建进程的工作量巨大，此时就可以用到multiprocessing模块提供的Pool方法。
# 初始化Pool时，可以指定一个最大进程数，当有新的请求提交到Pool时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果
# 池中的进程数已经达到指定的最大值，那么该请求就会等待，直到池中有进程结束，才会用之前的进程来执行新的任务。
def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%s" % (t_stop - t_start))


# 进程执行的时候，不加__name__ == '__main__'为什么会报错？(windows系统)
# 原因：无限递归
if __name__ == '__main__':
    po = Pool(3)        # 定义一个进程池，最大进程数为3
    for i in range(0, 10):
        po.apply_async(worker, (i,))

    print('---start---')
    po.close()          # 关闭进程池，关闭后po不再接收新的请求
    po.join()           # 等待po中所有子进程执行完成，必须放在close语句之后
    print('---end---')
