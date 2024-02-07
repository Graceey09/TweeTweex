from django.urls import path
from . import views

urlpatterns =[
    path('playground/home/', views.welcome),
    path('hello/<str:name>/', views.hello_world),
    path('<int:number>/', views.number)
]