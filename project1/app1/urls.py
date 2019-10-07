from django.urls import path

from . import views

urlpatterns =[
     path('',views.func1,name='func1'),
 
     path('add',views.add,name='add')
]