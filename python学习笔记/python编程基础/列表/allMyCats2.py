cat = []
while True:
    print(str(len(cat)))
    name = input()
    if name == ' ':
        break
    cat = cat + [name]
print('cat is :')
for i in cat:               #列表用于循环
    print(' '+ i)