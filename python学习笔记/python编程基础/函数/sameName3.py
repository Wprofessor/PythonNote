def spam():
    global eggs
    eggs = 'spam'
    bacon()
    ham()

def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)