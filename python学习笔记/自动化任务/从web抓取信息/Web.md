# _*Web抓取信息*_
* ## webbrowser：是 Python 自带的，打开浏览器获取指定页面。 
* ## requests：从因特网上下载文件和网页。 
* ## Beautiful Soup：解析 HTML，即网页编写的格式。 
* ## selenium：启动并控制一个 Web 浏览器。selenium 能够填写表单，并模拟鼠标 在这个浏览器中点击。 

## 1.webbrowser的基本用法
```
#! python3 
# mapIt.py - Launches a map in the browser using an address from the # command line or clipboard. 
 
import webbrowser, sys, pyperclip 
if len(sys.argv) > 1:     
# Get address from command line.     
address = ' '.join(sys.argv[1:]) 
else:     
# Get address from clipboard.     
address = pyperclip.paste()   //取得剪切板内容并保存在address中
 
 //调用webbrowser.open()启动外部浏览器访问URL
webbrowser.open('https://www.google.com/maps/place/' + address) 
```
### *不用和利用 mapIt.py 取得地图*

 手工取得地图 | 利用 mapIt.py 
----------- | -----------
高亮标记地址 |高亮标记地址 
拷贝地址 |拷贝地址 
打开 Web 浏览器 |运行 mapIt.py 
打开 http://maps.google.com/|  
点击地址文本字段  |
拷贝地址  |
按回车|

## 2. 用 requests 模块从 Web 下载文件 
* ### 用 requests.get()函数下载一个网页 (其中type()返回一个Response对象)
```
>>> import requests 
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') >>> type(res) 
<class 'requests.models.Response'>  
>>> res.status_code == requests.codes.ok     //判断是否下载成功（OK的状态码是“200）
True 
>>> len(res.text) 
178981 
>>> print(res.text[:250]) 
The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare 
 
This eBook is for the use of anyone anywhere at no cost and with almost no restrictions whatsoever. You may copy it, give it away or re-use it under the terms of the Proje 
 
```
* ### 检查错误
### *检查是否下载成功还有一个简单的方法，就是在Response对象上调用 raise_for_status()方法。如果下载文件出错，这将抛出异常。如果下载成 功，就什么也不做。*
```
>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist') >>> res.raise_for_status() 
Traceback (most recent call last):   File "<pyshell#138>", line 1, in <module>     res.raise_for_status()   
    File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status     raise HTTPError(http_error_msg, response=self) requests.exceptions.HTTPError: 404 Client Error: Not Found
```
* ### 将下载的文件保存在硬盘上
### *注意*：将 Web 页面保存到硬盘中的一 个文件。但是，这里稍稍有一点不同。首先，必须用“写二进制” 模式打开该文件， 即向函数传入字符串'wb'，作为 open()的第二参数。
为了将 Web 页面写入到一个文件，可以使用 for 循环和 Response 对象的 *iter_content()方法*。
```
>>> import requests 
>>> res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') >>> res.raise_for_status() 
>>> playFile = open('RomeoAndJuliet.txt', 'wb') 
>>> for chunk in res.iter_content(100000):
         playFile.write(chunk) 
 
100000 78981 
>>> playFile.close() 
``` 
## iter_content()方法在循环的每次迭代中，返回一段内容。每一段都是  *bytes* 数据类型，你需要指定一段包含多少字节。10 万字节通常是不错的选择，所以将 100000 作为参数传递给iter_content()。 
## 如果你想改变路径，你可以：
```
import webbrowser, os,requests

print(os.getcwd())  # 取得当前工作路径

os.chdir(r'C:\Users\王教授\Desktop')  # 修改当前工作路径
print(os.getcwd())
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
file = open('webtest1.txt','wb')      #在新的工作路径中创建新文件
for chunk in res.iter_content(100000):
    file.write(chunk)
file.close()
```
## *回顾一下，下载并保存到文件的完整过程如下：*
### 1. 调用 requests.get()下载该文件。 
### 2.用'wb'调用 open()，以写二进制的方式打开一个新文件。 
### 3.利用 Respose 对象的 iter_content()方法做循环。 
### 4.在每次迭代中调用 write()，将内容写入该文件。 
### 5.调用 close()关闭该文件。 

## 3.HTML
### 在你拆解网页之前，需要学习一些 HTML 的基本知识。你也会看到如何利用 Web 浏览器的强大开发者工具，它们使得从 Web 抓取信息更容易。 

## 4.用BeautifulSoup模块解析HTML
### BeautifulSoup将解析HTML文件
* ###  从 HTML 创建一个 BeautifulSoup 对象 
    * ### 通过直接下载主页来解析
    ```
    >>> import requests, bs4   #导入模块
    >>> res = requests.get('http://nostarch.com')   #下载主页 
    >>> res.raise_for_status()   #判断是否下载成功
    >>> noStarchSoup = bs4.BeautifulSoup(res.text) 
    >>> type(noStarchSoup)    #type()判断类型
    <class 'bs4.BeautifulSoup'> 
    ```
    * ### 也可以通过传递File对象来解析
    ```
    >>> >>> exampleFile = open(r'C:\Users\王教授\PycharmProjects\python学习笔记\自动化任务\从web抓取信息\example.html')    #打开创建好的HTML文件
    >>> exampleSoup = bs4.BeautifulSoup(exampleFile) 
    >>> type(exampleSoup) 
    <class 'bs4.BeautifulSoup'> 
    ```
    ## 有了BeautifulSoup对象之后，就可以利用它的方法，定位HTML文档中的特定部分。
 
 * ### 用select() 方法寻找元素

     *传递给 select()方法的选择器*    |    *将匹配…*
     --------------------------- | -------------------------------
    soup.select('div')  |   所有名为< div>的元素
    soup.select('#author') | 带有 id 属性为 author 的元素 
    soup.select('.notice') | 所有使用 CSS class 属性名为 notice 的元素 soup.select('div span') | 所有在< div>元素之内的< span>元素 
    soup.select('div > span') | 所有直接在< div>元素之内的< span>元素，中间没有其他元素 
    soup.select('input[name]') | 所有名为< input>，并有一个 name属性，其值无所谓的元素 
    soup.select('input[type="button"]') | 所有名为< input>，并有一个 type 属性，其值为 button 的元素

### *select()方法将返回一个 Tag 对象的列表，这是 Beautiful Soup 表示一个 HTML 元素的方式。*
```
>>> exampleFile = open(r'C:\Users\王教授\PycharmProjects\python学习笔记\自动化任务\从web抓取信息\example.html')    #打开创建好的HTML文件
>>> exampleSoup = bs4.BeautifulSoup(exampleFile) 
>>> elems = exampleSoup.select('#author')     #得到Tag对象的列表
>>> type(elems) 
<class 'list'>      #显示得到的类型为list
>>> len(elems) 
1 
>>> type(elems[0]) 
<class 'bs4.element.Tag'>      #表明是Tag对象
>>> elems[0].getText()        #返回该元素的文本
'Al Sweigart' 
>>> str(elems[0]) 
'<span id="author">Al Sweigart</span>' 
>>> elems[0].attrs          #返回一个字典
{'id': 'author'}
```

* ## 通过元素的属性获取数据

### *Tag 对象的 get()方法让我们很容易从元素中获取属性值。*

```
>>> exampleFile = open(r'C:\Users\王教授\PycharmProjects\python学习笔记\自动化任务\从web抓取信息\example.html')    #打开创建好的HTML文件
>>> spanElem = soup.select('span')[0] 
>>> str(spanElem) 
'<span id="author">Al Sweigart</span>' 
>>> spanElem.get('id')   #获取属性
'author' 
>>> spanElem.get('some_nonexistent_addr') == None 
True 
>>> spanElem.attrs 
{'id': 'author'}
```