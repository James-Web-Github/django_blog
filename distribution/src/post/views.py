from django.shortcuts import render,get_object_or_404
from .models import Post
from marketing.models import Signup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q

def get_category_count():

    queryset = Post.objects.values('category__title').annotate(Count('category__title'))

    return queryset

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains = query) |
            Q(overview__icontains = query)
        ).distinct()
    context = {
        'query_set':queryset
    }
    return render(request, "search_result.html", context)


def index(request):
    featured_post = Post.objects.filter(feature = True)
    # query_set = Post.objects.filter(title = "先面用雖發來仍空前我要看")
    latest_post = Post.objects.order_by('-timestamp')[0:3]

    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()


    context = {
        'post_list': featured_post,
        'latest_post':latest_post
    }
    return render(request, "index.html", context)

def blog(request):
    # qu = Post.objects.filter(category__title='Django').filter(category__title='Bissness')
    # print(qu)
    category_count = get_category_count()
    # print(category_count)
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 3)#一頁幾個文章
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'post_list': paginated_queryset,
        'page_request': page_request_var,
        'most_recent':  most_recent,
        'category_count': category_count

    }
    return render(request, "blog.html", context)

def post(request, id):
    most_recent = Post.objects.order_by('-timestamp')[0:3]
    category_count = get_category_count()

    post = get_object_or_404(Post, id=id)
    context = {
        'most_recent':  most_recent,
        'category_count': category_count,
        'post':post
    }
    return render(request, "post.html", context)