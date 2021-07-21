from django.db import models
from datetime import datetime
from django.utils.html import format_html
from mdeditor.fields import MDTextField
class Category(models.Model):
    '''Classification des articles'''
    name = models.CharField(max_length=20, verbose_name='Nom de catégorie')
    index = models.IntegerField(default=1, verbose_name='Sorte')
    add_menu = models.BooleanField(default=False, verbose_name='Ajouter à la barre de navigation')
    icon = models.CharField(max_length=30, default='fas fa-home',verbose_name='Icône de navigation')
    class Meta:
        verbose_name_plural=verbose_name = 'classification'

    #Correspondance de la classification statistique et le mettre à l'arrière-plan
    def get_items(self):
        return len(self.article_set.all())
    get_items.short_description = "Nombre d'articles"  # 设置后台显示表头
    #后台图标预览
    def icon_data(self):#引入Font Awesome Free 5.11.1
        return format_html('<h1><i class="{}"></i></h1>',self.icon) #转化为<i class="{self.icon}"></i>
    icon_data.short_description = "Aperçu de l'icône"
    def __str__(self):
        return self.name

class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=20, verbose_name="Nom de l'étiquette")
    class Meta:
        verbose_name = 'étiqueter'
        verbose_name_plural = verbose_name

    # 统计分类对应文章数,并放入后台
    def get_items(self):
        return len(self.article_set.all())
    get_items.short_description = "Nombre d'articles"  # 设置后台显示表头
    def __str__(self):
        return self.name

class Article(models.Model):
    '''文章'''
    title = models.CharField(max_length=200, verbose_name="Le titre de l'article")
    author = models.CharField(max_length=40, verbose_name='Auteur',blank=True,null=True)
    desc = models.CharField(max_length=400, verbose_name="Description d'article")
    cover = models.ImageField(upload_to='articles/', verbose_name='Couverture de l!article')
    content = MDTextField(verbose_name="Contenu de l'article")
    click_count = models.PositiveIntegerField(default=0, verbose_name='Quantité de lecture')
    is_recommend = models.BooleanField(default=False, verbose_name='Est-il recommandé?')
    # 文章创建时间。参数 default=datetime.now 指定其在创建数据时将默认写入当前的时间
    add_time = models.DateTimeField(default=datetime.now, verbose_name='Date de l!ajout')
    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='Dernières mise à jour')
    category = models.ForeignKey(Category, blank=True, null=True, verbose_name='Classification des articles', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,blank=True, verbose_name='Annonce')
    class Meta:
        verbose_name = 'article'
        verbose_name_plural = verbose_name
        ordering = ('-add_time',) #以创建时间倒序排列
    def cover_preview(self):
        return format_html('<img src="{}" width="200px" height="150px"/>',self.cover.url,)
    cover_preview.short_description = "Aperçu de la couverture de l'article"

    def __str__(self):
        return self.title    #将文章标题返回

class Link(models.Model):
    '''成员'''
    title = models.CharField(max_length=10,verbose_name='Titre')
    url = models.URLField(verbose_name='Site Internet',blank=True)
    avatar = models.URLField(default='https://i.loli.net/2020/04/23/jGP8gQOYW75TSJp.png',verbose_name='Avataratar')
    desc = models.TextField(max_length=50,verbose_name='la description')
    button_word =models.CharField(default='Visiter le blog',max_length=10,verbose_name='Texte de saut')
    class Meta:
        verbose_name=verbose_name_plural='membre'
    #后台头像预览
    def avatar_admin(self):
        return format_html( '<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />',self.avatar,)
    avatar_admin.short_description = 'Avatar Aperçu'
    def __str__(self):
        return self.title

class Notice(models.Model):
    '''公告栏'''
    title = models.CharField(max_length=30,verbose_name='Titre du babillard')
    content = models.TextField(max_length=500,verbose_name='Contenu de l!annonce')
    icon = models.CharField(default='far fa-lightbulb',max_length=50,verbose_name='Icône d!annonce')
    class Meta:
        verbose_name=verbose_name_plural='公告栏'
    def icon_data(self):
        return format_html('<h1><i class="{}"></i></h1>',self.icon) #转化为<i class="{self.icon}"></i>
    icon_data.short_description = 'Aperçu de l!icône'
    def __str__(self):
        return self.title

class Valine(models.Model):
    '''valine评论'''
    appid = models.CharField(max_length=100,verbose_name='appId')
    appkey = models.CharField(max_length=100, verbose_name='appKey')
    avatar = models.CharField(default='',blank=True,max_length=100, verbose_name='avatar')
    pagesize = models.IntegerField(default='10',verbose_name='pageSize')
    placeholder = models.CharField(max_length=100, verbose_name='placeholder')
    class Meta:
        verbose_name = 'examen de la valine'
        verbose_name_plural = verbose_name

class About(models.Model):
    '''A-propos'''
    avatar = models.URLField(verbose_name='Avatar')
    career = models.CharField(max_length=50,verbose_name='profession')
    introduction = models.TextField(verbose_name='introduction')
    skill_title = models.CharField(default='compétence',max_length=50, verbose_name='Titre de compétence')
    class Meta:
        verbose_name_plural = verbose_name = 'A-propos'
    def avatar_admin(self):
        return format_html( '<img src="{}" width="50px" height="50px" style="border-radius: 50%;" />',self.avatar,)
    avatar_admin.short_description = 'Aperçu de l!avatar'

class Social(models.Model):
    '''Lien social'''
    social_url = models.URLField(verbose_name='Lien social')
    social_desc = models.CharField(max_length=50,verbose_name='introduction')
    social_icon =models.CharField(max_length=50, default='fas fa-envelope', verbose_name='Icônes sociales')
    class Meta:
        verbose_name_plural = verbose_name = 'Social'
    # 后台图标预览
    def icon_data(self):
        return format_html('<h1><i class="{}"></i></h1>', self.social_icon)
    icon_data.short_description = '图标预览'

class Skill(models.Model):
    '''关于页技能'''
    skill_name = models.CharField(max_length=50,verbose_name='Nom du compétence')
    skill_precent =models.CharField(default='%',max_length=50,verbose_name='pourcentage')
    class Meta:
        verbose_name_plural = verbose_name = 'compétence'
    # 后台图标预览
    def icon_data(self):
        return format_html('<h1><i class="{}"></i></h1>', self.social_icon)
    icon_data.short_description = 'Aperçu de l!icône'

class Site(models.Model):
    """站点配置"""
    site_name = models.CharField(default='radio mega',max_length=30,verbose_name='Nom de site Web')
    keywords = models.CharField(default='Test de mots-clés',max_length=50, verbose_name='Mot-clé')
    logo = models.ImageField(upload_to='logo/', verbose_name='logo du site')
    desc = models.CharField(max_length=50, verbose_name='Description du site Web')
    slogan = models.CharField(max_length=50, verbose_name='Slogan de site')
    dynamic_slogan = models.CharField(max_length=50, verbose_name='Slogan dynamique')
    icp_number = models.CharField(max_length=40, verbose_name='numéro d!enregistrement')
    icp_url = models.URLField(default='http://example.com/',max_length=100, verbose_name='Lien d!enregistrement')
    bg_cover = models.ImageField(upload_to='home-baner/', verbose_name='Image de fond')

    class Meta:
        verbose_name = 'Paramètres du site Web'
        verbose_name_plural = verbose_name
    def logo_preview(self):#logo预览
        return format_html('<img src="{}" width="40px" height="40px" alt="logo" />',self.logo.url)
    logo_preview.short_description = 'Aperçu du logo'
    def bgcover_preview(self):#背景图片预览
        return format_html('<img src="{}" width="100px" height="80px" alt="bgcover" />',self.bg_cover.url)
    bgcover_preview.short_description = 'Aperçu de l!arrière-plan'
    def __str__(self):
        return self.site_name


