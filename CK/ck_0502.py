# !usr/bin/env python


#通用装饰器
def add(func):
    def fun(*args,**kwargs):        #*可以对元组形式的数据进行
        # print('相乘：', a*b)
        # print('相除：', a/b)
        func(*args,**kwargs)
    return fun


@add
def add_num(a,b):
    print('相加：', a + b)

@add
def index():
    print('这是网站的首页！')


index()
add_num(11,33)


