#这是一个猜数字游戏
import random
number = random.randint(1,20)
print('我猜的数字为1-20')

for i in range(1,7):
    print('输入你猜得数字')
    i = int(input())

    if i < number:
        print('too low')
    elif i > number:
        print('too high')
    else:
        break
if i == number:
    print('good luck!你猜的数字是 '+str(i))
else:
    print('正确答案是 '+str(i))