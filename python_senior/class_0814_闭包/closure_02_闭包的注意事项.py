x = 300


def test1():
    x = 200                 # 如果在函数中对全局变量进行修改，需要加global
    def test2():
        nonlocal x          # 如果在闭包中修改上面函数中的变量，需要在下面的函数中加上nonlocal 变量名（python3可用，2.7不可用）
        print("---1---%d" % x)
        x = 100
        print("---2---%d" % x)
    return test2


t1 = test1()
t1()
