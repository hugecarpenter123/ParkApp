from django.urls import path
from .views import parking_space_api, locations_api, statistics_api

urlpatterns = [
    path('update/<int:pk>', parking_space_api, name="update_parking_place"),
    path('list/<int:pk>', parking_space_api, name="list_parking_place"),
    path('locations/', locations_api, name="locations_api"),
    path('statistics/<int:pk>', statistics_api, name="statistics_api"),
]