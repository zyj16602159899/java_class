# 2.对有参数、没有返回值的函数进行装饰


def set_func(func):
    def call_func(a):
        print("---权限验证---")
        func(a)
    return call_func


@set_func
def test1(num):
    num = num + 100
    print("最新的num是{}".format(num))


@set_func
def test2(num):
    num = num + 88
    print("最新的num是{}".format(num))


test1(88)
test1(788)
test2(100)
test2(200)
