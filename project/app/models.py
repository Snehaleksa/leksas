
from django.db import models


# Create your models here.


class CustomUser(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)



    def __str__(self):
        return self.username
    

class Student(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE) 
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)
    branch=models.IntegerField()
    rollno=models.IntegerField()
       