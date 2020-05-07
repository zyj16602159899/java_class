# 1.多个装饰器装饰一个函数
#   (1)装饰时，从下往上一层一层装饰；执行时，从上往下依次执行

import time

def wrapper(func):
    def count_time(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('函数的运行时间是：{:.5f}'.format(end_time-start_time))
    return count_time

users = {"user":"python","pwd":"123456","token":False}
def login_check(func):
    
    def ado(*args,**kwargs):
        if not users['token']:           # 判断token是否为False
            print('---登录页面---')
            username = input('请输入账号：')
            password = input('请输入密码：')
            if users['user'] == username and users['pwd'] == password:
                users['token'] = True
                func(*args,**kwargs)                  # 调用被装饰的函数
        else:
            func(*args,**kwargs)                  # token为true时直接调用函数
    return ado


@wrapper
@login_check
def func():
    print('这是需要被装饰的函数！')

func()

# 2.python中，类里面三个内置的装饰器（只能在类中使用）
class MyTest:

    @classmethod        # 类方法（被classmethod装饰了之后，该方法就是一个类方法）
    def add(cls):       # cls:代表的是类本身
        print('add')
        print(cls)

    @staticmethod       # 静态方法，实例和类都可以调用该装饰器装饰的函数
    def static():
        print('这是静态方法')
    
    @property           # 设定只读属性
    def read_attr(self):
        print('被此装饰器装饰之后，该方法可以像属性一样被调用，调用是不需要加括号')
        return '18岁'

    
    def sub(self):      # self：代表的是实例本身
        print('sub')
        print(self)


MyTest.add()
MyTest.static()
print(MyTest.read_attr)
t = MyTest()
t.sub()
t.static()
print(t.read_attr)

# 3.用类实现装饰器