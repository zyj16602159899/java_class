import multiprocessing


# Queue队列（先进先出）
# 相反，栈则是：先进后出
q = multiprocessing.Queue(3)        # 可为空，队列中能放入的最大数量

q.put('111')            # 向队列中放入值，不限数据类型
q.put(222)
q.put([11, 22, 33])
# q.put_nowait(55)      # 无法放入值就以异常的形式返回
print(q.full())         # 队列是否填满
print(q.qsize())        # 队列中当前任务数量
print(q.empty())        # 队列是否为空
print(q.get())          # 从队列中取值
print(q.full())
print(q.get())
print(q.qsize())
print(q.get())
print(q.empty())
# q.get_nowait()        # 获取不到值就以异常的形式返回
