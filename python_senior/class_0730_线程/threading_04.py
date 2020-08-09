import time
import threading
# 多线程之间共享全局变量
global_num = 100


def test1():
    global global_num
    global_num += 100
    print(global_num)


def test2():
    print(global_num)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    time.sleep(1)
    t2.start()


if __name__ == '__main__':
    main()
