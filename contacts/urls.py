from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.register, name='register'),
    url(r'^$', views.contactview, name='contactview'),
    
    ]
