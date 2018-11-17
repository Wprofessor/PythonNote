# Python中文件读写
## 1.调用 open()函数，返回一个 File 对象。 
```
>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt') 
```
## 2.调用 File 对象的 read()或 write()方法。
* ### 读取文件内容
    ```
    //。如果你希望将整个文件的 内容读取为一个字符串值，就使用 File 对象的 read()方法。
    >>> helloContent = helloFile.read() 
    >>> helloContent 
    'Hello world!' 

    //可以使用 readlines()方法，从该文件取得一个字符串的列表。列表中的 每个字符串就是文本中的每一行。
    ```
* ### 写入文件(分为‘写模式’和‘添加模式’)
    #### 1.写模式将覆写原有的文件，从头开始，就像你用一个新值覆写一个变量的值。将'w'作为第二个参数传递给 open()，以写模式打开该文件。 
    #### 2.添加模式将 在已有文件的末尾添加文本。将'a'作为第二个参数传递给 open()，以添加模式打开该文件。
    ### 注意：如果传递给 open()的文件名不存在，写模式和添加模式都会创建一个新的空文 件。在读取或写入文件后，调用 close()方法，然后才能再次打开该文件。
    ```
    >>> baconFile = open('bacon.txt', 'w') 
    >>> baconFile.write('Hello world!\n')     #返回的是字符串个数
    13 
    >>> baconFile.close() 
    >>> baconFile = open('bacon.txt', 'a') 
    >>> baconFile.write('Bacon is not a vegetable.') 
    25 
    >>> baconFile.close() 
    >>> baconFile = open('bacon.txt') 
    >>> content = baconFile.read() 
    >>> baconFile.close() 
    >>> print(content) 
    Hello world! 
    Bacon is not a vegetable. 
    ```    
## 3.调用 File 对象的 close()方法，关闭该文件。 