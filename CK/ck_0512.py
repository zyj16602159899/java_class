# 上下文管理器
# 概念：上下文管理器是一个python对象，为操作提供了额外的上下文信息。这是额外的信息，在使用with语句初始化上下文，
# 以及完成with块中的所有代码时，采用可调用的形式。
# object.__enter__(self)
# 输入与此对象相关的运行时上下文。如果存在的话，with语句将绑定该方法的返回值到该语句的as子句中指定的目标。
# object.__exit__(self,exc_type,exc_val,exc_tb)
# exc_type:异常类型
# exc_val：异常值
# exc_tb：异常回溯追踪

# with open('test.txt','w+',encoding='utf8') as f:        # with 后面跟的是一个上下文管理器
#     f.write('今天是个好日子，加油！')

class MyOpen(object):
    """文件操作的上下文管理器"""

    def __init__(self, file_name, open_method, encoding='utf8'):
        self.file_name = file_name
        self.open_method = open_method
        self.encoding = encoding

    def __enter__(self):
        self.f = open(self.file_name, self.open_method, encoding=self.encoding)
        return self.f

    def __exit__(self,exc_type,exc_val,exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.f.close()
    

with MyOpen('test.txt', 'w') as f:
    content = f.read()
    print(content)