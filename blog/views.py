from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
# Create your views here.
def index(request):
    return HttpResponse("Hi, You are at blog's index")

def detail(request, post_id):
    return HttpResponse(f"You are viewing post detail page. And ID is {post_id}")