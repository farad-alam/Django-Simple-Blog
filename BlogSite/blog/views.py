from django.shortcuts import render
from . models import Categories, Post, Comments
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    posts = Post.objects.filter(Publish=True)[::-1]
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    show_homePagePost = paginator.get_page(page_number)
    total_page_num = paginator.num_pages

    category = Categories.objects.all()
    context = {'posts':show_homePagePost, 'total_page':total_page_num,'category': category}
    return render(request, 'blog/home.html',context)


def singlePost(request, slug):
    singlepost = Post.objects.filter(slug=slug).first()
    category = Categories.objects.all()
    posts = Post.objects.all()[::-1][0:10]
    if request.method =='POST':
        postpk = request.POST.get('postpk')
        post = Post.objects.filter(pk=postpk).first()
        author_name= request.POST.get('author_name')
        email= request.POST.get('email')
        comments= request.POST.get('comments')
        new_comment = Comments(post=post,author_name=author_name,email=email,comments=comments)        
        new_comment.save()
        
    
    context ={"singlePost":singlepost,"posts":posts,'category': category}
    return render(request,'blog/singlepost.html', context)

def categories(request,slug):
    categori = Categories.objects.get(slug=slug)
    category_list = Categories.objects.all() 
    context={'categori':categori,'category': category_list,}
    return render(request,'blog/categories.html',context)