from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *

from app.models import *

def insert_topic(request):
    TFO=TopicForm()
    d={"TFO":TFO}
    if request.method=="POST":
        TFD=TopicForm(request.POST)
        TFD.save()
        
        return HttpResponse("topic data insert successfully")
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={"WFO":WFO}
    if request.method=="POST":
        WFD=WebpageForm(request.POST)
        WFD.save()
        
        return HttpResponse("webpage data insert successfully")
    
    
    
    return render(request,'insert_webpage.html',d)


def insert_access_record(request):
    AFO=AccessRecordForm()
    d={"AFO":AFO}
    if request.method=="POST":
        AFD=AccessRecordForm(request.POST)
        AFD.save()
        
        return HttpResponse("access_record data insert successfully")
    
    

    return render(request,'insert_access_record.html',d)