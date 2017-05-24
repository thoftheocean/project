# !/usr/bin/env python
# coding:utf-8
# author hx
# str1 = 'http://www.maiziedu.com:8080/userinfo/1'
# str1 = "www.maiziedu.com"
# str1 = "https://www.maiziedu.com/"
# str1 = "https://www.maiziedu.com/userinfo/"
str1 = "www.maiziedu.com/userinfo"
resul = dict()
#protocol
if str1.find('http') == -1 and str1.find('https') == -1:
    resul['protocol'] = 'http'
else:
    end1 = str1.find('/')
    print end1
    resul['protocol'] = str1[0:end1-1]
#host
start2 = str1.find('www')
print start2
end2 = str1.find('.com')+4
print end2
resul['host'] = str1[start2:end2]
#port
if str1.find(':8080') == -1:
    resul['port'] = '80'
    end3 = end2
    print end3
else:
    start3 = str1.rfind(':')
    end3 = start3+5
    print end3
    resul['port'] = str1[start3:end3]
#page
if len(str1) > end3:
    resul['page'] = str1[end3:]
else:
    resul['page'] = '/'
print resul

