birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + 'is ' + name)
    else:
        print('i do not know')
        bday = input()
        birthdays[name] = bday  # 若键不存在，直接添加
        print('have append!')
