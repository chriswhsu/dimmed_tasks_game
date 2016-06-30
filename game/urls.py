from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^memory', views.memory, name='memory'),
    url(r'^game_2048', views.game_2048, name='game_2048')

]