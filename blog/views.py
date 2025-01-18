from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
from django.urls import reverse
# Create your views here.
def index(request):
    blog_title = "New Feeds"
    return render(request,'index.html',{'blog_title':blog_title})   #variable interpolation

def detail(request, post_id):
    return render(request,'detail.html')

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the New Url")