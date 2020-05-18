# 自定义属性访问

class Test(object):

    def __getattr__(self, item):        # 访问属性的时候，如果属性不存在，该方法会触发。
        print('这是getattr')
        return 200


t = Test()
t.name = 100
print(t.name)
print(t.age)        # 访问属性的时候，如果属性不存在，会触发__getattr__方法。