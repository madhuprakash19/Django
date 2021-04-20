from django.urls import path
from basicapp import views

#template_tagging
app_name = 'basicapp' 

urlpatterns =[
    path('other',views.other,name = 'other'),
    path('relative',views.relative,name = 'relative'),
]
