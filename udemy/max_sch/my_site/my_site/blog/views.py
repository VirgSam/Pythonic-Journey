from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, # DetailView 
from django.views import View
from . models import Post
from . forms import CommentForm


# Create your views here.
class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts" 

    def get_queryset(self):
        queryset= super().get_queryset()
        data = queryset[:3]
        return data

# retired function view    
# def starting_page(request):
#     latest_post= Post.objects.all().order_by("-date")[:3]
#     return render (request,"blog/index.html",{"posts":latest_post})

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# retired function view 
# def posts(request):
#     posts_list= Post.objects.all().order_by("-date")
#     return render (request,"blog/all-posts.html",{"all_posts":posts_list})

class SinglePostView(View):
    template_name = "blog/post-detail.html"
    model = Post

    def get(self, request, slug):
        post=Post.objects.get(slug=slug)
        context= {
            "post": post,
            "post_tags":post.tags.all(),
            "comment_form": CommentForm()
        }
        return render(request,"blog/post-detail.html")
        pass

    def post(self, request):
        pass

    

# retired DetailView and used View to get more control on handling post request
# class SinglePostView(DetailView):
#     template_name = "blog/post-detail.html"
#     model = Post

#     def get_context_data(self, **kwargs: Any):
#         context= super().get_context_data(**kwargs)
#         context["post_tags"] = self.object.tags.all()
#         context["comment_form"] = CommentForm
#         return context
    
# retired function view 
# def posts_detail(request, slug):
#     search_post =get_object_or_404(Post, slug=slug)
#     return render(request,"blog/post-detail.html",{
#                                                     "post":search_post,
#                                                     "post_tags":search_post.tags.all(),
                                                    
#                                                     })