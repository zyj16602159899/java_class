# 4.对带有返回值的函数进行装饰
# 通用装饰器


def set_func(func):
    def call_func(*args, **kwargs):
        print("---对带有返回值的函数进行装饰---")
        return func(*args, **kwargs)
    return call_func


@set_func
def test1(num, age=22):
    num = num + 100
    return num, age


res = test1(88)
print(res)
data = test1(788, 30)
print(data)
