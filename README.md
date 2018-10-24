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
