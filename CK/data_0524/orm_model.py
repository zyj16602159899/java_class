# 利用元类实现模型类

from data_0524.filed import BaseField,CharField,BoolField,IntField


class FieldMeatClass(type):
    """模型类的元类"""
    def __new__(cls, name, bases, dict1, *args, **kwargs):
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, dict1)
        else:
            table_name = name.lower()       # 将类名转换成小写，对应数据表的名称
            fields = {}         # 定义一个空字典，用来存放模型类字段和数据表中字段对应的关系
            for k, v in list(dict1.items()):    # 字典遍历的时候，不允许添加或修改元素，因此加list
                if isinstance(v, BaseField):
                    fields[k] = v

            dict1['t_name'] = table_name
            dict1['fields'] = fields

            return super().__new__(cls, name, bases, dict1)


class BaseModel(metaclass=FieldMeatClass):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)     # 遍历出所有关键字参数，并且对对象进行设置属性

    def save(self):
        t_name = self.t_name        # 获取表名
        fields = self.fields        # 获取字段名称
        field_dict = {}             # 创建一个字典存储键值对
        # 获取对应字段的值
        for field in fields.keys():
            field_dict[field] = getattr(self, field)

        # 生成对应的sql语句
        sql = 'INSERT INTO {} VALUE {}'.format(t_name, tuple(field_dict.values()))
        print(sql)


class User(BaseModel):
    """用户模型类"""
    username = CharField()
    pwd = CharField()
    age = IntField()
    live = BoolField()


# print(User.fields)
# print(User.t_name)
xiaom = User(username='小米', pwd='123', age=20, live=True)
xiaom.save()
print(xiaom.username)