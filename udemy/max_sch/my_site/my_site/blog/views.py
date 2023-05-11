from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . models import Post


# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    pass
def starting_page(request):
    latest_post= Post.objects.all().order_by("-date")[:3]
    return render (request,"blog/index.html",{"posts":latest_post})
                               
def posts(request):
    posts_list= Post.objects.all().order_by("-date")
    return render (request,"blog/all-posts.html",{"all_posts":posts_list})

def posts_detail(request, slug):
    search_post =get_object_or_404(Post, slug=slug)
    return render(request,"blog/post-detail.html",{
                                                    "post":search_post,
                                                    "post_tags":search_post.tags.all(),
                                                    
                                                    })