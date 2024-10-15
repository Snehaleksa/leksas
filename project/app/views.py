from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.hashers import make_password
from .models import CustomUser,Student
from .serializers import PostSerializer,CustomUserSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        data = request.data
        serializer = PostSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save() 
            return Response({"success": "Student registered successfully"}, status=201)
        else:
            return Response(serializer.errors, status=400)
    
    elif request.method == 'GET':
        return Response({"message": "Send a POST request with user details to register a student."}, status=400)
