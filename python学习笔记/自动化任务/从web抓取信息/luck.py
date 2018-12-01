import requests,sys,webbrowser,bs4,os
#sys：在命令行输入内容

res = requests.get('http://google.com/search?q=lucky python programming tutorials')
res.raise_for_status()         #检验是否下载成功

soup = bs4.BeautifulSoup(res.text,"html.parser")

linkElems = soup.select('.r a')

numopen = min(5,len(linkElems))
for i in range(numopen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))