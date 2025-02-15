from django.shortcuts import render


posts = [
    {
        'author': 'Nicolas Francisco',
        'title': 'Blog 1',
        'content': 'Esse eh o primeiro blog',
        'date_posted': '30, Janeiro, 2025'
    },
    {
        'author': 'Valdonei Francisco',
        'title': 'Blog 2',
        'content': 'Esse eh o segundo blog',
        'date_posted': '31, Janeiro, 2025'
    }
]


# Create your views here.
def home(request):

    data = {
        'posts': posts
    }

    return render(request, 'blog/home.html', data)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
