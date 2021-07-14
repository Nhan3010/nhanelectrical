from django.urls import path
from . import views
from .models import Post
from django.views.generic import ListView, DetailView

urlpatterns = [
   path('', views.PostListView.as_view(), name='blog'),
   path('<int:pk>/', views.PostDetailView.as_view(), name='post'),
]
urlpatterns = [
   path('', ListView.as_view(
      queryset = Post.objects.all().order_by('-date'),
      template_name = 'blog/blog.html',
      context_object_name = 'Posts',
      paginate_by = 10)
      , name='blog'),
   path('<int:pk>/', DetailView.as_view(
      model = Post,
      template_name = 'blog/post.html'),
      name='post'),
]