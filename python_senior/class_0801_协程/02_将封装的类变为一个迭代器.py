from collections.abc import Iterable, Iterator
# 一个对象，既有__iter__方法，又有__next__方法，就是迭代器。


class Classmate(object):

    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想让一个对象成为可迭代对象，即可以使用for循环，那么必须实现__iter__方法，且该方法必须返回一个迭代器"""
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            res = self.names[self.current_num]
            self.current_num += 1
            return res
        else:
            raise StopIteration         # for循环在检测到StopIteration异常后，会自动停止遍历！


classmate = Classmate()
classmate.add("张三")
classmate.add("李四")
classmate.add("王五")

print("判断classmate是否是可迭代对象：", isinstance(classmate, Iterable))
classmate_iterator = iter(classmate)
print("判断classmate_iterator是否是迭代器：", isinstance(classmate_iterator, Iterator))

for i in classmate:
    print(i)
