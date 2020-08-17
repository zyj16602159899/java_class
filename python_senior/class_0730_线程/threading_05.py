import time
import threading
# args参数
# target指定将来这个线程去哪个函数执行代码
# args指定将来调用函数的时候，传递什么数据。该属性是一个元组，如果只有一个参数也需要在末尾加逗号。


def test1(num):
    num.append(33)
    print(str(num))


def test2(num):
    print(num)


num_list = [11, 22]


def main():
    t1 = threading.Thread(target=test1, args=(num_list,))
    t2 = threading.Thread(target=test2, args=(num_list,))
    t1.start()
    time.sleep(1)
    t2.start()


if __name__ == '__main__':
    main()
