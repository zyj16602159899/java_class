# 创建生成器的方法：

# 列表推导式
# nums = [i*2 for i in range(10)]
# print(nums)

# 方法一：把列表推导式的中括号变成小括号
# num = (i*2 for i in range(10))
# for i in num:
#     print(i)

# 方法二：在函数中添加yield
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        res = yield a                 # 如果一个函数中有yield语句，那么它就不再是函数，而是一个生成器的模板
        print("send传入的值是：", res)
        a, b = b, a + b
        current_num += 1


# 使用next()方法依次按顺序读取生成器中的值
num = create_num(10)
res1 = next(num)
print(res1)
# res2 = next(num)
# print(res2)
res2 = num.send(None)       # send()传None，表示传的值为空
print(res2)
res3 = num.send("hello, 生成器")   # 一般第一次取值不用send，如果用的话，send传值必须为None，否则会报错。
print(res3)
