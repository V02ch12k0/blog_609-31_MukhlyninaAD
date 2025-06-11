from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article


def homepage(request):
    articlesList = Article.objects.all()[:5]
    data = {"message": "Discover Stories That Resonate",
            "articlesList": articlesList}
    return render(request, 'homepage.html', context=data)


def about(request):
    header = "About us"
    staff = ['John Nichols', 'John Rogers', 'Timothy Smith']
    director = {"name": "David Lee", "img": '/director.jpg'}
    address = ('20 W 34th St.', 'New York', 'NY 10001', 'USA')
    data = {"header": header, "staff": staff, "director": director, "address": address}
    return render(request, 'about.html', data)

def articles(request):
    return render(request, 'article_list.html', name='article')