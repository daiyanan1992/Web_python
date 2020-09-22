# print('这是我git的第一个代码')

#写函数，检查传入的列表的长度，如果大于2，那么仅保留两个长度的值，并打印出来

def listCheck(list1):
    if len(list1)>2:
        return list1[0:2]
    else:
        return list1[::]


list=[1]
a=listCheck(list)
print(a)
