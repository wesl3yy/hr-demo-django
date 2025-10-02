from django.urls import path
from location.views import LocationViews

urlpatterns = [
    path("search/", LocationViews.as_view(), name="search-locations"),
]
