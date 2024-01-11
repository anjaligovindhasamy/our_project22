from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topic.html',d)

def webpage(request):
    QLTO=Webpage.objects.all()
    d={'webpage':QLTO}
    return render(request,'webpage.html',d)

def access(request):
    QLTO=AccessRecord.objects.all()
    d={'access':QLTO}
    return render(request,'access.html',d)
def insert_topic(request):
    to=input('enter the topic_name')
    NTO=Topic.objects.get_or_create(topic_name=to)[0]
    NTO.save()

    QLTO=Topic.objects.all()
    d={'topic':QLTO}
    return render(request,'display_topic.html',d)

def insert_webpage(request):
    to=input('enter topic_name')
    no=input('enter the name')
    uo=input('enter the url')
    NTO=Topic.objects.get(topic_name=to)
    NWO=Webpage.objects.get_or_create(topic_name=NTO,name=no,url=uo)[0]
    NWO.save()

    QLTO=Webpage.objects.all()
    d={'webpage':QLTO}
    return render(request,'webpage.html',d)

def insert_access(request):
    PK=int(input('enter the pk webpage'))
    do=input('enter the date')
    ao=input('enter the author')
    NWO=Webpage.objects.get(pk=PK)
    NAO=AccessRecord.objects.get_or_create(name=NWO,date=do,author=ao)[0]
    NAO.save()


    QLTO=AccessRecord.objects.all()
    d={'access':QLTO}
    return render(request,'access.html',d)