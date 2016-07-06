from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^run_game/(?P<plan>[A-z_]+)', views.run_game, name='run_game'),
    url(r'^start_game/(?P<game_round_user_id>[0-9]+)', views.start_game, name='start_game')
]