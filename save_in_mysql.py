# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/10/22 15:01
#   email : youyou.xu@enesource.com
#   project_name :  getstock
#   file_name :  save_in_mysql
#   function：

import pymysql

class MyMysql:
    def __init__(self):
        host = '192.168.1.157'
        db = 'use_test'
        user = 'root'
        pwd = 'Ene!@#2019'
        port = 3306

        self.mysql = pymysql.connect(host=host, user=user, password=pwd, db=db, port=port)
        self.cursor = self.mysql.cursor()

    # def my_execute(self, a, b, c, d, e, f, g):
    #     sql = "insert into stock_basic  values(%s, %s, %s, %s, %s, %s, %s)"
    #     self.cursor.execute(sql, (a, b, c, d, e, f, g))  # execute()方法传入sql和对应的值，值是元组格式
    #     self.mysql.commit()

    def my_execute(self, sql, values):
        try:
            self.cursor.execute(sql, values)
            self.mysql.commit()
        except:
            print('Fail')
            self.cursor.close()

    # 往stock_basic表插入数据
    def insert_stock_basic(self, data):  # data 是一个字典，key:value  字段名：字段值
        """
              Data keys:
                  code:指数代码
                  name:指数名称
                  PE:市盈率
                  amount:总金额（亿元）
                  area：地区
                  industy：行业
                  section：所属板块
                  change:涨跌幅
                  open:开盘价
                  preclose:昨日收盘价
                  close:收盘价
                  high:最高价
                  low:最低价
                  volume:成交量(手)

            """
        keys = ', '.join(data.keys())  # 只插入传入的字段
        values = ', '.join(['%s'] * len(data))  # sql里后面values跟着几个 %s 取决于字典里传了几个参数
        sql = """insert into stock_basic ({keys}) values ({values})""".format(keys=keys, values=values)
        self.my_execute(sql, tuple(data.values()))   # values 要是元组格式，将字典的值变成元组



if __name__ == '__main__':
        db = MyMysql()
        # a = db.my_execute('a','b', 'c', 'd', 'e', 'f', 'g')

