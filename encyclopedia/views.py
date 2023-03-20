from turtle import title
from django.shortcuts import redirect, render
from django.http import HttpResponse
import markdown2
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
import random


from . import util



def index(request):
    if request.GET.get('q'):
        return searchbar(request, request.GET['q'])
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def searchbar(request, query):
    searchlist = [x.lower() for x in util.list_entries()]
    searchresult = [f"<li> <a href='wiki/{result}'> {result} </a> </li>" for result in searchlist if query.lower() in result.lower()]
    
    if query in searchlist:
        return entries(request, query)

    else: 
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "searchresult": ''.join(searchresult)
        })

@csrf_exempt
def entries(request, title):
    md = util.get_entry(title)
    if md:
        html = markdown2.markdown(md)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "body": html
            })
    else:
        return render(request, "encyclopedia/notfound.html", {
            "title": title,
        })

@csrf_exempt
def newpage(request):
    if request.method == 'POST' and 'savebutton' in request.POST:
        title = request.POST.get('title_entry')
        content = request.POST.get('body_entry')
        searchlist = [x.lower() for x in util.list_entries()]
        if title.lower() in searchlist:
            error = "<li id='error' style='color:red;'>A page with that title already exists</li>"
            return render(request, "encyclopedia/newpage.html", {
            "error": error,
        })
        else:
            util.save_entry(title, content)
            return redirect("wiki/" + title)
    return render(request, "encyclopedia/newpage.html")

@csrf_exempt
def edit(request):
    if request.method == 'POST' and 'editbutton' in request.POST:
        title = request.POST.get('editbutton')
        body = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html", {
            "title": title,
            "body": body
        })
    elif request.method == 'POST' and 'savebutton' in request.POST:
        title = request.POST.get('savebutton')
        content = request.POST.get('body_edit')
        util.save_entry(title, content)
        return entries(request, title=title)

def randompage(request,):
    titlelist = util.list_entries()
    titlenumber = random.randint(0, len(titlelist) - 1)
    title = titlelist[titlenumber]
    md = util.get_entry(title)
    body = markdown2.markdown(md)
    return entries(request, title)