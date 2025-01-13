from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
def index(request):
    return HttpResponse("Hi, You are at blog's index")

def detail(request, post_id):
    return HttpResponse(f"You are viewing post detail page. And ID is {post_id}")

def old_url_redirect(request):
    return redirect("new_url")

def new_url_redirect(request):
    return HttpResponse("This is the New Url")