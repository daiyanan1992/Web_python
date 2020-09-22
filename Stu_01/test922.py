

'''
class Add:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        if self.a>0 and self.b>0:
            print('jieguoshi{0}'.format(self.a+self.b))


if __name__ == '__main__':
    Add(-10,20).add()'''
'''
测试集合数据登录接口案例


import unittest
from Stu_01.Homework.HttpTestDemo import HttpTestDemo

class TestHttpJuHe(unittest.TestCase):

    def setUp(self):
        # self.url=url
        # self.data=data
        # self.method=method
        # self.cookie=cookie
        print('执行用例开始')

    def test_success_demo01(self):
        url='https://www.juhe.cn/login/login'
        data='username=18018039181&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
        res = HttpTestDemo().HttpTestDemo(url,data,method='post',cookie=None)
        print('结果是{0}'.format(res.status_code))

    def test_success_demo02(self):
        url='https://www.juhe.cn/login/login'
        data='username=18018039183&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
        res = HttpTestDemo().HttpTestDemo(url,data,method='post',cookie=None)
        print('结果是{0}'.format(res.status_code))'''

'''
import requests
import json
url = 'http://88.143.47.246/api/oauth/oauth/token'
# data = 'username=18018039181&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
data={"grant_type":"password","username":"admin","password":"123456","client_id":"zhuanyan","client_secret":"chjSecret"}
# headers = {}
# headers['Accept'] = 'application/json'
# url='http://88.143.47.246/api/fixedAsset/assetInfo/assetInfoPage'
# data={"pageNum":1,"pageSize":10,"param":{"assetCategoryId":"","assetInfoName":"","assetInfoStatus":"","assetRfid":"","custodianId":"","manageDepartmentId":"","storageAreaId":"","useDepartmentId":""}}
headers = {'Authorization':'Bearer '+'dasdasdasdadasdasdas'}
res =requests.post(url=url,data=data)
# print(res.json()['body']['access_token'])
print(res.json()['body']['access_token'])
print(res.cookies)'''

class GetData:
    Cookie='daiyanan'


setattr(GetData,'Cookie','xiaohuang')
print(GetData.Cookie)