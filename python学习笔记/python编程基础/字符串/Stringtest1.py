def printTable(tableData):
    StrlenWidth = [0] * len(tableData)  # 初始化
    for i in range(len(tableData)):
        for j in range(len(tableData[0])):
            if len(tableData[i][j]) > StrlenWidth[i]:
                StrlenWidth[i] = len(tableData[i][j])
    for i in range(len(tableData[0])):
        for j in range(len(tableData)):
            if j % 2 == 0:
                print(tableData[j][i].rjust(StrlenWidth[j]), end='')
            else:
                print(tableData[j][i].ljust(StrlenWidth[j]), end='')
            if j < len(tableData) - 1:
                print(' ', end='')
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
