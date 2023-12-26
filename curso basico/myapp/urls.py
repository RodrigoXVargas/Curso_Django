from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),

    path('projects/', views.getAllProjects),
    
    path('tasks/', views.getAllTasks),

    path('create_task/', views.create_task),
    path('create_project/', views.create_project)
    
]