# coding:utf-8

import urllib2
import re
import threading
import os

class A:  # 经典类  2.x
    pass

class B(object):  # 新式类 3.x 2.x
    pass



class spiderMaizi(threading.Thread):

    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(spiderMaizi, self).__init__(group, target, name, args, kwargs, verbose)
        self.__args = args
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36' \
                          ' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

    # 抓取网页内容
    def get_page(self, pageIndex):
        headers = {'User-Agent': self.user_agent}
        request = urllib2.Request(url=self.url % str(pageIndex), headers=headers)
        response = urllib2.urlopen(request)
        # print response.read()
        return response.read()

    #分析网页,获取需要的内容
    def analysis(self, content):
        pattern = re.compile('<p class="font20 color00 marginB14 t3out p">(.*?)<a href.*?简介：</span>(.*?)</p>', re.S)
        items = re.findall(pattern, content)
        return items

    # 保存内容
    def save(self, items):
        if not os.path.exists('maizi_teachers'):
            os.makedirs('maizi_teachers')
        for item in items:
            f = open('maizi_teachers/maizi_teachers4.txt', 'a')
            f.write(item[0]+':\n'+item[1].strip()+'\n')
            f.close()

    def run(self):
        try:
            print u'开始抓取内容....'
            content = self.get_page(self.__args[0])
            items = self.analysis(content)
            self.save(items)
            print u'内容抓取完毕....'
        except urllib2.HTTPError as e:
            print e
        except urllib2.URLError as e:
            print e
        except Exception as e:
            print e

if __name__ == '__main__':
    for x in range(1, 25):
        spider = spiderMaizi(args=(x,))
        spider.run()
        # spider.start()

