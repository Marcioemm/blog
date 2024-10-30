from django.urls import path
from core.views import index, blog, tag


urlpatterns = [
    path('',index,name='index'),
    path('blog',blog,name='blog'),
    path('tag',tag,name='tag')
   
]