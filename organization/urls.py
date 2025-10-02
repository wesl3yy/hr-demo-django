from django.urls import path
from organization.views import OrganizationSearchView

urlpatterns = [
    path("search/", OrganizationSearchView.as_view(), name="search-organizations"),
]
