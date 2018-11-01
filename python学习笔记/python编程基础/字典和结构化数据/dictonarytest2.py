def addToInventory(inventory, addedItems):  # 字典的修改
    for i in addedItems:
        inventory.setdefault(i, 0)  # 添加新的内容
        inventory[i] = inventory[i] + 1
    return inventory


def displayInventory(inventory):  # 输出
    print("Inventory:")
    item_total = 0
    for k in inventory.keys():
        print(str(inventory[k]) + ' ' + k)
        item_total += int(inventory[k])
        print("Total number of items: " + str(item_total))


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
