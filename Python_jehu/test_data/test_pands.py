import pandas as pd

df = pd.read_excel(r'D:\Web_python2\Python_jehu\test_data\test_case925.xlsx')
# data = df.head()
# data = df.values
# data=df.loc[:].values
data = df.loc[1,['num','url','data']].to_dict()


print(data)
