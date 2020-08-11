import re


# 3.判断开头和结尾

# ^ 匹配字符串开头
# $ 匹配字符串结尾

# match方法默认匹配字符串开头，但不匹配字符串结尾！

# 判断变量名是否有效
# names = ["name", "_name", "2_name", "__name__", "name1", "name!", "___name", "name_n"]
# for name in names:
#     ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
#     if ret:
#         print('变量名 %s 符合要求' % name)
#     else:
#         print('变量名 %s 不符合要求，错误的！' % name)

# 练习：匹配出163邮箱地址，且@符号之前必须有4-20位(英文、字母、数字、下划线都可以)
email = input("请输入您的邮箱：")
# 如果在正则表达式中要用到一些普通的字符，比如./?等，只需要再它们前面添加一个\进行转义即可！！
ret = re.match(r"^[a-zA-Z0-9_]{4,20}@163\.com$", email)
if ret:
    print("您输入的邮箱 %s 符合要求！" % email)
else:
    print("您输入的邮箱 %s 不符合要求！" % email)

