import time
# 1.对没有参数、没有返回值的函数进行装饰
# 统计一个函数的运行时间


def set_func(func):
    def call_func():
        print("---权限验证---")
        start_time = time.time()
        func()
        end_time = time.time()
        print("函数运行时间为：%f" % (end_time - start_time))
    return call_func


@set_func
def test1():
    for i in range(1000000):
        pass
    print("---test1---")


test1()
