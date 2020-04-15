#测试函数或字符串的性能（执行时间）
# import timeit

# def func():
#     for i in range(10):
#         print(i)

# res = timeit.Timer(func).timeit(100)        #timer(执行的函数或字符串/列表).timeit(执行次数)
# print(res)
# res2 = timeit.timeit('[1,2,3]')              #默认是执行一千万次
# print(res2)

"""
1.元祖和列表性能分析
计算创建元祖和列表所需时间：ipython中使用timeit
pip install ipython
执行命令：ipython
输入：timeit list1 = [1,2,3]
输入：timeit tuple1 = (1,2,3)
计算时间模块介绍：import timeit
"""

#命名元祖
from collections import namedtuple

student_info = namedtuple('student_info',['name','age','sex'])
tuple2 = student_info('john',20,'man')
print(tuple2)
print(tuple2.name)
print(tuple2.age)
print(tuple2.sex)

