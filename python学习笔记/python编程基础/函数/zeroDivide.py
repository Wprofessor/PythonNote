def spam(x):
    try:
        return 42/x
    except ZeroDivisionError:
        print('Error')

def spam1(x):
    return 42 / x
print(spam(2))
print(spam(12))
print(spam(0))           #执行完except后，程序照常运行
print(spam(1))
try:                     #一旦执行except，就不会跳到try
    print(spam1(2))
    print(spam1(12))
    print(spam1(0))
    print(spam1(1))
except ZeroDivisionError:
    print('Error x')