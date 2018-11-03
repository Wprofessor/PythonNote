def printPicnic(count, left, right):
    print('PICNIC ITEMS'.center(left + right, '-'))  # just()和center()都是填充
    for k, v in count.items():
        print(k.ljust(left, '.') + str(v))


count = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(count, 12, 5)
printPicnic(count, 20, 6)
