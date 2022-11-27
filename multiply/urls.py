from django.urls import path
from . import views
#app_name = 'jughead4'

urlpatterns = [
    path('', views.index, name='index'),
    path('launcher/', views.launcher, name='launcher'),
    path('results/', views.results, name='results'),
]