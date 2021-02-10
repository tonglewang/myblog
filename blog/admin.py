from django.contrib import admin

# Register your models here.
from .models import Banner, Category, Tag, Article, Link, About, Userinfo


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'tui', 'user', 'views', 'created_time')
    list_per_page = 50
    ordering = ('-created_time',)
    list_display_links = ('id', 'title')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'linkurl')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_update_time', 'QQ', 'email', 'about_content', 'weixin')

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display =  ('id', 'motto', 'photo')