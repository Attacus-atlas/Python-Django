from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^$', views.homep, name ='homep'),

]