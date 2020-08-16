from collections.abc import Iterable

# 查看数据类型是否可迭代
print(isinstance('111', Iterable))
print(isinstance(111, Iterable))
