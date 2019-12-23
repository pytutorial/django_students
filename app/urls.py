from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_student',createStudent, name='create-student'),
    path('update_student/<int:id>',updateStudent,name='update-student'),
    path('delete_student/<int:id>',deleteStudent,name='delete-student'),
]