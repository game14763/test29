from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('start/', views.start, name='start'),
]
