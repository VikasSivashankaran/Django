from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.urls import reverse
# Create your views here.
def index(request):
    blog_title = "New Feeds"
    posts = [
        {'id':1,'title':'Post 1', 'content':'Content of Post 1'},
        {'id':2,'title':'Post 2', 'content':'Content of Post 2'},
        {'id':3,'title':'Post 3', 'content':'Content of Post 3'},
        {'id':4,'title':'Post 4', 'content':'Content of Post 4'},
    ]
    return render(request,'index.html',{'blog_title':blog_title, 'posts':posts })   #variable interpolation

def detail(request, post_id):
    return render(request,'detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the New Url")