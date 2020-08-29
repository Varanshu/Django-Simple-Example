from django.shortcuts import render
from django.urls import reverse
from markdown2 import Markdown
from . import util
from django.http import HttpResponseRedirect
import random

def index(request):
    try:
        a=request.GET['q']
        if(util.get_entry(a)):
            return HttpResponseRedirect(reverse("title",kwargs={'title':a}))
        else:
            list=[]
            for i in util.list_entries():
                if((i.lower()).find(a.lower())>-1):
                    list.append(i)
            if list==[]:
                return render(request, "encyclopedia/index.html", {
                    "title":"No Search Results",
                })
            else:
                return render(request, "encyclopedia/index.html", {
                    "title":"Search Results",
                    "entries": list
                })
    except:
        return render(request, "encyclopedia/index.html", {
            "title":"All Pages",
            "entries": util.list_entries()
        })

def title(request, title):
    a=util.get_entry(title)
    markdown=Markdown()
    if(a==None):
        b=None
    else:
        b=markdown.convert(a)
    return render(request,"encyclopedia/title.html",{
    "title":b,
    "t":title})

def create(request):
    if request.method=='POST':
        t=request.POST.get('title')
        c=request.POST.get('content')
        if(util.get_entry(t)):
            return render(request,"encyclopedia/create.html",{
            "error":True
            })

        util.save_entry(t,c)
        return HttpResponseRedirect(reverse("title",kwargs={'title':t}))
    return render(request,"encyclopedia/create.html",{
    "title":"Add a New Entry"
    })

def rand(request):
    a=util.list_entries()
    x=random.choice(a)
    return HttpResponseRedirect(reverse("title",kwargs={'title':x}))

def edit(request,title):
    return render(request,"encyclopedia/edit.html",{
        "t":title,
        "c":util.get_entry(title)
    })

def final(request):
    t=request.POST.get('title')
    c=request.POST.get('content')
    util.save_entry(t,c)
    print(t)
    return HttpResponseRedirect(reverse("title", kwargs={'title':t}))
