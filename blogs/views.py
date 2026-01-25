from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    # Fetch the posts that belongs to the category with the id category id
    posts = Blog.objects.filter(status="Publish", category=category)

    context = {
        'posts': posts
    }
    return render(request, 'posts_by_category.html', context)