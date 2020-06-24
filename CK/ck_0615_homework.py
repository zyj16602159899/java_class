# 10000个请求，使用开启2个进程，进程中开启3个线程，线程中开启5个协程来处理。

import time
from threading import Thread
from multiprocessing import Process, Queue
import gevent
import requests


def green_work(q, gname):
    """每个协程的工作函数"""
    count = 0
    while not q.empty():
        url = q.get(timeout = 0.01)
        requests.get(url)
        gevent.sleep(0.001)
        count += 1
    print('---协程{}执行了{}个任务'.format(gname, count))

def thread_work(q, tname):
    # 每个线程的执行任务函数，在该线程中开启5个协程
    g_list = []
    for i in range(5):
        gname = '{}-g-{}'.format(tname, i)
        print('创建协程---{}'.format(gname))
        g = gevent.spawn(green_work, q, gname)
        g_list.append(g)
    gevent.joinall(g_list)

def process_work(q, pname):
    # 每个进程执行的任务函数，在该进程中开启3个线程
    # 创建3个线程，并执行
    thread_list = []
    for i in range(3):
        tname = '{}-th-{}'.format(pname, i)
        print('创建线程{}'.format(tname))
        t = Thread(target=thread_work, args=(q, tname))
        thread_list.append(t)
        t.start()
    # 让主线程堵塞，等待子线程
    for t in thread_list:
        t.join()

def count_time(func):
    "计算函数运行时间的装饰器"
    def wrapper(*args, **kwargs):
        print('开始执行')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print('执行结束')
        print('总耗时：{}'.format(end_time - start_time))
    return wrapper

@count_time
def main():

    # 创建10000个请求的队列
    q = Queue()

    for i in range(10000):
        q.put('http://127.0.0.1:5000')
    
    # 开启2个进程处理
    print('队列创建完成：数量{}'.format(q.qsize()))
    pro_list = []
    for i in range(2):
        pname = 'pro-{}'.format(i)
        print('创建进程{}'.format(pname))
        p = Process(target=process_work, args=(q, pname))
        p.start()
        pro_list.append(p)
    # 让主进程等待子进程执行结束再往下执行
    for p in pro_list:
        p.join()