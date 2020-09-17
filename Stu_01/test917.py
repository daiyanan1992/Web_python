'''
import os
2020年9月17日14:41:23测试代码

path = os.getcwd()
print('获取当前工作目录是：{0}'.format(path))
print('获取当前工作目录是：%s' %path)

path_02 = os.path.realpath(__file__)#__file__指当前文件的
print('realpath is %s' %path_02)
print('real path is {0},{1}'.format(path,path_02))

#如何拼接路劲
new_path01 = os.getcwd()+'\python1'
print(new_path01)

new_path02 = os.path.join(os.getcwd(),'python11')
print(new_path02)'''

#异常处理
'''
import os


try:
    os.mkdir('python01')  # FileExistsError
    # os.rmdir('python01')
except FileExistsError as e:
    print('文件已存在')'''
'''
#冒泡排序法
list1 = [1,23,12,55,81,31,2,4,6]
for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
    print(list1)'''


'''
list1=[11,22,33,44,1,22]
for i in range(0,len(list1)-1):
    for j in range(0,len(list1)-1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)'''


















