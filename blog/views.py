from django.shortcuts import render
from .models import Blogs
# Create your views here.
def allblogs(request):
     blogs= Blogs.objects.all()
     return render(request,'blog/allblogs.html',{'blogs':blogs})
