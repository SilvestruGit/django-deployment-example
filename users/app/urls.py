from django.urls import path
from app import views


# TEMPLATE URLS!

app_name = 'app'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
]
