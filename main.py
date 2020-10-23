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
excel = DoExcel()
stocks = excel.read()
n = 1
for each in stocks:
    n += 1
    industry = s.get_stock_industry(each.code)
    excel.write(n, industry)
