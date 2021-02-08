from django.shortcuts import render, get_object_or_404
from .models import Blogs
# Create your views here.
def allblogs(request):
     blogs= Blogs.objects.all()
     return render(request,'blog/allblogs.html',{'blogs':blogs})
def detail(request,blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':blog})
