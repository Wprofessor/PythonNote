# 利用 requests 模块下载页面。
# 利用 Beautiful Soup 找到页面中漫画图像的 URL。
# 利用 iter_content()下载漫画图像，并保存到硬盘。
# 找到前一张漫画的链接 URL，然后重复。
import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)  # 确保文件夹存在
while not url.endswith('#'):
    print('下载网页 %s' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,"html.parser")
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('no find')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)  # 保存漫画图像文件
        res.raise_for_status()
        # 保存漫画
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')    #basename只返回URL的最后部分
        for chunk in res.iter_content(100000):      #循环将图像数据写入文件
            imageFile.write(chunk)
        imageFile.close()

    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done')
