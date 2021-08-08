from django.shortcuts import render
from .models import Post

# Create your views here.

def showblog(rq):
	posts = Post.objects
	return render(rq,'blog/blog.html',{'posts':posts})