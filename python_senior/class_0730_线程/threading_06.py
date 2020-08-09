import time
import threading
# 多线程任务的资源竞争问题
# 互斥锁
global_num = 0


def test1(num):
    global global_num
    mutex.acquire()         # 执行上锁。如果之前没有上锁，此时上锁成功；如果已被上锁，此时会堵塞在此处，直到被解开为止
    for i in range(num):
        global_num += 1
    mutex.release()         # 解锁
    print(global_num)


def test2(num):
    global global_num
    mutex.acquire()         # 互斥锁放在for循环外面，会执行完for循环内代码后才解锁。放在for循环里面，会每执行一次运算就解锁
    for i in range(num):
        global_num += 1
    mutex.release()
    print(global_num)


# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))
    t1.start()
    t2.start()
    time.sleep(1)


if __name__ == '__main__':
    main()
