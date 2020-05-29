# 并发和性能

# 一、并发和并行

# 1.多任务
# 概念：简单来说，就是操作系统可以同时运行多个任务
# 真正的并行执行多任务只能在多核cpu上实现，但由于任务数量远远多于cpu的核心数量，所以操作系统也会自动把很多任务
# 轮流调度到每个核心上执行。

# 2.并发和并行
# 并发：指的是任务数多于cpu核数，通过操作系统的各种任务调度算法，实现用多个任务“一起”执行（实际上总有一些任务
# 不在执行，因为切换任务的速度相当快，看上去一起执行而已）
# 并行：指的是任务数小于等于cpu核数，即任务真的是一起执行的
# 串行

# 3.同步和异步
# 同步：即同步协调，是指线程在访问某一资源时，获得了资源的返回结果后才会执行其他操作（先做某件事，再做某件事）
# 异步：与同步相对，指线程在访问某一资源时，无论是否取得返回结果，都进行下一步操作；当有了资源返回结果时，系统
# 自会通知线程。


# 二、线程

# 1. threading模块介绍
# 创建线程：threading.Thread(target=func)
# 参数target指定线程执行的任务（函数）
# 方法              # 说明
# run()             用以表示线程活动的方法
# start()           启动线程活动
# join(time)        设置主线程会等待time秒后再往下走，time默认为子线程结束，多个子线程之间设置的时间值会叠加
# is_alive()         返回线程是否活动的
# getName()         返回线程名
# setName()         设置线程名

# threading.currentThread():    返回当前执行的线程
# threading.enumerate():        返回正在运行的所有线程（list）。正在运行执线程启动后，结束前，不包括启动前和终止后的线程。
# threading.activeCount():      返回正在运行的线程数量


# 2. 多线程实现多任务
# （1）使用Thread类来创建线程
# 第一步：创建线程      t1 = threading.Thread(target=func)
# 第二步：启动线程      t1.start()      # 当调用start()时，才会真正的创建线程，并且开始执行


# import time
# import threading


# def func1():
#     for i in range(5):
#         time.sleep(1)
#         print('---事情1---')

# def func2():
#     for i in range(6):
#         time.sleep(1)
#         print('---事情2---')


# t1 = threading.Thread(target=func1, name='th_1')     # 创建一个线程去执行事情1
# t2 = threading.Thread(target=func2, name='th_2')     # 创建一个线程去执行事情2

# print(t1.name)          # 打印t1的name属性（方法一）
# print(t2.name)
# print(t1.getName())     # 打印t1的name属性（方法二）
# print(t2.getName())
# t1.setName('线程1')     # 设置t1的name属性
# print(t1.getName())

# start_time = time.time()
# print(t1.is_alive())
# t1.start()      # 开始执行线程1
# print(t1.is_alive())
# t2.start()      # 开始执行线程2

# print(threading.active_count())         # 打印当前活动线程的数量
# print(threading.enumerate())            # 打印所有活动的线程
# print(threading.current_thread())       # 打印当前活动的线程

# t1.join()       # 设置主线程等待子线程结束后再往下走
# t2.join()
# end_time = time.time()

# print('耗时：',end_time-start_time)

# （2）通过继承Thread类来创建线程
# 传参数需要重写__init__方法（重写之后要调用父类的init方法）

import threading
import requests


class RequestThread(threading.Thread):
    """发送requests请求"""

    def __init__(self, url):
        self.url = url
        super().__init__()      # 必须调用父类的__init__方法！

    def run(self):
        res = requests.get(self.url)
        print('线程：{}--返回的状态码：{}'.format(threading.current_thread(),res.status_code))


for i in range(5):
    t = RequestThread('http://www.baidu.com')
    t.start()