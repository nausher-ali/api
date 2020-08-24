from django.urls import path, include
from api import views 
urlpatterns = [
    path('users/', views.userApi)
]