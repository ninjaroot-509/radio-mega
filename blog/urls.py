from django.urls import path
from django.conf.urls import url
from blog import views
from django.contrib.staticfiles.views import serve
from django.views.generic.base import RedirectView

urlpatterns = [
    #Page d'accueil
    path('', views.index,name='index'),
    #Page d'article Page
    path('article/<int:id>/',views.article_detail,name='article_detail'),
    #Page de membre
    path('member/',views.member,name='member'),
    #Classification et onglet
    path('category_tag/',views.category_tag,name='category_tag'),
    #Article Catégorie Détails Page
    url(r'^article_category/(?P<id>[0-9]+)$',views.article_category,name='article_category'),
    #Détails de la balise d'article
    path('article_tag/<int:id>',views.article_tag,name='article_tag'),
    #au
    path('about/', views.about, name='about'),
    #path('favicon.ico', serve, {'path': 'static/img/favicon.ico'}),
    #path('favicon.ico', RedirectView.as_view(url='static/img/favicon.ico')),
] 