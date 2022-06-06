from django.shortcuts import get_object_or_404, render
from .models import BlogPost

def all_blogs(request):
    
    blog_posts = BlogPost.objects.order_by("-publishing_date")
    
    return render(request, 'blogs/all_blogs.html', {'blog_posts': blog_posts})


def detail(request, blog_id):
    blog = get_object_or_404(BlogPost, pk=blog_id)
    return render(request, "blogs/detail.html", {'blog': blog})