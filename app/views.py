from django.shortcuts import render

students = [
    {"id": 1, "name": "Student 1", "studentNo": "1001"},
    {"id": 2, "name": "Student 2", "studentNo": "1002"}
]
def index(request):
    context = {'students' : students}
    return render(request, 'index.html', context)