"""
URL configuration for IT_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from test_api.views import test_api,clear_test_api
from django.conf.urls.static import static
from post.views import index,blog,post,search,get_category_post
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('', blog,name='post-list'),
    path('post/<id>/', post,name='post-detail'),
    path('test_api/', test_api,name="testapi1"),
    path('search/', search,name="search"),
    path('clear_test_api/', clear_test_api,name="clear_testapi1"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/', include('allauth.urls')),
    path('category/<str:category>/', get_category_post,name = 'get_category'),
    # path('accounts/profile/', index),
]

if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
