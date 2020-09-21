import unittest
from Stu_01.API_AUTO.MathMethod import MathMethod
from Stu_01.test921 import TestMathMethod
import HTMLTestRunner


suite = unittest.TestSuite()#存储用例

#第一种方法
# suite.addTest(TestMathMethod('test_add_two_positive'))
# suite.addTest(TestMathMethod('test_add_two1_positive'))


#方法二TestLoader
loader = unittest.TestLoader()#创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))


#执行-原始方法
# with open('test.txt','w+',encoding='utf-8') as file :
#     runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
#     runner.run(suite)
# file.close()

#执行测试报告-最新。HTML
with open('test_report.html','wb') as file:
    runner =  HTMLTestRunner.HTMLTestRunner(stream=file, verbosity=2, title='Web_python测试报告',
                                            description='第一次测试报告')
    runner.run(suite)

