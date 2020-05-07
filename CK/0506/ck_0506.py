# 通用装饰器

# 装饰器可以装饰函数，可以不加return
# def add(func):
#     def fun(*args,**kwargs):
#         print('装饰器的功能代码：登录')
#         func(*args,**kwargs)

#     return fun


# @add
# def index():
#     print('这是网站的首页！')


# @add
# def goods_list(n):
#     print('这是商品列表第{}页'.format(n))


# index()
# goods_list(4)


# 装饰器可以装饰类，装饰器一定要加return！
# def add(func):
#     def fun(*args,**kwargs):
#         print('装饰器的功能代码：登录')
#         return func(*args,**kwargs)

#     return fun


# @add            # MyClass = add(MyClass)
# class MyClass:

#     def __init__(self):
#         pass


# m = MyClass()
# print(m)


# 作业
# 1.一个完整的闭包须满足那几个条件？
#       （1）函数中嵌套一个函数
#       （2）外层函数返回内层函数的函数名
#       （3）内层嵌套函数有引用外层的一个非全局的变量
# 2.定义一个计算函数运行时间的装饰器（计算时间使用time模块实现）
import time

def wrapper(func):
    def count_time(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('函数的运行时间是：{:.5f}'.format(end_time-start_time))
    return count_time

# 3.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），要求登录成功一次，后续的函数都无需
# 再次输入用户名和密码
with open('user.txt') as f:
    users = eval(f.read())


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


@login_check
def index():
    print('这是首页！')


@login_check
def page1(num):
    print('这是第{}页！'.format(num))


if __name__ == '__main__':
    index()
    page1(10)