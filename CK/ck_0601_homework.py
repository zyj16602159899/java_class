# 作业：
# 1.用一个队列来存储商品
# 2.创建一个专门生产商品的线程类，当商品数量少于50时，开始生产商品，每次生产200个商品，每生产完一轮暂停1秒
# 3.创建一个专门消费商品的线程类，当商品数量大于10时就开始消费，循环消费，每次消费3个，当商品实例少于10的时候
# 暂停2秒
# 4.创建一个线程生产商品
# 5.创建5个线程消费商品

import time
from queue import Queue
from threading import Thread


q = Queue()

# 生产者和消费者模式
class Producer(Thread):
    
    def run(self):
        # 判断队列中的商品数量是否少于50，少于50的话就生产200个
        count = 0
        while True:
            if q.qsize()<50:
                for i in range(200):
                    count += 1
                    goods = '--第{}个商品--'.format(count)
                    q.put(goods)
                    print('生产：',goods)
            time.sleep(1)


class Consumer(Thread):
    
    def run(self):
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    print('消费：{}'.format(q.get()))
            time.sleep(0.1)


p = Producer()
p.start()

for i in range(5):
    c = Consumer()
    c.start()
