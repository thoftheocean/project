# !/usr/bin/env python
# coding:utf-8
# author hx
#描述：使用urllibs抓取麦子学院的老师信息

import urllib2
import re
import os


class Spider(object):
    # 构造方法
    def __init__(self):
        self.url = 'http://www.maiziedu.com/course/teachers/?page=%s'
        self.user_agent ='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'

    # 获取网页源代码
    def get_page(self, page_index):
        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url=self.url % str(page_index), headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print e
        except urllib2.URLError as e:
            print e

    # 分析源代码
    def analysis(self, content):
        pattern = re.compile('<p class="font20 color00 marginB14 t3out p">(.*?)<a href.*?简介：</span>(.*?)</p>', re.S)
        items = re.findall(pattern, content)
        return items

    # 保存数据
    def save(self, items, path, page_index):
        for item in items:
            #path = 'maiziTeachers'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path + '/' + 'maizi_teachers' + '_page' + str(page_index) + '.txt'
            teachers = item[0] + ':\n' + item[1].strip() + '\n'
            with open(file_path, 'a')as f:
                f.write(teachers)

    # 运行
    def run(self):
        print 'Honey开始抓内容咯'
        for i in range(1, 10):
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items, 'maiziTeachers', i)
        print '好累啊，终于抓取内容完咯'

if __name__ == '__main__':
    spider = Spider()
    spider.run()

