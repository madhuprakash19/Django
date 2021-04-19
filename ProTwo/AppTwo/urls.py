from django.urls import path
from AppTwo import views

urlpatterns = [
path('index',views.index,name='index'),
path('users',views.users,name = 'users'),
]