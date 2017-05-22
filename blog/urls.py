from django.conf.urls import url
from django.contrib import admin
from . import views as blog_views
urlpatterns = [

    url(r'^$', blog_views.Blog_list,name="list")
]