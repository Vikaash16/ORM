from django.db import models
from django.contrib import admin
class Student (models.Model):
    rid=models.CharField(max_length=20,help_text="Student ID")
    name=models.CharField(max_length=100)
    grade=models.IntegerField()
    age=models.IntegerField()
    email=models.EmailField()

class StudentAdmin(admin.ModelAdmin):
    list_display=('rid','name','grade','age','email')



