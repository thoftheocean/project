from django.shortcuts import render, render_to_response, redirect
from todolist.models import Todolist
from django.http import HttpRequest,HttpResponse

def todolist(request):
    todolists=Todolist.objects.all()

    if request.method == 'POST':
        event = request.POST['event']
        Todolist.objects.create(event=event, status='undo')

    if request.GET.get('operate') == "delete":
        # 删除
        delete_event = Todolist.objects.filter(id = request.GET.get('id'))
        if delete_event != None:
            delete_event.delete()

    if request.GET.get('operate') == "save":
        # 保存编辑
        Todolist.objects.filter(id=request.GET.get('id')).update(event=request.GET.get('value'))

    if request.GET.get('status'):
        # 保存状态
        Todolist.objects.filter(id=request.GET.get('id')).update(status = request.GET.get('status'))

    return render(request, 'todolist.html', locals())