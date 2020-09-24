import configparser

cf=configparser.ConfigParser()
cf.read('case.config',encoding='utf-8')

#读取配置文件数据
res_1=cf.get('MODE','mode')
print(res_1)

res_2=cf.get('PYTHON11','name')
print(res_2)



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