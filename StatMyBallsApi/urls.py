from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('all-contests', views.all_contests, name='all_contests'),
    path('contest/<int:contest_id>', views.contest, name='contest'),
    path('ajax/start_contest', views.start_contest, name='start_contest'),
]
