from multiprocessing import Process
import time
# 进程：一个程序运行起来之后，代码+用到的资源被称之为进程，它是操作系统分配资源的基本单元。
# 不仅可以通过线程完成多任务，进程也是可以的。


def test1():
    while True:
        print("---1---")
        time.sleep(1)


def test2():
    while True:
        print("---2---")
        time.sleep(1)


def main():
    p1 = Process(target=test1)
    p2 = Process(target=test2)
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
