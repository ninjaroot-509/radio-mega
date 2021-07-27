from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.db import models
# 注册Article到admin中
#admin.site.register(Article)

#修改后台管理页面头部显示内容和后台名称
admin.site.site_header = 'radio mega'
admin.site.site_title = 'radio mega'


#文章
@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    #设置要显示在后台列表中的字段
    list_display = ('add_time','title','cover_preview','category','show_tag','is_recommend','click_count','update_time')
    list_per_page = 10 #设置每页显示多少条记录，默认是100条
    list_editable = ['category','is_recommend'] #设置默认可编辑字段，在列表里就可以编辑
    ordering = ('-add_time','is_recommend') #设置默认排序字段，负号表示降序排序
    list_display_links = ('title',) #设置哪些字段可以点击进入编辑界面
    search_fields = ('title', 'desc', 'content') #置哪些字段可以查询
    list_filter = ('title','add_time')  #过滤器，按字段进行筛选
    date_hierarchy = 'add_time'  #详细时间分层筛选　
    readonly_fields = ('cover_preview',)#只读字段，添加该字段才能在后台预览封面，否则报错
    fieldsets = (  #后台文章编辑页面排版
        ('Article éditorial', {
            'fields': ('title','author','cover','cover_preview', 'desc','content')
        }),
        ('autres réglages', {
            'classes': ('collapse', ),
            'fields': ('is_recommend','category','tag', 'add_time'),
        }),
    )

    '''在后台展示文章的所有tag'''
    def show_tag(self, obj):
        return [t.name for t in obj.tag.all()]
    show_tag.short_description = "étiqueter"   # 设置后台表头


#分类
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','add_menu','get_items','icon','icon_data']
    list_editable = ['add_menu','icon']
    search_fields = ('name',)
    list_display_links = ('name',) #设置哪些字段可以点击进入编辑界面

#标签
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','name','get_items']
    search_fields = ('name',)

#成员
@admin.register(Link)
class LinkAdmin(ImportExportModelAdmin):
    list_display = ['name','avatar_admin','desc']
    search_fields = ('name',)

@admin.register(Site)
class SiteAdmin(ImportExportModelAdmin):
    list_display = ['site_name','logo_preview','keywords','about_text','slogan','dynamic_slogan','bgcover_preview','icp_number','icp_url']

# 技能
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'body', 'created']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name',  'sujet', 'email', 'body', 'created']

@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):
    '''Admin View for Emission'''

    list_display = ('title', 'date_time',)
    list_filter = ('date_time',)
    search_fields = ('title',)
    date_hierarchy = 'date_time'