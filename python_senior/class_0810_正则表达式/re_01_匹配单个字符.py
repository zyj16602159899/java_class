import re


# 1.匹配单个字符

# .  匹配任意一个字符(\n除外)
# [] 匹配[]中列举的字符
# \d 匹配数字，即0-9
# \D 匹配非数字，即不是数字
# \s 匹配空白，即空格、tab键
# \S 匹配非空白
# \w 匹配单词字符，即a-z,A-Z,0-9,_(下划线) 此外，\w也支持中文、日文、韩文等语言文字，因此要慎用！！
# \W 匹配非单词字符

data1 = re.match(r"速度与激情\d", "速度与激情1").group()
print(data1)
data2 = re.match(r"速度与激情[12345678]", "速度与激情5").group()
print(data2)
data3 = re.match(r"速度与激情[1-8]", "速度与激情4").group()
print(data3)
data4 = re.match(r"速度与激情[1-36-8]", "速度与激情6").group()
print(data4)
data5 = re.match(r"速度与激情[1-8a-zA-Z]", "速度与激情E").group()
print(data5)
data6 = re.match(r"速度与激情\w", "速度与激情_").group()
print(data6)
data7_1 = re.match(r"速度与激情\s\d", "速度与激情 8").group()
print(data7_1)
# \t代表tab键
data7_2 = re.match(r"速度与激情\s\d", "速度与激情\t6").group()
print(data7_2)
data8 = re.match(r"速度与激情.", "速度与激情啊").group()
print(data8)
