from django.urls import path
from user.views import UserSearchView

urlpatterns = [
    path("search/", UserSearchView.as_view(), name="search-user"),
]
