class BaseField(object):
    pass


class CharField(BaseField):

    def __init__(self, max_length=20):
        self.max_length = max_length

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_length:
                self.value = value
            else:
                raise ValueError('字符串长度应该在{}以内'.format(self.max_length))
        else:
            raise TypeError('need a str')

    def __delete__(self, instance):
        self.value = None


class IntField(BaseField):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise TypeError('need a int')

    def __delete__(self, instance):
        self.value = None


class BoolField(BaseField):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, bool):
            self.value = value
        else:
            raise TypeError('need a bool')

    def __delete__(self, instance):
        self.value = None
