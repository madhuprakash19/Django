from django.urls import path
from first_app import views

urlpatterns = [
path('index',views.index,name='index'),
path('database',views.database,name='database'),
]