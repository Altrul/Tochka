from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from json import dumps as json_dumps
import uuid
import datetime

from .models import Manager
from .models import Meeting

def generate_token():
	return str(uuid.uuid4())

def get_error(string):
	return {'status':'error', 'error':string}

def index(request):
	return HttpResponse('OK')

def add_manager(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	if 'name' not in request.POST:
		return JsonResponse(get_error('Field "name" not found'))
	if 'surname' not in request.POST:
		return JsonResponse(get_error('Field "surname" not found'))

	manager_token = generate_token()

	manager = Manager.objects.create(name=request.POST['name'], surname=request.POST['surname'], token=manager_token)

	manager.save()

	return JsonResponse({'status':'ok'})

def create_meeting(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	if 'name' not in request.POST:
		return JsonResponse(get_error('Field "name" not found'))
	if 'surname' not in request.POST:
		return JsonResponse(get_error('Field "surname" not found'))
	if 'time' not in request.POST:
		return JsonResponse(get_error('Field "time" not found'))

	if not request.POST['time'].isdecimal():
		return JsonResponse(get_error(f'Field time is invalid: {request.POST["time"]}'))
	time = datetime.datetime.fromtimestamp(int(request.POST['time']))
	# manager = Manager.objects.get(token=manager_token).all()

	# if len(manager) == 0:
	# 	return JsonResponse(get_error('Manager not found'))

	# manager = manager[0]

	meeting = Meeting.objects.create(name=request.POST['name'], surname=request.POST['surname'], time=time)
	meeting.save()

	return JsonResponse({'status':'ok'})

def get_manager_meetings(request):
	if request.method != 'GET':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))
	
	managers = []

	return HttpResponse(json_dumps(managers))