from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# signup


# login
def user_login(request):
    if request.method == 'POST':
        content = json.loads(request.body)
        print(content)
        username = content['username']
        password = content['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return JsonResponse({"username": username, "password": password})


# logout
