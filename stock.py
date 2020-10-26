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

    def get_K_data(self, code, start_date, end_date=None, frequency='d'):
        # code：代码
        # start：开始日期（包含）  格式“YYYY-MM-DD”，为空时取2015-01-01；
        # end：结束日期（包含），格式“YYYY-MM-DD”，为空时取最近一个交易日
        # requency：数据类型，默认为d，日k线；d=日k线、w=周、m=月、5=5分钟、15=15分钟、30=30分钟、60=60分钟k线数据，不区分大小写

        # open    开盘价
        # close    收盘价
        # high   最高价
        # low最低价
        # preclose 前收盘价
        # volume   成交量
        # amount   成交额（单位：人民币元）
        # turn  换手率
        # pctChg 	涨跌幅

        result = baostock.query_history_k_data_plus(code, fields="open, close, high, low, preclose, volume,amount,turn,pctChg,isST", start_date=start_date,end_date=end_date, frequency=frequency).get_row_data()
        data = {}
        data['open'] = float('%0.2f' % eval(result[0]))
        data['close'] = float('%0.2f' % eval(result[1]))
        data['high'] = float('%0.2f' % eval(result[2]))
        data['low'] = float('%0.2f' % eval(result[3]))
        data['preclose'] = float('%0.2f' % eval(result[4]))
        if result[5]:
            data['volume'] = float('%0.2f' % eval(result[5]))
        else:
            data['volume'] = None
        if result[6]:
            data['amount'] = float('%0.2f' % (eval(result[6]) / 10000))
        else:
            data['amount'] = None
        if result[7]:
            data['turn'] = eval(result[7])
        else:
            data['turn'] = None
        if result[8]:
            data['pctChg'] = float('%0.2f' % (eval(result[8])))
        else:
            data['pctChg'] = None
        data['isST'] = eval(result[-1])
        return data

    def get(self):
        result = tushare.fund_holdings('2020', 3)
        print(result)








if __name__ == '__main__':
    s = GetStock()
    # s.get_K_data('sh.603345', start_date='2020-10-22', end_date='2020-10-25')
    s.get()


