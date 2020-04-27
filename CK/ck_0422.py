# 递归函数
# 在函数中调用函数自身，我们把这样的函数叫做递归函数
# 递归边界：退出递归的终止条件(必须要设置，否则会陷入死循环)
# 递归次数的最大限制是1000次

# def func():
#     print('999')
#     func()

# 通过递归函数实现任意数的阶乘
# def fun(n):
#     if n == 1:      # 递归临界点：不再调用自身函数的条件
#         return n
#     else:
#         return n*fun(n-1)

# a = fun(4)
# print(a)

# 作业：
# 1.实现斐波那契数列，输入一个数列的位置数，返回斐波那契数列相应位置的值（第一个数是1，后面的数等于前2个数相加）
# def fixb(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fixb(n-1)+fixb(n-2)
# res = fixb(3)
# print(res)
# 2.第三个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假设兔子都不死，问每个月的兔子
# 总数是多少？（意味着生长期为2）
# def fun(n):
#     if n==1 or n==2:
#         return 1
#     else:
#         return fun(n-1)+fun(n-2)
# res = fun(6)
# print(res)
# 3.小明有100元，打算买100本书，A类书籍5元一本，B类书籍3元一本，C类数据1元两本，请算出小明一共有多少
# 种买法？
# 方式一：
# money = 100
# book = 100
# count = 0
# for a in range(int(money/5)):
#     for b in range(int(money/3)):
#         for c in range(int(money/0.5)):
#             if a*5 + b*3 + c*0.5 <=100 and a + b + c ==100:
#                 print(a,b,c)
#                 count += 1
# print(count)

# 方式2：
count = 0
def count_book(a=0,b=0,c=0):
    if a*5 + b*3 + c*0.5 <=100 and a + b + c ==100:
        print(a,b,c)
        global count
        count += 1
    if a < int(100/5):
        if b < int(100/3):
            if c < 100:
                return count_book(a,b,c+1)
            else:
                return count_book(a,b+1)
        else:
            return count_book(a+1)
res = count_book()
print(res)

# 纯函数
# 一个函数的返回结果只依赖于它的参数，并且在执行过程里面没有副作用，就把这个函数叫做纯函数
# 3个原则：
# 1.变量都只在函数作用域内获取，作为函数的参数传入
# 2.不会产生副作用，不会改变被传入的数据或其他数据（全局变量）
# 3.相同的输入保证相同的输出结果
# 函数的副作用：指函数被调用，完成了函数既定的计算任务，但同时因为访问了外部数据，尤其是因为对外部数据
# 进行了写操作，从而一定程度地改变了系统环境。

# 内置函数
# 内置函数都属于纯函数（有些内置函数是类，这种不是纯函数）
# 常用的内置函数：
# map()函数：会根据提供的函数对指定序列做映射
# filter()函数：用于过滤序列，【一般可结合匿名函数来进行使用】
# zip()函数：用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元祖

# res = zip([1,2,3],[11,22,33])
# print(list(res))

# 匿名函数
# 定义：是python中的一种特殊的函数，不需要使用def去定义，也不用起名字，用lambda表达式来定义，这种就叫匿名函数。
# 格式：lambda 参数： 表达式(返回值)
# 适用场景：简单的函数定义（只有一个表达式）

# 一般方式：
# def add(a,b):
#     return a+b
# # lambda方式一
# res1 = lambda a,b:a + b
# print(res1(11,22))
# # lambda方式二：一般不用这种方式！
# res2 = (lambda a,b:a + b)(22,33)
# print(res2)

# 案例
# li = [1,2,33,4,66,777,9]
# res3 = filter(lambda x: x<10,li)
# print(list(res3))

# li2 = [lambda i: i%5==0 for i in range(11)]
# print(li2)

# 三目运算符
# 方式一
# a = 100
# if a > 100:
#     print('100')
# else:
#     print('000')
# # 方式二【三目运算符】
# print('100') if a > 100 else print('000')

# 偏函数
# 在python的内置模块functools提供了很多有用的功能，其中一个就是偏函数（partial）
# 偏函数的作用：
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定
# 住原函数的部分参数，从而在调用时更简单。
# 用法：

# from functools import partial

# li = [1,3,5,66,777,88,222]
# li2 = [6,15,3,0,999]
# filter2 = partial(filter,lambda x: x>5)
# res = filter2(li)
# res2 = filter2(li2)
# print(list(res))
# print(list(res2))