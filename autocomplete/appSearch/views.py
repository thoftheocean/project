from appSearch.models import Search
import json
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import connection

@csrf_exempt
def search(request):
    return render(request, 'search1.html')


@csrf_exempt
def process(request):
    #原生sql

    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM appSearch_search WHERE keys='北京' ")
    # content = cursor.fetchall()
    # print(content[0][1])


    search_content = request.GET['search_content']
    print(search_content)
    recontents=Search.objects.filter(keys__startswith=search_content)
    rejson={}
    for i in recontents:
        rejson[i.keys] = i.keys
    print(rejson)
    # rejson={'1': 1}
    return HttpResponse(json.dumps(rejson), content_type='application/json')
    # return HttpResponse(rejson)