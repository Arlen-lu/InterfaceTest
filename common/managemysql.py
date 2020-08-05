import pymysql
from info import InfoPart
import pysnooper

class MySqlconnect(object):


    def __init__(self):
        self.db_info = eval(InfoPart().db_info)
        self.sql1 = ["begin;","create temporary table if not exists my_test(select * from table_user);","select * from my_test;",]

    def connect_db(self):
        conn = pymysql.connect(host=self.db_info['host'],
                                port = self.db_info['port'],
                                user=self.db_info['user'],
                                password=self.db_info['password'],
                                database=self.db_info['db'],
                                charset='utf8')
        return conn
    # @pysnooper.snoop()
    def db_sql(self):
        sql_seclect = ["select id from table_user limit 2;","select user_id from table_user limit 3,2;"]
        # sql_insert = "insert into test1(testname) values('arlen')"
        # sql_seclect = "select * from test1"
        return sql_seclect

    @pysnooper.snoop('log.log',watch=('args',))
    def db_search(self,*args):
        cursor = self.connect_db().cursor()
        for sql in args[0]:
            # print(type(args))
            data = []
            cursor.execute(sql)
            all = cursor.fetchall()
            data.append(all)
        cursor.close()
        self.close_db_connect()
        return data
    
    def close_db_connect(self):
        self.connect_db().close()

if __name__ == "__main__":
    mysql_connect = MySqlconnect()
    data = mysql_connect.db_search(mysql_connect.db_sql())
    print(data)
    data1 = mysql_connect.db_search(mysql_connect.sql1)
    print(data1)
    # print(data)
    # print(type(data))
    # data1 = data[0]
    # print(data1)
    # print(type(data1))
    # data2 = data1[0]
    # print(data2)
    # print(type(data2))
    # data3 = data2[0]
    # print(data3)
    # print(type(data3))
