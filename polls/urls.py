from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^bad', views.bad_mofo, name = "bad_mofo"),
    url(r'^save/$', views.save_user, name = "save_user"),
    url(r'^get/$', views.get_all_users, name = "get_all_users"),
    
]