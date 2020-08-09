import time
import threading


def sing():
    """唱歌5秒"""
    for i in range(5):
        print("---正在唱歌---")
        time.sleep(1)


def dance():
    """跳舞5秒"""
    for i in range(5):
        print("---正在跳舞---")
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)           # 当调用Thread时，没有创建线程
    print(threading.enumerate())
    t1.start()                                    # 当调用Thread创建出来的实例对象的start方法时，才会创建线程及让线程开始运行
    t2.start()
    print(threading.enumerate())                  # 打印当前所有线程（列表）


if __name__ == '__main__':
    main()