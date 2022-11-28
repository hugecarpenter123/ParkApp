from django.urls import path, include
from .views import index, parking, index_parking

urlpatterns = [
    path('', index, name='index'),
    path('parkingi/', index_parking, name='parkingi'),
    path('<int:pk>/', parking, name='parking'),
]