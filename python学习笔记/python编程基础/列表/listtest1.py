def sign(spam):
    spam.insert(-1,'and')
spam =  ['apples', 'bananas', 'tofu', 'cats']
sign(spam)
ll = len(spam)
for i in range(ll):
    ok = spam[i]
    for j in range(len(ok)):
        print(ok[j],end='')
    if i < ll-2:
        print(', ',end='')
    if i == ll-2:
        print(' ',end='')
