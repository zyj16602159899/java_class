# 内存管理

# 1.对象引用
# 小整数池（针对数值）
# 在python中，[-5,256]是提前创建好的，放在一个小整数池里
# 2.intern机制---大整数池（针对字符串）
# 只存储包含标准字符（字母/数字/下划线）的字符串，不存储包含特殊字符/空格的字符串

# 深浅拷贝
# 通常只在列表嵌套列表时讨论

import copy

list1 = [1,2,3]
list2 = copy.deepcopy(list1)        # 深拷贝
list3 = list1.copy()
list1.append(5)
print(list1)
print(list2)
print(list3)

# 垃圾回收机制
# 一句话形容：引用计数机制为主，标记清除和分代收集两种机制为辅的策略
# 计数机制
#
# 标记清除
#
# 分代回收
#

import gc


res = gc.get_threshold()

print(res)