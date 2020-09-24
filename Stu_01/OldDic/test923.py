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
# print(type(data))
from ddt import ddt,data,unpack
import unittest


# test_data=[1,3]

@ddt
class TestMath(unittest.TestCase):


    @data([1,2,3])
    def test_print_data(self,item):
        print('item',item)

    # def test_add(self):
    #     a=10
    #     b=20
    #     print(a+b)

