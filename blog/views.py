from django.shortcuts import render
from .models import *
from .forms import *
from django import template
import mistune
def index(request):
    """首页展示"""
    # 取出所有博客文章
    all_articles = Article.objects.all()
    # 取出要推荐的博客文章
    top_articles = Article.objects.filter(is_recommend=True)
    top_emission = Emission.objects.all()[:8]
    links = Link.objects.all()
    # 需要传递给模板（templates）的对象
    context = {
        'all_articles': all_articles,
        'top_articles': top_articles,
        'top_emissions': top_emission,
        'links':links,
               }
    return render(request, 'index.html',context)

def articles(request):
    all_articles = Article.objects.all()
    top_articles = Article.objects.filter(is_recommend=True)
    context = {
        'all_articles': all_articles,
        'top_articles': top_articles,
    }
    return render(request, 'blog-list.html',context)

def podcast(request):
    emi = Emission.objects.all()
    context = {
        'emis': emi,
    }
    return render(request, 'podcast.html',context)

def podcast_detail(request, id):
    emi = Emission.objects.get(id=id)
    context = {
        'emi': emi,
    }
    return render(request, 'play.html',context)

def article_detail(request,id):
    """文章详情页"""
    # 取出相应的文章
    article = Article.objects.get(id=id)
    # 增加阅读数
    article.click_count += 1
    article.save(update_fields=['click_count'])
    #前台mK解析
    mk = mistune.Markdown()
    output = mk(article.content)
    # 需要传递给模板的对象
    context = {
        'article': article,
        'article_detail_html': output,
    }
    # 载入模板，并返回context对象
    return render(request,'article_detail.html',context)

def member(request):
    '''成员详情页'''
    links = Link.objects.all()
    context = {'links':links,}
    return render(request,'member.html',context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
        else:
            form = ContactForm()
        return render(request, template, {'contactform':form})
    return render(request, "contact.html")

def category_tag(request):
    '''分类和标签页'''
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'categories':categories,
        'tags':tags,
    }
    return render(request,'category_tag.html',context)

def article_category(request,id):
    '''文章分类详情页'''
    categories = Category.objects.all()
    articles = Category.objects.get(id=id).article_set.all()#获取该id对应的所有的文章
    context = {
        'categories': categories,
        'id': id,
        'articles': articles
    }
    return render(request, 'article_category.html', context)

def article_tag(request,id):
    '''文章标签详情页'''
    tags = Tag.objects.all()
    articles = Tag.objects.get(id=id).article_set.all()
    context = {
        'tags': tags,
        'id': id,
        'articles': articles
    }
    return render(request, 'article_tag.html', context)

def add_nav(request):
    category_nav = Category.objects.filter(add_menu=True).order_by('index')
    context = {
        'category_nav': category_nav,
    }
    return render(request, 'layout/header.html', context)

def about(request):
    articles = Article.objects.all().order_by('-add_time')
    categories = Category.objects.all()
    tags = Tag.objects.all()
    links = Link.objects.all()
    return render(request, 'about.html', {
        'articles': articles,
        'categories': categories,
        'tags': tags,
        'links':links,
    })

def global_params(request):
    category_nav = Category.objects.filter(add_menu=True).order_by('index')
    site_name = Site.objects.first().site_name
    logo = Site.objects.first().logo.url
    keywords = Site.objects.first().keywords
    desc = Site.objects.first().desc
    about_text = Site.objects.first().about_text
    slogan = Site.objects.first().slogan
    dynamic_slogan = Site.objects.first().dynamic_slogan
    bg_cover = Site.objects.first().bg_cover.url
    icp_number = Site.objects.first().icp_number
    icp_url = Site.objects.first().icp_url
    social = Social.objects.all()
    return {
        'category_nav': category_nav,
        'SITE_NAME': site_name,
        'LOGO': logo,
        'KEYWORDS': keywords,
        'DESC': desc,
        'SLOGAN': slogan,
        'DYNAMIC_SLOGAN': dynamic_slogan,
        'BG_COVER': bg_cover,
        'ICP_NUMBER': icp_number,
        'RADIO_URL': icp_url,
        'social': social,
        'ABOUT_TEXT': about_text
    }