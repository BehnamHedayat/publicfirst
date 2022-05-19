from unicodedata import category
from django.shortcuts import render
from .models import Post, Category, Author

# Create your views here.

def homepage(request):
    categories = Category.objects.all()[0:3]
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context = {
        'object_list' : featured,
        'latest': latest,
        'categories': categories,
    }
    return render(request, 'homepage.html', context)


def post(request,slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context)


def about(request):
    return render(request, 'about_page.html')


def postlist(requset, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category__in=[category])
    context = {
        'posts': posts,
    }
    return render(requset, 'post_list.html', context)


def allposts(request):
    posts =Post.objects.order_by('-timestamp')
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)


def search(request):
    
    return render(request, 'search_bar.html')

