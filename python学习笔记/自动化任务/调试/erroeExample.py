def spam():
    bacon();


def bacon():
    raise Exception("Error")


try:
    spam()  # 抛出的异常要及时处理
except Exception as err:
    print(str(err))