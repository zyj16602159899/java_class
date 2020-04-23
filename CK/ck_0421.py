"""
作业：
转换成字典格式：
john_str = "name=john;age=22;sex=man;score=100;phone=88888888"
"""
john_str = "name=john;age=22;sex=man;score=100;phone=88888888"

dict_str = {i.split("=")[0]: i.split("=")[1] for i in john_str.split(";")}
print(dict_str)

# list_01 = ({i:j} for i in range(1,5) for j in range(1,5))
# print(list_01)
# print(next(list_01))
# print(next(list_01))
# print(next(list_01))
# for i in list_01:
#     print(next(list_01))
for  i in range(1,5):
    for j in range(1,5):
        print({i:j})