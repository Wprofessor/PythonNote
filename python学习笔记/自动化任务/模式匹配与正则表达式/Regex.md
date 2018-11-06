# 正则表达式
- ## 创建正则表达式对象
    ### 向 re.compile()传入一个字符串值，表示正则表达式，
    它将返回一个 Regex 模式 对象（或者就简称为 Regex 对象）
    ```
    >>>phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    ```
    现在phoneNumRegex变量包含了一个Regex对象，r代表原始字符串。
- ## 匹配Regex对象
    Regex 对象的 search()方法查找传入的字符串，寻找该正则表
    达式的所有匹配。如 果字符串中没有找到该正则表达式模式，
    search()方法将返回None。如果找到了该模式， search()方法将
    返回一个Match 对象。Match 对象有一个group()方法，它返回被
    查找字 符串中实际匹配的文本。
    ```
    >>>phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    >>>mo = phoneNumRegex.search(''My number is 415-555-4242.')
    >>>print('mo.group()')
    ```
    Match对象的group()方法会返回匹配结果。
## 基本步骤非常简单（python）
    1.用 import re 导入正则表达式模块；
    2.用 re.compile()函数创建一个 Regex 对象（记得使用原始字符串）；
    3.向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象；
    4.．调用 Match 对象的 group()方法，返回实际匹配文本的字符串。


##  利用括号分组：
```
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') 
>>> mo = phoneNumRegex.search('My number is 415-555-4242.') 
>>> mo.group(1) 
'415'
>>> mo.group(2) 
'555-4242' 
>>> mo.group(0) 
'415-555-4242' 
>>> mo.group() 
'415-555-4242'
>>> mo.groups() 
('415', '555-4242') 
>>> areaCode, mainNumber = mo.groups() 
>>> print(areaCode) 
415 
>>> print(mainNumber) 
555-4242
```
### 你也可以在文本中匹配括号
```
>>> phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)') 
>>> mo = phoneNumRegex.search('My phone number is (415) 555-4242.') 
>>> mo.group(1) 
'(415)' 
>>> mo.group(2) 
'555-4242'
```
## 用管道匹配多个分组：
### 字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它。
```
>>> heroRegex = re.compile (r'Batman|Tina Fey') 
>>> mo1 = heroRegex.search('Batman and Tina Fey.') 
>>> mo1.group() 
'Batman'  
>>> mo2 = heroRegex.search('Tina Fey and Batman.') 
>>> mo2.group() 
'Tina Fey' 
```
### 也可以使用管道来匹配多个模式中的一个，作为正则表达式的一部分
## 用问号实现可选匹配:
```
>>> batRegex = re.compile(r'Bat(wo)?man') 
>>> mo1 = batRegex.search('The Adventures of Batman') 
>>> mo1.group() 
'Batman'  
>>> mo2 = batRegex.search('The Adventures of Batwoman') 
>>> mo2.group() 
'Batwoman' 
```
### 正则表达式中括号部分表明是可选部分，如果要匹配？，则要加转义字符。
## 用星号匹配零次或多次：
```
>>> batRegex = re.compile(r'Bat(wo)*man') 
>>> mo1 = batRegex.search('The Adventures of Batman') 
>>> mo1.group() 
'Batman'  
>>> mo2 = batRegex.search('The Adventures of Batwoman') 
>>> mo2.group() 
'Batwoman'  
>>> mo3 = batRegex.search('The Adventures of Batwowowowoman') >>> mo3.group() 
'Batwowowowoman'
```
##  用加号匹配一次或多次 ：
### 注意：正则表达式中+号和*号的区别是，*号不必要求分组必须出现在字符串中，但是+号要求分组至少在字符串中出现一次。
```
>>> batRegex = re.compile(r'Bat(wo)+man') 
>>> mo1 = batRegex.search('The Adventures of Batwoman') 
>>> mo1.group() 
'Batwoman'  
>>> mo2 = batRegex.search('The Adventures of Batwowowowoman') 
>>> mo2.group() 
'Batwowowowoman'  
>>> mo3 = batRegex.search('The Adventures of Batman') 
>>> mo3 == None 
True
```
## 用花括号匹配特定次数：
### 例如：(Ha){3}将匹配3次，(Ha){3,}将匹配 3 次或更多次实例，(Ha){,5}将匹配 0 到 5 次实例。花括号让正则表 达式更简短。这两个正则表达式匹配同样的模式。 
```
>>> haRegex = re.compile(r'(Ha){3}') 
>>> mo1 = haRegex.search('HaHaHa') 
>>> mo1.group() 
'HaHaHa'  
>>> mo2 = haRegex.search('Ha') 
>>> mo2 == None 
True 
```

## findall()方法：
### 除了search()方法外，Regex对象也有一个findall()方法。不过findall()方法返回一个列表，包含被查找字符串的所有匹配。
```
>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups 
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
['415-555-9999', '212-555-0000']
```
```
>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups 
>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') 
[('415', '555', '1122'), ('212', '555', '0000')] 
```
### 作为 findall()方法的返回结果的总结，请记住下面两点： 
    1.如果调用在一个没有分组的正则表达式上，例如\d\d\d-\d\d\d-\d\d\d\d，方法 findall()将返回一个匹配字符串的列表，例如['415-555-9999', '212-555-0000']。 
    2.．如果调用在一个有分组的正则表达式上，例如(\d\d\d)-(\d\d\d)-(\d\d\d\d)，方 法 findall()将返回一个字符串的元组的列表（每个分组对应一个字符串），例如[('415', '555', '1122'), ('212', '555', '0000')]。 