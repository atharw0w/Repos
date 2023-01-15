from django.urls import path,include
from . import views

urlpatterns=[
    path('repos/<str:user>/',views.getRepos,name='list all repos'),
    path('repos/<str:user>/<str:repo>/languages/',views.getLanguages,name='list repository languages')
]