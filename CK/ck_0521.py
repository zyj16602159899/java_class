# 描述器

# 描述器是一个具有“绑定行为”的对象属性，该对象的属性访问通过描述器协议覆盖：__get__() __set__()和__delete__()。
# 如果一个对象定义这些方法中的任何一个，他被称为一个描述器。

# object.__get__(self, instance, owner)
# 获取属主类的属性（类属性访问）或者该类的一个实例的属性（实例属性访问）。owner始终是属主，instance是属性访问
# 的实例，当属性通过owner访问时则为None。这个方法应该返回（计算后）的属性值，或者引发一个AttributeError异常。

# object.__set__(self, instance, value)
# 设置属主类的实例instance的属性为一个新值value。

# object.__delete__(self, instance)
# 删除属主类的实例instance属性

class Test(object):
    """
    如果一个类中，出现这些方法中的任何一个，就被称为一个描述器
    """

    def __get__(self, instance ,owner):
        print('查询了属性')

    def __set__(self, instance ,value):
        print('设置了属性')

    def __delete__(self, instance):
        print('删除了属性')


class Model(object):
    name = 'xin'
    attr = Test()       # Test()是一个描述器对象，会覆盖类属性相关操作


m = Model()