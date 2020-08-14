import re


# 2.匹配多个字符

# * 匹配前一个字符出现0次或无数次，即可有可无
# + 匹配前一个字符出现1次或无数次，即至少有一次
# ? 匹配前一个字符出现1次或0次，即要么有一次，要么没有
# {m} 匹配前一个字符出现m次
# {m,n} 匹配前一个字符出现从m到n次

data1 = re.match(r"12\d{2}", "1255678").group()
print(data1)
data2_01 = re.match(r"12\d{1,3}", "125").group()
print(data2_01)
data2_02 = re.match(r"12\d{1,3}", "1255").group()
print(data2_02)
data2_03 = re.match(r"12\d{1,3}", "125556").group()
print(data2_03)
data3_01 = re.match(r"021-?\d{8}", "021-56072222").group()
print(data3_01)
data3_02 = re.match(r"021-?\d{8}", "02156072222").group()
print(data3_02)
# 判断是不是电话号码
phone_01 = re.match(r"\d{3,4}-?\d{7,8}", "021-56072222").group()
print(phone_01)
phone_02 = re.match(r"\d{3,4}-?\d{7,8}", "03706691253").group()
print(phone_02)

text = """abcdefg
hijklmn
opqrst
uvwxyz"""
# 验证.只能匹配\n以外的任意一个字符
data4_01 = re.match(r".*", text).group()
print(data4_01)
# 在后面加上re.S,可以让.匹配所有字符，包括\n
data4_02 = re.match(r".*", text, re.S).group()
print(data4_02)

data5_01 = re.match(r".+", 'ABCD').group()
print(data5_01)
data5_02 = re.match(r".+", '123').group()
print(data5_02)

# 判断变量名是否有效
names = ["name", "_name", "2_name", "__name__"]
for name in names:
    ret = re.match(r"[a-zA-Z_]+[\w]*", name)
    if ret:
        print('变量名 %s 符合要求' % name)
    else:
        print('变量名 %s 不符合要求，错误的！' % name)
