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



if __name__ == '__main__':
    url = 'https://www.juhe.cn/login/login'
    data = 'username=18018039181&password=wdRMXJ%2FJ%2Fv88doMwVdbUAwZBHQd9QBP7%2FTgXB3uUhwBljrGzPeza3sG4RHL5zJQpILDzbEQPDAlV6VDeqk8SMfRt6zl5r1KO8iZ2luT2fnR8IdhmvgEo6V%2FHTar7z5ZMs2GcmVNriWgtsk%2FwYzg1ALJMfjQFfmmdVAZvt9xZIPGzma5uvV7ewkjKMYe2tS1itxk7EdxbhLPwXl9wzuk3AP4gX%2FzNOlhdVbhJveaVWeeHRDi%2BDi1FYlGfTZE6SBdeZB1FrQozHgJrvHZF%2B7tRXoD%2F27Pt4zRzG9r6bmYd2XMYqFsoHEDD%2BUhn%2BXpN7yTkopY%2BkPG9wacvzBVpqS3G5Q%3D%3D&secondMobile=&secondCode=&captcha=&uuid=&bind=0'
    # url='https://www.baidu.com/'
    # data=''
    headers = {}
    headers['Accept'] = 'application/json'
    res = HttpTestDemo().HttpTestDemo(url=url,data=data,method='post')
    print(res.text)
