PythonNote
python学习笔记

方法
index()方法在列表中查找对应位置
append()方法在列表末尾添加参数
insert()方法在列表任意位置添加参数
remove()方法从列表中删除值

注意：
append和insert，remove方法类似于c语言中的void函数，无返回值（或者说返回值是none）
用 sort()方法将列表中的值排序

sort方法也没有返回值
例如：spam = [1,2,3,4,7,6,5]
spam.sort()使得spam升序排序
spam.sort(reverse=True)使得逆序排序
spam.sort(key=str.lower) 使字符串列表按字典序排序

默认为“ASCLL字符顺序”
注意：sort方法中不能整数和字符串混合排序

元组使用方法和列表基本类似
区别是:元组不允许插入，删除，修改

函数list()将元组转换为列表
函数tuple()将列表转换为元组

引用;对列表的引用类似于指针（链表），指向的是列表的地址，改变其一，都会改变

浅复制:copy 一般情况下对于简单的对象(数字，列表，字符串时) 与deepcopy无区别
当是复杂对象时(list嵌套list): copy相当于赋值，内层list id不变，会随着原来对
象的改变而发生改变。

而对于深复制:deepcopy会创建独立对象，id会发生改变，不会因为原来对象的改变而发生改变。

字典:字典中的表项是不排序的。
例如: spam = {'name':'Bob','age':18}
字典的三个方法(keys(),values(),items()):
keys():返回的是键，是一个元组
values():返回的是值，是一个元组
items():返回的是嵌套式的元组  内层也是元组(包含键和值)

字典的get()方法：检查改键是否存在于字典中，spam.get('name'，0)
若存在，返回该键的值，否则返回备用值(0)。
