# 元类

# 1.旧式类VS新式类
# 在python范畴中，一个类可以是两种类型之一。它们被非正式的称为旧式类和新式类。

# 旧式类
# 对于旧式类，类(class)和类型(type)并不完全相同。一个旧式类的实例总是继承自一个名为instance的内置类型。
# 如果obj是旧式类的实例，那么obj.class就表示该类，但type(obj)始终是instance类型。

# 新式类
# 新式类统一了类(class)和类型(type)的概念。如果obj是新式类的实例，type(obj)则与obj.class相同：
# 在python2中，默认所有类都是旧式类。
# 在python3中，所有类都是新式类。因此，python3可以交换一个引用对象的类型和类。

# type：python3中所有的类都是通过type来创建出来的：元类
# object：python3中所有类的顶级父类都是object

# 2.类(class)和类型(type)
# 在python中，一切都是对象，类也是对象。所以一个类(class)必须有一个类型(type)。
# 什么是元类？
# python中的任何新式类以及python中的任何类都是type元类的一个实例。函数type实际上是一个元类，type就是
# python在背后用来创建所有类的元类。
# 注意区分元类和继承的基类：
# type：是元类，所有的类都是通过type所创建出来的
# object：顶层的基类，所有类的继承顶层父类都是object

# 3.使用type动态定义类
# 内置type()函数在传递了一个参数时将返回一个对象的类型。对于新式类，通常与对象的class属性相同。
# type(name, bases, dict)调用type():
# name:指定类名称，将成为该类的name属性
# bases:指定继承类的基类元组，将成为该类的bases属性
# dict:指定包含类主体定义的名称空间字典，将成为该类的dict属性


class Test(object):
    pass


t = Test()
print(type(t))
print(type(Test))
print(type(type))       # type的类型也是type

# 以这种方式调用type()将创建一个type元类的新实例。换句话说，它动态地创建了一个新的类
Use = type('User', (object,), {'name': 'xin', 'Test': Test})
print(type(Use()))


# 4.自定义元类
# 自定义元类必须继承于type
# type创建类：三个参数

class MyMetaClass(type):
    """自定义的元类"""
    def __new__(cls, name, bases, attr_dict, *args, **kwargs):
        return super().__new__(cls, name, bases, attr_dict)


class Test(metaclass=MyMetaClass):      # 通过自定义的元类来创建类
    pass


print(type(Test))


class MyTest(Test):     # 父类指定元类，子类可以继承父类所指定的元类
    pass
