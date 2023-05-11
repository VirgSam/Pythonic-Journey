from django.urls import path
from . import views

urlpatterns = [
    path("",views.StartingPageView.as_view(), name="starting-page"),
    path("posts",views.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>",views.posts_detail,name="posts-detail-page"),

]