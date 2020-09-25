import requests

class HttpTestDemo:



    def HttpTestDemo(self,url,data,method,cookie=None,verify=False,headers=None):
        try:
            if method.lower() == 'get':
                res = requests.get(url=url,data=data,cookies=cookie,headers=headers)
                return res
            elif method.lower() == 'post':
                res = requests.post(url=url,data=data,cookies=cookie,headers=headers)
                return res
        except :
            print('你的输入有误')