import random

def get(x):
    return x

r = random.randint(1,get(2))
print(r)
print('hello',end=' ')  #end有禁用换行的作用
print('world')
print('sd','dsf','sdf',sep=',')    #sep能替换掉默认分隔符