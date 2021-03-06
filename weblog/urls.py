"""youtube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from weblog import settings
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.entries_index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^watch/(?P<slug>[^\.]+).html', views.category_detail, name='view_more'),
    url(r'^(?P<slug>[\w\-]+)/$', views.view_more, name="vidz"),
    url(r'^cats/(?P<slug>[\w\-]+)/$', views.category_detail, name="category_detail"),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^images/(.*)$', 'django.views.static.serve', {'document_root' : settings.MEDIA_ROOT}),
    
]
