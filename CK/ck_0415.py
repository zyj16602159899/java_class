# 字典和集合
# 1.集合可以自动去重
# 2.可用于对列表去重（将列表先转换为集合，再转换为列表）
# 3.集合是可变的
# 4.集合是无序的
# 5.集合中只可存储不可变的数据类型（内部放入一个列表会报错）

se = set()      # 空集合
dict1 = {}      # 空字典

set1 = {1,2,3}
print(set1)
print(type(set1))       # 类型是set

list1 = [1,1,2,2,3,3,4,4]
list2 = list(set(list1))        # 用于对列表去重
print(list2)

set1.add(5)                 # 集合添加数据
print(set1)
set1.remove(2)              # 集合删除数据
print(set1)
set1.update({6,7,8})        # 批量添加数据，等同于列表的extend方法
print(set1)
set2 = set1.copy()          # 复制数据
print(set2)
set1.clear()                # 清空集合内数据
print(set1)

# python三大数据类型：
# 1.数值：1
# 2.序列：字符串、列表、元祖
# 3.散列：字典、集合（特征：内部元素是无序的）
# 数据类型分为可变和不可变（可变的不可hash，不可变的可hash）

# 性能分析：
# 时间上比较：集合、字典、元祖、列表
# 占用内存比较：字典、集合、列表、元祖

# 

