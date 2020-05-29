import threading
import requests
import time


count = 0

class RequestThread(threading.Thread):
    """发送requests请求"""

    def __init__(self, url):
        self.url = url
        super().__init__()      # 必须调用父类的__init__方法！

    def run(self):
        global count
        for i in range(100):
            requests.get(self.url)
            count += 1
            print('线程-{}--第{}次请求'.format(self.name,i+1))

def main():
    s_time = time.time()

    th = [RequestThread('http://www.baidu.com') for j in range(10)]
    for i in th:
        i.start()
    for j in th:
        j.join()
    e_time = time.time()

    print('平均时间：{}'.format((e_time-s_time)/count))
    print(count)


main()