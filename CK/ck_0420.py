# 推导式
# 1.列表推导式
# 2.字典推导式

# 生成一个列表，存储1-99
# 方法一：
# list_01 = []
# for i in range(1,100):
#     list_01.append(i)
# print(list_01)
# 方法二（列表推导式）：
# list_02 = [i for i in range(1,100)]
# print(list_02)

# 字典推导式
# dict_01 = {i:i*i for i in range(1,10)}
# print(dict_01)

# 生成器
# 1.生成器可以通过生成器表达式(提高性能，节约内存)创建
# a = (i for i in range(1,10))          #生成器对象
# print(a)

# 2.通过yield关键字也可以定义生成器
# def get_fun():
#     yield 100
#     print('hello world')
#     yield 200

# res = get_fun()
# print(next(res))
# print(next(res))
# print(next(res))        # 生成器数据读取完毕之后再进行读取，会报错

# 迭代器(iterator)：内部既实现了__iter__方法，也实现了__next__方法
# 可迭代对象(iterable)：可以for循环遍历的都是可迭代对象，内部只实现了__iter__方法
# 生成器(generator)是迭代器的一种，如何区分迭代器和生成器呢？
# 1.生成器相比迭代器多了3种方法：send方法、close方法、throw方法
# （1）send方法：发送数据，可与生成器进行交互
# （2）close方法：关闭生成器
# （3）throw方法：
# 生成器<迭代器<可迭代对象

# li = [1,2,3,4]
# li2 = iter(li)             # iter()函数
# print(next(li2))
# print(next(li2))

def gen():
    for i in range(1,5):
        se = yield i
        print(se)
g = gen()
print(next(g))
print(g.send(100))
print(next(g))
g.close()           # 关闭生成器，再次执行print(next(g))会报错