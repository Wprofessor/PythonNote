import re

begain = re.compile(r'^Hello')  # 匹配以‘Hello开始的字符串’
print(begain.search('Hello world'))
print(begain.search('He said hello.'))  # 输出None

end = re.compile(r'\d$')  # 匹配以数字结尾的字符串
print(end.search('fhdbs 5454'))
print(end.search('sdgs dour'))  # 输出None

whoel = re.compile(r'^\d+$')  # 匹配以数字开头数字结尾的字符串（自己也必须如此）
print(whoel.search('564645'))
print(whoel.search('45645 45654'))  # 输出None

robocop = re.compile(r'robocop', re.I)  # re.I意味着忽略大小写
x = robocop.search('RoboCop is part man, part machine, all cop.')
print(x.group())
