from django.urls import path
from . import views
app_name = 'app1'
urlpatterns = [
    path('', views.app),
    path('app1-2', views.app1, name = 'app1'),
]