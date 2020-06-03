# 进程池
from multiprocessing import Pool,Manager
import os
import time
import requests


a = 0

def work(q):
    while q.qsize > 0:
        global a
        url = q.get()
        requests.get(url)
        print('work正在执行任务{}'.format(os.getpid()))
        a += 1


if __name__ == '__main__':
    q = Manager().Queue()

    for i in range(10):
        q.put('http://www.baidu.com')

    pool = Pool(5)
    while True:
        if q.qsize() > 0:
            pool.apply_async(work, args=(q,))
        else:
            break

    pool.close()
    pool.join()