# 自定义属性访问

# __getattr__方法和__getattribute__方法都存在的时候，先执行__getattribute__方法

class Test(object):

    def __init__(self):
        self.age = 18

    def __getattr__(self, item):        # 访问属性的时候，如果属性不存在(出现AttrError)，会触发该方法。
        print('这是getattr')
        # object.__getattribute__(self, item)     # 这是父类的方法
        return 200
    
    def __getattribute__(self, item):   # 访问属性的时候，第一时间触发该方法去查找属性
        print('这是__getattribute__方法')
        # return 500
        return super().__getattribute__(item)

    def __setattr__(self, key, value):  # 这个方法是在给对象设置属性的时候触发(可以在设置属性的时候干扰操作)
        if key == 'age':
            super().__setattr__(key, 18)
        else:
            print('设置属性时触发该方法！')
            super().__setattr__(key, value)



t = Test()
t.name = 100
t.age = 888
print(t.name)
print(t.age)        # 访问属性的时候，如果属性不存在，会触发__getattr__方法。