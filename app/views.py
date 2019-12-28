from django.shortcuts import render, redirect
from . import db
import os
from django.core.files.storage import FileSystemStorage

def saveFile(studentNo, file):
    path = 'static/' + studentNo + '.jpg'
    if os.path.exists(path):
        os.remove(path)
    fs = FileSystemStorage()
    fs.save(path, file)

import time

def index(request):
    context = {'students' : db.getAllStudents(), 
                'time': time.time()}
    return render(request, 'index.html', context)

def createStudent(request):
    if request.method == 'POST':
        studentNo = request.POST['studentNo']
        name = request.POST['name']
        db.createStudent(studentNo, name)        
        file = request.FILES.get('image')
        if file and file.name:
            saveFile(studentNo, file)
        return redirect('home')

    return render(request, 'student_form.html')

def updateStudent(request, id):
    st = db.getStudentById(id)
    studentNo = st.studentNo
    name = st.name
    if request.method == 'POST':
        studentNo = request.POST['studentNo']
        name = request.POST['name']
        db.updateStudent(id, studentNo, name)
        file = request.FILES.get('image')
        if file and file.name:
            saveFile(studentNo, file)
        return redirect('home')

    return render(request, 'student_form.html', 
                {'studentNo': studentNo, 'name': name})

def deleteStudent(request, id):
    db.deleteStudent(id)
    return redirect('home')