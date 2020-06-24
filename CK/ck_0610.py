# 协程(微线程)

# 协程的本质是单任务
# 协程依赖于线程
# 相对线程来讲，占用的资源更少（几乎不占用资源）

# 通过生成器实现多任务
import time


def work1():
    for i in range(10):
        print('---work1---{}'.format(i))
        yield

def work2():
    for i in range(10):
        print('---work2---{}'.format(i))
        yield

g1 = work1()
g2 = work2()

while True:
    try:
        next(g1)
        next(g2)
    except StopIteration:
        break


# 1.什么是协程？

# 2.协程和线程的差异

# 3.greenlet
# 为了更好地使用协程来完成多任务，greenlet模块对其进行了封装，从而使得切换任务变得更加简单
# 安装方式：使用pip进行安装：pip install greenlet