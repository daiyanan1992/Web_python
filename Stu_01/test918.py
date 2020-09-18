#2020年9月18日学习代码
'''
常见http返回状态码
200服务器接收成功
302重定向
304未做修改，缓存
403禁止范文
404地址找不到
500服务器错误
504访问超时
'''

class MathMethod:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        return self.a - self.b



class MathMethod_1(MathMethod):

    def divide(self):#拓展
        return self.a/self.b

    def add(self):#重写+超继承
        super(MathMethod_1, self).add()
        return self.a + self.b + 10
    
    
    
    

