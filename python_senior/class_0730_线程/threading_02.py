import time
import threading

# 使用threading创建线程有2种方式：
# 1是直接指定函数名，threading.Thread(target=函数名)
# 2是通过类来继承threading.Thread类，且类中必须定义(重写)一个run方法，并调用start()方法来创建线程。适用于一个线程做的事情比较复杂，分成
# 多个函数来做的情况，将其封装成一个类，在类中创建一个实例对象进行调用。


class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            msg = "I'm" + self.name + "@" + str(i)      # name属性中保存的是当前线程的名字
            print(msg)


if __name__ == '__main__':
    t = MyThread()
    print(threading.enumerate())
    t.start()
    print(threading.enumerate())
