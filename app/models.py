from django.db import models

class Student(models.Model):
    studentNo = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=50)


#python manage.py makemigrations
#python manage.py migrate
