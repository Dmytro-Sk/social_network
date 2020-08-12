from django.shortcuts import render


# todo This is temporary block
def home_page(request):
    context = {
            'posts': posts
        }
    return render(request, 'posts/home_page.html', context)


# todo This is temporary block
posts = [
    {
        'author': 'User1',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'August 12, 2020'
    },
    {
        'author': 'User 2',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'August 13, 2020'
    }
]
