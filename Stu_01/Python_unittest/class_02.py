import unittest
from Stu_01.API_AUTO.MathMethod import MathMethod
from Stu_01.test921 import TestMathMethod



suite = unittest.TestSuite()#存储用例

#第一种方法
suite.addTest(TestMathMethod('test_add_two_positive'))
suite.addTest(TestMathMethod('test_add_two1_positive'))


#方法二TestLoader
loader = unittest.TestLoader()#创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))


#执行
runner = unittest.TextTestRunner()
runner.run(suite)
