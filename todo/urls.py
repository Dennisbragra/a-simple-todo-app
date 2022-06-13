from django.urls import path
from .views import index, deletetodo


urlpatterns = [
    path('', index, name='index'),
    path('deletetodo/<int:todo_id>/', deletetodo, name='delete'),
]