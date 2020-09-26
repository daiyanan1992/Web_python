import unittest
from Python_jehu.tools.do_excel import DoExcel
import HTMLTestRunner
from Python_jehu.TestHttpCase import TestHttpCase
import json


test_data=DoExcel(r'D:\Web_python2\Python_jehu\test_data\test_case925.xlsx','juhe',result=None).get_data()




#suite存储用例
suite = unittest.TestSuite()


#方法二TestLoader
loader = unittest.TestLoader()#创建一个加载器
for item in test_data:
    suite.addTest(TestHttpCase('test_api',item['url'],data=eval(item['data']),method=item['method'],expected=eval(item['expected']),case_name=item['case_name']))



#执行测试报告-最新。HTML
with open(r'D:\Web_python2\Python_jehu\test_result\html_report\test_juhe_report_new.html','wb') as file:
    runner =  HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='聚合数据测试报告',
                                            description='聚合登录测试报告')
    runner.run(suite)
