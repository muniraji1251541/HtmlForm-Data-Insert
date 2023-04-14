from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('Topic data inserted successfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        url=request.POST['url']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=em)[0]
        WO.save()
        return HttpResponse('Webpage data inserted successfully')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    LWO=Webpage.objects.all()
    d={'webpages':LWO}

    if request.method=='POST':
        na=request.POST.get('na')
        au=request.POST.get('au')
        da=request.POST.get('da')
        WO=Webpage.objects.get(name=na)

        AO=AccessRecord.objects.get_or_create(name=WO,author=au,date=da)[0]
        AO.save()
        return HttpResponse('AccessRecord data inserted successfully')
    return render(request,'insert_accessrecord.html',d)