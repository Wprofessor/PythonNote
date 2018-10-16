print('my name is:')
for i in range(5):
    print(str(i))
total = 0
for num in range(101):
    total += num
    print(total)       #对齐是代码块
print(total)
i=0
while i < 5:            #和for等价
    print(str(i))
    i += 1
for val in range(0,10,2):    #0是起始值，10是上限，2是步长
    print(val)