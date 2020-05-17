#!usr/bin/env python

# 数据和自省

# 私有属性
# 类里面定义的变量叫类属性，类属性有2种，分为：公有属性/私有属性。都是可以继承的。
# 私有属性定义：
# 单下划线开头：_attr
# 双下划线开头：__attr

# python中并没有真正的私有化，但可用下划线得到伪私有，有一项大多数python代码都遵顼的习惯：带有下划
# 线，前缀名称应被视为非公开的API的一部分（无论是函数/方法，还是数据成员），它应被视为实现细节。


class Test(object):
    attr1 = 10          # 公有属性
    _attr = 100         # 私有属性，在外部可以直接访问
    __attr2 = 200       # 私有属性，在外部不能直接访问，被改名了，所以在外部访问不了，改成了_Test__attr2


t = Test()
# 类属性可以通过类和实例对象去访问
print(Test.attr1)
print(t.attr1)

# 私有属性
print(Test._attr)
print(t._attr)

print(Test._Test__attr2)
print(t._Test__attr2)

print(Test.__dict__)        # 所有的属性值

# __dict__
# 类调用__dict__属性，返回类属性的方法的字典
# 实例调用__dict__属性，返回的是实例相关的属性和方法

# __slots__
# 指定类对象所能绑定的属性
# 作用：
# 1.限制属性
# 2.节约内存：定义了slots属性之后，那么该对象不会再自动生成__dict__属性


class Base(object):

    __slots__ = ['name', 'age']

    def __init__(self, name):
        self.name = name

    pass


b = Base('xin')
print(b.__dict__)