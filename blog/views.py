from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def showblog(rq):
	posts = Post.objects
	return render(rq,'blog/blog.html',{'posts':posts})

def specific_post(rq,post_id):	
	post=get_object_or_404(Post, pk=post_id)
	return render(rq,'blog/specific_post.html',{'post':post})
