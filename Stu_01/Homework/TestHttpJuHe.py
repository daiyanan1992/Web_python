import unittest
from Stu_01.Homework.HttpTestDemo import HttpTestDemo

class TestHttpJuHe(unittest.TestCase):

    def setUp(self):
        self.url = 'http://88.143.47.246/api/oauth/oauth/token'
        # data='username=18018039181&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
        self.data = {"grant_type": "password", "username": "admin", "password": "123456", "client_id": "zhuanyan",
                "client_secret": "chjSecret"}
        self.chaxun_url='http://88.143.47.246/api/fixedAsset/assetInfo/assetInfoPage'
        self.cahxun_data={"pageNum":1,"pageSize":10,"param":{"assetCategoryId":"","assetInfoName":"","assetInfoStatus":"","assetRfid":"","custodianId":"","manageDepartmentId":"","storageAreaId":"","useDepartmentId":""}}
        self.cookies = HttpTestDemo().HttpTestDemo(url=self.url, data=self.data, method='post').json()['body']['access_token']
        print('执行用例开始,获取cookies是{0}'.format(self.cookies))

    def test_success_demo01(self):#登录成功
        # url='http://88.143.47.246/api/oauth/oauth/token'
        # data='username=18018039181&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
        # data = {"grant_type":"password","username":"admin","password":"123456","client_id":"zhuanyan","client_secret":"chjSecret"}
        res = HttpTestDemo().HttpTestDemo(url=self.url,data=self.data,method='post',cookie=None)
        self.assertEqual('操作成功',res.json()['resultMsg'])
        print('结果是{0}'.format(res.json()))

    def test_success_demo02(self):#用户名密码错我
        # url='http://88.143.47.246/api/fixedAsset/assetInfo/assetInfoPage'
        # data='username=18018039183&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
        # data={"pageNum":1,"pageSize":10,"param":{"assetCategoryId":"","assetInfoName":"","assetInfoStatus":"","assetRfid":"","custodianId":"","manageDepartmentId":"","storageAreaId":"","useDepartmentId":""}}
        headers={'Authorization':'Bearer '+self.cookies}
        res = HttpTestDemo().HttpTestDemo(self.chaxun_url,self.cahxun_data,method='post',headers=headers)
        print('Bearer '+self.cookies)
        print('结果是{0}'.format(res.status_code))
        print(res.json())