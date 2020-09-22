import unittest
from Stu_01.Homework.TestHttpJuHe import TestHttpJuHe
import HTMLTestRunner


suite = unittest.TestSuite()#存储用例



#方法二TestLoader
loader = unittest.TestLoader()#创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestHttpJuHe))


#执行-原始方法
# with open('test.txt','w+',encoding='utf-8') as file :
#     runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
#     runner.run(suite)
# file.close()

#执行测试报告-最新。HTML
with open('test_juhe_report.html','wb') as file:
    runner =  HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='聚合数据测试报告',
                                            description='聚合登录测试报告')
    runner.run(suite)

