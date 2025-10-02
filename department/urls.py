from django.urls import path
from department.views import DepartmentViews

urlpatterns = [
    path('search/', DepartmentViews.as_view(), name='search-department'),
]