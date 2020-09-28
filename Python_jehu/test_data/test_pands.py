import unittest


class TestHttpCase(unittest.TestCase):
    def setUp(self):
        print('执行用例开始')

    def test01(self):
        print('one')

    def test02(self):
        print('two')

    def test03(self):
        print('three')


    def tearDown(self):
        print('执行用例结束')



if __name__ == '__main__':
    suite = unittest.TestSuite()

    loader = unittest.TestLoader()

    # suite.addTest(TestHttpCase('test01'))#方法一：直接通过suite.addTest(用例名)
    # suite.addTest(loader.loadTestsFromTestCase(TestHttpCase))#方法二 通过加载器来加载用例，从用例类加载
    suite.addTest(loader.loadTestsFromModule(TestHttpCase))

    runner = unittest.TextTestRunner()
    runner.run(suite)


