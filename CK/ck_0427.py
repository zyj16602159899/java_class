# 闭包
# 概念：一个完整的闭包必须满足以下3个条件：
#       函数中嵌套一个函数
#       外层函数返回内层函数的函数名
#       内层嵌套函数有引用外层的一个非全局的变量
# 作用：实现数据的锁定，提高稳定性
# 最简单的闭包案例：
# def func(num):
#     def count():
#         print(num)
#         print('count')
#     return count

# res = func(999)
# print(res.__closure__)
# res()

# 装饰器
# 开放封闭原则（面向对象原则的核心）：软件实体应该是可扩展、而不可修改的。也就是说，对扩展是开放的，对修改是封闭的。
# 装饰器的作用：在不更改原功能函数内部代码，并且不改变调用方法的情况下为原函数添加新的功能。
# 装饰器的应用场景：
# 1.登录验证
# 2.函数运行时间统计
# 3.执行函数之前做准备工作
# 4.执行函数后清理功能
# 
def login(func):
    def fun():
        username = 'python'
        password = '123456'
        user = input('请输入账号：')
        pw = input('请输入密码：')
        if user == username and pw == password:
            func()
        else:
            print('账号或密码错误！')
    return fun

@login      # @login是语法糖，等同于：index = login(index)
def index():
    print('这是网站的首页！')

index()