from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^adminhome',views.adminhome,name='adminhome'),
    url(r'^category_add',views.category_add,name='category_add'),
    url(r'^category_show',views.category_show,name='category_show'),
    url(r'^enquiry',views.enquiry,name='enquiry'),
    url(r'^create_category',views.create_category,name='create_category'),
    url(r'^delete_category/(?P<id>\d+)$', views.delete_category, name='delete_category'),
    url(r'^deleteblog/(?P<id>\d+)$', views.deleteblog, name='deleteblog'),
    url(r'^create_enquiry',views.create_enquiry,name='create_enquiry'),
    url(r'^blog_add',views.blog_add,name='blog_add'),
    url(r'^create_blog',views.create_blog,name='create_blog'),
    url(r'^blog_show',views.blog_show,name='blog_show'),
    url(r'^logout',views.logout,name='logout'),

 ]

