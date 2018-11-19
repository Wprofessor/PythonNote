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