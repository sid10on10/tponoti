# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Devices
# Create your views here.
@csrf_exempt
def register(request):
    email = request.POST['email']
    token = request.POST['token']
    person = Devices.objects.filter(email=email)
    if not person is None:
        return HttpResponse("1")
    else:
        Devices.objects.create(email=email, token = token)
        return HttpResponse("2")

def get_all_tokens():
    persons = list(Devices.objects.all())
    list_devices = []
    for i in persons:
        list_devices.append(i.token)
    return list_devices

def get_token_by_email(email):
    person = Devices.objects.filter(email=email)
    token = person.token
    return token


