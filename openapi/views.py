from django.http import HttpResponse
from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def swagger_ui(request):
    return render(request, "swagger.html")

def openapi_yaml(request):
    yaml_path = os.path.join(BASE_DIR, "openapi.yaml")
    with open(yaml_path, "r") as f:
        content = f.read()
    return HttpResponse(content, content_type="text/yaml")
