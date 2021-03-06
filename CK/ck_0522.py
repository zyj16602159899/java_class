# ORM模型

# O(objects):类和对象
# R(Relation):关系，关系数据库中的表格
# M(Mapping):映射

# ORM框架的功能：
# 1.建立模型类和表之间对应关系，允许我们通过面向对象的方式来操作数据库
# 2.根据设计的模型类生成数据库中的表格
# 3.通过方便的配置就可以进行数据库的切换


class CharField(object):

    def __init__(self,max_length=20):
        self.max_length = max_length
    
    def __get__(self, instance ,owner):
        return self.value

    def __set__(self, instance ,value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError('字符串长度应该在{}以内'.format(self.max_length))
        else:
            raise TypeError('need a str') 

    def __delete__(self, instance):
        self.value = None


class IntField(object):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError('need a int')

    def __delete__(self, instance):
        self.value = None


class BoolField(object):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError('need a bool')

    def __delete__(self, instance):
        self.value = None


class UserModel(object):

    name = CharField(max_length=8)
    pwd = CharField(max_length=16)
    age = IntField()
    man = BoolField()


u = UserModel()
u.name = 'xi'
u.pwd = '123456789'
u.age = 11
u.man = True
print(u.name)
print(u.pwd)
print(u.age)
print(u.man)


