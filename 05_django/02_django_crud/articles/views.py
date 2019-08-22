from Ipython import embed
from django.core.exception import ValidationError
from django.shortcuts import render
from .models import Article


# Create your views here.
def index(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.all()[::-1]
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2
    article = Article(title=title, content=content)
    article.save()

    #3
    # Article.objects.create(title=title, content=content)

    return redirect(f'/articles/{article.pk}/')
    # return redirect('/articles/', article.pk') 

    return render(request, 'articles/create.html')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'article/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}')