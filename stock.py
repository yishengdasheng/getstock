# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/10/22 14:00
#   email : youyou.xu@enesource.com
#   project_name :  getstock
#   file_name :  stock
#   function：
import tushare
import baostock
import pandas
# result = baostock.query_history_k_data_plus("sh.000001",
# "date,code,open,high,low,close,preclose,volume,amount,pctChg", start_date='2020-10-20', end_date='2020-10-23')
# data = tushare.get_index()


class GetStock:
    def __init__(self):
        self.login = baostock.login()

    def get_hs300_stocks(self):
        result = baostock.query_hs300_stocks().get_data()
        result.to_excel(r'''E:\桌面\PycharmProjects\getstock\test.xlsx''', index=False)

    def get_stock_industry(self, code):
        result = baostock.query_stock_industry(code).get_row_data()
        industry = result[3]
        return industry






if __name__ == '__main__':
    s = GetStock()
    s.get_stock_industry('')


