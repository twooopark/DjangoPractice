from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Emaillist
# Create your views here.

# # 핸들러 함수
# def index(request):
#     emaillist_list = Emaillist.objects.all().order_by('-id')
#     data = {'emaillist_list': emaillist_list}
#     # example에서 했던 HTTP 송수신 처리를 손쉽게 한다.
#     return render(request, 'index.html', data)

def index(request):
    emaillist_list = Emaillist.objects.all().order_by('-id')
    data = {'emaillist_list': emaillist_list}
    return render(request, 'emaillist/index.html', data)

def form(request):
    return render(request, 'emaillist/form.html')


def add(request):
    emaillist = Emaillist()
    emaillist.first_name = request.POST['fn']
    emaillist.last_name = request.POST['ln']
    emaillist.email = request.POST['email']

    # DB에 저장
    emaillist.save()

    # 응답
    return HttpResponseRedirect('/emaillist')
    # return render(request, 'index.html') # 'success.html')
