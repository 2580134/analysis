import requests
from bs4 import BeautifulSoup
import urllib.request
src_list = []

def getHTMLText(url_photo):
    kv={"User-Agent":"Mozilla/5.0"}
    r = requests.get(url_photo, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    count = 1   #图片计数
    count = count + 1
    root = "E:/课程设计/2020-2021-1数据采集课设/高考数据分析/各省高考一分一段表数据/山东数据图片/" + str(count) + ".jpg"
    urllib.request.urlretrieve(url_photo,root)
    print("正在存储第" + str(count) + "张")

def getpthoto():
    res = requests.get("https://dy.163.com/article/FIFV0P9T0512ES8F.html")
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    for i in soup.find_all('p', attrs={"class": "f_center"}):
        #print(i)
        src = i.find('img').attrs['src']  # 读
        src_list.append(src)
    # print(src_list)
    return src_list

def main():
    url = getpthoto()
    # print(url)
    for str in url:
        #print(str)
        html = getHTMLText(str)
        print(html)
main()

