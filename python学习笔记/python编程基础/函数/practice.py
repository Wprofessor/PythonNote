def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number + 1
try:
    x = int(input())
except ValueError:
    print('请输入整数')
while x != 1:
    x = collatz(x)
    print(x)