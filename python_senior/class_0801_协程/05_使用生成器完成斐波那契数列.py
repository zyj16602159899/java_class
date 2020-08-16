# 使用生成器生成斐波那契数列


def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        yield a                 # 如果一个函数中有yield语句，那么它就不再是函数，而是一个生成器的模板
        a, b = b, a + b
        current_num += 1


num = create_num(10)            # 如果在调用一个函数时，如果其中有yield,那么此时不是调用函数，而是创建一个生成器
for i in num:
    print(i)
