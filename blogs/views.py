from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):

    try:
        category = get_object_or_404(Category, id=category_id)
    except:
        return redirect('home')

    # Fetch the posts that belongs to the category with the id category id
    posts = Blog.objects.filter(status="Publish", category=category)

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'posts_by_category.html', context)


# def blog_detail(request, blog_id):
#     blog = get_object_or_404(Blog, pk=blog_id)
#     return render(request, 'blog_detail.html', {'blog_detail': blog})