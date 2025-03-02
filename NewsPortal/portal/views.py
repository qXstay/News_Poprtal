from django.shortcuts import render, get_object_or_404
from .models import Post

def news_list(request):
    # Получаем все новости (посты с типом 'news')
    news = Post.objects.filter(post_type='news').order_by('-created_at')
    return render(request, 'portal/news_list.html', {'news': news})

def news_detail(request, post_id):
    # Получаем конкретную новость по её ID
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'portal/news_detail.html', {'post': post})

def home(request):
    return render(request, 'portal/index.html')