import re


# 4.匹配分组

# | 匹配左右任意一个表达式
# (ab) 将括号中字符作为一个分组
# \num 引用分组num匹配到的字符串
# (?P<name>) 分组起别名
# (?P=name) 引用别名为name分组匹配到的字符串

data1_01 = re.match(r"123|456", "123456").group()
print(data1_01)
data1_02 = re.match(r"123|456", "456666").group()
print(data1_02)
data2_01 = re.match(r"^[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "18888@163.com").group()
print(data2_01)
data2_02 = re.match(r"^[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "1555@126.com").group()
print(data2_02)
# 用小括号括住(分组)，在group中输入对应的排序，可以提取对应的值
data3_01 = re.match(r"^([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "1555@126.com").group(1)
print(data3_01)
data3_01 = re.match(r"^([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "1555@126.com").group(2)
print(data3_01)

text1 = '<h1>hahaha</h1>'
text2 = '<body><h1>hahaha</h1></body>'
# 引用分组num匹配到的字符串（用小括号进行分组）
data4_01 = re.match(r"<(\w*)>.*</\1>", text1).group()
print(data4_01)
# 方式一：有多个分组，就用\数字来引用
data4_02 = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", text2).group()
print(data4_02)
# 方式二：起别名后，进行引用
data4_03 = re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", text2).group()
print(data4_03)
