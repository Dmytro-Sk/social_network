from django.shortcuts import render
from .models import Post


def home_page(request):
    context = {
            'posts': Post.objects.all()
        }
    return render(request, 'posts/home_page.html', context)
