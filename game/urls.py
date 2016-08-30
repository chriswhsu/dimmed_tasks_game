from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^run_game/(?P<game_round_id>[0-9]+)', views.run_game, name='run_game'),
    url(r'^start_game/(?P<game_round_user_id>[0-9]+)', views.start_game, name='start_game'),
    url(r'^get_going/(?P<game_round_user_task_id>[0-9]+)/(?P<dim_percent>[0-9]+)', views.get_going, name='get_going'),
    url(r'^continue_game/(?P<game_round_user_task_id>[0-9]+)', views.continue_game, name='continue_game'),
    url(r'^next_iteration_ajax/$', views.next_iteration_ajax, name='next_iteration_ajax'),
    url(r'^get_comparison_points_ajax/$', views.get_comparison_points_ajax),
    url(r'^get_summary_points_ajax/$', views.get_summary_points_ajax)

]
