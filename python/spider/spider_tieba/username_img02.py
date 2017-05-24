# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
# 描述：利用正则抓取贴吧头像，并将用户名作为头像的名字。

import requests
import re
import os

class Spider_tieba:
    def __init__(self):
        self.content = None
        self.m = None
        self.n = None

    #获取网页源代码
    def get_page(self):
        url = 'http://tieba.baidu.com/p/1072881148?pn=2'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
        r = requests.get(url, headers)
        self.content = r.content
        # print self.content

    #分析源代码
    def get_content(self):
        pattern1 = re.compile(r'<a style="" target="_blank" class="p_author_face " (.*?)<img username="(.*?)" class="" src="(.*?)"/></a>',re.S)
        pattern2 = re.compile(r'<img username="(.*?)" class="" (.*?)data-tb-lazyload="(.*?)"/></a>', re.S)
        self.m = re.findall(pattern1, self.content)
        self.n = re.findall(pattern2, self.content)

    #下载图片
    def download_img(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        #贴吧前三个头像获取
        for i in range(0, 3):
            name = self.m[i][1]
            url = self.m[i][2]
            print name, url
            r = requests.get(url)
            file_path = path + '/' + name.decode('utf-8') + '.jpg'
            with open(file_path, 'wb') as f:
                f.write(r.content)
        #贴吧后面的头像获取
        for j in range(0, len(self.n)):
            name = self.n[j][0]
            url = self.n[j][2]
            print name, url
            r = requests.get(url)
            file_path = path + '/' + name.decode('utf-8') + '.jpg'
            with open(file_path, 'wb',) as f:
                f.write(r.content)

if __name__ == "__main__":
    st = Spider_tieba()
    st.get_page()
    st.get_content()
    st.download_img('img')

