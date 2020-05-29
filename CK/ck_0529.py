# 队列

# 三种类型
# 1.先入先出
# 2.后入先出
# 3.优先级队列

# 生产者消费者模式


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