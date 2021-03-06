# import unittest
#
#
# class TestHttpCase(unittest.TestCase):
#     def setUp(self):
#         print('执行用例开始')
#
#     def test01(self):
#         print('one')
#
#     def test02(self):
#         print('two')
#
#     def test03(self):
#         print('three')
#
#
#     def tearDown(self):
#         print('执行用例结束')
#
#
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#
#     loader = unittest.TestLoader()
#
#     # suite.addTest(TestHttpCase('test01'))#方法一：直接通过suite.addTest(用例名)
#     # suite.addTest(loader.loadTestsFromTestCase(TestHttpCase))#方法二 通过加载器来加载用例，从用例类加载
#     suite.addTest(loader.loadTestsFromModule(TestHttpCase))
#
#     runner = unittest.TextTestRunner()
#     runner.run(suite)
#
# #
# str1 = 'daiyananisshuaige'
# res1 = str1.find('s')
# str2= str1.replace('s','D')
# print(str2)

import logging

# logging.debug('这是dubug信息')
# logging.info('这是info信息')
# logging.warning('这是warning信息')
# logging.error('这是error信息')
# logging.critical('这是cri信息')

class Ny_Log:
    def my_log(self,msg,level,):
        #定义日志收集器
        my_logger = logging.getLogger('python11')

        #设置级别
        my_logger.setLevel('DEBUG')

        #设置日志输出格式
        foematter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')



        #穿件我们自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(foematter)
        fh = logging.FileHandler('py11.txt','a',encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(foematter)



        #两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        #收集日志
        if level=='DEBUG':
            my_logger.debug(msg)
        elif level=='INFO':
            my_logger.info(msg)
        elif level=='WARNING':
            my_logger.warning(msg)
        elif level=='ERROR':
            my_logger.error(msg)
        elif level=='CRITICAL':
            my_logger.critical(msg)

        #关闭日志收集器
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)


    def debug(self,msg):
        self.my_log(msg,'DEBUF')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')















