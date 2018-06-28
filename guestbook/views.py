from django.shortcuts import render
from .models import Guestbook
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    guestbook_list = Guestbook.objects.all().order_by('-regdate')
    context = {'guestbook_list' : guestbook_list}
    return render(request, 'guestbook/index.html', context)


def add(request):
    guestbook = Guestbook()
    guestbook.name = request.POST['name']
    guestbook.password = request.POST['password']
    guestbook.message = request.POST['message']

    # DB에 저장
    guestbook.save()

    # 응답
    return HttpResponseRedirect('/guestbook')
