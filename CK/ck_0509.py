# 面向对象

# 魔术方法
# 定义：在python中，像__init__这种双下划线开头和结尾的方法，称之为魔术方法。
# 注意点：魔术方法都是python内部调用的，自己不要去定义__init__这种双下划线的方法。
# 
# __init__方法有什么作用？
# 在创建对象的时候，自动调用。对 创建的对象 进行初始化设置的。

# 1.__new__方法
# 创建实例对象的时候会触发此方法
# 应用场景：单例模式（只能实例化一个对象）

# 例：最简单的单例模式
class MyClass(object):
    instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance

n1 = MyClass()
n1.name = 'john'

n2 = MyClass()          # 返回的还是n1接收的对象，所以可以打印name属性
n2.age = 18


print(n2.name)
print(n1.age)           # 返回的都是同一个对象，因此n1.age可以打印成功

# 作业：装饰器实现单例模式！

def single(cls):
    instance = {}

    def fun(*args, ** kwargs):
        if cls in instance:
            return instance[cls]
        else:
            instance[cls] = cls(*args, **kwargs)
            return instance[cls]

    return fun


@single
class MyTest:
    pass

t1 = MyTest()