
'''
url = 'http://japi.juhe.cn/qqevaluate/qq'
data = {'key':'afee44814ddc1ae5b0f98e7755ee9b6c',
'qq':'450176668'}

res = requests.post(url=url,data=data)
print(res)
print(res.text)
print(res.headers)
print(res.js on())'''

'''
import requests
class HttpRequest:
    
    # 利用request来测试接口
    # url:传递的url
    
    def http_request(self,url,data,method,cookie=None):
        try:
            if method.lower() == 'get':
                res = requests.get(url=url,data=data,cookies=cookie)
            elif method.lower() == 'post':
                res = requests.post(url=url,data=data,cookies=cookie)
            return res
        except:
            print('输入有误')'''


'''
import unittest
from Stu_01.API_AUTO.MathMethod import MathMethod

class TestMathMethod(unittest.TestCase):

    def test_add_two_positive(self):
        res = MathMethod(1,1).add()
        print("1+1结果是",res)
        #加一个断言，期望值和结果比对
        try:
            self.assertEqual(2,res,'比对成功')
        except AssertionError as e:
            print('出错啦断言错误是{0}'.format(e))
            raise e

    def test_add_two1_positive(self):
        res = MathMethod(-1,-9).add()
        print('2+3结果是',res)
        try:
            self.assertEqual(-9,res,'预期和实际不一致')
        except AssertionError as e:
            print('出错啦断言错误是{0}'.format(e))
            raise e


'''






