def spam():
    eggs = '123'
    print(eggs)

def bacon():
    eggs = '789'
    print(eggs)
    spam()
    print(eggs)

eggs = 'emmm'
bacon()
print(eggs)