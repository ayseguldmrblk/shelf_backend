from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# https://blog.logrocket.com/using-react-django-create-app-tutorial/

def index(request):
    return render(request, 'index.html')
