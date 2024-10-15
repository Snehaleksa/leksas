from rest_framework.serializers import ModelSerializer
from .models import CustomUser,Student

class CustomUserSerializer(ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'

class PostSerializer(ModelSerializer):
    
    class Meta:
        model = Student
        fields ='__all__'
