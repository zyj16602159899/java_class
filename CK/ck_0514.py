# 算术运算符相关的魔术方法
# __add__(self, other)      定义加法的行为：+
# __sub__(self, other)      定义减法的行为：-
# __mul__(self, other)      定义乘法的行为：*
# __truediv__(self, other)  定义真除法的行为：/
# __floordiv__(self, other) 定义整数除法的行为：//
# __mod__(self, other)      定义取余算法的行为：%

# python的魔术方法大全：https://www.cnblogs.com/nmb-musen/p/10861536.html

class MyStr(object):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data

    def __add__(self, other):       # other是一个对象
        print('---触发了add方法---')
        return self.data + other.data
    
    def __sub__(self, other):
        print('---触发了sub方法---')
        return self.data.replace(other.data, '')


s1 = MyStr('sss111')
s2 = MyStr('aaa222')
print(s1)
print(s2)
s3 = MyStr(s1+s2)
print(s3)
print(s3-s1)