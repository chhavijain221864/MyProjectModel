from django.shortcuts import render
from .models import Student
# Create your views here.
def studinfo(request):
    stud=Student.objects.all()
    return render(request,"enroll/studentinfo.html",{'stu':stud})