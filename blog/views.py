import markdown
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from comments.forms import CommentForm
# Create your views here.


def index(request):
    article_list = Article.objects.all().order_by("-create_time")
    return render(request, "blog/index.html", context={"article_list": article_list})


def detail(reqeust, pk):
    article = get_object_or_404(Article, pk=pk)
    article.body = markdown.markdown(article.body, [
        'extra',
        'codehilite',
        'toc',
    ])
    form = CommentForm()
    comment_list = article.comment_set.all()
    context = {
        "article": article,
        'form': form,
        'comment_list': comment_list
    }
    return render(reqeust, "blog/detail.html", context=context)


def archives(request, year, month):
    article_list = Article.objects.filter(
        create_time__year=year,
        create_time__month=month
    ).order_by('-create_time')
    return render(request, "blog/index.html", context={'article_list': article_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article = Article.objects.filter(category = cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'article_list': article})
