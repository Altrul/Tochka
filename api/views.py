from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from json import dumps as json_dumps, loads as json_loads
import uuid
from random import getrandbits
import datetime
import json

from .models import Manager
from .models import Meeting

def get_json(request):
	try:
		return json_loads(request.body)
	except:
		return None

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

	print(manager_token)

	return JsonResponse({'status':'ok'})

def create_meeting(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'name' not in json:
		return JsonResponse(get_error('Field "name" not found'))
	if 'surname' not in json:
		return JsonResponse(get_error('Field "surname" not found'))
	if 'time' not in json:
		return JsonResponse(get_error('Field "time" not found'))

	if not json['time'].isdecimal():
		return JsonResponse(get_error(f'Field "time" is invalid: {json["time"]}'))
	time = datetime.datetime.fromtimestamp(int(request.POST['time']))
	# manager = Manager.objects.get(token=manager_token).all()

	# if len(manager) == 0:
	# 	return JsonResponse(get_error('Manager not found'))

	# manager = manager[0]

	token = b64encode(randbytes(32)).replace('/', '+').replace('-', '_')

	meeting = Meeting.objects.create(json, time=time, token=token)
	meeting.save()

	return JsonResponse({'status':'ok'})

def get_manager_meetings(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))



	if 'token' not in request.POST:
		return JsonResponse(get_error('Field "token" not found'))

	token = request.POST['token']

	manager = Manager.objects.get(token=token)

	if not manager:
		return JsonResponse(get_error('Manager not found'))
	
	meetings = Meeting.objects.filter(manager=manager)

	meetings_json = []

	for i in meetings:
		meetings_json.append({'name':i.name, 'surname':i.surname, 'time':int(i.time.timestamp())})

	print(meetings_json)

	return JsonResponse({'meetings':meetings_json})

def get_managers(request):
	if  request.method != 'GET':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	managers = Manager.objects.all()
	managers_json = []
	for i in managers:
		managers_json.append({'name':i.name, 'surname':i.surname})

	return JsonResponse({'managers':managers_json})

def bind_meeting_to_manager(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	mee