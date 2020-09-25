'''import configparser

cf=configparser.ConfigParser()
cf.read('case.config',encoding='utf-8')

secs=cf.sections()
print(secs)
options=cf.options('MODE')
print(options)

items=cf.items('MODE')
print(items)


#读取配置文件数据
res_1=cf.get('MODE','mode')
print(res_1)

res_2=cf.get('PYTHON11','name')
print(res_2)

res_3=cf.get('LEMON','name')
print(res_3)'''



# list1=[1,'string',{'name':'daiyanan'}]
# dict1={'name':'daiyn','age':20}
# print(list1)
# list1[1]='hello'
# print(list1)
# dict1['name']='huahua'
# print(dict1)
# list2=(1,'str',{'name':'dai'})
# list2[2]['name']='kj'
# print(list2)

class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        print(self.a+self.b)


    @classmethod
    def jian(cls):
        print('self.b-self.a')

    @staticmethod
    def hh():
        print('woshijingdai')



if __name__ == '__main__':
    # Math(1,2).add()
    # Math.jian()
    Math.hh()