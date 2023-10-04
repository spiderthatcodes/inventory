from django.urls import path
from .api_views import user_login, user_logout, signup


urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('signup/', signup, name='signup')
]
