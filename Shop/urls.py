from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view',views.display,name = 'display'),
    path('form',views.form_dis,name = "form_dis")
]
