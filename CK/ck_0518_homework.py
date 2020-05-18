# 作业
import pymysql
# 1.实现一个操作mysql的上下文管理器（可以自动断开连接）
class DB(object):

    def __init__(self, data_conf):
        self.con = pymysql.connect(**data_conf)
        self.cursor = self.con.cursor()
    
    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()

DATABASES_CONF = dict(
    host = 'localhost',
    user = 'root',
    password = 'mysql',
    database = 'test',
    port = 3306,
    charset = 'utf8')

with DB(DATABASES_CONF) as cur:
    cur.execute('select * from students')
    print(cur.fetchone())