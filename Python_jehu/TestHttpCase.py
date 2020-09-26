import unittest
from Python_jehu.tools.HttpTestDemoNew import HttpTestDemo


class TestHttpCase(unittest.TestCase):
    def setUp(self):
        print('执行用例开始')

    def __init__(self,methodName,url,data,method,expected,case_name):
        super(TestHttpCase, self).__init__(methodName)
        self.url = url
        self.data = data
        self.method = method
        self.expected=expected
        self.case_name=case_name



    def test_api(self):
        res = HttpTestDemo().HttpTestDemo(self.url,self.data,self.method)
        try:
            self.assertEqual(self.expected,res.json()['reason'])
            print(self.case_name)
            print(res.json())
            # DoExcel(r'D:\Web_python2\Python_jehu\test_data\test_case925.xlsx', 'juhe',str(res.json())).save_data()

        except AssertionError as e:
            print('服务异常')
            raise e




    def tearDown(self):
        print('执行用例结束')