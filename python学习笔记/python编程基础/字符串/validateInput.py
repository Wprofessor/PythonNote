while True:
    print('Enter your age')
    age = input()
    if age.isdecimal():  # 如果年龄都是数字
        break
    print('重新输入')
while True:
    print('输入你的密码')
    password = input()
    if password.isalnum():  #如果密码仅由数字和字母构成
        break
    print('重新输入密码')