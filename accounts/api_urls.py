from django.urls import path
from .api_views import user_login


urlpatterns = [
    path('login/', user_login, name='user_login')
]
