from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('getmanagermeetings', views.get_manager_meetings, name='get_manager_meetings'),
	path('addmanager', views.add_manager, name='add_manager'),
	path('createmeeting', views.create_meeting, name='create_meeting'),
	path('getmanagers', views.get_managers, name='get_managers'),
	path('getmeeting', views.get_meeting, name='get_meeting'),
	path('getpath', views.get_path, name='get_path'),
	path('deletemanager', views.delete_manager, name='delete_manager'),
	path('authorize', views.authorize, name='authorize'),
	path('getmeetingsforday', views.get_meetings_for_day, name='get_meetings_for_day')
]