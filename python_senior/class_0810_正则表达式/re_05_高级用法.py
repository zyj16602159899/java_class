import re


# 高级用法

# 1.match方法：从头开始匹配
# 2.search方法：不需要从头开始匹配，只要有符合条件的字符串就返回，不会继续往后匹配了。
# 3.findall方法：提取所有符合条件的字符串，并返回一个列表
# 4.sub(表达式,替换的字符,要被替换的字符串)方法：替换所有符合条件的字符串
# 5.split方法：根据匹配来切割字符串，并返回一个列表


data1 = re.search(r"\d+", "阅读次数为：9999").group()
print(data1)

data2 = re.findall(r"\d+", "python=111,java=222,c++=333,JS=444")
print(data2)

data3 = re.sub(r"\d+", '666', "python=111 java=222")
print(data3)

data4 = re.split(r":|,| ", "name:哈哈,age 22")
print(data4)
