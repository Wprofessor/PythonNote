def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('error')  # 抛出异常
    if width <= 2:
        raise Exception('Error')
    if height <= 2:
        raise Exception('Error')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as  err:  # 捕获异常，将之保存在err变量中
        print('An exception happened: ' + str(err))
