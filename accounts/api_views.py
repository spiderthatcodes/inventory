from django.shortcuts import render
import json
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


# signup
def signup(request):
    if request.method == 'POST':
        content = json.loads(request.body)
        username = content['username']
        password = content['password']
        password_confirmation = content['password_confirmation']

        if password == password_confirmation:
            user = User.objects.create_user(
                username,
                password=password
            )

            login(request, user)

            return JsonResponse({"username": username})
        else:
            return JsonResponse({'password':'passwords do not match'})


# login
def user_login(request):
    if request.method == 'POST':
        content = json.loads(request.body)
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
def user_logout(request):
    logout(request)
    return JsonResponse({'success': 'user logged out'})
