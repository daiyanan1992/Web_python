import unittest
from Stu_01.Homework.TestHttpJuHe import TestHttpJuHe
import HTMLTestRunner
from Stu_01.API_AUTO.do_excel import DoExcel

# test_data = [{"url":"http://88.143.47.246/api/oauth/oauth/token",
#              "data":{"grant_type":"password","username":"admin","password":"123456","client_id":"zhuanyan","client_secret":"chjSecret"},
#              "method":"post"},
#             {"url":"http://88.143.47.246/api/fixedAsset/assetInfo/assetInfoPage",
#             "data":{"pageNum":1,"pageSize":10,"param":{"assetCategoryId":"","assetInfoName":"","assetInfoStatus":"","assetRfid":"","custodianId":"","manageDepartmentId":"","storageAreaId":"","useDepartmentId":""}},
#              "method":"post"}]
test_data = DoExcel(r'D:\Web_python2\Stu_01\Homework\daiyn.xlsx','python1').get_data()



suite = unittest.TestSuite()#存储用例



#方法二TestLoader
loader = unittest.TestLoader()#创建一个加载器
# suite.addTest(loader.loadTestsFromTestCase(TestHttpJuHe))
for item in test_data:
    # suite.addTest(TestHttpJuHe('test_api',url=test_data[0]['url'],data=test_data[0]['data'],method=test_data[0]['method']))
    suite.addTest(TestHttpJuHe('test_api',item['url'],item['data'],item['method']))


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

