from .models import Student

def getAllStudents(): 
    return Student.objects.all()

def createStudent(studentNo, name):
    return Student.objects.create(
        studentNo=studentNo,
        name=name
    )

def getStudentById(id):
    return Student.objects.get(id=id)

def updateStudent(id, studentNo, name):
    st = getStudentById(id)
    st.studentNo = studentNo
    st.name = name
    st.save()
    return st

def deleteStudent(id):
    st = getStudentById(id)
    if st:
        st.delete()