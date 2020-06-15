from django.shortcuts import render,redirect
from django.http import HttpResponse
from restoran.models import *

from .forms import ZakazForm
a = 0
def index(request):
    len_c = int((len(Category.objects.all()))/2)
    #print(len_c)
    left_categories = Category.objects.all()[:len_c]
    right_categories = Category.objects.all()[len_c:]
    return render(request,'index.html',{'left_categories':left_categories,'right_categories':right_categories})


def AddZakaz(request):
    form = ZakazForm(request.POST)
    if form.is_valid():
        print('123')
        form.save()
    print(form)
    return redirect("/")

