from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Post, Category

def index(request):
    # posts = Post.objects.all()
    post_list = Post.objects.order_by('-published_date')[:5]
    # context = {'post_list': post_list}
    return render_to_response('blog/index.html', {'post_list': post_list, 'categories': Category.objects.all()})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/category.html', {'category': category, 'posts': Post.objects.filter(category=category)[:5]})

def post(request, slug):
    args = {'post': get_object_or_404(Post, slug=slug)}
    return render_to_response('blog/post.html', args) 


# def post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render_to_response('blog/post.html', {'post': post}, context_instance=RequestContext(request))