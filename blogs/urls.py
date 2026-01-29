from django.urls import path
from . import views


urlpatterns = [
    path('<int:category_id>/', views.posts_by_category , name="posts_by_category"),
    # path('<int:blog_id>/', views.blog_detail , name="blog_detail"),
]
