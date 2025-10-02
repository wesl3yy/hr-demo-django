from django.urls import path
from position.views import PositionViews

urlpatterns = [
    path("search/", PositionViews.as_view(), name="search-position"),
]