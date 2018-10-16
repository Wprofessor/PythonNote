import sys

while True:              #无限循环
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()       #程序提前结束
    print('You typed' + response + '.')
