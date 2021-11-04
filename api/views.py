from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from json import dumps as json_dumps, loads as json_loads
import uuid
from random import getrandbits
import datetime
import json
from geopy.geocoders import Nominatim

from .models import Manager
from .models import Meeting

geolocator = Nominatim(user_agent="tochka")

def get_json(request):
	try:
		json = json_loads(request.body)
		if type(json) == dict:
			return json
		return None
	except:
		return None

def generate_token():
	return str(uuid.uuid4())

def get_error(string):
	return {'status':'error', 'error':string}

def locate(address):
	location = geolocator.geocode(address)
	if location == None:
		return None
	return location.longitude, location.latitude

def index(request):
	return HttpResponse('OK')

def add_manager(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'name' not in json:
		return JsonResponse(get_error('Field "name" not found'))
	if 'surname' not in json:
		return JsonResponse(get_error('Field "surname" not found'))
	if 'phone' not in json:
		return JsonResponse(get_error('Field "phone" not found'))

	manager_token = generate_token()

	manager = Manager.objects.create(name=json['name'], surname=json['surname'], phone=json['phone'], token=manager_token)

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
	if 'address' not in json:
		return JsonResponse(get_error('Field "address" not found'))

	if not json['time'].isdecimal():
		return JsonResponse(get_error(f'Field "time" is invalid: {json["time"]}'))
	time = datetime.datetime.fromtimestamp(int(json['time']))
	# manager = Manager.objects.get(token=manager_token).all()

	# if len(manager) == 0:
	# 	return JsonResponse(get_error('Manager not found'))

	# manager = manager[0]

	token = b64encode(randbytes(32)).replace('/', '+').replace('-', '_')

	location = locate(json['address'])

	if location == None:
		return JsonResponse(get_error(f'Field "address" is invalid:{json["address"]}'))

	longitude, latitude = location

	manager = Manager.objects.all()[0]

	meeting = Meeting.objects.create(name=json['name'], surname=json['surname'], longitude=longitude, latitude=latitude, time=time, token=token, manager=manager)
	meeting.save()

	return JsonResponse({'status':'ok'})

def get_manager_meetings(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'token' not in json:
		return JsonResponse(get_error('Field "token" not found'))

	token = json['token']

	manager = Manager.objects.get(token=token)

	if not manager:
		return JsonResponse(get_error('Manager not found'))
	
	meetings = Meeting.objects.filter(manager=manager)

	meetings_json = []

	for i in meetings:
		meetings_json.append({'name':i.name, 'surname':i.surname, 'time':int(i.time.timestamp())})

	print(meetings_json)
	print(token, manager.token)

	return JsonResponse({'meetings':meetings_json})

def get_managers(request):
	if  request.method != 'GET':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	managers = Manager.objects.all()
	managers_json = []
	for i in managers:
		managers_json.append({'name':i.name, 'surname':i.surname, 'phone':i.phone, 'token':i.token})

	return JsonResponse({'managers':managers_json})

def bind_meeting_to_manager(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'meeting_id' not in json:
		return JsonResponse(get_error('Field "meeting_id" not found'))
	if 'token' not in json:
		return JsonResponse(get_error('Field "token" not found'))

	meeting = Meeting.objects.get(token=json['meeting_id'])
	manager = Manager.objects.get(token=json['token'])

	meeting.manager = manager
	meeting.save()

	return JsonResponse({'status':'ok'})

def get_meeting(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'meeting_id' not in json:
		return JsonResponse(get_error('Field "meeting_id" not found'))

	meeting = Meeting.objects.get(token=json['meeting_id'])

	return JsonResponse({'name':meeting.name, 'surname':meeting.surname, 'time':meeting.time.timestamp()})

def get_path(request):
	meetings = []

	for i in Meeting.objects.all():
		meetings.append({'name':i.name, 'surname':i.surname, 'time':int(i.time.timestamp()), 'longitude':i.longitude, 'latitude':i.latitude})

	points = []

	for i in meetings:
		points.append((i.longitude, i.latitude))

	return HttpResponse(str(points))

def delete_manager(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'token' not in json:
		return JsonResponse(get_error('Field "token" not found'))

	manager = Manager.objects.get(token=json['token'])

	if manager == None:
		return JsonResponse(get_error('Token is invalid'))

	manager.delete()

	return JsonResponse({'status':'ok'})

def authorize(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'name' not in json:
		return JsonResponse(get_error('Field "name" not found'))
	if 'surname' not in json:
		return JsonResponse(get_error('Field "surname" not found'))

	manager = Manager.objects.get(name=json['name'], surname=json['surname'])

	if manager == None:
		return JsonResponse(get_error('Manager not found'))

	return JsonResponse({'token':manager.token})

def get_meetings_for_day(request):
	if request.method != 'POST':
		return JsonResponse(get_error(f'Wrong method: {request.method}'))

	json = get_json(request)
	if not json:
		return JsonResponse(get_error('Invalid JSON'))

	if 'token' not in json:
		return JsonResponse(get_error('Field "token" not found'))
	if 'time' not in json:
		return JsonResponse(get_error('Field "time" not found'))

	manager = Manager.objects.get(token=json['token'])
	if manager == None:
		return JsonResponse(get_error('Invalid token'))

	meetings = Meeting.objects.filter(manager=manager)
	day = datetime.datetime.fromtimestamp(json['time']).date()

	meetings_day = []

	for i in meetings:
		if i.time.date() == day:
			meetings_day.append({'name':i.name, 'surname':i.surname, 'address':i.address, 'longitude':i.longitude, 'latitude':i.latitude, 'time':i.time})

	return JsonResponse({'meetings':meetings_day})