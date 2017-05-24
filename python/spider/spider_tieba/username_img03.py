# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
# 描述：利用HTMLParser抓取贴吧内容。

from HTMLParser import HTMLParser
import requests
import os

class TieBaParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.username = []

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    return attr[1]
            return None

        if tag == 'img' and _attr(attrs, 'username') and _attr(attrs, 'data-tb-lazyload'):
            user = {}
            user['username'] = _attr(attrs, 'username')
            user['url'] = _attr(attrs, 'data-tb-lazyload')
            self.username.append(user)
            print user
            _download_poster_image(user,'img')

#下载图片
def _download_poster_image(user,path):
    if not os.path.exists(path):
        os.makedirs(path)
    url = user['url']
    fname = user['username']
    r = requests.get(url)
    with open('img/'+fname.decode('utf-8')+'.jpg','wb') as f:
        f.write(r.content)

#获取网页信息
def get_page():
    url = 'http://tieba.baidu.com/p/1072881148?pn=2'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    r = requests.get(url=url, headers=headers)
    parser = TieBaParser()
    parser.feed(r.content)
    return parser.username

if __name__ == '__main__':
    user = get_page()

    # import json
    # print('%s' % json.dumps(user, sort_keys=True, indent=4, separators=(',', ': ')))