# -*- coding:utf-8 _*-

#   author : YOYO
#   time :  2020/10/23 17:49
#   email : youyou.xu@enesource.com
#   project_name :  getstock
#   file_name :  main
#   function：

from do_excel import DoExcel
from stock import GetStock

s = GetStock()
# 创建表，拉取沪深300成分股
# s.get_hs300_stocks()

# 获取股票的行业属性，并插入excel
def get_industry():
    excel = DoExcel()
    stocks = excel.read()
    n = 1
    for each in stocks:
        n += 1
        industry = s.get_stock_industry(each.code)
        # 获取最后一天的k线数据
        excel.write_industry(n, industry)

def get_k():
    excel = DoExcel()
    stocks = excel.read()
    n = 1
    for each in stocks:
        n += 1
        # 获取最后一天的k线数据
        k_data = s.get_K_data(each.code, start_date='2020-10-23')
        excel.write_k_data(n, k_data)



get_k()