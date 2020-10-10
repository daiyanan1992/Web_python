

str1 = '{"key":"${key}"}'

print(str1)
if str1.find('${key}') !=-1:
    str2 = str1.replace('${key}','daiyanan')
    print(str2)