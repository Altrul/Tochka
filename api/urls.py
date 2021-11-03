from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('getmanagermeetings', views.get_manager_meetings, name='get_manager_meetings'),
	path('addmanager', views.add_manager, name='add_manager'),
	path('createmeeting', views.create_meeting, name='create_meeting')
]