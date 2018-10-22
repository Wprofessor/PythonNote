def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3*number + 1
x = int(input())
while x != 1:
    x = collatz(x)
    print(x)