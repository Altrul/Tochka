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
	path('getmeetingsforday', views.get_meetings_for_day, name='get_meetings_for_day'),
	path('getweather', views.get_weather, name='get_weather'),
	path('getallmeetings', views.get_all_meetings, name='get_all_meetings'),
	path('generatemeetings', views.generate_meetings, name='generate_meetings'),
	path('setmanagerstatus', views.set_manager_status, name='set_manager_status'),
	path('getmanagerstatus', views.get_manager_status, name='get_manager_status'),
	path('setmeetingstotoday', views.set_meetings_to_today, name='set_meetings_to_today'),
	path('randomizepaths', views.randomize_paths, name='randomize_paths'),
	path('getallpathslength', views.get_all_paths_length, name='get_all_paths_length'),
	path('getmanagerstats', views.get_manager_meetings_count, name='get_manager_meetings_count'),
	path('getmeetingsof', views.get_meetings_of, name='get_meetings_of')
]