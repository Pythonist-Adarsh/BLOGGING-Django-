from . import views
from django.conf.urls import url,include
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^inherit',views.inherit,name='inherit'),
    url(r'^index',views.index,name='index'),
    url(r'^login',views.login,name='login'),
    url(r'^validateuser',views.validateuser,name='validateuser'),
    url(r'^contact',views.contact,name='contact'),
    url(r'^Contact_us',views.Contact_us,name='Contact_us'),
    url(r'^about',views.about,name='about'),
    url(r'^blogs',views.blogs,name='blogs'),
    url(r'^password',views.password,name='password'),

]
