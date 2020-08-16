# 3.对不定长参数的函数进行装饰


def set_func(func):
    def call_func(*args, **kwargs):
        print("---对不定长参数的函数进行装饰---")
        func(*args, **kwargs)
    return call_func


@set_func
def test1(num, age=22):
    num = num + 100
    print("最新的num是{}".format(num))
    print("年龄是%d" % age)


test1(88)
test1(788, 30)
