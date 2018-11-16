import re
def judge(x):
    if len(x) != 8:
        return False
    else :
        ok1 = re.compile(r'[a-z]+')
        ok2 = re.compile(r'[A-Z]+')
        ok3 = re.compile(r'[0-9]+')
        if ok1.search(x) and ok2.search(x) and ok3.search(x):
            return True
    return False

x = str(input())
print(str(judge(x)))