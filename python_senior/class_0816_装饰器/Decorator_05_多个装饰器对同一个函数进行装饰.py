# 5.多个装饰器对同一个函数进行装饰
# 当同一个函数有多个装饰器时，先装饰下面的，再装饰上面的；但执行时，先执行上面的，再执行下面的。


def add_01(func):
    print("---1---")

    def call_func(*args, **kwargs):
        print("---装饰器1---")
        return func(*args, **kwargs)
    return call_func


def add_02(func):
    print("---2---")

    def call_func(*args, **kwargs):
        print("---装饰器2---")
        return func(*args, **kwargs)
    return call_func


@add_01
@add_02
def test1(num, age=22):
    num = num + 100
    return num, age


res = test1(88)
print(res)
