# -*- coding: utf-8 -*-

# 请编写一个函数handler_url，该函数的传入参数为url，传出参数为一个字典result，该函数能够把url的每一部分分割,url个格式为：
# [http://]www.maiziedu.com[:8080]/[userinfo/1]
# []中的可以省略不写
#
# result的格式为：
# result={
#    "protocol":"http"（默认为http），
#    "host" : "www.maiziedu.com"，
#    "port" : 80（默认为80），
#    "page" : "/userinfo/1/"（默认为/）
# }


str1 = "http://www.maiziedu.com:8080/userinfo/1"
str2 = "www.maiziedu.com"
str3 = "https://www.maiziedu.com/"
str4 = "https://www.maiziedu.com/userinfo/"
str5 = "www.maiziedu.com/userinfo"


def handler_url(url):

    result = {
        "protocol": "http",
        "host": "www.maiziedu.com",
        "port": 80,
        "page": "/userinfo/1/"
    }

    if not url.endswith("/"):
        url = url + "/"

    pos_protocol = url.find("://")

    if pos_protocol != -1:
        result["protocol"] = url[0: pos_protocol]
        url = url[pos_protocol + 3: len(url)]
        print("url:" + url)

    pos_port = url.find(":")
    if pos_port != -1:
        result["host"] = url[0: pos_port]
        url = url[pos_port + 1: len(url)]
        print("url:" + url)

        pos_page = url.find("/")
        result["port"] = url[0: pos_page]
        result["page"] = url[pos_page: len(url)]
    else:
        pos_page = url.find("/")
        result["page"] = url[pos_page: len(url)]

    return result

result1 = handler_url(str1)
result2 = handler_url(str2)
result3 = handler_url(str3)
result4 = handler_url(str4)
result5 = handler_url(str5)

print("result1:" + str(result1))
print("result2:" + str(result2))
print("result3:" + str(result3))
print("result4:" + str(result4))
print("result5:" + str(result5))
