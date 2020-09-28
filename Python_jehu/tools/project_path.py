import os




path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(path)