# 2.__str__和__repr__方法
# 3.__call__方法
# 问题一：python中万物皆对象，函数也是对象，为什么函数可以被调用，而其他对象不行？
# 问题二：如果想让类创建出来的对象，可以像函数一样被调用可以实现吗？

# 交互环境下print打印的内容和直接输入变量，返回的内容不一样是为什么？
# >>>a = 'abc'
# >>>print(a)
# abc
# >>>a
# 'abc'

# 原因：使用print打印的时候触发的是__str__方法；直接输入变量时触发的是__repr__方法

# 注意点：
# 重写__str__和__repr__方法时，必须要记得写return
# 重写__str__和__repr__方法时，return返回的必须是一个字符串对象

class MyClass(object):
    
    def __init__(self,name):
        self.name = name

    def __str__(self):
        print('---str触发了---')
        return self.name

    def __repr__(self):         # 如果没有__str__方法，会触发__str__方法（相当于备胎）
        print('---repr触发了---')
        return 'hahaha'
    
    def __call__(self, *args, **kwargs):    # 对象像函数一样被调用的时候会触发该方法
        print('---call---')


m = MyClass('xin')
print(m)                        # 这3种方法都会触发__str__方法
str(m)
format(m)

res = repr(m)                   # 除了交互环境，repr(m)也会触发__str__方法
print(res)

m()

# 总结：使用str函数、format函数或者print打印对象时会优先触发str方法，没定义str方法的情况下，会再去找repr方法，
# 如果都没有，那么才会去找父类的str方法。

# 使用repr方法或者交互环境下输入变量，会先找自身的repr方法，自身没有的话，才会去找父类的repr方法。


# 作业：通过类来实现装饰器（用到__call__方法）