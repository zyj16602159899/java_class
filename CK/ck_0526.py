# 3. 多线程-共享全局变量

# 多线程全局变量的问题
# 如果多个线程同时对同一个全局变量操作，会出现资源竞争问题，从而数据结果会不正确!此时最简单的同步机制就是引入互斥锁！
# 互斥锁为资源引入一个状态：锁定/非锁定
# 某个线程要更改共享数据时，先将其锁定，此时资源的状态为“锁定”，其他线程不能更改直到该线程释放资源，将资源状态
# 变成“非锁定”，其他的线程才能再次锁定该资源
# 互斥锁保证了每次只有一个线程进行写入操作，从而保证了多线程情况下数据的正确性

# threading模块中定义了lock类，可以处理锁定。
# mutex = threading.Lock()      创建锁
# mutex.acquire()               锁定
# mutex.release()               释放

# 锁的好处：确保了某段关键代码只能由一个线程从头到尾完整地执行
# 锁的坏处：
# 1.阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率大大下降
# 2.由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁

# 注意：（多个线程同时用多把锁，会有死锁的情况出现）
# 1.如果这个锁之前是没有上锁的，那么acquire不会堵塞
# 2.如果在调用acquire对这个锁上锁之前，它已经被其他线程上了锁，那么此时acquire会堵塞，直到这个锁被解锁为止

# 全局解释器锁：GIL

# 描述python GIL的概念，以及它对python多线程的影响？

# python单线程和多线程分别来完成工作，到底哪个快？
# 网络io密集型：多线程快
# cpu密集型：单线程快



import threading
import time

a = 100

def func1():
    global a
    for i in range(1000000):
        meta.acquire()      # 上锁
        a += 1
        meta.release()      # 释放锁
    print('线程1修改后的a:',a)

def func2():
    global a
    for i in range(1000000):
        meta.acquire()
        a += 1
        meta.release()
    print('线程2修改后的a:',a)


meta = threading.Lock()         # 创建锁

t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)

t1.start()
t2.start()
t1.join()
t2.join()
print(a)