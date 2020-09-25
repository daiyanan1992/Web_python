# from openpyxl import load_workbook
#
# #1打开excel
# wb = load_workbook('daiyn.xlsx')
#
# #2定位sheet页
# sheet = wb['python1']
#
# #3定位单元格行列值
# res = sheet.cell(1,1).value
#
# print('结果是{}'.format(res))

# data = '{"grant_type":"password","username":"admin","password":"123456","client_id":"zhuanyan","client_secret":"chjSecret"}'
# print(eval(data))
# # print(type(data))
# from ddt import ddt,data,unpack
# import unittest
#
#
# # test_data=[1,3]
#
# @ddt
# class TestMath(unittest.TestCase):
#
#
#     @data([1,2,3])
#     def test_print_data(self,item):
#         print('item',item)
#
#     # def test_add(self):
#     #     a=10
#     #     b=20
#     #     print(a+b)
#
#
# import requests
# url='http://web.juhe.cn:8080/finance/gold/shgold'
# data={'key':'883e9d6d2988042a6d2a054e6f074557'}
#
# res=requests.get(url,data)
# print(res.json())

import unittest
from Python_jehu.tools.do_excel import DoExcel
import HTMLTestRunner
from Python_jehu.TestHttpCase import TestHttpCase
import json
import requests

test_data=DoExcel(r'D:\Web_python2\Python_jehu\test_data\test_case925.xlsx','juhe').get_data()

# for item in test_data:
#     # print(item['url'])
#     # print(eval(item['data']))
#     a=item['data']
#     print(a)
#     # print(type(a))


    # print(item['method'])
print(test_data[0]['url'])
# print(test_data[0]['data'])
data={"key":"883e9d6d2988042a6d2a054e6f074557"}
print(type(data))
res = requests.get(test_data[0]['url'],data)
print(res.json())







