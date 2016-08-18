from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^run_game/(?P<plan>[A-z_]+)', views.run_game, name='run_game'),
    url(r'^start_game/(?P<game_round_user_id>[0-9]+)', views.start_game, name='start_game'),
    url(r'^continue_game/(?P<game_round_user_task_id>[0-9]+)', views.continue_game, name='continue_game'),

    url(r'^next_iteration_ajax/$', views.next_iteration_ajax, name='next_iteration_ajax'),
    url(r'^get_comparison_points/$', views.get_comparison_points)

]
