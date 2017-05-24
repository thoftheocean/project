# usr/bin/env python
# encoding:utf-8
# author hexi
# python2环境
from HTMLParser import HTMLParser
import requests
import re

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.in_movies = False

    def handle_starttag(self, tag, attrs):
        def _attr(attrlist, attrname):
            for attr in attrlist:
                if attr[0] == attrname:
                    # print(attr)
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-title') and _attr(attrs,'data-category')=='upcoming':
            movie ={}
            movie['title'] = _attr(attrs, 'data-title')
            movie['duration'] = _attr(attrs, 'data-duration')
            movie['region'] = _attr(attrs, 'data-region')
            movie['director'] = _attr(attrs, 'data-director')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print('%(title)s|%(duration)s|%(region)s|%(director)s|%(actors)s' % movie)
            self.in_movies = True
        if tag == 'img' and self.in_movies:
            self.in_movies = False
            src = _attr(attrs,'src')
            movie = self.movies[len(self.movies)-1]
            movie['poster-url']=src
            _download_poster_image(movie)
#下载电影的海报
def _download_poster_image(movie):
    src = movie['poster-url']
    r = requests.get(src)
    fname =src.split('/')[-1]  #split()通过指定分隔符对字符串进行切片
    with open('img/'+fname,'wb') as f:   #图片通过wb写入。
        f.write(r.content)
        movie['poster-url'] = fname
#下载电影信息
def upcoming_movies():
    url = 'https://movie.douban.com/cinema/nowplaying/chengdu/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
    r = requests.get(url=url,headers=headers)
    parser = MovieParser() #实例化
    parser.feed(r.content) #将内容送入parser对象
    r.close()
    return parser.movies

if __name__ == '__main__':
    movies = upcoming_movies()

    import json
    print('%s' % json.dumps(movies, sort_keys=True, indent=4, separators=(',', ': '))) #字典转化为字符串