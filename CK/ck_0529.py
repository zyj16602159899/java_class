# 队列

# 三种类型
# 1.先入先出（FIFO队列Queue）
# 2.后入先出（LIFO队列LifoQueue）
# 3.优先级队列（PriorityQueue）
# 这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

# 队列的方法：
# Queue.qsize()：返回当前队列包含的消息数量
# Queue.empty()：如果队列为空，返回True，反之False
# Queue.full()：如果队列满了，返回True，反之False
# Queue.get(block=False,timeout=None)：获取队列，block表示是否等待，timeout表示等待时间
# Queue.put(item, block=False,timeout=None)：写入队列
# Queue.get_nowait()：相当于Queue.get(block=False)
# Queue.put_nowait()：相当于Queue.put(item, block=False)
# Queue.task_done()：在完成一项工作之后，使用Queue.task_done()方法可以向队列发送一个信号，表示该任务执行完毕
# Queue.join()：实际上意味着等到队列中所有的任务执行完毕之后，再往下，否则一直等待

# 注意点：join()是判断的依据，不单单指的是队列中没有数据，数据get出去之后，要使用task_done()向队列发送一个信号，
# 表示该任务执行完毕。

# 生产者消费者模式实现

# 为什么要使用生产者消费者模式？
# 在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处
# 理速度很慢，那么生产者就必须等消费者处理完，才能继续处理生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者
# 就必须等待生产者。为了解决这个问题，于是引入了生产者和消费者模式。

# 什么是生产者消费者模式？
# 生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行
# 通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞
# 队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力。


import queue


# 1.先入先出
q = queue.Queue(3)
# 往队列中添加数据
q.put(1)
q.put(22)
q.put(333)
# q.put(55, block=False)       # 往队列中添加数据（不等待），队列已满，会报错
# q.put_nowait()               # 往队列中添加数据（不等待）

# 获取队列中的数据
print(q.get())
print(q.get())
print(q.get())
# print(q.get(block=False))   # 往队列中获取数据（不等待），队列为空，也会报错
# print(q.get_nowait())       # 往队列中获取数据（不等待）

# 发消息
q.task_done()       # 完成一个任务之后，必须发送一条消息
q.task_done()
q.task_done()

# 获取队列中的任务数
print(q.qsize())

# 判断队列是否已满
print(q.full())

# 判断队列是否为空
print(q.empty())

# json: 队列中的任务是否执行完毕，完毕才会继续往下执行
q.join()

print('join之后的代码')


# 2.后入先出
q2 = queue.LifoQueue()

q2.put(1)
q2.put(22)
q2.put(333)
print(q2.get())


# 3.优先级队列
q3 = queue.PriorityQueue()

q3.put((1, '222'))
q3.put((22, '666'))
q3.put((3, '999'))
print(q3.get())
print(q3.get())