# 6.使用类当做装饰器


class Test(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("---这是类装饰器添加的功能---")
        return self.func()      # 注意：此处要加括号，代表返回调用的函数！


@Test
def test1():
    return "hello, Decorator!"


print(test1())
