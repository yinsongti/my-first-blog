from django.conf.urls import url, include
#from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
