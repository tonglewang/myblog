from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category,Banner,Article,Tag,Link,About, Userinfo
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger

def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:10]
    tui = Article.objects.filter(tui=True)[:5]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    remen = Article.objects.all().order_by('-views')[:6]
    tags= Tag.objects.all()
    about  = About.objects.all().order_by('-last_update_time').first()
    link = Link.objects.all()
    userinfo = Userinfo.objects.all().order_by('-id').first()
    context = {
        'allcategory':allcategory,
        'banner':banner,
        'tui':tui,
        'allarticle':allarticle,
        'remen':remen,
        'tags':tags,
        'link':link,
        'about':about,
        'userinfo':userinfo,
    }
    return render(request,'index.html',context)

def list(request, lid):
    list = Article.objects.filter(category_id=lid)
    canme = Category.objects.get(id=lid)
    remen = Article.objects.all().order_by('-views')[:6]
    allcategory = Category.objects.all()
    tags= Tag.objects.all()
    about = About.objects.all().order_by('-last_update_time').first()
    userinfo = Userinfo.objects.all().order_by('-id').first()
    page = request.GET.get('page')
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)

    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    return render(request,'list.html',locals())

def show(request, sid):
    show = Article.objects.get(id=sid)
    allcategory = Category.objects.all()
    tags= Tag.objects.all()
    about = About.objects.all().order_by('-last_update_time').first()
    remen = Article.objects.all().order_by('-views')[:6]
    userinfo = Userinfo.objects.all().order_by('-id').first()
    previous_blog=Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    next_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category_id).last()
    show.views= show.views + 1
    show.save()
    return render(request,'show.html',locals())


def tag(request, tag):

    list = Article.objects.filter(tags__name=tag)
    remen = Article.objects.all().order_by('-views')[:6]
    allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)
    page = request.GET.get('page')
    tags = Tag.objects.all()
    about  = About.objects.all().order_by('-last_update_time').first()
    userinfo = Userinfo.objects.all().order_by('-id').first()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())


def search(request):
    ss= request.GET.get("search")
    list=Article.objects.filter(title__icontains=ss)
    remen = Article.objects.all().order_by('-views')[:6]
    allcategory=Category.objects.all()
    page=request.GET.get('page')
    tags=Tag.objects.all()
    about = About.objects.all().order_by('-last_update_time').first()
    userinfo = Userinfo.objects.all().order_by('-id').first()
    paginator=Paginator(list,10)
    try:
        list=paginator.page(page)
    except PageNotAnInteger:
        list=paginator.page(1)
    except EmptyPage:
        list=paginator.page(paginator.num_pages)
    return render(request, "search.html", locals())

def about(request):
    allcategory=Category.objects.all()
    about_list = About.objects.all().order_by('-last_update_time').first()
    userinfo = Userinfo.objects.all().order_by('-id').first()
    return render(request, "about.html", locals())

