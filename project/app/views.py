from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password
from .models import User,Student
from .serializers import PostSerializer,UserSerializer

# Create your views here.
def studentlog(data):
    user=User(username=data['username'],password=make_password(data['password']))
    user.save()
    return user
class StudentRegister(APIView):
  def post(self,request,format=None):
    try:
        student=request.data.get('student')
        print(student)
        data=request.data.get('data')
        print(data)
        stdlog=studentlog(student)
        print(stdlog)
        student_data=Student.objects.create(
            user_id=stdlog,
            Name=data['name'],
            Phone=data['phone'],
            Address=data['address'],
            Branch=data['branch'],
            RollNo=data['rollno']
        )
        student_data.save()
        
    except Exception as e:
       print(e)
       data1={"status":0}
       return JsonResponse(data1,safe=False)