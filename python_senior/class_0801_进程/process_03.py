from multiprocessing import Process, Queue


# 使用Queue队列，完成进程间的数据共享
def test1(q):
    """取数据"""
    data = [11, 22, 33, 44]
    for temp in data:
        q.put(temp)
    print("---已将所有数据取出并放入队列---")


def test2(q):
    """从队列中获取数据"""
    data_list = list()      # 定义一个空列表
    while True:
        data = q.get()
        data_list.append(data)
        if q.empty():
            break
    # 模拟数据处理
    print(data_list)


def main():
    # 创建一个队列
    q = Queue()
    p1 = Process(target=test1, args=(q,))
    p2 = Process(target=test2, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
