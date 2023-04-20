from django.shortcuts import render,get_object_or_404,redirect,reverse
from django.db.models import Count,Q
from .models import Post,Category
from marketing.models import Subscribe
from django.core.paginator import PageNotAnInteger,EmptyPage,Paginator
from .forms import CommentForm
# from 

def get_category_count():
    query_set = Post.objects.values('categories__title').annotate(Count('categories__title'))

    return query_set


def index(request):
    featured = Post.objects.filter(featured = True)[0:3]
    latest_post = Post.objects.order_by('-timestamp')[0:3]
    # print("------------------------------------")
    print(len(latest_post))
    if request.method == "POST":
        email = request.POST["email"]
        new_subscribe = Subscribe()
        new_subscribe.email = email
        new_subscribe.save()
    context = {
        'object_list':featured,
        'latest_post':latest_post
    }
    return render(request, "index.html",context)

def blog(request):
    category_count = get_category_count
    post_list = Post.objects.all()
    most_recent = Post.objects.order_by("-timestamp")[:4]
    paginator = Paginator(post_list,4)
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'most_recent':most_recent,
        'queryset':paginated_queryset,
        'page_request_var':page_request_var,
        'category_count':category_count
    }
    return render(request, "blog.html",context)

def post(request,id):
    category_count = get_category_count
    most_recent = Post.objects.order_by("-timestamp")[:4]
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    #建立留言表單
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail',kwargs={
                'id': post.id
            }) )
    context = {
        'form':form,
        'post':post,
        'most_recent':most_recent,
        'category_count':category_count
    }
    return render(request, "post.html",context)
def search(request):
    query_set = Post.objects.all()
    query = request.GET.get("q")
    print(query_set)
    if query:
        query_set = query_set.filter(
            Q(title__icontains=query) |
            Q(over_view__icontains=query)
        ).distinct()
        print(query_set)
    
    context = {
        'queryset':query_set
    }
    return render(request,'search_result.html',context=context)
def get_category_post(request,category):
    query_set = Post.objects.filter(categories__title__contains=category)
    category_count = get_category_count
    most_recent = Post.objects.order_by("-timestamp")[:4]
    context = {
        'queryset':query_set,
        'most_recent':most_recent,
        'category_count':category_count
    }
    # return render(request,'blog.html')
    return render(request,'blog.html',context)