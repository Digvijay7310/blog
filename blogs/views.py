from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):

    category = get_object_or_404(Category, id=category_id)

    # Fetch the posts that belongs to the category with the id category id
    posts = Blog.objects.filter(status="Publish", category=category)

    context = {
        'posts': posts,
    }
    return render(request, 'posts_by_category.html', context)



def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    # First: same category, exclude current post
    related_posts = Blog.objects.filter(
        category=post.category,
        status="Publish"
    ).exclude(id=post.id)[:4]

    # Fallback: if not enough posts, get latest ones
    if related_posts.count() < 4:
        extra_posts = Blog.objects.filter(
            status="Publish"
        ).exclude(id__in=[p.id for p in related_posts]).exclude(id=post.id)[:4 - related_posts.count()]

        related_posts = list(related_posts) + list(extra_posts)

    context = {
        'post': post,
        'related_posts': related_posts,
    }

    return render(request, 'blog_detail.html', context)


def search(request ):
    keyword = request.GET.get('keyword')
    
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Publish')
  
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)