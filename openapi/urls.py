from django.urls import path
from openapi import views

urlpatterns = [
    path("docs/", views.swagger_ui, name="swagger-ui"),
    path("openapi.yaml", views.openapi_yaml, name="openapi-yaml"),
]
