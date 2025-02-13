from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('1', views.todolist, name='todolist'),
    path('2', views.history, name='history'),
    path('3', views.contact, name='contact'),
    path('4/<int:id>', views.single, name='single'),
    path('5/<int:id>', views.edit, name='edit'),
    
]